# Summary: 2026-07-22_19-49-38Z_AttributionMarkets_AFisher_MarketFormulationforFra.md
Saved: 2026-07-24 02:15
Source: 2026-07-22_19-49-38Z_AttributionMarkets_AFisher_MarketFormulationforFra.md
Model: None

---

## Summary  
The paper introduces a quasi‑linear Fisher‑market model that bridges the gap between what is planned (a task’s effort budget) and what actually occurs (logged actions), thereby preventing false stalls in active goals. It treats planned tasks as budget‑constrained buyers, performed actions as divisible goods, and derives each buyer’s valuation from a fused text/structural/temporal signal. The model yields three theorems—conservation, a hard budget cap, and a junk filter—as well as an empirically validated algorithm that converges via a satiation‑threshold fixed point. A de‑circularized benchmark reveals the market’s equilibrium is overly sensitive to affinity noise, which is mitigated by entropy‑regularized optimization.

## Key Contributions  
- **Quasi‑linear Fisher market formulation** linking planned tasks (budget buyers) with performed actions (divisible goods).  
- **Three theoretical results**: conservation theorem, hard budget cap, and junk filter theorem.  
- **Empirical validation** on random and adversarial instances plus a de‑circularized benchmark showing noise sensitivity in the zero‑entropy equilibrium.

## Methodology  
The authors construct a market where each planned task is a buyer whose valuation comes from a fused textual, structural, and temporal signal; performed actions are sold as divisible goods with a seller reserve price. Buyers may opt for a cash option to secure their budget. The solution is obtained by iterating a fixed‑point algorithm that respects diagonal dominance, ensuring existence (Brouwer) and local uniqueness. To handle progress discounting, the utility function is concave and discounts effort near plan completion. When noise inflates affinity scores, an entropy‑regularized optimization with a one‑parameter strength is applied adaptively to smooth the market.

## Results  
Theoretical analysis proves convergence under explicit diagonal‑dominance conditions; the algorithm converges faster than standard Fisher markets because of the satiation threshold. Experiments on synthetic and real data show lower attribution error, higher robustness, and stable performance across seeds. The de‑circularized benchmark demonstrates that the market’s zero‑entropy equilibrium is more sensitive to affinity noise than entropy‑regularized optimal transport; the regularization parameter reduces this sensitivity while preserving efficiency.

## Significance  
This work provides a principled, theoretically grounded mechanism for reconciling planning and execution data, which is crucial for multi‑touch attribution in digital advertising. By delivering provable budget caps and junk filters, it improves resource allocation and reduces false stalls. The entropy‑regularized extension offers a practical solution to noise‑induced instability, making the model suitable for real‑world noisy signals.

## Related Concepts  
- Fisher market  
- Optimal transport  
- Entropy regularization  
- Satiation threshold  
- Convex optimization  
- Budget constraints
