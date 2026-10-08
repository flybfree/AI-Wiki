---
title: LLM Persuasion Is in the Eye of the Evaluation
url: http://arxiv.org/abs/2610.10232v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_15-19-54Z_LLMPersuasionIsintheEyeoftheEvaluation.md
generated_at: 2026-10-07 22:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether different automated evaluation methods for measuring LLM persuasiveness produce consistent rankings when applied to the same set of models. By adapting nine published methods to a shared experimental setup and running them across fifteen LLMs, the authors find that agreement between methods is surprisingly weak, with a mean Spearman correlation of only 0.25, suggesting that persuasion scores are highly dependent on the specific task and evaluation framework chosen.

## Key Takeaways
- The nine automated persuasion evaluation methods disagree substantially in how they rank LLMs, with a mean Spearman correlation of just 0.25, indicating that broad claims about a model's persuasiveness cannot be reliably generalized across different evaluation paradigms.
- Model refusals significantly reduce agreement between methods by approximately one quarter, and these refusals disproportionately affect manipulation tasks rather than rational persuasion tasks, meaning that a model's willingness to engage with certain prompts heavily shapes its measured persuasiveness score.
- General model capability plays a differential role across evaluation types: most rational (non-manipulative) persuasion methods track a model's overall capability, whereas most manipulation-focused methods do not, implying that the task a method sets matters more than how it scores persuasion outcomes.

## Context
As LLMs increasingly match or surpass human experts in persuasive ability, regulators and developers face an urgent need for standardized evaluation frameworks. However, the existing literature is fragmented, with studies treating persuasion differently and drawing broad conclusions from narrow, situation-specific assessments. This paper addresses that fragmentation by providing one of the first systematic cross-method comparisons, using automated pipelines that can test high-risk persuasion scenarios that would be unethical to run on human participants.

## Implications
For practitioners and regulators, the findings caution against relying on a single persuasion benchmark to characterize a model's overall persuasive risk, since a score reflects both a model's ability and its willingness to persuade in a given setting. Model developers and safety teams should therefore evaluate persuasiveness across multiple task types and account for refusal behavior, rather than treating any one score as a universal indicator. The results also highlight the need for the field to converge on more consistent evaluation protocols before persuasion metrics can inform policy or deployment decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10232v1)
