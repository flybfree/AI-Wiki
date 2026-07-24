# Summary: 2026-07-22_19-49-38Z_AttributionMarkets_AFisher_MarketFormulationforFra.md
Saved: 2026-07-24 02:13
Source: 2026-07-22_19-49-38Z_AttributionMarkets_AFisher_MarketFormulationforFra.md
Model: None

---

## Summary  
The paper introduces an “Attribution Market” that treats the mismatch between a planned task’s effort budget and the logged actions performed as a quasi‑linear Fisher market, where each buyer (the planner) values the action according to its textual, structural, and temporal description. By modelling tasks as budget‑constrained buyers and actions as divisible goods, the authors derive a seller reserve price that enforces a hard cap on total effort and a buyer cash option that preserves conservation of effort. The framework is extended with a concave completion‑utility discount that rewards progress near plan completion, and its convergence properties are proved under diagonal dominance via a satiation‑threshold fixed point.

## Key Contributions  
- [Finding 1] A Fisher‑market formulation that separates planned tasks (budget buyers) from performed actions (divisible goods), enabling fractional credit assignment without all‑or‑nothing constraints.  
- [Finding 2] Theoretical guarantees—conservation, a hard budget cap, and a junk filter—derived as theorems of the market’s two instruments: seller reserve price and buyer cash option.  
- [Finding 3] An empirical benchmark showing that the market’s zero‑entropy equilibrium is more sensitive to affinity noise than entropy‑regularized optimal transport; this is remedied by a one‑parameter entropy‑regularized generalization with an adaptive regularization rule.

## Methodology  
The authors construct a quasi‑linear market where each planned task \(t\) has a budget \(B_t\) and each logged action \(a\) possesses a valuation vector \(\mathbf{v}_a = (\text{textual}, \text{structural}, \text{temporal})\). The planner’s utility is the discounted sum of valuations weighted by progress toward completion, yielding a concave completion‑utility function. The market equilibrium is obtained via a fixed point that respects diagonal dominance; existence follows from Brouwer’s theorem and uniqueness under the stated condition.

## Results  
Theoretically, the model guarantees that total effort never exceeds any budget \(B_t\) and that only actions with positive valuation are selected (junk filter). Experimentally, on random and adversarial instances—where affinity is corrupted independently of ground truth—the market converges to a sharp zero‑entropy equilibrium. A comparison with entropy‑regularized optimal transport shows the former is noisier; the proposed entropy‑regularized generalization reduces sensitivity while preserving optimality.

## Significance  
This work bridges planning and execution attribution, offering a mathematically rigorous mechanism for fractional credit assignment that can be applied to multi‑touch attribution, online Fisher‑market algorithms, and resource allocation problems where effort budgets must be respected. By providing provable guarantees and an empirically validated algorithm, it advances both theoretical understanding and practical deployment of attribution systems.

## Related Concepts  
- Fisher market (quasi‑linear pricing)  
- Optimal transport with entropy regularization  
- Multi‑touch attribution in digital marketing  
- Bounded knapsack / budget‑constrained optimization  
- Satiation threshold fixed point and diagonal dominance
