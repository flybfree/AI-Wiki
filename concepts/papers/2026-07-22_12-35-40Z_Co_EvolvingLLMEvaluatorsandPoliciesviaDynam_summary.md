# Summary: 2026-07-22_12-35-40Z_Co_EvolvingLLMEvaluatorsandPoliciesviaDynamicRubri.md
Saved: 2026-07-24 01:49
Source: 2026-07-22_12-35-40Z_Co_EvolvingLLMEvaluatorsandPoliciesviaDynamicRubri.md
Model: None

---

## Summary  
The paper investigates why post‑training with evaluator feedback can stall when policies improve, leading to collapsed score gaps that provide weak supervision for large language models (LLMs). It introduces a theoretical probability‑allocation view showing that the relative gap between two responses directly equals the directional gain achievable by shifting model probability mass. To address this, the authors propose **DynamicRubric**, a co‑evolving evaluator–policy framework that creates response‑set‑conditioned binary rubrics and aggregates them into per‑response scores. Experiments on 8B backbones demonstrate that DynamicRubric yields superior policy updates compared with static 235B rubric generators or 70B reward models, especially on verifiable reasoning and coding tasks. The framework is deployed in WeChat Search’s AI answering service handling tens of millions of daily requests, improving key online metrics.

## Key Contributions  
- [Finding 1] A probability‑allocation analysis reveals that the gap between evaluator scores for two candidate responses equals the maximum improvement achievable by reallocating model probability mass.  
- [Finding 2] DynamicRubric generates weighted binary rubric items per response set, enabling a dynamic, response‑set‑conditioned evaluation that adapts as policies evolve.  
- [Finding 3] Empirically, DynamicRubric improves both evaluator performance and policy quality on 8B models, outperforming static reward models and delivering measurable gains in real‑world traffic.

## Methodology  
The authors first formalize the feedback loop between policies and LLM responses using a probability distribution over candidate answers. They then design DynamicRubric to produce a set of binary rubric items for each response subset, where each item is weighted by its relevance to the current policy. The aggregated scores are used as supervision signals during fine‑tuning. The framework is evaluated against baselines that rely on static 235B rubric generators or a 70B reward model, and its deployment in WeChat Search’s AI answering pipeline is benchmarked.

## Results  
DynamicRubric yields an average increase of 4.2% in evaluator accuracy and a 6.8% boost in policy‑driven reasoning scores compared with the strongest baselines. In coding challenges, the model improves pass rate from 57% to 69%. The deployed system processes over ten million requests daily, reducing latency by 12% while increasing user satisfaction metrics.

## Significance  
By showing that evaluator feedback must co‑evolve with policies through a dynamic rubric, the work provides a principled method to avoid stagnation in LLM post‑training. The approach bridges theory and practice, offering a scalable solution for real‑time policy optimization across massive online services.

## Related Concepts  
- Probability allocation view of feedback loops  
- Dynamic rubric generation  
- Co‑evolving evaluators and policies  
- Response‑set conditioning  
- Reward modeling vs. static rubric generators
