# Summary: 2026-08-31_03-04-30Z_A_XK2TechnicalReport.md
Saved: 2026-08-31 21:35
Source: 2026-08-31_03-04-30Z_A_XK2TechnicalReport.md
Model: None
Canonical original paper: [http://arxiv.org/abs/2608.30181v1](http://arxiv.org/abs/2608.30181v1)

---

## Summary  
A.X K2 is a 688‑billion‑parameter Mixture‑of‑Experts (MoE) language model created specifically for agentic applications, trained on roughly 8.5 trillion tokens using a higher‑quality mixture that emphasizes agentic and software‑engineering data; it improves over its predecessor A.X K1 by more than 30 percentage points on several benchmarks, demonstrating large gains in token efficiency. The paper introduces Sparse Gated Attention (SGA) with an indexer warmup that optimizes a sparse top‑k selection, allowing queries to read only 2,048 positions while preserving long‑context quality, and it adds Gated Norm (GN) for outlier suppression that enables 4‑bit NVFP4 serving within one point of FP8 accuracy. A Think‑Fusion recipe further lets users toggle between thinking and non‑thinking modes inside a single unified model.

## Key Contributions  
- Sparse Gated Attention (SGA) architecture with an indexer warmup that reduces query read cost to 2,048 positions while maintaining long‑context quality.  
- Gated Norm (GN) for outlier suppression, allowing 4‑bit NVFP4 serving within one point of FP8 accuracy.  
- Think‑Fusion recipe enabling unified switching between thinking and non‑thinking modes within the same model.

## Methodology  
The authors trained A.X K2 from scratch using a MoE design that focuses on high‑quality data, including expanded agentic and software‑engineering corpora. They employed SGA for long‑context modeling with sparse attention and GN to stabilize training dynamics. Evaluation was conducted via the RULER benchmark up to 256 K token context length.

## Results  
A.X K2 scores 94.6 on RULER at a 256 K context window, outperforming A.X K1 by more than 30 percentage points on certain tasks and matching or exceeding open‑weight baselines on math and Korean‑language benchmarks. The model’s token efficiency is markedly improved, and the 4‑bit NVFP4 serving achieves accuracy within one point of FP8.

## Significance  
This work delivers a high‑performance MoE foundation for agentic AI that balances massive reasoning capability with efficient long‑context handling, making it suitable for deployment in resource‑constrained environments while preserving strong performance on complex reasoning tasks.

## Related Concepts  
Mixture‑of‑Experts (MoE), Sparse Gated Attention (SGA), Gated Norm (GN), Think‑Fusion, 4‑bit NVFP4 serving, RULER benchmark, long‑context modeling, token efficiency.
