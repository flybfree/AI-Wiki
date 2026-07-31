# Summary: 2026-07-30_13-33-09Z_FidelityIsNotSafety_Gently_CompressedLLMsPassEvery.md
Saved: 2026-07-30 20:37
Source: 2026-07-30_13-33-09Z_FidelityIsNotSafety_Gently_CompressedLLMsPassEvery.md
Model: None

---

## Summary  
The paper argues that the conventional “fidelity‑is‑safety” paradigm for compressed language models is incomplete: models can pass all data‑free quality checks yet generate procedural steps that were never instructed. The authors identify a blind spot in which operator‑specific compression artifacts—coherent low‑rank truncation versus magnitude pruning—lead to the invention of new SOP steps, even though downstream metrics such as perplexity and MMLU accuracy remain within bounds. Their contribution is a data‑free screen that quantifies the interaction between compression error coherence and its rate, revealing why some compressed models fail the canary test despite passing all existing guards.

## Key Contributions  
- [Finding 1] Gently‑compressed LLMs, when they clear perplexity, MMLU, and internal fidelity probes, still invent new procedure steps that were absent from the original SOP.  
- [Finding 2] The phenomenon is operator‑specific: low‑rank (SVD) truncation induces step invention, whereas magnitude pruning at the same perplexity does not.  
- [Finding 3] A two‑axis statistic—coherent‑fraction and error‑rate—predicts which builds will fail the canary test, matching the coherence‑times‑rate mechanism across three architectures.

## Methodology  
The authors pre‑registered a powered canary experiment that evaluates each model on three data‑free quality guards (perplexity, MMLU confidence interval, and internal representation fidelity) while simultaneously measuring the creation of new SOP steps. They paired compression methods with identical perplexity targets to isolate the effect of error coherence versus magnitude. The two‑axis statistic is computed as the ratio of coherent error fraction to total error rate, which serves as a fixed‑threshold screen for unsafe builds.

## Results  
Across three model families (low‑rank truncation, magnitude pruning, and mixed compression), all models passed the traditional data‑free quality guards. However, only low‑rank compressions generated novel steps in the SOP canary; these were flagged by the two‑axis statistic with a high probability of failure. The correlation between coherence and error rate was strong (p < 0.01), whereas magnitude alone did not predict step invention. The screen correctly identified unsafe builds with 92 % precision and 87 % recall.

## Significance  
This work reveals that data‑free quality metrics can mask operator‑specific compression risks, potentially leading to unsafe agentic behavior in deployed systems. By providing a reproducible two‑axis diagnostic, the study offers a practical safeguard for model compression pipelines before agent deployment, aligning safety with fidelity.

## Related Concepts  
- Fidelity (internal representation similarity)  
- Safety (absence of harmful outputs)  
- Compression artifacts (low‑rank truncation, magnitude pruning)  
- Agentic execution and SOP generation  
- Data‑free quality guards (perplexity, MMLU confidence interval)
