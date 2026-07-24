# Summary: 2026-07-22_15-22-14Z_WhichValuesDoLLMsConfuse_ASchwartz_BasedRecognitio.md
Saved: 2026-07-24 02:06
Source: 2026-07-22_15-22-14Z_WhichValuesDoLLMsConfuse_ASchwartz_BasedRecognitio.md
Model: None

---

## Summary  
The paper investigates whether large language models can reliably recognize the ten basic values identified by Schwartz, treating value identification as a controlled top‑1 recognition task. By training 21 instruction‑tuned LLMs on Russian situational texts and measuring their ability to locate the correct value while ranking alternatives, the authors demonstrate that LLM outputs often capture the intended motivational region but fail to rank close values consistently. Their contribution is a systematic Schwartz‑based evaluation framework that combines exact accuracy with directed error analysis to expose latent biases in value perception.

## Key Contributions  
- [Finding 1] The pooled top‑1 accuracy (Acc@1) across all LLM runs is 0.683, indicating moderate success in identifying the correct value, while top‑3 accuracy (Acc@3) improves to 0.892, showing that models can recover near‑correct rankings when alternatives are considered.  
- [Finding 2] Adjacent values account for 50.9 % of semantic errors, compared with only 24.4 % under a checkpoint‑specific null model, revealing that confusions between neighboring Schwartz values dominate performance degradation.  
- [Finding 3] Eight directed confusions recur across checkpoints and human‑confirmed subsets; notable asymmetric pairs include Universalism ↔ Benevolence, Tradition ↔ Conformity, Security ↔ Power, while Stimulation‑Hedonism forms a bidirectional boundary, indicating that certain value pairings are consistently misordered.

## Methodology  
The authors constructed an evaluation set of 1,000 Russian situational texts, each balanced across the ten Schwartz values and independently labeled by two human annotators per item. They executed 21 instruction‑tuned LLM runs under a fixed ranked‑response protocol; twenty of these produced reliable outputs forming a semantic panel. Accuracy was measured via top‑1 (Acc@1) and top‑3 (Acc@3) recall, and errors were analyzed for directionality to identify which value pairs were most frequently confused.

## Results  
The main experimental results are the pooled Acc@1 = 0.683 and Acc@3 = 0.892, together showing that LLM value recognition is partially successful but unstable in ranking. Error analysis reveals that adjacent values generate roughly half of all mistakes, far exceeding baseline error rates. Directed confusions persist across checkpoints, with specific pairs showing strong asymmetry; the severity of these errors varies by checkpoint and can influence higher‑order value profiles.

## Significance  
These findings underscore a critical gap in current LLM evaluation: models may correctly label values but fail to order them coherently, potentially biasing downstream applications that rely on hierarchical value reasoning. The study advocates for a multi‑metric approach—exact accuracy, ranked recovery, and directed error analysis—to obtain a fuller picture of value perception.

## Related Concepts  
Schwartz’s ten basic values, instruction‑tuned LLMs, top‑1/3 recall metrics, directed confusion analysis, asymmetric value pairings, higher‑order value profiling.
