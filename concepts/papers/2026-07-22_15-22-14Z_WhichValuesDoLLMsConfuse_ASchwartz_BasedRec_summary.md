# Summary: 2026-07-22_15-22-14Z_WhichValuesDoLLMsConfuse_ASchwartz_BasedRecognitio.md
Saved: 2026-07-24 02:02
Source: 2026-07-22_15-22-14Z_WhichValuesDoLLMsConfuse_ASchwartz_BasedRecognitio.md
Model: None

---

## Summary  
The paper investigates how large language models (LLMs) recognize Schwartz’s ten basic values in Russian situational texts, aiming to establish a reliable metric for value‑recognition beyond simple accuracy. It proposes a Schwartz‑based recognition framework that combines exact top‑1 scores with ranked recovery and directed error analysis.

## Key Contributions  
- The study demonstrates that LLMs achieve moderate but inconsistent top‑1 accuracy (Acc@1 = 0.683, Acc@3 = 0.892) on a balanced set of 1,000 sentences, revealing frequent misranking of adjacent values.  
- It identifies eight recurring directional confusions across checkpoints and human labels, notably Universalism→Benevolence, Tradition→Conformity, Security→Power, and Stimulation↔Hedonism, showing asymmetric and bidirectional boundaries that affect higher‑order value profiles.  
- The research introduces a Schwartz‑based evaluation protocol that evaluates both exact accuracy and the stability of ranked responses, providing a more nuanced assessment than standard top‑1 metrics.

## Methodology  
The authors constructed a dataset of 1,000 Russian situational narratives, each labeled by two human annotators for one of ten basic values (Schwartz). The texts are balanced across values to avoid bias. Twenty instruction‑tuned LLM runs were executed under a fixed ranked‑response protocol; the first twenty produced reliable outputs formed the semantic panel. Accuracy was measured via pooled top‑1 and top‑3 metrics, while directed error analysis compared model predictions with human labels to detect which value pairs are most often confused.

## Results  
Pooled Acc@1 is 0.683 and Acc@3 is 0.892, indicating that models correctly identify the dominant value in many cases but struggle to rank alternatives consistently. Adjacent values account for 50.9 % of semantic errors, compared with only 24.4 % under a checkpoint‑specific null model. The eight directed confusions persist across checkpoints and human‑confirmed subsets; Universalism is often confused with Benevolence (asymmetric), Tradition with Conformity, Security with Power, while Stimulation and Hedonism form a bidirectional boundary.

## Significance  
These findings highlight that value recognition in LLMs is fragile and sensitive to checkpoint variations, which can bias downstream applications relying on higher‑order value profiles. By integrating exact accuracy with ranked recovery and directed error analysis, the study offers a more robust evaluation framework for ethical AI systems that depend on nuanced value judgments.

## Related Concepts  
Schwartz’s ten basic values (Universalism, Benevolence, Tradition, Conformity, Security, Power, Hedonism, Stimulation), top‑1 accuracy, top‑3 accuracy, directed error analysis, instruction‑tuned LLMs, checkpoint stability.
