---
title: Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game
url: http://arxiv.org/abs/2611.14487v1
type: paper-summary
date: 2026-11-11
source_paper: 2026-11-10_18-47-22Z_Re_Search_DissectingLLMIdeationThroughaTwo_PlayerQ.md
generated_at: 2026-11-11 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Re-Search, a novel evaluation framework that adapts the Twenty Questions game format to study how large language models generate and refine research ideas iteratively. Built from 200 ICML 2026 papers, the framework requires an LLM to rediscover a published paper's core idea by asking yes-or-no questions and receiving binary oracle feedback, thereby isolating the ideation process from execution. The central finding is that the bottleneck in LLM ideation is generation rather than judgment: models can recognize good ideas and good questions when presented to them, but struggle to produce them independently, with most progress occurring within the first 30 of 100 questions before plateauing.

## Key Takeaways
- Nearly all meaningful progress in the ideation game happens within the first 30 questions out of 100, after which most models plateau. This suggests that LLMs quickly exhaust their initial search heuristics and lack mechanisms for sustained, productive exploration over longer horizons, raising concerns about the depth of autonomous research ideation these models can achieve.
- Through controlled interventions on candidate questions and the hypothesis space, the authors demonstrate that the core bottleneck is generation, not judgment. Models reliably identify a good idea or a good question when one is offered to them, but they frequently cannot produce such ideas on their own. This distinction between recognition and generation capability is critical for understanding where current LLMs fall short in creative research tasks.
- Analysis of ideation traces reveals two distinct failure modes: models either over-exploit a single direction, getting stuck in a narrow line of inquiry, or over-explore too many directions without committing to a productive path. These failure patterns point to concrete design principles for future autoresearch systems, specifically that enriching the search with externally sourced ideas and questions may be more effective than trying to improve a single model's generation ability.

## Context
Research ideation in academia is inherently iterative, involving cycles of hypothesis generation, feedback, and refinement. Existing LLM benchmarks for research tasks typically evaluate final outputs or execution quality, obscuring the search process itself and making it difficult to diagnose where models struggle. Re-Search fills this gap by creating a controlled, step-by-step evaluation that separates idea generation from downstream execution, offering a diagnostic lens that the field currently lacks. The work sits at the intersection of LLM evaluation methodology, creative problem-solving, and the emerging subfield of autonomous research systems, providing a structured way to probe the generative limits of frontier models.

## Implications
For practitioners building autonomous research assistants or autoresearch pipelines, the findings suggest that investing in external idea sources, curated question banks, and multi-agent search strategies will likely yield greater gains than fine-tuning a single model's generative capacity. The recognition-versus-generation gap implies that hybrid architectures—where one component proposes candidates and another evaluates them—could substantially outperform monolithic generation approaches. For the broader AI research community, this work provides a reproducible, fine-grained evaluation tool that can guide the design of next-generation systems intended to assist or automate scientific discovery.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.14487v1)
