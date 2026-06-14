from agents import Agent, WebSearchTool, ModelSettings

instructions = """
You are a reasearch assistant. Given a search term, you serach the web for that term and \
produce a consice summary of the results. the summary must 2-3 paragraphs and less than 1000 \
words. capture the main points. write succintly, no need to have complete sentences or good \
grammer. This will be consumed by someone synthesizing a report, so it's vital you capture the \
essence and ignore any fluff. do not include any additional comentatry other than the summary itself.
"""

search_agent = Agent(
    name = "Search Agent",
    instructions = instructions,
    tools = [WebSearchTool(search_context_size="low")],
    model = "gpt-4o-mini",
    model_settings = ModelSettings(tool_choice="required")
    
)