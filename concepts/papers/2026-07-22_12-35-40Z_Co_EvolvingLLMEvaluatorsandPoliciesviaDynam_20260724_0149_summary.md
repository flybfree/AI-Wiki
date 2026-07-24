# Summary: 2026-07-22_12-35-40Z_Co_EvolvingLLMEvaluatorsandPoliciesviaDynamicRubri.md
Saved: 2026-07-24 01:49
Source: 2026-07-22_12-35-40Z_Co_EvolvingLLMEvaluatorsandPoliciesviaDynamicRubri.md
Model: None

---

## Summary  
The paper addresses the problem that post‑training with evaluator feedback on policy‑induced samples suffers when scores become too similar, weakening supervision. It introduces DynamicRubric, a co‑evolving framework where evaluators and policies evolve together using weighted binary rubrics. This approach alleviates collapsed score gaps and yields stronger policy updates. Experiments show improved evaluator performance and better reasoning in deployed settings.  

## Key Contributions  
- The theoretical analysis shows that relative score gaps correspond to the directional probability shift needed for optimal policy improvement.  
- DynamicRubric generates response‑set conditioned weighted binary rubrics that aggregate into response‑level scores, providing stronger supervision than static or large reward models.  
- Empirical results demonstrate superior policy optimization and deployment benefits on WeChat Search.  

## Methodology  
The authors treat evaluator feedback as a signal of probability mass transfer between candidate responses. They design DynamicRubric to produce binary rubric items for each response set, weighting them based on the current policy state, then sum the judgments to obtain per‑response scores that guide model updates. This co‑evolution loop ensures evaluators adapt to shifting policy objectives.  

## Results  
Using 8B backbones, DynamicRubric outperforms a 70B reward model and a 235B static rubric generator in both evaluator quality and policy optimization. The optimized policies improve verifiable reasoning and coding benchmarks. When deployed across tens of millions of WeChat Search queries daily, the system lifts key online metrics.  

## Significance  
By aligning evaluators with evolving policies, the work resolves a bottleneck that previously limited post‑training improvement, enabling scalable, high‑quality policy alignment in production.  

## Related Concepts  
- Post‑training fine‑tuning  
- Policy‑induced sampling  
- Relative score gaps  
- Probability allocation view  
- Binary rubric aggregation  
- Co‑evolution of evaluators and policies
