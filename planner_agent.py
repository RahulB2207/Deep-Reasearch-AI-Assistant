from pydantic import BaseModel
from agents import Agent, Runner, trace

HOW_MANY_QUERIES = 3

INSTRUCTIONS = f"""
You are a helpful reasearch assistant. Given a query, come up with a set of web searches\
to perform to best answer the query. Output {HOW_MANY_QUERIES} terms to query for.
"""

class WebSearchItem(BaseModel):
    reason:str 
    "your reasoing for why this search is important to the query"
    query : str 
    "The search term to use for the web searches."

class WebSearchPlan(BaseModel):
    searches : list[WebSearchItem]
    "A list of web searches to perform to best answer to the query."

planner_agent = Agent(
    name="Planner agent",
    instructions = INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan
)