---
title: Fine-Tuning Qwen3-27B for C-to-Rust Code Translation: A Three-Stage Curriculum of Pretraining, Debugging-Aware SFT, and Task-Specific SFT
url: http://arxiv.org/abs/2608.13681v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_18-24-02Z_Fine_TuningQwen3_27BforC_to_RustCodeTranslation_AT.md
generated_at: 2026-08-16 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces a three‑stage curriculum for fine‑tuning Qwen3‑27B to translate C code into safe Rust while preserving functionality. The stages include pretraining on Rust corpora, supervised fine‑tuning with debugging data, and task‑specific SFT using LeetCode pairs. Evaluation via SACTOR shows improved success rates, idiomaticity, and reduced unsafe code compared to baselines.

## Key Takeaways  
- Continued pretraining on Rust corpora strengthens the model’s prior over idiomatic syntax and standard‑library usage.  
- Supervised fine‑tuning with Microsoft/Verus_Training_Data instills debugging and self‑repair behavior in generated Rust code.  
- Task‑specific SFT on LeetCode C/Rust pairs teaches direct semantic translation, boosting overall performance.

## Context  
LLMs can generate code but often lack the specialized knowledge needed for cross‑language translation tasks like C to Rust. Fine‑tuning approaches that ignore domain‑specific data or debugging feedback typically produce verbose or unsafe output, limiting practical deployment in safety‑critical systems.

## Implications  
The curriculum demonstrates a systematic way to align large language models with low‑level programming constraints, offering a template for other cross‑language translation tasks. Practitioners can leverage this framework to reduce manual code review effort and improve reliability of generated Rust implementations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13681v1)
