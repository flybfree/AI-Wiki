# Summary: 2026-07-21_22-24-18Z_TaskCompetenceIsNotInstructionFollowing_Evaluating.md
Saved: 2026-07-24 01:18
Source: 2026-07-21_22-24-18Z_TaskCompetenceIsNotInstructionFollowing_Evaluating.md
Model: None

---

## Summary  
The paper investigates whether small language models can be instructed to deviate from their usual task behavior when faced with conflicting instructions, and it does so by measuring both standard accuracy and instruction‑following performance. It introduces a cross‑task design that pairs each model’s normal task with an intentionally contradictory instruction, allowing the authors to differentiate between genuine task competence and mere compliance with prompts. The study evaluates Qwen models across three tasks (MCQA, sentiment classification, math QA) at varying sizes. The core contribution is showing that task competence and instruction following are distinct abilities.

## Key Contributions  
- Finding 1: Small language models remain competent on their native tasks but routinely ignore non‑standard instructions, indicating a gap between performance and obedience.  
- Finding 2: Larger models exhibit a clear divergence where standard accuracy improves with scale while instruction‑following ability lags behind, revealing that scaling does not automatically improve compliance.  
- Finding 3: The authors propose the Instruction‑Following Failure Rate (IFFR) as a metric to capture failures of instruction adherence beyond simple accuracy loss.

## Methodology  
The methodology pairs each model’s standard task with a deliberately conflicting non‑standard instruction—such as selecting an incorrect answer, outputting the opposite sentiment, or doubling the correct answer—and scores predictions against both the original ground truth and the intended instruction outcome. Accuracy is measured in three ways: standard accuracy (correctness to original data), non‑standard accuracy (correctness to the instructed deviation), and IFFR (proportion of times a model follows the non‑standard prompt). The experiments use Qwen models fine‑tuned on instruction tuning across sizes, evaluating them on three benchmark tasks.

## Results  
Standard accuracy generally increases with model size for all three tasks, confirming that larger models are more capable at their native objectives. In contrast, non‑standard accuracy and IFFR remain low for small models and show only modest improvement in larger models, suggesting a persistent failure to obey conflicting instructions. The gap between standard and instruction performance widens as scale increases, indicating that task competence does not translate into reliable instruction following.

## Significance  
These findings challenge the assumption that improving model size automatically yields better instruction compliance, highlighting a critical blind spot in evaluating language models. By reporting only standard accuracy, practitioners may overlook systematic instruction‑following failures that could degrade downstream applications. The IFFR metric provides a more honest measure of how well models obey user prompts, encouraging research and deployment practices to consider both competence and obedience.

## Related Concepts  
- Instruction tuning  
- Task competence  
- Instruction following failure rate (IFFR)  
- Cross‑task evaluation  
- Small vs. large language model scaling
