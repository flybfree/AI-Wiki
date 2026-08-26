---
title: SAGE: From Direct Answering to Evidence-Grounded Inference for Chinese Ancient Document Understanding
url: http://arxiv.org/abs/2608.24011v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_03-01-51Z_SAGE_FromDirectAnsweringtoEvidence_GroundedInferen.md
generated_at: 2026-08-25 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces SAGE, an evidence‑grounded multi‑agent framework for Chinese ancient document understanding that reformulates the task as inference rather than direct answer generation. Experiments on AncientDoc show that SAGE consistently outperforms matched direct‑answering baselines across three LVLM backbones and even surpasses larger monolithic models.

## Key Takeaways  
- SAGE uses specialized agents for planning, evidence acquisition, claim verification, and bounded replanning within a shared‑state runtime to enable bounded evidence seeking.  
- The framework supports answer revision and abstention when grounding is insufficient.  
- Experiments demonstrate consistent improvement over direct‑answering baselines on AncientDoc across three LVLM backbones.

## Context  
Large Vision‑Language Models have been applied to document understanding but often produce overconfident, weakly grounded answers due to single‑pass generation. This work addresses the need for structured reasoning and evidence grounding in historical text analysis.

## Implications  
The results suggest that modular, evidence‑grounded inference can outperform scaling alone in complex tasks like Chinese ancient documents. Practitioners may adopt multi‑agent approaches to improve reliability and reduce hallucinations in heritage data processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24011v1)
