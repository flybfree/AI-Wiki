---
title: Benchmarks Are Surprisingly Compaction-Friendly
published: 2026-10-22T18:15:54Z
authors: Jeanne Salle, Hardik Bhatnagar, Matthias Bethge, Sahar Abdelnabi, Maksym Andriushchenko
url: http://arxiv.org/abs/2610.31778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarks Are Surprisingly Compaction-Friendly

## Abstract
Long horizon agentic tasks are now pushing LLM agents past their context window. To continue the task, the agent scaffold has to free up the context window, a process known as context compaction. Compaction is generally lossy by design: agents can silently lose task constraints, instructions, or their reasoning behind earlier decisions. Although compaction is a standard component of coding agent scaffolds, it has not been studied systematically with frontier models on realistic, long horizon agentic tasks. Previous work evaluate smaller open weight models on toy or synthetic trajectories. We fix the agent scaffold (OpenCode), implement five compaction strategies inside it, and evaluate three frontier models on three long horizon benchmarks (PaperBench, ProgramBench, PostTrainBench). For the two 1M context models, the compaction threshold does not measurably affect the task performance, whereas GPT-5.3-Codex, the model with the smallest context window, performs worse at lower thresholds on PaperBench and, less clearly, on PostTrainBench. No compaction method outperforms default self-summarization, and methods that discard more content cost some models up to 20 points while leaving other models the same. Compaction can, however, silently remove task constraints: on ProgramBench, the first compaction summary already drops about one third of the task's anticheating rules on average, and this rises monotonically with the number of compactions. On real user-agent sessions from SWE-chat, instructions about how the agent should work and what it should not do are dropped around 6 times more than specifications of what to build. We argue that current benchmarks are compaction-friendly: i.e., the objective is fixed and the agent's progress stays on disk, so most of what compaction discards can be recovered, except constraints that don't exist anywhere else.

## Metadata
- **Published**: 2026-10-22T18:15:54Z
- **Authors**: Jeanne Salle, Hardik Bhatnagar, Matthias Bethge, Sahar Abdelnabi, Maksym Andriushchenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31778v1)