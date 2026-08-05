---
title: AI/ML Foundations Edit Plan
date: 2026-05-08
status: draft
tags: [ai-ml-foundations, edit-plan, course-design, foundations]
source_pages:
  - ai-ml-foundations-course-map.md
  - ai-ml-foundations-syllabus.md
  - dive-into-claude-code.md
  - claude-code-linked-sources.md
---

## Summary

Placeholder summary — please add a concise summary.


# AI/ML Foundations Edit Plan



**Source**: [Original Article](https://example.com/placeholder)
This is the concrete lesson-by-lesson revision checklist for the 16-lesson AI/ML Foundations course.

Primary goal:
- Keep the course concept-first and math-light
- Preserve the existing sequence
- Add the Claude Code / harness-engineering material where it actually changes the teaching story
- Avoid bloating the early fundamentals lessons with unrelated agent details

Edit rules:
- Define new terms on first use
- Add at least one concrete scenario for every new concept
- Prefer short bridge paragraphs over rewrites when a lesson only needs a light update
- Keep the core ML lessons stable unless the new material materially changes them

Priority order:
1. Lesson 13 — biggest rewrite
2. Lesson 12 — major rewrite
3. Lesson 16 — major rewrite
4. Lesson 15 — major rewrite
5. Lesson 14 — major rewrite
6. Lesson 11 — moderate rewrite
7. Lesson 9 — moderate bridge update
8. Lesson 8 — moderate bridge update
9. Lesson 10 — light-to-moderate update
10. Lessons 1–7 — light bridge updates only

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md|AI/ML Foundations Lesson 01 - AI, Machine Learning, and Deep Learning]] — 1 title term overlap; shared tags: foundations; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-course-map.md|AI/ML Foundations Course Map]] — 1 title term overlap; shared tags: foundations; 2 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-07-convolutional-networks-for-vision.md|AI/ML Foundations Lesson 07 - Convolutional Networks for Vision]] — 1 title term overlap; shared tags: foundations; 6 backlinks

## Lesson-by-lesson plan

### Lesson 1 — AI, Machine Learning, and Deep Learning
Edit level: light

Edits:
- Add 1 short sentence in the overview that modern AI products are usually model + system + interface, not just a model.
- Add 1 bridge sentence in the closing summary pointing forward to Lessons 11–13.
- Leave the core definitions unchanged.

Why:
- This keeps the opening lesson grounded without overloading it.

### Lesson 2 — How an ML System Works
Edit level: light

Edits:
- Add a note in the system diagram / pipeline section that modern AI systems often include orchestration, memory, tool access, and monitoring around the model.
- Add one example of a workflow where the model is only one component in a larger product.
- Keep the classic data → training → evaluation → deployment → monitoring structure.

Why:
- This is the best place to introduce “system, not just model.”

### Lesson 3 — Data as the Foundation of Learning
Edit level: light

Edits:
- Add one sentence explaining that in agentic systems, retrieved documents and conversation history can function like working context.
- Keep the data quality lesson intact.
- Add one scenario contrasting training data with runtime context.

Why:
- Good bridge, but no real conceptual overhaul needed.

### Lesson 4 — Supervised Learning: Learning from Labels
Edit level: none or very light

Edits:
- Leave the lesson mostly unchanged.
- Optional: add one sentence contrasting labeled training with tool-using agents that still need labels or feedback for evaluation.

Why:
- The new material does not change the core supervised-learning story.

### Lesson 5 — Unsupervised Learning: Finding Hidden Structure
Edit level: none or very light

Edits:
- Leave the lesson mostly unchanged.
- Optional: add one sentence distinguishing clustering from memory or retrieval in agent systems.

Why:
- The new research does not materially change this lesson.

### Lesson 6 — Neural Networks: The Core Building Blocks
Edit level: light

Edits:
- Add one short bridge paragraph noting that transformers, LSTMs, and agent systems still rely on the same basic neural-network building blocks.
- Keep the explanation of neurons, layers, weights, and activations intact.
- Add one example of a neural network feeding into a larger workflow.

Why:
- This helps readers understand continuity across model families.

### Lesson 7 — Convolutional Networks for Vision
Edit level: none or very light

Edits:
- Leave the lesson as-is unless you want a single sentence noting that architecture choice depends on task shape.
- No agent-specific rewrite needed.

Why:
- The new material is not vision-specific.

### Lesson 8 — Recurrent Networks and LSTMs
Edit level: moderate

Edits:
- Add a subsection near the memory discussion: “Sequence memory vs external memory.”
- Explain that RNN/LSTM hidden state is internal, while agent memory is often external and workflow-specific.
- Add one paragraph on why LSTMs helped sequence tasks but still had context limits.
- Add one scenario comparing text sequence memory with project/task memory.

Suggested new subheadings:
- Sequence memory is internal
- External memory can persist outside the model
- Why LSTMs were a bridge, not the end state

Why:
- This is a natural bridge into attention, context windows, and agent memory.

### Lesson 9 — Attention and Transformers
Edit level: moderate

Edits:
- Add a subsection on “attention is not durable memory.”
- Clarify that attention helps the model focus on the current context window, but it does not create long-term persistence by itself.
- Add a short bridge to context windows and compaction.
- Add one example where a long prompt still fails if the important information is not surfaced well.

Suggested new subheadings:
- Attention connects parts of the current sequence
- Context windows are bounded working memory
- Attention helps, but it does not replace persistence

Why:
- The Claude Code material strongly reinforces this distinction.

### Lesson 10 — Generative AI: Creating New Content
Edit level: light to moderate

Edits:
- Add a short section showing generative AI as part of a workflow: draft → revise → check → hand off.
- Add one scenario where generation is followed by tool use or human review.
- Keep the main distinction between generation and prediction.

Why:
- This prepares readers for the move from generation to agentic systems.

### Lesson 11 — Large Language Models: The Modern AI Interface
Edit level: moderate

Edits:
- Add a subsection: “An LLM is part of a larger system.”
- Add a short explanation that the model is the interface layer, but the product may also include harness logic, retrieval, memory, and tool use.
- Add a short paragraph on prompt quality as a system input, not just a user skill.
- Add a bridge note that longer context helps, but system design still matters.
- Keep the token/context-window explanation, but connect it explicitly to workflow design.

Suggested new subheadings:
- LLMs are the interface, not the whole product
- Context windows are useful but limited
- Better systems wrap the model with control logic

Why:
- This is the pivot point between LLM basics and Claude Code-style systems.

### Lesson 12 — Prompting: Guiding Model Behavior
Edit level: major

Edits:
- Reframe the lesson from “prompt writing” to “prompting + context engineering.”
- Add a new section on instruction hierarchy / prompt layering.
- Add a new section on persistent instructions versus task-specific prompts.
- Add a new section on examples of prompt augmentation: source text, style examples, policy constraints, and role instructions.
- Add a new section on when prompting is enough and when you need retrieval, tools, or a harness.
- Add one concrete scenario showing the same task with:
  - only a prompt
  - prompt + source context
  - prompt + retrieval + tool use

Suggested new subheadings:
- Prompting is not the same as context engineering
- Instructions, examples, constraints, and source context
- When to improve the prompt and when to change the system

Why:
- This is one of the biggest conceptual upgrades from the new material.

### Lesson 13 — Agents and Agentic Workflows
Edit level: major

Edits:
- Expand the lesson into a full agent systems chapter.
- Add a section that distinguishes a one-shot workflow from a multi-step agent loop.
- Add a section on harness engineering: the wrapper logic that manages tool use, retries, state, permissions, and result handling.
- Add sections on:
  - tools
  - planning
  - memory
  - iteration
  - context compaction
  - subagents / delegation
  - sandboxing / permissions / guardrails
- Add one example from coding or research where the agent needs to search, edit, check, and revise.
- Add one example where the system should not be fully autonomous.

Suggested new subheadings:
- Agent vs workflow
- The harness is the real product surface
- Tools, planning, memory, and iteration
- Subagents and delegation
- Permissions and sandboxing
- Autonomy needs guardrails

Why:
- This is the centerpiece of the revision.

### Lesson 14 — Choosing the Right Architecture for the Task
Edit level: major

Edits:
- Extend the architecture-choice lesson from “which model family?” to “which system pattern?”
- Add a decision ladder:
  - plain model call
  - prompt + context
  - retrieval-assisted workflow
  - agent loop with tools
  - managed agent with permissions and isolation
- Add one section explaining that “best” means simplest reliable system, not the fanciest system.
- Add one scenario comparing a simple summarizer, a retrieval assistant, and an agentic coding helper.

Suggested new subheadings:
- Task shape still matters
- System pattern matters too
- Choose the simplest reliable architecture

Why:
- The new research makes system design part of architecture selection.

### Lesson 15 — Evaluation, Overfitting, and Limits
Edit level: major

Edits:
- Expand evaluation to include agent behavior, not just model accuracy.
- Add criteria for:
  - task completion
  - tool success
  - long-horizon consistency
  - safety / policy adherence
  - hallucination under pressure
  - recovery after failure
- Add a subsection on offline versus online evaluation for agentic systems.
- Add one example showing a model that scores well but fails in a real workflow.
- Keep the overfitting / underfitting / drift material, but connect it to runtime behavior.

Suggested new subheadings:
- Evaluate the system, not just the model
- Offline and online evaluation
- Agent failures are different from classifier failures

Why:
- Agent systems need different metrics than classic ML pipelines.

### Lesson 16 — Deployment, Scaling, and What Comes Next
Edit level: major

Edits:
- Expand deployment from “serving a model” to “deploying an AI system.”
- Add a section on runtime controls: sandboxing, logging, retries, approvals, and observability.
- Add a section on state: sessions, memory, compaction, and checkpoints.
- Add a section on cost, latency, and caching.
- Add a section on scaling agentic systems, not just model training.
- End with a forward-looking note that the field is moving toward longer-running systems with more coordinated control logic.

Suggested new subheadings:
- Deploying a model vs deploying a system
- Observability and control in production
- State, memory, and compaction
- Scaling multi-step systems
- What comes next for AI systems

Why:
- This is where the course should connect classical MLOps to modern agent platforms.

## Cross-lesson consistency updates

Apply these across the revised lessons:
- Define these terms on first use: LLM, RAG, harness, sandbox, subagent, context compaction, observability
- Add one concrete scenario per new concept
- Keep terminology stable across Lessons 11–16
- Use “system,” “workflow,” and “harness” consistently where appropriate
- Do not overload the early lessons with jargon

## Suggested implementation order

1. Lesson 13
2. Lesson 12
3. Lesson 16
4. Lesson 15
5. Lesson 14
6. Lesson 11
7. Lesson 9
8. Lesson 8
9. Lesson 10
10. Lessons 1–7

## Delivery rule for the actual lesson edits

When editing the lessons, prefer small, reviewable patches:
- update overview + closing summary first
- then add one new subsection at a time
- then adjust key takeaways and self-check questions
- then add follow-up reading only if it changes the lesson’s source base

