---
title: Guiding AI Agents to Generate Conjectures by Encoding How Theorems Build on One Another
url: http://arxiv.org/abs/2611.19108v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-14_02-42-34Z_GuidingAIAgentstoGenerateConjecturesbyEncodingHowT.md
generated_at: 2026-11-16 21:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Theorem Evolution Graph (TEG), a structured graph representation that encodes how mathematical theorems build upon one another through modifications, strengthenings, and extensions, and uses it as a search framework for LLM agents to generate novel mathematical conjectures. The authors demonstrate that TEG-guided conjecture generation is preferred by both LLM judges and an expert mathematician over an unconstrained baseline, with TEG outputs scoring higher on significance, ambition, and insight while baseline outputs retain an edge on plausibility.

## Key Takeaways
- The TEG is constructed in two explicit steps: first, an agent identifies relevant theorems by traversing citation graphs backward and forward from a seed paper, and second, it compares those theorems pairwise to record structural relationships such as hypothesis modification, conclusion strengthening, or scope extension. This two-stage pipeline transforms unstructured literature into a directed relational structure that an LLM agent can query to propose conjectures that are grounded in actual mathematical progress.
- Evaluation by both LLM judges and a human mathematician showed a clear preference split: TEG-generated conjectures were favored for significance, ambition, and insight, while unconstrained baseline conjectures were preferred for plausibility. This split suggests that encoding theorem-to-theorem relationships pushes agents toward bolder, more creative hypotheses at the cost of some immediate verifiability, a tradeoff that mirrors how human mathematicians often prioritize ambitious conjectures.
- Ablation experiments indicate that the benefit of constructing and using a TEG persists even when the pool of available papers is held fixed, implying that the value lies in the relational encoding itself rather than in discovering additional source material. This finding strengthens the case for TEG as a reasoning scaffold independent of retrieval breadth.

## Context
Recent LLM-based mathematics research has concentrated heavily on proving existing open conjectures, leaving the harder and less formalized problem of deciding what to conjecture comparatively unexplored. By formalizing the intuition that theorems evolve incrementally—through hypothesis relaxation, conclusion strengthening, or domain extension—the authors provide a concrete, machine-actionable structure that bridges the gap between literature retrieval and creative mathematical reasoning. This positions the work at the intersection of automated theorem proving, citation-graph analysis, and LLM agent design, a space where structured reasoning scaffolds are increasingly seen as necessary for reliable AI-assisted discovery.

## Implications
For AI research practitioners, the TEG framework offers a transferable template for any domain where knowledge accumulates through incremental modification of prior results, from software engineering to legal reasoning to scientific hypothesis generation. For the mathematics community, it suggests a practical workflow in which agents can propose conjectures that are both grounded in existing literature and ambitious enough to extend it, potentially accelerating the pipeline from published results to new open problems. The observed tension between plausibility and ambition also highlights a design challenge for future systems: balancing creative reach against immediate verifiability when guiding autonomous research agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.19108v1)
