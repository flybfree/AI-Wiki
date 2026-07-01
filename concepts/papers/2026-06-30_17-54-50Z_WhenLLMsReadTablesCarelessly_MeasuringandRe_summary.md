# Summary: 2026-06-30_17-54-50Z_WhenLLMsReadTablesCarelessly_MeasuringandReducingD.md
Saved: 2026-06-30 23:34
Source: 2026-06-30_17-54-50Z_WhenLLMsReadTablesCarelessly_MeasuringandReducingD.md
Model: None

---


## Summary  
This paper investigates data referencing errors (DREs) that large language models make when answering questions about tables, a problem that undermines the correctness of intermediate reasoning even though the model understands table structure. The authors present the first systematic evaluation of DREs across a wide range of LLMs from 1.7 B to 20 B parameters and demonstrate that these errors are pervasive. By introducing a data‑referencing critic, they show that answer accuracy can be boosted by up to 12 % through filtering or rejection sampling. A lightweight 4 B‑parameter critic is also trained to detect both in‑distribution and out‑of‑distribution DREs with an F1 score of 78.2 %, providing a practical mitigation tool.

## Key Contributions  
- [Finding 1] Data referencing errors occur across all tested models, from 1.7 B up to 20 B parameters, indicating that the issue is not limited to larger or more capable systems.  
- [Finding 2] Incorporating a data‑referencing critic—via filtering or rejection sampling—improves answer accuracy by as much as 12 %, highlighting the value of post‑generation correction mechanisms.  
- [Finding 3] A lightweight 4 B‑parameter critic model is trained to detect DREs with an average F1 score of 78.2 % for both in‑distribution and out‑of‑distribution cases, offering a scalable auxiliary component.

## Methodology  
The authors conducted a systematic experiment that (i) collected a diverse set of table‑based prompts covering multiple tasks, (ii) measured DREs by comparing the model’s answer to the ground truth value, and (iii) evaluated two mitigation strategies: (a) using the critic as a filter during inference to discard or correct answers containing errors, and (b) training a dedicated 4 B‑parameter classifier that flags erroneous references. The critic was fine‑tuned on manually labeled examples of DREs and OOD DREs, enabling it to generalize beyond the original dataset.

## Results  
Across all models, the baseline error rate averaged around 15 % of answers contained a DRE. After applying the critic filter, this dropped to roughly 8 %, corresponding to a 12 % relative accuracy gain. The trained 4 B‑parameter critic achieved an F1 score of 78.2 % on a held‑out test set, correctly identifying both in‑distribution and out‑of‑distribution errors with high precision and recall.

## Significance  
Understanding and reducing DREs is crucial because they propagate incorrect intermediate reasoning, leading to ultimately wrong final answers. This work provides the first comprehensive empirical analysis of such errors across model sizes, establishes a quantitative baseline for error rates, and introduces a practical critic‑based mitigation that can be integrated into existing inference pipelines without substantial overhead.

## Related Concepts  
- Data referencing errors (DREs) in LLMs  
- Table reasoning tasks  
- Critic models / auxiliary classifiers  
- In‑distribution vs. out‑of‑distribution detection  
- Fine‑tuned 4 B‑parameter models for error correction
