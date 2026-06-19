---

title: "Summary: AdaCodec: A Predictive Visual Code for Video MLLMs"
url: http://arxiv.org/abs/2606.02569v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-01_17-56-35Z_AdaCodec_APredictiveVisualCodeforVideoMLLMs.md
generated_at: "2026-06-11 10:51"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces AdaCodec, a predictive visual code that reduces redundant video token usage in multimodal large language models by transmitting full frames only when necessary and otherwise encoding inter‑frame changes as compact tokens. Across eleven benchmarks it matches or exceeds per‑frame RGB baselines while using fewer visual tokens.

## Key Takeaways
- AdaCodec replaces full RGB frames with P‑tokens that describe motion and prediction residuals, saving visual token budget.
- It uses a conditional predictive cost to decide when to send a reference frame versus compact change description.
- On long videos it outperforms 224k‑token baselines at one seventh of the token budget.

## Context
Video multimodal models currently treat each frame independently, ignoring temporal redundancy and causing inefficient token usage. This work proposes a smarter interface that leverages prediction confidence to compress visual information.

## Implications
The approach lowers latency for video generation by cutting time‑to‑first‑token from 9.26s to 1.62s on general videos. It also reduces compute cost, making large‑scale video LLMs more scalable and accessible.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.02569v1)
