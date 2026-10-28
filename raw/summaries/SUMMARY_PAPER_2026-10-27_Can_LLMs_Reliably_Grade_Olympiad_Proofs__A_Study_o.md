---
title: Can LLMs Reliably Grade Olympiad Proofs? A Study of Mathematical Verification with LLMs
url: http://arxiv.org/abs/2610.36767v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_07-28-08Z_CanLLMsReliablyGradeOlympiadProofs_AStudyofMathema.md
generated_at: 2026-10-27 20:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether Large Language Models can reliably grade Olympiad-level mathematical proofs, a task that demands meticulous verification of each claim in long reasoning chains. The authors introduce a human-curated dataset of USAMO 2025 candidate solutions with expert grading, conduct a comprehensive evaluation across 20 frontier models, and propose two novel contributions: TROJAN, an iterative self-critique pipeline for generating adversarial proofs, and MABGrader, a Multi-Armed Bandit framework that reframes grading as arm selection over a discrete score space. Their findings show that state-of-the-art models still leave considerable room for improvement, though MABGrader outperforms the prior SOTA ProofGrader by 26.4% in Quadratic Weighted Kappa and reduces grading error by 14%.

## Key Takeaways
- The authors constructed a human-curated dataset of USAMO 2025 candidate solutions annotated with expert grading, providing a rigorous benchmark for evaluating LLM-based proof verification. This addresses a critical gap, as Olympiad proofs require meticulous assessment of each claim in a long reasoning chain, making them fundamentally different from single-answer math problems where LLMs already perform well.
- A sweeping evaluation was conducted across 20 models spanning seven metrics, two prompt styles, three inference methods, and three prompt templates, revealing that even frontier models struggle with reliable proof grading. The authors also introduced TROJAN, an iterative self-critique pipeline designed to generate high-fidelity adversarial proofs at scale, pushing models to confront harder verification challenges.
- MABGrader reframes the grading task as a Multi-Armed Bandit problem over a discrete score space, a novel algorithmic approach that outperforms the previous state-of-the-art ProofGrader by 26.4% in Quadratic Weighted Kappa and reduces grading error by 14%, demonstrating that structured decision-theoretic frameworks can substantially improve automated proof assessment.

## Context
While LLMs have demonstrated remarkable capability in solving competition-level mathematics problems, the complementary task of verifying natural-language proofs remains significantly underexplored in the research community. Olympiad-level proofs involve long, multi-step reasoning chains where a single subtle error in a lemma or inequality can invalidate an entire solution, making verification a fundamentally harder task than generation. This paper sits at the intersection of automated theorem proving, educational assessment, and LLM evaluation, addressing a practical bottleneck where expert human inspection of proofs is costly and difficult to scale.

## Implications
For the field of automated mathematics and AI-assisted education, this work signals that current LLMs are not yet trustworthy as standalone proof graders, cautioning against premature deployment in high-stakes academic settings such as olympiad judging or university coursework. For practitioners, the MABGrader framework offers a concrete, reproducible method to improve automated grading accuracy, and the released dataset and code provide a foundation for future benchmarking. Industry stakeholders in EdTech and automated assessment could leverage these findings to design hybrid systems where LLMs assist rather than replace expert graders, reducing costs while maintaining reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36767v1)
