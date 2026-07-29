# Summary: 2026-07-28_11-12-03Z_HowSmallCanYouGo_AControlledStudyofLoRARank_Target.md
Saved: 2026-07-28 20:29
Source: 2026-07-28_11-12-03Z_HowSmallCanYouGo_AControlledStudyofLoRARank_Target.md
Model: None

---

## Summary  
The paper investigates how much task accuracy is sacrificed when applying parameter‑efficient fine‑tuning (PEFT) and low‑bit quantization to a 60 M‑parameter encoder‑decoder model (T5‑small) on the single‑table WikiSQL benchmark. It conducts a controlled, single‑variable study varying LoRA rank, the set of adapted modules, and numerical precision to quantify each efficiency knob’s cost. The goal is to demonstrate that high accuracy can be achieved with minimal parameter overhead and reduced memory consumption. By framing adaptation as a constrained trade‑off rather than an absolute accuracy target, the authors provide actionable guidance for deployment scenarios.

## Key Contributions  
- Finding 1: LoRA rank = 16 recovers within 11.6 percentage points of full fine‑tuning accuracy (59.6 % vs. 71.2 % exact‑match) while training fewer than 1 % of parameters and consuming 31 % less peak GPU memory.  
- Finding 2: QLoRA with INT8 or NF4 quantization achieves comparable accuracy (52.8 % and 53.2 %) at a dramatically lower memory cost of only 0.60 GB each, highlighting a strong trade‑off for memory‑constrained deployments.  
- Finding 3: Increasing LoRA rank beyond 16 yields no measurable accuracy gain; the optimal rank is capped at 16 within this model size.

## Methodology  
The authors employ a systematic experiment on T5‑small, varying LoRA rank (2, 4, 8, 16, 32), testing each possible target module (attention layers) and applying QLoRA with INT8 and NF4 quantization. All runs are reproducible; the study measures task accuracy alongside system metrics such as trainable parameters, peak training memory, inference latency, and throughput to frame adaptation as a constrained trade‑off.

## Results  
Full fine‑tuning yields 71.2 % exact‑match on WikiSQL. LoRA with r=16 reaches 59.6 % accuracy, using <0.01 M trainable parameters and reducing peak memory by 31 %. QLoRA with INT8 achieves 52.8 % and NF4 quantization 53.2 %, each requiring only 0.60 GB GPU memory. System‑level metrics show latency and throughput improvements, confirming that efficiency gains are realized without sacrificing meaningful performance.

## Significance  
These findings prove that high‑quality text‑to‑SQL adaptation can be performed with a tiny fraction of the parameters and memory required for full fine‑tuning, making large language models viable on edge devices or low‑power servers. The study provides concrete guidance for practitioners seeking to balance accuracy, compute, and storage constraints in real‑world deployments.

## Related Concepts  
PEFT (Parameter‑Efficient Fine‑Tuning), LoRA (Low‑Rank Adaptation), QLoRA (Quantized LoRA), INT8 quantization, NF4 quantization, trainable parameters, peak GPU memory, inference latency, throughput, exact‑match accuracy on WikiSQL.
