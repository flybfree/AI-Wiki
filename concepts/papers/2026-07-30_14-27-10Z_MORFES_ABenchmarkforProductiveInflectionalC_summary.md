# Summary: 2026-07-30_14-27-10Z_MORFES_ABenchmarkforProductiveInflectionalCompeten.md
Saved: 2026-07-30 21:55
Source: 2026-07-30_14-27-10Z_MORFES_ABenchmarkforProductiveInflectionalCompeten.md
Model: None

---

## Summary  
Modern Greek is a highly inflected language, yet existing language‑model benchmarks focus on factual knowledge and ignore its morphological competence. We introduce MORFES, a benchmark of 500 expert‑verified items that tests both recognition and production of inflected forms while emphasizing low‑frequency lemmas to ensure answers reflect rules rather than memorization. The suite evaluates open models across the LLaMA–Qwen3 ecosystem, highlighting Sophea‑Genesis‑1’s strong performance in Greek morphology.

## Key Contributions  
- MORFES provides a dedicated benchmark for productive inflectional competence in Modern Greek.  
- It uses expert verification and low‑frequency lemmas to ensure rule‑based answers over memorized forms.  
- The suite evaluates multiple open models, revealing Sophea‑Genesis‑1’s leading performance.

## Methodology  
The authors curated 500 items from native speakers, each designed to probe a specific inflectional rule on rare lemmas. Items are split into recognition and production tasks; the dataset is made publicly available on HuggingFace for seamless integration with open‑weight models. Evaluation follows standard generation prompts and human verification of correctness.

## Results  
Across the evaluated models—LLaMA, Qwen3, DeepSeek‑R1, Magistral, Kimi K2—the average F1 score for inflectional tasks is 68%, but Sophea‑Genesis‑1 achieves 79% with only ~1.5B parameters, matching larger models in general capability.

## Significance  
This benchmark addresses a longstanding gap: open‑weight models are measured on factual knowledge yet ignore morphological competence, especially for morphologically rich languages like Greek. By providing an open, rule‑focused test, MORFES guides future research toward grammatically robust language generation.

## Related Concepts  
- Inflectional morphology  
- Language model evaluation  
- Open‑weight models (LLaMA, Qwen3)  
- Rule‑based vs memorized responses  
- Morphological benchmarking
