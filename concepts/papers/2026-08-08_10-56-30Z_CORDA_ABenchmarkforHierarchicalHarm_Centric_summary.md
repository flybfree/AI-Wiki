# Summary: 2026-08-08_10-56-30Z_CORDA_ABenchmarkforHierarchicalHarm_CentricMoralRe.md
Saved: 2026-08-10 22:53
Source: 2026-08-08_10-56-30Z_CORDA_ABenchmarkforHierarchicalHarm_CentricMoralRe.md
Model: None

---

## Summary  
The paper introduces CORDA, a benchmark for hierarchical harm‑centric moral reasoning in large language models (LLMs), addressing the gap that current evaluations only test default moral responses rather than how models prioritize competing harms when no option is cost‑free. It proposes nine complex dilemmas across four ethical frameworks to evaluate whether LLMs can adapt their decisions according to ordered moral chains. The study assesses ten instruction‑tuned models from seven providers on their ability to follow these priority orders and on categorical versus outcome‑based choices. Findings reveal a strong deontological bias, with most models defaulting to personal harm avoidance over aggregate harm reduction.

## Key Contributions  
- [Finding 1] CORDA provides the first benchmark that explicitly tests hierarchical, principle‑priority moral reasoning in LLMs.  
- [Finding 2] Models consistently prioritize avoidance of direct personal harm (e.g., killing) over reducing total harm, indicating recognition of moral red lines.  
- [Finding 3] Several models fail to respect specified priority orderings such as humans > animals > robots, revealing brittleness under chain conditioning.

## Methodology  
The authors constructed CORDA by generating nine complex moral dilemmas that involve trolley‑style scenarios, medical trade‑offs, resource allocation, and human‑animal‑robot conflicts. Each dilemma is encoded into a “morality chain” specifying an ordered set of ethical principles (Utility, Utility + Agent Harm, Dual‑Process, Dual‑Process + Agent Harm). The benchmark was applied to ten instruction‑tuned LLMs from seven vendors; responses were scored on adherence to the chain’s priority order and on categorical versus outcome‑based decisions.

## Results  
Across all models, 9 out of 10 prioritized personal harm avoidance over aggregate harm reduction, confirming a deontological default. Categorical rules (e.g., “do not kill”) were obeyed more reliably than nuanced comparisons. However, only two models consistently followed the human‑over‑animal‑over‑robot priority; others reverted to default or random choices.

## Significance  
This work shows that moral reliability in LLMs depends on controllability under conflict, not just default restraint. It highlights a critical gap in existing evaluation frameworks and calls for benchmarks that test hierarchical reasoning.

## Related Concepts  
Moral hierarchy, deontological ethics, consequentialism, dual‑process theory, harm‑centric reasoning, morality chains, LLM alignment, instruction tuning, ethical red lines.
