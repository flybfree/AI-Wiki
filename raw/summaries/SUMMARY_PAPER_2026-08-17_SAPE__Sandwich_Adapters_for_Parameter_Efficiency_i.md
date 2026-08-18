---
title: SAPE: Sandwich Adapters for Parameter Efficiency in Large Language Model Fine-Tuning
url: http://arxiv.org/abs/2608.15360v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_18-32-47Z_SAPE_SandwichAdaptersforParameterEfficiencyinLarge.md
generated_at: 2026-08-17 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SAPE, a sandwich‑style parameter sharing method for PEFT that reduces memory and avoids dynamic masking overhead while preserving performance on encoder‑only and causal decoder models. Experiments show SAPE reaches state‑of‑the‑art results with only 10 % of the baseline’s parameters, outperforming AdaLoRA by up to 4.85 % on GSM8K.

## Key Takeaways
- SAPE employs hard weight sharing across intermediate Transformer layers while keeping input embeddings and final projections isolated to prevent gradient interference.
- The sandwich topology achieves lower memory consumption than uniform or dynamic sharing methods without sacrificing convergence speed.
- On LLaMA‑3.2 under a 0.6 M parameter budget, SAPE improves GSM8K by 4.85 % and CommonsenseQA by 3.11 %, surpassing AdaLoRA.

## Context
Parameter‑efficient fine‑tuning has become essential for deploying large language models on limited hardware, yet most sharing strategies either hinder convergence or incur extra computation. SAPE addresses this tension by leveraging the hierarchical structure of Transformers to share parameters in a static, sandwich fashion, offering a more efficient alternative.

## Implications
For researchers, SAPE provides a clear path to further reduce parameter budgets while maintaining strong performance on both NLP tasks and reasoning benchmarks. Practitioners can adopt this topology to deploy models like LLaMA‑3.2 at scale with minimal hardware cost, accelerating real‑world applications that require low‑resource fine‑tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15360v1)
