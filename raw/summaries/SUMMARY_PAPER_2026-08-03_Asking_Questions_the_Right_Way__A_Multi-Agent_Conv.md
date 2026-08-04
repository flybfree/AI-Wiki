---
title: Asking Questions the Right Way: A Multi-Agent Conversational System for Prompt Formulation in Complex Task Resolution
url: http://arxiv.org/abs/2608.01366v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_16-33-27Z_AskingQuestionstheRightWay_AMulti_AgentConversatio.md
generated_at: 2026-08-03 23:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PAWNI, a multi‑agent conversational system that converts unstructured user queries into structured prompts by guiding users through iterative question‑and‑answer dialogue using an evolving knowledge base. Evaluation across four complex tasks showed that PAWNI-generated prompts contained 42 % to 91 % of the assessed prompt elements, LLM outputs improved in all quality dimensions, and participants experienced lower cognitive load (NASA‑TLX score 39.6 vs. 21.7). Crucially, every participant achieved satisfactory output in a single turn, whereas unaided attempts required between one and twelve turns.

## Key Takeaways
- PAWNI optimizes the question itself by front‑loading intent clarification rather than optimizing the model response.
- Structured prompts produced by PAWNI contain up to 91 % of the assessed prompt elements, significantly increasing completeness.
- Participants reported a NASA‑TLX workload reduction from 21.7 to 39.6 and higher perceived output quality.

## Context
Large language models rely heavily on user‑provided prompts, yet iterative prompting often degrades context and reduces cognitive returns. Existing approaches focus on refining model outputs rather than improving prompt formulation, limiting the impact of human‑AI interaction efficiency.

## Implications
Optimizing prompt formulation at the front end can streamline complex task resolution, enabling single‑turn solutions that reduce user effort and improve output quality. This approach holds promise for industry adoption where rapid, high‑quality AI interactions are essential.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01366v1)
