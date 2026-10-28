---
title: Clearing the FoG: Training KG Agents to Retrieve the Evidence Behind Their Answers
url: http://arxiv.org/abs/2610.37405v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_15-20-37Z_ClearingtheFoG_TrainingKGAgentstoRetrievetheEviden.md
generated_at: 2026-10-27 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces FoG, a training framework that addresses a critical gap in knowledge graph (KG) agents: while existing agents can produce correct answers, they fail to retrieve the supporting evidence (triples) that make those answers traceable and auditable. FoG combines evidence-grounded question synthesis, a KG interaction agent that records retrieved triples, and an evidence-coverage process reward (ECPR) that credits each supporting triple to the specific turn that first retrieves it. Experiments on three KGQA benchmarks show that small 3B–4B open-source agents trained with FoG outperform substantially larger baselines in both answer accuracy and evidence coverage, while also demonstrating zero-shot transfer across different knowledge graphs.

## Key Takeaways
- Existing KG agents treat knowledge graphs solely as answer sources, meaning their training data contains answers but not the supporting triples, and their reward signals evaluate only final answers rather than the evidence retrieval process. This leads to agents that answer correctly without actually retrieving or citing the underlying KG triples, undermining auditability and trustworthiness.
- FoG's evidence-grounded synthesis recursively hides explicit entities behind verifiable sub-questions, ensuring that every generated question inherently carries its supporting triples by construction. This structural design forces the agent to interact with the KG to uncover evidence rather than relying on parametric knowledge alone.
- The Evidence-Coverage Process Reward (ECPR) provides fine-grained, turn-level credit assignment: each supporting triple is credited to the specific interaction turn that first retrieves it. This process-level reward signal trains agents to actively seek and record evidence throughout multi-step reasoning, rather than merely optimizing for a correct final answer.

## Context
The broader AI landscape increasingly demands that language model outputs be verifiable and grounded in external sources, particularly in high-stakes domains like healthcare, law, and scientific research. Knowledge graphs have emerged as structured, auditable sources of factual evidence, yet the training paradigms for agents that interact with KGs have largely ignored the evidence-retrieval dimension. This paper sits at the intersection of retrieval-augmented generation, reinforcement learning with process rewards, and knowledge graph reasoning, addressing a fundamental trust and transparency gap in agentic AI systems.

## Implications
For practitioners building KG-augmented agents in production systems, FoG demonstrates that evidence grounding can be achieved with small, open-source models rather than expensive large proprietary models, dramatically lowering deployment costs while improving auditability. The zero-shot cross-KG transfer capability suggests that evidence-grounded training produces generalizable retrieval skills, making it practical for organizations that maintain multiple or evolving knowledge graphs. For the research community, the ECPR mechanism offers a template for process-level reward design in any agentic system where intermediate evidence retrieval matters as much as the final output.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37405v1)
