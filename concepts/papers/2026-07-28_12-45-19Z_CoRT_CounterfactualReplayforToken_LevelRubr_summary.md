# Summary: 2026-07-28_12-45-19Z_CoRT_CounterfactualReplayforToken_LevelRubric_Guid.md
Saved: 2026-07-28 22:48
Source: 2026-07-28_12-45-19Z_CoRT_CounterfactualReplayforToken_LevelRubric_Guid.md
Model: None

---

## Summary  
The paper proposes CoRT, a token‑level credit weighting method for rubric‑guided GRPO that allocates credit within responses based on counterfactual likelihood contrasts. It avoids auxiliary scorers and retains the simplicity of response‑level reward while enabling fine‑grained redistribution of signed advantage across tokens. By comparing token scores under the original rubric‑conditioned prompt versus an equivalent criteria‑free prompt, CoRT creates tokenwise log‑likelihood differences that serve as a proxy for rubric dependence. This approach allows the policy to credit only those positions where the rubric context matters.

## Key Contributions  
- [Finding 1] CoRT introduces a counterfactual replay framework that rescores the same response under two prompt variants to derive token‑level likelihood contrasts.  
- [Finding 2] The method maps these contrasts to bounded, response‑normalized weights for redistributing signed GRPO advantage without an auxiliary scorer.  
- [Finding 3] Experiments show CoRT improves over matched response‑level GRPO by an average of 4.4 percentage points across instruction‑tuned models and reward granularities.

## Methodology  
The authors address the limitation that rubric‑based RL collapses structured criteria into a scalar reward, preventing intra‑token credit allocation. Their solution is to generate a paired set of responses: one conditioned on the original rubric prompt and another on an equivalent but criteria‑free prompt. By feeding both prompts to the language model they obtain token probabilities for each position under two contexts. The difference in log‑likelihoods per token serves as a proxy for how much the output depends on the rubric context. These differences are normalized across tokens within the response and used to adjust the signed advantage from GRPO, redistributing credit where it is most appropriate. No separate relevance learning or auxiliary scorer is required; the method leverages the existing policy gradient signal.

## Results  
Across a suite of instruction‑tuned models evaluated on multiple rubric granularities (e.g., factuality, style, formatting), CoRT consistently outperformed baseline approaches that either use response‑level rewards or learned token‑level credit baselines. The average gain over matched response‑level GRPO was 4.4 percentage points in reward, indicating more accurate alignment with rubric criteria. Token‑wise analysis revealed that credits were allocated primarily to tokens where rubric context had a strong influence, reducing over‑rewarding of irrelevant positions. Ablation studies confirmed that the counterfactual replay mechanism is essential; removing it reduced gains to near zero.

## Significance  
CoRT demonstrates that policy‑internal signals can capture nuanced rubric dependence without sacrificing GRPO’s simplicity or stability. By preserving the response‑level reward while enriching token‑level credit allocation, CoRT offers a scalable way to improve RL alignment for language models, especially in settings where fine‑grained evaluation is critical.

## Related Concepts  
- Rubric‑based reinforcement learning  
- GRPO (Generalized Policy Optimization)  
- Counterfactual replay  
- Token‑level credit weighting  
- Likelihood contrast
