---
title: "AI Agents Lesson 2 - Tools, Actions, and Observation Loops"
date: 2026-07-15
status: draft
tags: [lesson, agents, tools]
---

# Lesson 2: Tools, Actions, and Observation Loops

**Source**: [OpenAI Agents SDK](https://developers.openai.com/api/docs/guides/agents) · [OpenAI Building agents](https://developers.openai.com/tracks/building-agents) · [LangGraph agents docs](https://docs.langchain.com/oss/python/langchain/agents)

## Lesson goal
Understand why tools turn a language model into something that can do work.

## What is a tool?
A tool is an external capability the agent can call.
Examples:
- search
- retrieval
- code execution
- database lookup
- calendar access
- file operations
- API calls

A plain model can talk about those things.
An agent with tools can actually use them.

## The action-observation loop
Most agentic systems run a loop like this:
1. choose an action
2. execute the action through a tool
3. observe the result
4. decide what to do next

That loop is what makes the system adaptive.
The model is not just producing one answer; it is reacting to evidence.

## Why tools matter
Without tools, the model is limited to what it can recall or infer.
With tools, the model can:
- verify facts
- fetch current information
- write outputs into real systems
- inspect code or files
- test assumptions
- branch based on results

This is the main practical difference between chat and agentic work.

## Good tool design
Good tools are:
- narrow
- explicit
- easy to log
- easy to verify
- cheap to call when possible

A tool should do one thing well.
If a tool is too broad, the agent becomes harder to debug and harder to trust.

## Tool boundaries matter
The harness decides:
- which tools exist
- when they can be called
- what parameters are allowed
- whether a human must approve the action

This is important because the model is not the final authority.
The system wrapper is.

## Concrete examples
### Example 1: calendar lookup
If an agent needs today’s meeting time, it should check a calendar tool instead of guessing.

### Example 2: file editing
A coding agent should read a file, edit it, and then run tests before claiming success.

### Example 3: policy answer
A support agent should retrieve the latest policy page before drafting a response.

## Common failure modes
- calling the wrong tool
- using a tool with bad parameters
- trusting a tool output too quickly
- looping on the same failed action
- forgetting to check the result

## Build this
Design a tiny toolset for a scheduling assistant:
- find availability
- draft a meeting invite
- send with approval

For each tool, write:
- name
- input fields
- output
- when it should be blocked

## Exercises
1. Pick one everyday task. Which part should be a tool?
2. What goes wrong if a tool is too broad?
3. Why is observation as important as action?

## What this means in practice
The best agent systems are usually not the ones with the most tools.
They are the ones with the right tools, clear permissions, and clean feedback loops.

## Practical takeaway
If the model needs to do something in the world, define a tool for it.
If the model only needs to think or write, a tool may not be necessary.

## Key takeaways
- Tools extend the model beyond words.
- The agent loop is action → observation → next decision.
- Tool boundaries are part of the safety design.
- Narrow tools are easier to trust and debug.
- Good tooling is a core part of agent quality.

## Review checklist
- Can you explain why tools matter?
- Can you describe the action-observation loop?
- Can you give one example of a well-designed tool?
- Can you name three common tool failures?

## Glossary
- **Tool**: an external function or system the agent can call
- **Action**: the step the agent takes through a tool
- **Observation**: the result returned by the tool or environment
- **Loop**: repeated action and observation until the task is done
- **Permission**: a rule about what the agent is allowed to do

## Quick self-check
1. Why can’t a plain model replace tools?
2. What is the difference between action and observation?
3. Why should tools be narrow?
4. Why does the harness matter?

## Research slots to add later
- tool design patterns
- function-calling reliability
- permissions and sandboxing patterns from current agent stacks
