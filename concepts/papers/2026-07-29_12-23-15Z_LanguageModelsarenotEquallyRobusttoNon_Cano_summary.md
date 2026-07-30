# Summary: 2026-07-29_12-23-15Z_LanguageModelsarenotEquallyRobusttoNon_CanonicalTo.md
Saved: 2026-07-29 20:33
Source: 2026-07-29_12-23-15Z_LanguageModelsarenotEquallyRobusttoNon_CanonicalTo.md
Model: None

---

## Summary  
The paper investigates whether language models remain robust to non‑canonical tokenizations across languages, extending prior English invariance results. It finds that tokenization robustness varies systematically by language and model size, with instruction‑tuned LLMs showing performance drops ranging from 9 % to 24 %. The study also proposes LoRA fine‑tuning on diverse tokenizations as a mitigation strategy.

## Key Contributions  
- [Finding 1] Tokenization invariance does not generalize beyond English; model behavior varies substantially across languages.  
- [Finding 2] Sensitivity correlates with token fragmentation: languages that exhibit higher token fragmentation are more affected by non‑canonical tokenizations.  
- [Finding 3] LoRA fine‑tuning on multi‑tokenization training data improves robustness, especially when diverse non‑canonical tokenizations are sampled.

## Methodology  
The authors evaluate six downstream tasks across 27 languages using instruction‑tuned language models (Llama‑3.1‑8B, Qwen3‑8B, Gemma‑3‑12B). For each string they generate alternative tokenizations and measure the relative performance drop compared to canonical tokenization. They also perform LoRA fine‑tuning on English‑only data versus systematic sampling of diverse non‑canonical tokenizations.

## Results  
Average relative performance drops are 23.7 % for Llama‑3.1‑8B, 11.4 % for Qwen3‑8B, and 9.9 % for Gemma‑3‑12B. Languages with higher token fragmentation exhibit larger drops. Fine‑tuning on English improves robustness across languages, while systematic multi‑tokenization training yields the strongest overall performance.

## Significance  
These findings demonstrate that tokenization robustness is not a universal property of language models but depends strongly on the language and its interaction with the tokenizer. The study provides a diagnostic for model‑tokenizer coupling and suggests fine‑tuning strategies to mitigate sensitivity, which is crucial for multilingual LLM deployment.

## Related Concepts  
- Tokenization invariance  
- Non‑canonical tokenization  
- Downstream task performance  
- LoRA fine‑tuning  
- Token fragmentation  
- Model‑tokenizer coupling
