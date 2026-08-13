# Summary: 2026-08-12_15-11-35Z_WhoThinksBestDependsonHowLongYouLetThem_Budget_Dep.md
Saved: 2026-08-12 21:36
Source: 2026-08-12_15-11-35Z_WhoThinksBestDependsonHowLongYouLetThem_Budget_Dep.md
Model: None

---

## Summary  
The paper challenges the assumption that large language model rankings remain stable across different inference conditions, showing that performance can degrade or reverse when token budgets are increased. It introduces a budget‑dependent evaluation protocol and demonstrates that model rankings shift systematically as the maximum token count grows. The authors collect data across seven budget levels (64–4,096 tokens) on four models evaluated at three reasoning benchmarks to quantify these phenomena. Their contribution is a framework for evaluating LLMs under varying computational constraints.

## Key Contributions  
- Finding 1: Some items show non‑monotone accuracy, decreasing with more tokens (3–19 % of cases), model‑specific.  
- Finding 2: Model rankings reverse across all budgets (p < 0.01).  
- Finding 3: Oracle analysis reveals complementarity up to +27.8 pp at constrained budgets.

## Methodology  
The authors generate inference instances on seven budget levels ranging from 64 to 4,096 tokens, applying four models to three reasoning benchmarks, resulting in 56,476 inferences per model. They control for truncation and compute cross‑model overlap, ranking reversals via McNemar’s test, and oracle gaps using human judgments.

## Results  
Among the seven budgets, 3–19 % of items exhibit decreasing accuracy with longer tokens; all four models rank differently across budgets (p < 0.01). Oracle analysis shows up to +27.8 percentage‑point complementarity at low budgets, while a budget‑aware router recovers about 14.1 % of the oracle gap within domains (+1.6–5.7 pp) but incurs domain‑specific penalties (-1.2 pp).

## Significance  
These findings demonstrate that LLM evaluation is not invariant to token limits, prompting a shift toward budget‑aware protocols and highlighting trade‑offs between computational cost and performance.

## Related Concepts  
budget‑dependent ranking, oracle gap, complementarity, McNemar test, token generation limit, cross‑model overlap.

## Original Paper Reference

- [Read the original paper](http://arxiv.org/abs/2608.12150v1)
