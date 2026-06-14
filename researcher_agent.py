from agents import Agent
from pydantic import BaseModel

writing_instructions = """
You are a senior reasearcher taskes with writing a cohesive report for a reserach query. \n
you will be provided with original query, and some initial research done by research assistant. \n
you should first come up with an outline for report that describes the structure and output \ng
flow of report. Then genrate the report and return that as your final output. \n
The final output should be markdown format, and it should be lengthy detaild.
Aim for 5-10 pagess of content, at least 1000 words

"""
class ReportData(BaseModel):
    Executive_summary : str
    key_findings:str
    Introduction:str
    research_methodology:str
    compartive_analysis:str
    background:str
    challenges:str
    recommondation:str
    future_trends:str
    conclusion : str

    


reasearch_agent = Agent(
    name="Reasearch Agent",
    instructions = writing_instructions,
    model = "gpt-4o-mini",
    output_type = ReportData
)

