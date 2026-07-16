---
title: "AI Agents Lesson 1 - What an AI Agent Is"
date: 2026-07-16
status: draft
tags: [lesson, agents, foundations]
---

# Lesson 1: What an AI Agent Is

**Source**: [OpenAI: A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/) · [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) · [LangGraph: Agent orchestration framework](https://www.langchain.com/langgraph)

## Lesson goal
Build a plain-language definition of an AI agent and learn how it differs from a chat model or a fixed workflow.

## What is an AI agent?
An AI agent is a system that works toward a goal by taking actions, observing results, and deciding what to do next.

A chatbot answers.
An agent tries to complete a task.

That is the simplest useful distinction, but it leaves out the important part: the agent is not just the model. It is the model plus the tools, rules, memory, and control layer around it.

## The simplest mental model
Think of an agent as three parts working together:
- **Model**: proposes the next step
- **Harness**: decides what the model is allowed to do
- **Environment**: gives the result back after an action

The model can suggest a next move, but the harness decides whether that move is allowed and how it gets executed.
The environment answers back with evidence, errors, or changes in the world.

## The core loop
Most agent systems follow a version of this loop:
1. receive a goal
2. decide on a next step
3. take an action
4. observe the result
5. update the plan
6. repeat until done or stopped

That loop is what turns a language model from a one-shot responder into a system that can keep working over time.

## What makes a system feel agentic
A system feels agentic when it can:
- choose among possible next steps
- use tools or external systems
- respond to feedback from the environment
- recover from mistakes and try again
- carry state across steps

If a system can only produce a reply, it is still just chat.
If it can inspect the situation, act, and adapt, it is becoming an agent.

## What an agent is not
- not every chatbot is an agent
- not every workflow is autonomous
- not every tool-using system is a full agent
- not every agent needs to be fully autonomous

A single response from a model does not automatically mean the system is agentic.
The agent label only fits when the system can actually pursue a goal over time.

## Workflow, chatbot, and agent
A useful way to compare them:

- **Chatbot**: answers the user in text
- **Workflow**: follows a prescribed sequence of steps
- **Agent**: can choose the next step inside a guided loop

A workflow is usually easier to test because its path is fixed.
An agent is more flexible because it can adapt when the environment changes.

## Why this matters
Agents are useful when the task is messy, multi-step, and too dynamic for one perfect prompt.
They are also riskier than plain chat because they can do something incorrect, not just say something incorrect.

That tradeoff is the whole story of the course.
The course is really about one question:
**How do you get useful autonomy without losing control?**

## Concrete examples
### Example 1: support triage
A support assistant reads a ticket, checks the knowledge base, drafts a reply, and asks for approval before sending.

### Example 2: research assistant
A research agent searches the web, collects sources, compares them, and drafts a summary.

### Example 3: coding assistant
A coding agent reads the issue, edits files, runs tests, and fixes failures.

In each case, the system is not just generating text. It is trying to make progress.
Each step changes what the next step should be.

## Agent vs workflow
A workflow is a fixed or lightly guided sequence of steps.
An agent is a system that can choose steps inside that sequence.

A workflow says:
- always do A, then B, then C

An agent says:
- inspect the situation, then choose whether to do A, B, or C next

That distinction matters because workflows are usually simpler and safer, while agents are usually more flexible.

## The two things to keep in mind
### 1. Capability
Can the system do the task?

### 2. Control
Can you keep the system inside safe boundaries while it does it?

Good agent design is not maximum autonomy.
It is useful autonomy with appropriate control.

## Where agents fit best
Agents help most when the task has these traits:
- open-ended
- multi-step
- uncertain
- dependent on current information
- likely to benefit from retries or branching decisions

Agents help less when the task is:
- narrow
- deterministic
- easily scripted
- high-risk and hard to supervise

## Where the definition breaks down
Some systems sit in the middle.
A scripted workflow with one conditional branch may look agentic even though it is mostly deterministic.
A chat model with a retrieval step may look like an agent even if it never really chooses among actions.

That is normal.
The useful question is not “is it perfectly pure?” but “does this architecture need goal-directed action?”

## More detailed notes
An agent is not defined by how impressive the output sounds. It is defined by whether the system can keep choosing, acting, and revising its approach over time.

A useful test is this: if you removed the action loop, would the system still do the job? If yes, it may just be a workflow with a chat interface. If no, the system is probably relying on agent behavior.

### Extra examples
- **Travel planning**: the agent checks dates, compares options, and updates the plan after each constraint changes.
- **Customer support**: the agent drafts a reply, checks policy, waits for approval, and only then sends.
- **Research**: the agent searches, compares sources, and changes its hypothesis when one source contradicts another.

### Common misconception
People often call any tool-using app an agent. That is too loose. A tool call alone does not make a system agentic; the system must also decide what to do with the result.

## Build this
Create a simple agent spec on paper:
- goal
- available tools
- what counts as success
- what must be approved
- what the agent should do if it gets stuck

If you can write those five things clearly, you have the start of a real agent design.

## Exercises
1. Pick a chatbot you use. What would have to change for it to count as an agent?
2. Name one task that should stay a workflow instead of becoming an agent.
3. List three steps in an agent loop for a travel-planning assistant.

## Practical takeaway
Before building an agent, ask:
> Do I need a system that only answers, or do I need a system that can act?

If it needs to act, you are in agent territory.

The next lesson shows how the harness turns that idea into a runnable loop.

## Key takeaways
- An agent is a goal-seeking system that can take actions.
- The key difference from chat is action plus observation plus iteration.
- Not every tool-using app is a real agent.
- Agents are useful for messy work and risky if they are unconstrained.
- The harness around the model matters as much as the model itself.

## Review checklist
- Can you define an agent in one sentence?
- Can you explain the agent loop without jargon?
- Can you tell the difference between a workflow and an agent?
- Can you name one reason agents are useful and one reason they are risky?

## Glossary
- **Agent**: a system that pursues a goal through actions and feedback
- **Workflow**: a predetermined or lightly guided sequence of steps
- **Tool**: an external capability the system can call
- **Harness**: the control layer around the model that manages the loop
- **Observation**: the result the agent sees after taking an action

## Quick self-check
1. What is the simplest difference between a chatbot and an agent?
2. Why do agents need observation?
3. When is a workflow safer than an agent?
4. Why is the harness important?

## Research slots to add later
- current product examples from OpenAI and Anthropic agent docs
- agent loop patterns from LangGraph and similar orchestrators
- recent research on long-horizon goal completion
