---
title: Tied Trit-Planes: Constraining PTQTP to a Uniform Nine-Level Quantizer, with a Persistent Folded Format for Disk-Streamed Mixture-of-Experts Serving
url: http://arxiv.org/abs/2608.08910v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-09_20-53-47Z_TiedTrit_Planes_ConstrainingPTQTPtoaUniformNine_Le.md
generated_at: 2026-08-10 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents PTQTP constrained to a uniform nine‑level quantizer, which collapses two ternary planes into a single 4‑bit code plane for lossless serving. Applied to the DeepSeek‑V4‑Flash‑0731 mixture‑of‑experts model, it matches the official API on most fixtures while delivering faster decode and smaller storage.

## Key Takeaways
- Tying the two free per‑group scales to a fixed ratio of three yields a single uniform nine‑level quantizer that simplifies PTQTP’s solver.  
- The two trit planes fold losslessly into one 4‑bit code plane, creating a persistent serving representation where disk bytes, expert‑cache bytes and kernel input are identical 4.0625‑bits/weight blocks consumed in one integer dot pass.  
- This approach matches the official serving API on 5 of 5 fixtures at step 0 (vs 4/5 for Q4_K), captures 12 of 14 continuation steps (vs 11/14) and scores 86 vs 84 on MMLU, while reducing file size by 9% with no fidelity loss at small evaluation sizes.

## Context
Large mixture‑of‑experts models require efficient storage and low‑latency inference, yet standard quantization often sacrifices quality for memory savings. This work demonstrates that a uniform nine‑level quantizer can preserve both performance and compactness, enabling disk‑streamed serving on consumer hardware without explicit trade‑offs.

## Implications
Practitioners can deploy high‑fidelity LLMs with reduced storage footprints and faster inference cycles, especially on limited resources like laptops. The open‑source code and persistent byte format encourage broader adoption across the AI community for efficient model serving.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08910v1)
