# Summary: 2026-07-21_11-32-41Z_MedDDC_Eval_Diagnosis_DecoupledEvaluationofMulti_T.md
Saved: 2026-07-24 00:45
Source: 2026-07-21_11-32-41Z_MedDDC_Eval_Diagnosis_DecoupledEvaluationofMulti_T.md
Model: None

---

## Summary  
Multi‑turn medical consultation agents must decide what to ask, adapt to patient replies, and judge when the gathered evidence is sufficient. However, existing evaluation methods often couple the quality of the elicited history with the terminal diagnosis generation, leading to misleading trade‑offs where strong generation can mask a thin history. MedDDC‑Eval introduces a diagnosis‑decoupled testbed that treats the history as the sole comparison object while keeping the history‑to‑diagnosis mapping fixed via a shared frozen reader. This separation enables interpretable measurement of diagnostic usefulness, information acquisition, and efficiency across two held‑out sources.

## Key Contributions  
- [Finding 1] Diagnosis‑decoupled evaluation separates the quality of the elicited medical history from the generation of the final diagnosis, allowing each component to be measured independently.  
- [Finding 2] The system employs directional semantic coverage followed by deterministic one‑to‑one assignment, yielding precise precision‑recall counts for open‑ended items with at most one credited match per prediction or reference.  
- [Finding 3] Gradient‑based policy optimization (GRPO) using diagnosis results and trajectory feedback improves the Qwen‑3‑32B policy by 9.7 points on the Record split and 4.6 points on the Dialogue split, demonstrating that both primary signals are essential for performance.

## Methodology  
The authors built MedDDC‑Eval around a shared frozen reader that maps patient utterances to a fixed diagnostic label, thereby isolating the history generation process from diagnosis output. Two held‑out corpora—Record and Dialogue—serve as test sets. A Diagnosis‑Trajectory‑Efficiency (D/T/E) harness records three metrics: diagnostic usefulness, information acquisition, and efficiency. Directional semantic coverage ensures that each patient statement is assigned to a single relevant diagnosis category, while deterministic assignment guarantees one‑to‑one matches between predictions and references. The evaluation also measures how changing only the diagnostic reader affects F1 scores and pairwise policy orderings.

## Results  
Holding histories constant while varying the diagnostic reader shifts the F1 score by 2.2–19.0 points and reverses 18 % and 36 % of pairwise ordering decisions on the Record and Dialogue splits, respectively. Applying GRPO over interactive multi‑turn rollouts yields a policy that improves its total‑score by 9.7 points (Record) and 4.6 points (Dialogue) relative to initialization; removing either primary signal—diagnosis result or trajectory feedback—degrades the held‑out joint performance, confirming their necessity.

## Significance  
MedDDC‑Eval provides a controlled framework for attributing diagnostic value to elicited histories, offering interpretable metrics that guide evidence‑acquisition policies. By decoupling diagnosis from history generation, it enables researchers and developers to design agents that prioritize rich patient narratives without sacrificing final accuracy, fostering more reliable and transparent medical consultation systems.

## Related Concepts  
MedDDC (Medical Dictionary for Diseases and Conditions), diagnosis decoupling, shared frozen reader, Gradient‑based Policy Optimization (GRPO), multi‑turn consultation agents, precision‑recall, diagnostic usefulness, information acquisition, evidence‑acquisition policy.
