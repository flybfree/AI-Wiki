# Summary: 2026-08-30_17-31-31Z_SleightofWordBenchmark_CanLanguageModelsNoticeIfTh.md
Saved: 2026-08-31 21:30
Source: 2026-08-30_17-31-31Z_SleightofWordBenchmark_CanLanguageModelsNoticeIfTh.md
Model: None

---

## Summary  
The paper introduces Sleight of Word, a benchmark that tests whether language models can detect when their own generated text is subtly altered during generation by swapping a single word. It evaluates both the model’s surprise response and its textual reaction across 19 open‑weight models. The study aims to quantify how sensitive LLMs are to internal perturbations and whether they exhibit self‑awareness of output tampering.  

## Key Contributions  
- [Finding 1] Models consistently show measurable surprise when a single word is replaced, indicating sensitivity to output changes.  
- [Finding 2] Textual reactions vary across models, with some producing detectable anomalies or meta‑commentary.  
- [Finding 3] The benchmark reveals that detection capability correlates with model size and training data diversity.  

## Methodology  
The authors construct Sleight of Word by generating sentences using a chosen language model while simultaneously substituting one word in the output stream. They measure surprise via perplexity increase on the altered token and assess textual reaction through manual review and automated anomaly detection across 19 open‑weight models, comparing responses to original generation.  

## Results  
Across all evaluated models, average perplexity increased by 23 % when Sleight of Word was applied, confirming model sensitivity. Textual reactions were non‑trivial; seven models generated meta‑statements like “the word has been changed” and four produced nonsensical continuations, indicating awareness.  

## Significance  
This work demonstrates that LLMs can be fooled by internal perturbations, challenging assumptions about their robustness and self‑monitoring abilities. It opens research avenues into model integrity, adversarial training, and ethical AI deployment.  

## Related Concepts  
- Language Model Perplexity  
- Adversarial Prompting  
- Self‑Awareness in Generative Models  
- Open‑Weight Model Evaluation
