# Summary: 2026-07-26_03-46-03Z_DoLLMDebatesRepeatArgumentsDifferentlyAcrossLangua.md
Saved: 2026-07-27 20:15
Source: 2026-07-26_03-46-03Z_DoLLMDebatesRepeatArgumentsDifferentlyAcrossLangua.md
Model: None

---

## Summary  
The paper investigates whether language‑specific factors cause large language models to repeat arguments differently across debate transcripts. It introduces *prior‑argument similarity* as a diagnostic that measures how later argument units compare to earlier ones in the same debate, focusing on multilingual settings. The study finds that Chinese debates consistently show higher repetition than English under all tested conditions, suggesting that evaluation must capture argumentative development over time rather than rely solely on final answers.

## Key Contributions  
- Finding 1: Chinese is the only language with a consistently positive prior‑argument similarity gap relative to English across three multilingual embedding models.  
- Finding 2: The gap persists across all agents, turn positions, regression adjustments, metric variants, extraction‑length controls, second‑extractor subsets, and cross‑encoder tail rescoring.  
- Finding 3: A diversity‑aware prompt lowers overall prior‑argument similarity but does not significantly narrow the Chinese–English gap.

## Methodology  
The authors conducted controlled eight‑turn debates on 71 motions across six languages using four model agents. Argument units were extracted with a cross‑encoder and compared via multilingual embeddings (e.g., Sentence‑BERT). The *prior‑argument similarity* score aggregates pairwise similarities, comparing each later turn to all earlier turns while controlling for various factors.

## Results  
Across every experiment, Chinese debates exhibited higher average prior‑argument similarity than English, with gaps ranging from 0.12 to 0.34 on a normalized scale. Manual calibration revealed weak item‑level alignment but a high‑similarity tail indicating substantive repetition. Applying diversity‑aware prompts reduced overall similarity by roughly 8 %, yet the Chinese gap remained unchanged.

## Significance  
These results challenge the assumption that multilingual debate evaluation can be uniform and highlight language‑specific argumentative dynamics. Reporting both average and gap metrics is essential for fair cross‑language comparison, as mitigation strategies may affect one metric more than another.

## Related Concepts  
- Prior‑argument similarity: a diagnostic of argumentive development over time.  
- Multilingual embedding models: Sentence‑BERT variants that support cross‑lingual similarity computation.  
- Cross‑encoder tail rescoring: post‑hoc alignment improvement techniques.  
- Diversity‑aware prompting: strategies aimed at reducing repetitive output while preserving content fidelity.
