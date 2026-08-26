---
title: Beyond Accuracy: A Dual-Judge Evaluation Protocol for Vision-Language Models in Legally Grounded Tasks
published: 2026-08-25T08:49:46Z
authors: Su Myat Noe, Ha Thanh Nguyen, May Myo Zin, Ken Satoh
url: http://arxiv.org/abs/2608.24258v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Accuracy: A Dual-Judge Evaluation Protocol for Vision-Language Models in Legally Grounded Tasks

## Abstract
AI systems are increasingly evaluated for legally accountable settings, where correct outputs must also be justifiable against an applicable legal standard. Existing legal-AI benchmarks and LLM-as-judge protocols provide important infrastructure for measuring task performance and open-ended response quality. We contribute one additional evaluation signal: a dual-judge protocol that pairs a standard 0-10 quality judge with a strict binary semantic-equivalence judge against a human-curated reference.   We study a controlled, visually grounded regulatory task - UK traffic-sign interpretation, whose meaning is a codified question with a known reference for every input - and measure not merely whether the two judges disagree (by construction they must) but how much and where. On 4,680 evaluations under seven visibility levels and two occlusion modes, the two judges are moderately associated (point-biserial r = 0.644), while revealing an asymmetric Type II pattern affecting 8.0% of all evaluations.   Its distribution is instructive: the marginal rate peaks at high visibility (14.2% at v = 0.8) simply because high-scoring answers are common there, but conditioned on the answer already scoring above 7, the rate is highest under heavy occlusion (54-63% at v <= 0.3), so a high quality score is least trustworthy when the input is most degraded.   We are explicit that the signal is a property of this judge and reference: a 49-row human check shows the 0-10 judge aligns closely with everyday-reader judgement (Pearson r = 0.81; r = 0.80 with the LLM accuracy sub-score), while the equivalence judge is fairly but one-directionally stricter. The protocol adds one LLM call per evaluation and surfaces a signal single-judge protocols do not report. We release the prompt template, occluded variants, and full evaluation results.

## Metadata
- **Published**: 2026-08-25T08:49:46Z
- **Authors**: Su Myat Noe, Ha Thanh Nguyen, May Myo Zin, Ken Satoh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24258v1)