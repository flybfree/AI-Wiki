# Summary: 2026-08-08_09-34-22Z_DoAllLLMsKnowWhenThey_reBeingHarmful_AReproducibil.md
Saved: 2026-08-10 22:52
Source: 2026-08-08_09-34-22Z_DoAllLLMsKnowWhenThey_reBeingHarmful_AReproducibil.md
Model: None

---

## Summary  
The paper investigates whether lightweight MLP probes can reliably detect harmful prompts across different large language model families, reproducing and extending the original LLaMA‑3.1‑8B study with cross‑model generalization and a non‑determinism analysis. It shows that a small probe trained on final‑layer activations yields F1 scores close to those of much larger guard models while being deterministic across inference seeds.

## Key Contributions  
- [Finding 1] The same MLP probe architecture reproduces the original LLaMA‑3.1‑8B benchmark results within 0.37 percentage points overall and within 0.2 points on BeaverTails when applied to Gemma‑4‑E4B, Mistral‑7B‑v0.3, and Qwen2‑7B.  
- [Finding 2] Cross‑model generalization is robust; probe performance does not degrade beyond a one‑point difference across the three model families.  
- [Finding 3] Latent vectors extracted for harmful prompts remain identical regardless of the five random seeds used, indicating that non‑determinism does not affect F1 scores.

## Methodology  
We trained three identical MLP probes on final‑layer activations of the models Gemma‑4‑E4B, Mistral‑7B‑v0.3, and Qwen2‑7B using the same benchmark suites (WildJailbreak, BeaverTails, AEGIS 2.0). For each model we extracted latent vectors under five different random seeds to measure variance in F1 scores. The probes were evaluated end‑to‑end, comparing their performance against the original LLaMA‑3.1‑8B results and across seeds.

## Results  
The reproduced LLaMA‑3.1‑8B benchmark scores are within 0.37 percentage points of the original values overall and within 0.2 points on BeaverTails. Across all seeds, probe F1 scores vary by less than one point, confirming that non‑deterministic inference does not degrade detection accuracy. The same MLP architecture yields comparable performance for Gemma, Mistral, and Qwen models.

## Significance  
These findings demonstrate that a compact, interpretable safety probe can be generalized across diverse LLM families without sacrificing the high F1 scores achieved by massive guard models. It also clarifies that deterministic latent representations mitigate concerns about randomness in inference, supporting more efficient deployment of lightweight safety mechanisms.

## Related Concepts  
- Latent‑space safety probing  
- MLP probe architecture for classification  
- Large language model scaling and performance trade‑offs  
- Non‑deterministic inference and variance measurement  
- F1 metric for binary classification in safety evaluation  
- Cross‑model generalization of safety mechanisms
