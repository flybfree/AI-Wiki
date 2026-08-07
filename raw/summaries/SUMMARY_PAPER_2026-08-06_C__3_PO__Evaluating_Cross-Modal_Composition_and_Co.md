---
title: C$^3$PO: Evaluating Cross-Modal Composition and Counterfactual Performance in Omnimodal Models
url: http://arxiv.org/abs/2608.05381v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_20-04-05Z_C__3_PO_EvaluatingCross_ModalCompositionandCounter.md
generated_at: 2026-08-06 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces C$^3$PO as a benchmark for evaluating cross‑modal composition and counterfactual performance in multimodal large language models, revealing that human accuracy reaches 88.64% while the best model (Gemini-3.1-Pro) achieves only 73.17%. Attention analysis shows that failures are largely caused by modality dominance, with most attention concentrated on text.

## Key Takeaways
- Human accuracy 88.64% while Gemini‑3.1‑Pro reaches only 73.17%, indicating a significant gap due to reliance on one modality.
- Attention probes reveal 86‑95% of failures stem from models committing to a single modality and ignoring contradictory evidence, with 87‑95% attention directed at text.
- Mid‑layer attention entropy predicts correctness: sustained exploration leads to success, while premature collapse results in failure.

## Context
Multimodal LLMs often treat dominant modalities such as text as primary sources, leading to brittle reasoning across video, audio, image and text inputs. This paper fills a gap by providing a structured benchmark that isolates composition versus conflict tasks within multimodal systems.

## Implications
The 56‑point accuracy gap underscores that performance depends on the structural roles of modalities rather than mere combinations. Practitioners must design architectures that enforce sustained cross‑modal attention to prevent premature collapse and improve robust reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05381v1)
