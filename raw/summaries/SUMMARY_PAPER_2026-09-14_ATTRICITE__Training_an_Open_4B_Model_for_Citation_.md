---
title: ATTRICITE: Training an Open 4B Model for Citation Recovery toward Faithful Attribution
url: http://arxiv.org/abs/2609.14248v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-13_02-55-38Z_ATTRICITE_TraininganOpen4BModelforCitationRecovery.md
generated_at: 2026-09-14 21:24
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces ATTRICITE, an open-source 4B-parameter model specifically trained for citation recovery within the CiteGuard retrieval environment. The authors address the critical challenge of faithful attribution by developing a system capable of identifying the intended source paper from citation-bearing scientific passages. Through controlled evaluations on a newly constructed benchmark subset, they demonstrate that GRPO fine-tuning significantly boosts target-match accuracy while enabling competitive performance against larger proprietary models.

## Key Takeaways
- The authors introduce CITEALIGN, a curated dataset of 7,607 computer science instances drawn from recent literature, alongside a strictly partitioned benchmark subset containing development data from 2024 and temporally held-out test data from 2025 to ensure rigorous temporal evaluation.
- GRPO fine-tuning elevates the baseline Qwen3-4B model’s target-match accuracy from 49.4% to 59.8%, representing a substantial 10.4 percentage point improvement across multiple inference runs conducted at an temperature of 0.7.
- Despite its compact parameter count, ATTRICITE surpasses gpt-oss-20b and approaches GPT-5.4-mini’s performance by only 3.9 points, though Gemma 4 31B IT currently leads the benchmark at 72.0%, highlighting both rapid progress and remaining gaps in open scientific attribution tools.

## Context
Faithful citation attribution remains a persistent challenge in large language models, particularly as hallucinated or mismatched references undermine scientific reproducibility and scholarly trust. While retrieval-augmented frameworks have improved source grounding, specialized training for precise source identification within controlled environments like CiteGuard is still emerging. This work bridges that gap by focusing on tool-using architectures optimized specifically for recovering author-intended citations rather than generating plausible but incorrect references.

## Implications
The successful fine-tuning of a 4B parameter model demonstrates that highly specialized, open-weight architectures can rival or approach proprietary systems in domain-specific attribution tasks. By publicly releasing both the trained model and its data collection pipeline, the authors provide a reproducible foundation for researchers aiming to build reliable citation verification tools. This advancement encourages broader adoption of transparent, auditable AI systems in academic publishing and scientific literature analysis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14248v1)
