from agents import Runner, trace, gen_trace_id
from search_agent import search_agent
from planner_agent import planner_agent, WebSearchItem, WebSearchPlan
from researcher_agent import reasearch_agent, ReportData
from html_converter_agent import html_converter_agent
import asyncio
from xhtml2pdf import pisa
import tempfile
import os 
import gradio as gr
from markdownify import markdownify


class ResearchManager:

    async def run(self, query: str):
        """ Run the deep research process, yielding the status updates and the final report"""
        trace_id = gen_trace_id()
        with trace("Research trace", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}")
            yield f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}", gr.update(visible=False)
            print("Starting research...")
            search_plan = await self.plan_searches(query)
            yield "Searches planned, starting to search...", gr.update(visible=False)    
            search_results = await self.perform_searches(search_plan)
            yield "Searches complete, writing report...",gr.update(visible=False)
            report = await self.write_report(query, search_results)
            yield "Report written, converting it into HTML format",gr.update(visible=False)
            html_formated_report = await self.html_converter(query,report)
            yield "saving report into an PDF",gr.update(visible=False)
            pdf_path = await self.save_report(query,html_formated_report)
            asyncio.create_task(self.cleanup(pdf_path))
            yield "report saved. research complete sucessfully!",gr.update(visible=False)
            yield markdownify(html_formated_report), gr.update(value=pdf_path,visible=True)
        

    async def plan_searches(self, query: str) -> WebSearchPlan:
        """ Plan the searches to perform for the query """
        print("Planning searches...")
        result = await Runner.run(
            planner_agent,
            f"Query: {query}",
        )
        print(f"Will perform {len(result.final_output.searches)} searches")
        return result.final_output_as(WebSearchPlan)

    async def perform_searches(self, search_plan: WebSearchPlan) -> list[str]:
        """ Perform the searches to perform for the query """
        print("Searching...")
        num_completed = 0
        tasks = [asyncio.create_task(self.search(item)) for item in search_plan.searches]
        results = []
        for task in asyncio.as_completed(tasks):
            result = await task
            if result is not None:
                results.append(result)
            num_completed += 1
            print(f"Searching... {num_completed}/{len(tasks)} completed")
        print("Finished searching")
        return results

    async def search(self, item: WebSearchItem) -> str | None:
        """ Perform a search for the query """
        input = f"Search term: {item.query}\nReason for searching: {item.reason}"
        try:
            result = await Runner.run(
                search_agent,
                input,
            )
            return str(result.final_output)
        except Exception:
            return None

    async def write_report(self, query: str, search_results: list[str]) -> ReportData:
        """ Write the report for the query """
        print("Thinking about report...")
        input = f"Original query: {query}\nSummarized search results: {search_results}"
        result = await Runner.run(
            reasearch_agent,
            input,
        )

        print("Finished writing report")
        return result.final_output_as(ReportData)
    
    async def html_converter(self,query:str,report:ReportData):
        print("Converting in HTML")
        report1 = f"here is the detaild report {report} and query {query}"
        result = await Runner.run(html_converter_agent,report1 )
        print("HTML conversion done")
        return result.final_output

    async def save_report(self,query:str,report):
        temp_pdf = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
        )
        with open(temp_pdf.name, "wb") as pdf_file:
             pisa.CreatePDF(report, dest=pdf_file)
        
        return temp_pdf.name

    async def cleanup(self, path):
        await asyncio.sleep(300)  # 5 minutes

        if os.path.exists(path):
            os.remove(path)
            print(f"Deleted temporary file: {path}")