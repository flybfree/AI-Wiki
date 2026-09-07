---
title: Knowing What Not to Answer: Selective Non-Compliance in Vision-Language Models
url: http://arxiv.org/abs/2609.04720v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-04_04-45-26Z_KnowingWhatNottoAnswer_SelectiveNon_ComplianceinVi.md
generated_at: 2026-09-06 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces KoNA, a benchmark for evaluating selective non-compliance in vision-language models across five categories of queries where partial compliance is needed. It demonstrates that current models often fail to refuse or correct appropriately when queries contain both answerable and non-answerable parts. Fine-tuning on KoNA improves non‑compliance accuracy while preserving performance on fully answerable tasks.

## Key Takeaways
- The benchmark separates query-level and component-level non-compliance, revealing that models treat whole queries as binary rather than handling mixed content.
- Fine-tuning with selective examples yields substantial gains in refusal or correction rates without hurting answerability on fully answerable tasks.
- The study demonstrates that current VLMs cannot reliably distinguish between safe answerable components and unsafe ones requiring abstention.

## Context
Vision-language models aim to be helpful yet responsible, but existing evaluation frameworks ignore the nuance of mixed queries. This limitation hampers progress toward truly adaptive and ethically aligned AI systems.

## Implications
Practitioners must adopt benchmarks that capture selective non-compliance to guide model training. Future research should focus on component-aware responses to improve safety and utility in real-world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04720v1)
