---
title: MoganBert-TR: A Turkish Encoder Foundation Model Trained from Scratch with a CLM-to-MLM Curriculum
url: http://arxiv.org/abs/2608.25768v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_13-12-51Z_MoganBert_TR_ATurkishEncoderFoundationModelTrained.md
generated_at: 2026-08-26 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents MoganBert-TR, a 149M‑parameter Turkish encoder foundation model trained from scratch on a language‑specific corpus using a two‑stage CLM‑to‑MLM curriculum. The model achieves significantly higher performance than pure MLM on Turkish retrieval and benchmark suites, with improvements attributed to embedding geometry and extended long‑context handling.

## Key Takeaways
- The CLM‑to‑MLM curriculum yields 2.7–3.7× better recall on the MS MARCO Turkish dataset compared with a baseline pure MLM model, indicating that early causal modeling preserves useful token order information.
- Embedding geometry analysis shows a single direction captures 28.1% variance under the curriculum versus only 11.9% for pure MLM, highlighting how training objectives shape vector space structure.
- Long‑context extension and learning‑rate decay are split into two branches after a shared prefix; extending context to 1024 tokens improves TrGLUE scores by 0.49 points while the model‑soup alternative gains only 0.75 points at a modest cost.

## Context
The work addresses a gap in Turkish NLP where encoder models rely on generic MLM objectives, limiting language‑specific adaptation and long‑range understanding. By training from scratch with curriculum strategies, MoganBert‑TR demonstrates that domain‑aware pretraining can outperform fine‑tuned foreign models without heavy transfer.

## Implications
For developers building Turkish applications, the model offers a lightweight yet powerful alternative to large multilingual backbones, reducing computational cost while preserving high retrieval accuracy. Its architecture also provides insights into how curriculum design influences embedding quality, guiding future research on language‑specific foundation learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25768v1)
