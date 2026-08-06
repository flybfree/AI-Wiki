# Summary: 2026-08-05_05-38-34Z_TheEvaluatorIsPartoftheExperiment_MeasuringOpen_En.md
Saved: 2026-08-05 20:30
Source: 2026-08-05_05-38-34Z_TheEvaluatorIsPartoftheExperiment_MeasuringOpen_En.md
Model: None

---

## Summary  
This paper challenges the assumption that conventional flip‑rate metrics fully capture how large language models (LLMs) respond to open‑ended prompts. By treating conformity as a graded, latent quality rather than a binary label, the authors develop an experimental protocol that isolates peer influence, evaluator bias, and calibration issues across multiple generators and benchmarks. Their work demonstrates that wrong peer inputs degrade revision quality, that human and AI judges are systematically non‑neutral, and that terse correct anchors can mislead the latent scale unless explicitly calibrated.

## Key Contributions  
- [Finding 1] All‑wrong peer input consistently produces the lowest‑quality revisions in every generator‑dataset cell examined.  
- [Finding 2] Blind versus informed ratings of identical answers differ across judges, and even GPT‑4o and GPT‑5.4‑mini exhibit evaluator bias, indicating non‑neutrality.  
- [Finding 3] Short correct anchors are often misread by the latent scale, destabilizing convergence unless explicit calibration is applied.

## Methodology  
The authors introduced a pooled main peer‑condition corpus alongside separately constructed decomposition corpora to disentangle four components: ordinary re‑answering, candidate‑content exposure, bundled peer presentation residual, and directional judge sensitivity to visible peer context. This protocol was applied across four open‑weight generators and three benchmark datasets. Evaluators were measured both blindly and with informed feedback on identical model outputs, while anchor calibration was tested by varying the length of correct responses.

## Results  
Across all generator‑dataset combinations, revisions generated from “all‑wrong” peer inputs ranked lowest in quality metrics such as coherence and factuality. Blind ratings showed a systematic shift toward the peer‑endorsed position for one judge, while two judges shifted away; a third remained near neutral. GPT‑4o and GPT‑5.4‑mini audits mirrored this pattern, confirming evaluator bias beyond humans. Moreover, when correct answers were rendered as terse anchors, their latent quality dropped significantly unless the system performed explicit calibration checks.

## Significance  
These findings reveal that conventional flip‑rate measures are inadequate for open‑ended LLM conformity, that peer influence can be detrimental even when it is “wrong,” and that evaluator neutrality cannot be assumed. The necessity of calibrating anchors underscores a practical challenge in scaling high‑quality open‑ended generation.

## Related Concepts  
- Open‑ended LLM conformity  
- Peer‑conditioned revision quality  
- Evaluator bias and non‑neutrality  
- Anchor calibration for latent scales
