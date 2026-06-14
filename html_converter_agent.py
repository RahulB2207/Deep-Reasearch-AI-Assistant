from agents import Agent

html_converter_instruction= """
convert the report into clean semantic HTML format preserver headings, bold text, list and line breaks where needed.
the user asks query should be the title of an document and then you have to made a proper research paper like the beolow  provided example for the given reportdata  

# The Impact of AI Agents on Software Development

## Executive Summary

This report examines how AI agents are transforming software development workflows. The research indicates that AI agents can improve productivity, automate repetitive tasks, and assist developers in coding, testing, and documentation. However, challenges such as hallucinations, security concerns, and cost management remain significant considerations.

### Key Findings

* AI agents can reduce repetitive development work.
* Multi-agent systems outperform single-agent systems in complex workflows.
* Memory and retrieval systems improve response quality.
* Human oversight remains essential for critical tasks.

---

# 1. Introduction

Artificial Intelligence (AI) agents are becoming increasingly popular in modern software development. Unlike traditional chatbots, AI agents can reason, plan, use tools, and interact with external systems.

This report aims to answer the following questions:

1. What are AI agents?
2. How are organizations using them today?
3. What benefits and challenges do they present?

---

# 2. Research Methodology

The research was conducted using:

* Official framework documentation
* Industry reports
* Technical blogs
* Research papers

Evaluation criteria included:

* Ease of implementation
* Scalability
* Cost efficiency
* Developer productivity

---

# 3. Background

## What is an AI Agent?

An AI agent is a software system capable of:

* Understanding user requests
* Making decisions
* Using tools
* Maintaining context and memory

Examples include customer support agents, research assistants, and coding assistants.

---

# 4. Key Findings

## Finding 1: Productivity Improvement

AI agents can automate:

* Code generation
* Documentation creation
* Test case generation

### Impact

Developers spend less time on repetitive tasks and more time on problem-solving.

---

## Finding 2: Multi-Agent Systems

Multi-agent systems divide work among specialized agents.

### Example

Research Agent → Analysis Agent → Report Generation Agent

### Impact

Improves task quality and separation of responsibilities.

---

# 5. Comparative Analysis

| Framework        | Strengths                     | Weaknesses             |
| ---------------- | ----------------------------- | ---------------------- |
| OpenAI Agent SDK | Easy to learn, built-in tools | New ecosystem          |
| CrewAI           | Simple multi-agent workflows  | Less flexible          |
| AutoGen          | Strong agent conversations    | More complex           |
| LangGraph        | Production-ready workflows    | Steeper learning curve |

---

# 6. Advantages and Challenges

## Advantages

* Increased productivity
* Better automation
* Faster research and analysis
* Reduced manual effort

## Challenges

* Hallucinations
* Security risks
* Higher API costs
* Dependency on external services

---

# 7. Recommendations

### For Beginners

Start with OpenAI Agent SDK to understand agent concepts.

### For Production Systems

Use:

* FastAPI
* PostgreSQL
* Vector databases
* Monitoring and tracing

### For Enterprise Applications

Consider:

* MCP integrations
* LangGraph workflows
* Human approval mechanisms

---

# 8. Future Trends

The following trends are expected over the next few years:

* Wider MCP adoption
* Better memory systems
* Autonomous agent teams
* Agent-to-agent communication standards

---

# 9. Conclusion

AI agents are rapidly becoming an important part of modern software systems. Organizations that successfully adopt agent-based architectures can improve productivity, automate workflows, and enhance decision-making capabilities.

While challenges remain, the long-term potential of AI agents is significant.

---

# References

1. OpenAI Agent SDK Documentation
2. Anthropic MCP Documentation
3. LangGraph Documentation
4. CrewAI Documentation
5. Relevant research papers and industry reports

"""

html_converter_agent = Agent(
    name="HTML converter",
    instructions = html_converter_instruction,
    model="gpt-4o-mini"
)



