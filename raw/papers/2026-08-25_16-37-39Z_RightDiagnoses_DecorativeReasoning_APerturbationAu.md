---
title: Right Diagnoses, Decorative Reasoning:A Perturbation Audit of Medical Chain-of-Thought
published: 2026-08-25T16:37:39Z
authors: Mengzhu Xu, Jifan Gao, Xia Jiang, Yaoxin Wu, Xi Long
url: http://arxiv.org/abs/2608.24790v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Right Diagnoses, Decorative Reasoning:A Perturbation Audit of Medical Chain-of-Thought

## Abstract
Clinicians read chain-of-thought (CoT) rationales as evidence of medical reasoning, but whether the visible chain plays that role is rarely tested. General-domain CoT-faithfulness probes ignore clinical cost, and medical LLM evaluations treat the chain as a black box. We close this gap with a medical perturbation audit: a 30-operator battery edits both the chain and the question with clinically motivated operators (severity reversal, negation flip, demographic swap, evidence ablation), paired with a chain-update times answer-flip joint analysis that classifies each model by its failure mode. Applied to 14 LLMs on four medical QA benchmarks, three independent tests converge: the Chain-Decoupling Rate (CDR; chain does not register the edit and the answer does not flip) is 72.9% panel-wide on clinically meaningful destructive edits, chain corruption leaves accuracy unchanged, and removing CoT prompting does not reduce accuracy. Two board-certified clinicians re-annotate N=197 perturbed questions; 98.5% leave the gold defensible. The pattern holds across medical and reasoning fine-tuning and scale; on the closed-source tier, where the chain text is unavailable, the answer-side signals are consistent with the same decoupling. Our framework and CDR provide a reusable yardstick for auditing whether medical CoT is faithful or merely documentation.

## Metadata
- **Published**: 2026-08-25T16:37:39Z
- **Authors**: Mengzhu Xu, Jifan Gao, Xia Jiang, Yaoxin Wu, Xi Long
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24790v1)