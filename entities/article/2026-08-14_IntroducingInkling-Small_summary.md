# Summary: 2026-08-14_IntroducingInkling-Small.md
Saved: 2026-08-14 00:14
Source: 2026-08-14_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts (MoE) transformer that delivers performance comparable to its larger sibling Inkling while using only a quarter of the total parameters. By leveraging 276 B total parameters with just 12 B active, it runs on NVIDIA GB300 NVL72 hardware and supports audio‑image reasoning, variable thinking effort, and a 1 M‑token context window, achieving strong results across Terminal‑Bench 2.1, HLE (text‑only), and IFBench benchmarks.

## Key Takeaways  
- **Parameter efficiency:** Inkling‑Small’s 276 B total parameters (vs. Inkling’s 975 B) cut compute roughly to a quarter while preserving comparable reasoning ability.  
- **MoE cost reduction:** Only 12 B active parameters are engaged per inference, dramatically lowering TFLOPs and dollar‑per‑sample costs relative to full‑parameter models.  
- **Adaptive thinking effort:** The variable‑effort design lets users tune the model’s reasoning depth on a per‑task basis, balancing performance and expense.

## Context  
The release reflects a growing industry focus on compressing massive transformer architectures through MoE techniques and open‑weight distribution. Competing models such as Nemotron 3 Super/Ultra, DeepSeek V4 Flash, Qwen3.5‑A17B, MiMo V2.5, Minimax M2.7, Kimi K2.5/2.6, GLM 5.2, and gpt‑oss‑120b illustrate a crowded landscape where efficiency, cost, and accessibility are critical evaluation criteria.

## Implications  
This work proves that cutting‑edge reasoning can be achieved with far less hardware and cloud spend, encouraging developers to adopt smaller, more sustainable models for real‑world applications. It also sets a benchmark for open‑weight MoE performance, potentially reshaping market dynamics by lowering entry barriers and enabling broader deployment of advanced AI capabilities.
