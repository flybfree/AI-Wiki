---
title: Agency as a New Organizing Abstraction for Computer Science
url: http://arxiv.org/abs/2610.17410v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_21-21-21Z_AgencyasaNewOrganizingAbstractionforComputerScienc.md
generated_at: 2026-10-14 00:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper by Ian Foster argues that agentic AI systems—persistent, autonomous computational entities that pursue goals and interact with open environments—should not be understood merely as applications of foundation models but as a candidate new organizing abstraction for computer science. The author contends that what distinguishes modern agentic systems is their general-purpose, open-ended form, where systems synthesize courses of action from goals, observations, and memory without a pre-specified task-specific model. The paper identifies recurring failures in deployed agentic systems as symptoms of structural abstraction gaps across six dimensions rather than isolated engineering defects.

## Key Takeaways
- The paper draws a direct analogy between the "process" abstraction, which organized computation around executing programs, and "agency," which organizes computation around pursuing goals under bounded resources. This reframing elevates agency from an AI modeling concept to a systems-level abstraction comparable in foundational importance to process, threads, or objects in computer science history.
- The author identifies six specific dimensions where structural abstraction gaps manifest: execution, interfaces, correctness, oversight, coordination, and persistence. Recurring failures such as runaway resource consumption, behavior redirected by adversarial content, and opaque continuous operation are argued to be symptoms of these gaps rather than isolated bugs that can be patched individually.
- The novelty is not the concept of an agent or runtime policy generation per se, but the general-purpose, open-ended form in which systems can synthesize courses of action from goals, observations, and memory over tools and environments for which no complete task-specific model was specified in advance. Closing these gaps requires coordinated advances across systems research, not incremental fixes.

## Context
This paper arrives at a critical juncture where large-scale machine learning has enabled agentic AI systems that operate persistently and autonomously, yet the field largely frames them as downstream applications of foundation models. Foster's contribution is to challenge this framing by proposing agency as a first-class organizing abstraction in computer science, comparable to how process abstractions shaped operating systems and concurrency models. This matters because without a proper abstraction, the field lacks the conceptual vocabulary and architectural frameworks needed to reason about, verify, and govern these systems at scale.

## Implications
For practitioners and industry leaders deploying agentic systems, this reframing suggests that current failures—runaway costs, adversarial manipulation, opaque behavior—are not bugs to be patched but structural consequences of missing abstractions, meaning incremental engineering fixes will be insufficient. For the research community, the paper calls for coordinated advances in systems research to build the execution, correctness, oversight, and coordination frameworks that agency as an abstraction demands, potentially reshaping curricula, tooling, and evaluation standards across computer science.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17410v1)
