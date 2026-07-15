---
title: "AI Agents Lesson 4 - Retrieval, Context, and Long-Context Work"
date: 2026-07-15
status: draft
tags: [lesson, agents, retrieval, context]
---

# Lesson 4: Retrieval, Context, and Long-Context Work

**Source**: [Agents-K1: Towards Agent-native Knowledge Orchestration](https://arxiv.org/abs/2606.13669) · [Context-Aware RL for Agentic and Multimodal LLMs](https://arxiv.org/abs/2606.17053) · [OpenAI: A practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

## Lesson goal
Understand how outside knowledge enters an agent workflow and why retrieval often beats guessing.

## What retrieval does
Retrieval fetches relevant material from outside the model.
That material might come from:
- a document store
- a search index
- a knowledge graph
- a database
- a vector store
- a live web query

The point is not just to have more text.
The point is to have the right text.

## Context vs long context
**Context** is what the model can see right now.
**Long context** means the model can see more tokens at once.
Those are related, but not the same thing.

A larger context window helps, but it does not automatically give better reasoning.
The model still needs the right evidence.

## Why retrieval matters
Agents get better when they search first and act second.
This matters most for:
- policy
- code
- research
- current events
- long documents
- multi-document comparison

If the answer depends on something specific, retrieve it.
Do not guess.

## Structured retrieval
A structured source, such as a knowledge graph or curated index, often works better than a giant text dump when the task requires relationships rather than raw passages.

That is why agent-native knowledge orchestration is important: it gives the agent a way to navigate facts instead of just reading chunks.

## Concrete examples
### Example 1: policy assistant
A policy assistant should retrieve the latest policy document before drafting an answer.

### Example 2: research assistant
A research agent should fetch the relevant papers, compare them, and only then write the synthesis.

### Example 3: coding assistant
A coding agent should retrieve repo files, docs, and test output before proposing a fix.

## When long context is enough
Long context is helpful when:
- the source set is small
- the task is mostly reading and summarizing
- the answer depends on a long contiguous passage

## When retrieval is better
Retrieval is better when:
- the relevant evidence is scattered
- the sources change often
- the task needs precision
- the model must justify its answer with specific sources

## Common failure modes
- retrieving too much irrelevant text
- retrieving the wrong document
- trusting stale context
- confusing more context with better evidence
- skipping retrieval entirely

## Build this
Design a retrieval stack for a policy assistant:
- source of truth
- how documents are chunked
- how the agent searches
- what it should cite
- what happens if retrieval returns nothing

## Exercises
1. Why is retrieval useful for agents?
2. What is the difference between context and long context?
3. When is a knowledge graph better than plain text chunks?
4. Why should an agent search before it acts?

## Practical takeaway
Use retrieval to bring the model the facts it actually needs.
Use long context to carry those facts farther once they are found.

## Key takeaways
- Retrieval fetches outside knowledge into the agent loop.
- Context is what the model can currently see.
- Long context is helpful but not magic.
- Structured retrieval often beats flat text when relationships matter.
- Search first, act second is a strong default.

## Review checklist
- Can you explain why retrieval matters?
- Can you distinguish context from long context?
- Can you name a case where structured retrieval is better?
- Can you say why stale context is risky?

## Glossary
- **Retrieval**: fetching relevant information from an external source
- **Context window**: the amount of text the model can attend to at once
- **Knowledge graph**: structured representation of entities and relationships
- **Vector store**: a similarity search store for embeddings
- **RAG**: retrieval augmented generation

## Quick self-check
1. Why is retrieval useful for agents?
2. What is the difference between context and long context?
3. When is a knowledge graph better than plain text chunks?
4. Why should an agent search before it acts?

## Research slots to add later
- RAG patterns for agents
- structured retrieval vs flat text retrieval
- long-context limits and when they matter
