---

title: "AlignAtt4LLM: Fast AlignAtt for Decoder-Only LLMs at IWSLT 2026 Simultaneous Speech Translation Task"
url: http://arxiv.org/abs/2606.03967v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-02_17-52-18Z_AlignAtt4LLM_FastAlignAttforDecoder_OnlyLLMsatIWSL.md
generated_at: "2026-06-11 10:51"
model: nvidia/nemotron-3-nano-4b

---


## Summary
AlignAtt4LLM introduces a decoder‑only simultaneous speech translation system for English to German, Italian and Chinese that leverages Qwen3‑ASR with forced alignment and Gemma‑4 E4B‑it under an AlignAtt policy. The method achieves state‑of‑the‑art results on the IWSLT 2026 development set, outperforming baselines in both low‑latency (≈2 s) and high‑latency (≤4 s CU‑LongYAAL) regimes.

## Key Takeaways
- The system replaces encoder‑decoder cross‑attention with a deterministic prompt layout that explicitly marks source spans, enabling alignment without relying on the missing cross‑attention.
- Offline selection of translation‑specific attention heads and selective replay of the draft‑to‑source block reduces computational cost while preserving output fidelity.
- Runtime query/key capture ensures bit‑identical model outputs, allowing reuse of AlignAtt for stronger decoder‑only MT backbones on non‑European targets.

## Context
This work demonstrates that alignment strategies can be adapted to pure decoder models, a trend toward lightweight, low‑latency translation in real‑time settings. It highlights the flexibility of prompt engineering and attention control as key enablers for efficient multilingual AI services.

## Implications
For industry practitioners, AlignAtt4LLM offers a template for deploying fast, high‑quality simultaneous translation without costly encoder components. Practitioners can integrate similar alignment policies into existing decoder‑only pipelines to meet latency constraints across diverse language pairs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.03967v1)
