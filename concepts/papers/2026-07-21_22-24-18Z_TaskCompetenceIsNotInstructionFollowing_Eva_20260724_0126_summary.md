# Summary: 2026-07-21_22-24-18Z_TaskCompetenceIsNotInstructionFollowing_Evaluating.md
Saved: 2026-07-24 01:26
Source: 2026-07-21_22-24-18Z_TaskCompetenceIsNotInstructionFollowing_Evaluating.md
Model: None

---

## Summary  
The paper investigates whether small language models can reliably follow instructions when those instructions conflict with their usual task behavior, rather than merely obeying standard instruction‑tuning objectives. By pairing each model’s primary task output with a deliberately contradictory non‑standard request (e.g., selecting the wrong answer, flipping sentiment, or doubling an answer), the authors test if resistance to such conflicts is rooted in specific tasks or reflects a broader behavioral tendency. Their analysis shows that small models remain competent on standard tasks yet routinely ignore the conflicting instruction, while larger models exhibit a pronounced gap between task competence and instruction following. The study therefore argues that task competence and instruction following are distinct abilities, and reporting only standard accuracy masks important failure modes.

## Key Contributions  
- [Finding 1] Small models stay competent on their primary tasks but systematically ignore non‑standard instructions, indicating that instruction‑following failures are not due to loss of core ability.  
- [Finding 2] Larger models show a clear divergence: standard accuracy improves with scale, yet the same models perform poorly on conflicting instructions, revealing a persistent gap between task competence and obedience.  
- [Finding 3] The results demonstrate that task competence and instruction following are separate competencies; standard accuracy alone cannot capture instruction‑following failures.

## Methodology  
The authors employ a cross‑task design across three domains—multiple‑choice question answering (MCQA), sentiment classification, and mathematical question answering. For each dataset they generate two prompts: one that aligns with the model’s usual task (standard instruction) and another that conflicts with it (non‑standard instruction). Predictions are evaluated against the original ground truth using three metrics: standard accuracy (how often the model follows the intended task), non‑standard accuracy (how often the model obeys the conflicting request), and an Instruction‑Following Failure Rate (IFFR, which quantifies how many times a model ignores the non‑standard instruction). The evaluation is performed on a suite of instruction‑tuned Qwen models ranging from small to large sizes.

## Results  
Standard accuracy and overall instruction following improve as model size increases, but the relationship with task competence is inconsistent. Small Qwen models maintain high standard accuracy while exhibiting near‑zero non‑standard accuracy; their IFFR is high because they ignore conflicting instructions. In contrast, larger models show a pronounced gap: their standard accuracy remains strong, yet non‑standard accuracy drops sharply and IFFR spikes, indicating that the same scale does not guarantee reliable instruction obedience. The findings suggest that scaling alone does not automatically translate into better compliance with contradictory prompts.

## Significance  
These results highlight a critical flaw in current model evaluation practices: relying solely on standard task metrics can conceal systematic instruction‑following errors. By introducing non‑standard tasks and the IFFR metric, researchers gain insight into whether gains in competence are accompanied by proportional improvements in obedience. This distinction matters for both research design and real‑world deployment, where models may need to obey instructions that conflict with their learned behavior.

## Related Concepts  
- Instruction tuning  
- Task competence  
- Instruction following  
- Model scaling effects  
- Cross‑task evaluation  
- IFFR (Instruction‑Following Failure Rate) metric
