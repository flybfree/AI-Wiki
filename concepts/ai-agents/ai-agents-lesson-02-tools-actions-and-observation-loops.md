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

The important detail is that a tool is not just an API wrapper.
It is a boundary between what the model can imagine and what the system can verify.

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
When tools are available, the model can stop guessing and start checking.

## The action-observation loop
Most agentic systems run a loop like this:
1. choose an action
2. execute the action through a tool
3. observe the result
4. decide what to do next

That loop is what makes the system adaptive.
The model is not just producing one answer; it is reacting to evidence.

A strong loop has a clear question before every step:
- What do we know?
- What do we need?
- Which tool answers that question?
- What did the tool actually return?

## Tool design is part of agent quality
Good tools are:
- narrow
- explicit
- easy to log
- easy to verify
- cheap to call when possible

A tool should do one thing well.
If a tool is too broad, the agent becomes harder to debug and harder to trust.

A good tool should also have a shape the agent can reason about:
- clear input fields
- predictable output
- obvious failure modes
- a response the harness can validate

## Tool boundaries matter
The harness decides:
- which tools exist
- when they can be called
- what parameters are allowed
- whether a human must approve the action

This is important because the model is not the final authority.
The system wrapper is.

That separation is what keeps tool use from becoming uncontrolled behavior.

## Concrete examples
### Example 1: calendar lookup
If an agent needs today’s meeting time, it should check a calendar tool instead of guessing.

### Example 2: file editing
A coding agent should read a file, edit it, and then run tests before claiming success.

### Example 3: policy answer
A support agent should retrieve the latest policy page before drafting a response.

In each case, the tool does two jobs:
- it gets the truth closer to the model
- it gives the harness something measurable to inspect

## Common failure modes
- calling the wrong tool
- using a tool with bad parameters
- trusting a tool output too quickly
- looping on the same failed action
- forgetting to check the result

The most common bug is not “the model is dumb.”
It is “the loop is missing a good stopping rule or validation step.”

## When to avoid a tool
Not every task needs one.
If the model only needs to explain, draft, or transform text, a tool may not be necessary.

Tools are worth adding when the system needs:
- external truth
- an external side effect
- a check on its own work
- access to data that changes over time

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
