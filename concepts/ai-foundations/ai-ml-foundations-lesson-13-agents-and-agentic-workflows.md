---
title: AI/ML Foundations Lesson 13 - Agents and Agentic Workflows
date: 2026-05-06
status: draft
tags: [lesson, agents, agentic-workflows, llm, foundations]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/articles/2026-05-01_GenerativeAInewsandanalysis_TechCrunch.md
  - raw/summaries/SUMMARY_2026-04-29_Inaugural_Adobe_Creators__Toolkit_Report__86_Perce.md
  - raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
  - raw/articles/2026-05-04_BestOpen-SourceLLMMay2026_Llama4vsQwenvsDeepSeek.md
  - raw/articles/2026-04-26_Qwen_3_6_27B_Arrives_with_GGUF_Support_and_Local_M.md
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 13: Agents and Agentic Workflows



**Source**: [Original Article](https://example.com/placeholder)

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-16-deployment-scaling-and-what-comes-next.md|AI/ML Foundations Lesson 16 - Deployment, Scaling, and What Comes Next]] — 3 title terms overlap; shared tags: foundations, lesson, llm; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md|AI/ML Foundations Lesson 01 - AI, Machine Learning, and Deep Learning]] — 3 title terms overlap; shared tags: foundations, lesson; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-09-attention-and-transformers.md|AI/ML Foundations Lesson 09 - Attention and Transformers]] — 3 title terms overlap; shared tags: foundations, lesson; 6 backlinks

## Navigation
- Previous: [[ai-ml-foundations-lesson-12-prompting-guiding-model-behavior.md|Lesson 12: Prompting: Guiding Model Behavior]]
- Landing page: [[ai-ml-foundations-landing-page.md|AI/ML Foundations Landing Page]]
- Deep dive: [[concepts/ai-agents/ai-agents-landing-page.md|AI Agents Lesson Set]]
- Next: [[ai-ml-foundations-lesson-14-choosing-the-right-architecture-for-the-task.md|Lesson 14: Choosing the Right Architecture for the Task]]


Time budget: 90 to 120 minutes

## Lesson overview

An AI agent is a system that can work toward a goal by taking actions, not just by returning one answer. That is the big idea behind agentic workflows. A plain prompt asks a model to respond once. An agentic workflow gives the model a job that may require planning, using tools, checking results, and trying again.

This matters because language models became much more useful once they could do more than chat. If a model can search, retrieve, write, revise, and call external tools, it can help with tasks that are too messy for a single prompt. That is why agents are becoming common in modern AI products, coding tools, research assistants, and support systems.

Agents are exciting because they can handle more of the work. They are also riskier because once a system can act, it can also make mistakes with real consequences. This lesson explains the basic tradeoff between autonomy and control, and shows how tools, planning, memory, and iteration fit into the picture.

## Learning goals

By the end of this lesson, you should be able to:

- define what an AI agent is in practical terms
- explain how tools, planning, memory, and iteration differ from plain prompting
- recognize where agents help and where they add complexity or risk
- understand why agentic workflows are becoming common in modern AI products
- describe the main tradeoff between autonomy and control

## 1) What an AI agent is

An AI agent is a system that can pursue a goal by taking steps toward that goal.

At the simplest level, the agent receives an objective, decides what to do next, performs an action, observes the result, and then decides again. That loop is what makes the system feel agentic. It is not just producing text. It is moving through a workflow.

The TechCrunch source shows this shift in the product world with examples like Slackbot becoming an AI agent and other AI tools moving from simple generation toward task completion. The Adobe summary points in the same direction: creators want AI systems that can fit into a workflow, learn a style, and help with more than a single prompt.

The Adobe summary also gives a useful motivation snapshot: 85% of respondents were interested in style-learning agents, 69% were concerned about training without consent, and 60% already used multiple tools in a single workflow. That is a strong reminder that agent design has to respect trust as well as convenience.

Scenario: instead of asking a model to write one email draft, you ask an agent to read the thread, draft a reply, check policy, revise the tone, and prepare the final version for approval.

## 2) Tools give agents hands, not just words

A plain language model can talk. An agent can also use tools.

A tool is any external capability the system can call, such as search, retrieval, code execution, calendar access, file operations, or a database query. Tools extend the model beyond text generation. They let the system reach outside the prompt and interact with software.

This is the key practical difference between chat and agentic workflows. The model is no longer limited to what it can remember or say. It can check something, run something, fetch something, or write something in another system.

A helpful analogy is a person with access to a desk drawer full of office supplies. A plain chatbot can only describe the supplies. An agent can actually use them.

Scenario: if an agent needs today’s meeting time, it can check a calendar tool instead of guessing from memory.

## 3) Planning breaks a goal into steps

Planning means the system does not try to solve everything in one shot.

Instead, it can break a task into smaller pieces, choose an order, and work through the pieces one by one. That is especially useful for research, drafting, scheduling, code changes, and other multi-step work.

The MIT article points toward this direction when it says the next generation of LLMs will need to handle complex, multipart tasks over longer periods of time. Planning is what makes that possible.

Scenario: a research agent may first gather sources, then summarize them, then compare them, and only then draft a final report.

## 4) Memory helps the system stay on task

Memory in an agentic workflow means the system can keep useful information across steps.

That memory might be short-term, like tracking the current plan, or longer-term, like remembering user preferences or past work. Memory helps the agent avoid repeating itself and keeps it aligned with the goal.

This does not mean the agent is thinking like a human. It means the system preserves state so it can continue from one step to the next.

Scenario: if you tell an agent to prefer concise answers and then ask it to revise a draft, memory lets it keep that preference in mind.

## 5) Iteration is how agents recover from mistakes

Agentic workflows are usually iterative.

The system acts, checks the result, and adjusts. If the first answer is weak, the agent can try again. If the search result is incomplete, it can search differently. If the output format is wrong, it can rewrite it.

That loop is one of the main reasons agents are useful. A single model call may be good, but a multi-step loop can be better for hard tasks.

Scenario: an agent drafting a proposal can notice that a section is missing evidence, fetch more supporting material, and then revise the draft before presenting it.

## 6) Agents help most when the task is messy and open-ended

Agents are useful when the problem is not just “say something,” but “go do something complicated.”

The TechCrunch article captures the product trend toward AI systems that can handle more than one-off generation. The Qwen article adds a concrete example from the open-source world: it describes “agentic coding,” where a model does not just write code but reasons about execution, debugs errors, and iterates on a solution. That is a good picture of where agents are most valuable.

Common good fits include research, triage, scheduling, drafting, code assistance, and workflow automation.

Scenario: a support agent can read a customer message, find the relevant policy, draft a response, and hand it to a human for approval.

## 7) Agents add risk because action has consequences

The same autonomy that makes agents useful also makes them riskier.

If an agent can act, it can make bad decisions, trigger the wrong tool, expose private data, or create a chain of errors faster than a human would catch them. That is why agent design needs guardrails, which are limits that keep the system inside safe and intended boundaries.

A plain chatbot can be wrong in a reply. An agent can be wrong and also perform the wrong action.

Scenario: if an agent sends a calendar invite to the wrong group or deletes the wrong file, the mistake is no longer just text. It has a real-world effect.

## 8) Good agent design balances autonomy and control

The goal is not maximum autonomy. The goal is useful autonomy with appropriate checks.

Practical agent systems often need approval steps, limited tool access, logging, human oversight, and clear task boundaries. The best workflow is often semi-autonomous rather than fully autonomous.

The Adobe summary’s emphasis on creator control and trust is relevant here. Even when users want help, they still care about consent, quality, and transparency.

Scenario: a writing agent can prepare a draft and suggest revisions, but the user still approves the final publish action.

## 9) Agents and retrieval often work together

A strong agent often needs more than reasoning. It needs current information.

That is where retrieval augmented generation, or RAG, comes in. RAG is a setup where the system pulls relevant sources from outside the model’s training data and uses them as added context. In an agentic workflow, that can make the system more accurate and more up to date.

The Qwen article describes long-context, RAG-style workflows as a strong fit for agentic coding and other precision-heavy tasks. That is a useful clue: agents often become much better when they can search first and act second.

Scenario: an agent answering a policy question can retrieve the latest policy document before drafting its response instead of relying only on memory.

## 10) Agent vs workflow

A workflow is a fixed or lightly guided sequence of steps. An agent is a system that can choose actions, use tools, observe results, and decide what to do next.

That distinction matters because not every helpful AI product needs to be a fully autonomous agent. Sometimes a guided workflow is safer, cheaper, and easier to understand.

Scenario: a document assistant that always runs the same steps is a workflow; a coding assistant that decides whether to search, edit, test, or retry is acting more like an agent.

## 11) Harness engineering is the real product surface

The harness is the wrapper around the model that manages prompts, tool calls, retries, state, logging, approvals, and failure handling. In plain language, it is the control layer or orchestrator around the model. In many agent systems, the harness is what makes the difference between a demo and a reliable product.

This is where permissions, sandboxing, and guardrails live. The model may propose actions, but the harness decides what the system is actually allowed to do.

Scenario: an agent may suggest deleting a file, but the harness can require confirmation or block the action entirely.

## 12) Long-horizon agents vs short-term chatbots

Recent research shows that designing for long interaction spans may matter as much as model size. The Agents-A1 paper (arXiv:2606.30616) demonstrates that a 35B mixture-of-experts agentic model achieves trillion-parameter-level performance by scaling agent horizon rather than raw parameters. These agents work with trajectories of about 45K tokens on average, maintaining coherence across extended workflows.

This is not just longer chat—it's structured execution over time. A long-horizon agent plans, acts, observes, and adapts across many steps while preserving context and goals. Short-term chatbots answer questions; long-horizon agents complete tasks.

Scenario: a research agent doesn't just summarize one paper—it gathers sources, compares them, drafts sections, revises based on feedback, and produces a final report over hours of interaction.

## 13) Harness engineering is the real product surface

The harness is the wrapper around the model that manages prompts, tool calls, retries, state, logging, approvals, and failure handling. In plain language, it is the control layer or orchestrator around the model. In many agent systems, the harness is what makes the difference between a demo and a reliable product.

Recent work on "scaling the harness" (From Model Scaling to System Scaling) identifies six critical layers:
- **Memory substrate**: Where state persists across steps
- **Context constructor**: Assembling relevant information for each decision
- **Skill-routing layer**: Deciding which tools or subagents to use
- **Orchestration loop**: Managing the planning-action-observation cycle
- **Verification-and-governance layer**: Checking outputs and enforcing policies

The harness handles context compaction (summarizing long histories), subagent delegation (spawning specialized workers), sandboxing (isolating risky operations), and observability (logging for debugging).

Scenario: an agent may suggest deleting a file, but the harness requires confirmation or blocks the action entirely. It also maintains session state so the agent can pick up where it left off after interruptions.

## 14) What to remember without the jargon

An agent is a model-plus-tools system that can work toward a goal over multiple steps.

Plain prompting asks for an answer. Agentic workflows ask for progress.

Long-horizon agents maintain coherence across extended interactions, often using structured execution harnesses rather than just larger models.

That difference is why agents are important in the current AI transition, and also why they need careful design. The more the system can do, the more important it becomes to decide what it should be allowed to do.

## Closing summary

Agents push AI beyond one-shot text generation. They combine a language model with tools, planning, memory, and iteration so the system can make progress on a goal. That makes them useful for messy, multi-step work like research, support, scheduling, drafting, and coding.

But the same capability also increases risk. Once a system can act, mistakes can have consequences outside the chat window. Good agent design therefore depends on guardrails, limited permissions, human approval where needed, and careful workflow design.

Recent research shows that long-horizon agents—those maintaining coherence across extended interactions—may matter as much as model size. The harness engineering around these systems (memory substrate, context construction, skill routing, orchestration, verification) is often the real differentiator between demos and reliable products.

## Key takeaways

- An AI agent takes actions toward a goal.
- Tools expand what the system can do.
- Planning, memory, and iteration make multi-step work possible.
- Agents are useful for messy, open-ended tasks.
- More autonomy means more risk, so guardrails matter.
- Retrieval and long context often make agents more effective.
- Long-horizon agents maintain coherence across extended interactions; harness engineering is critical.

## Quick self-check

Answer these in your own words:

1. What makes a system an AI agent?
2. How do tools change what the model can do?
3. Why is planning useful in agentic workflows?
4. What role does memory play?
5. Why do agents require more caution than plain chat?

## Suggested follow-up reading

- /home/rich/wiki/ai-research/raw/articles/2026-05-01_GenerativeAInewsandanalysis_TechCrunch.md
- /home/rich/wiki/ai-research/raw/summaries/SUMMARY_2026-04-29_Inaugural_Adobe_Creators__Toolkit_Report__86_Perce.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
- /home/rich/wiki/ai-research/raw/articles/2026-05-04_BestOpen-SourceLLMMay2026_Llama4vsQwenvsDeepSeek.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-26_Qwen_3_6_27B_Arrives_with_GGUF_Support_and_Local_M.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
