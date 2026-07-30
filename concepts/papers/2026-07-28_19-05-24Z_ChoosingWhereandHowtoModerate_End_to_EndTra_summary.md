# Summary: 2026-07-28_19-05-24Z_ChoosingWhereandHowtoModerate_End_to_EndTrade_offs.md
Saved: 2026-07-29 22:12
Source: 2026-07-28_19-05-24Z_ChoosingWhereandHowtoModerate_End_to_EndTrade_offs.md
Model: None

---

## Summary  
The paper investigates how to place moderation filters in the conversational pipeline and what response should be shown after a flag, focusing on trade‑offs between user usefulness and harmful exposure. It proposes two end‑to‑end customer‑outcome metrics—Usefulness (the fraction of turns with a non‑harmful, relevant response) and Harmful Exposure (the fraction with a harmful response)—to evaluate moderation configurations rather than component accuracy. The study compares three placement strategies (Input only, Response only, Input + response hard blocking) on both a human‑labelled product benchmark and the public ToxicChat dataset. It finds that Response‑only yields highest Usefulness while Input + response reduces Harmful Exposure.

## Key Contributions  
- [Finding 1] Response‑only moderation achieves the best overall Usefulness metric across both evaluation settings.  
- [Finding 2] Adding a hard block to response (Input + response) lowers Harmful Exposure compared with Response only, indicating a better safety trade‑off.  
- [Finding 3] Replacing Response‑only blocking with Response + rewrite recovers most blocked traffic while keeping Harmful Exposure count comparable to Response‑only, showing that rewrites can mitigate exposure without sacrificing usefulness.

## Methodology  
The authors evaluate moderation configurations end‑to‑end by measuring customer outcomes rather than internal component accuracy. They instrument the deployment pipeline with latency and error diagnostics, then run controlled experiments on two datasets: a human‑annotated product conversation set (where each turn is labeled as safe or unsafe) and the ToxicChat benchmark. For each configuration they compute Usefulness and Harmful Exposure, record routing time, and compare them.

## Results  
Across all operating points, Response only yields the highest Usefulness in both settings; Input + response reduces Harmful Exposure but at the cost of some usefulness. Rewriting blocked responses restores most lost traffic while maintaining Harmful Exposure counts similar to Response‑only blocking. Probe routing is shown to reduce conditional route‑and‑generation latency relative to LLM routing for comparable outcomes.

## Significance  
By linking moderation placement and response strategy to real user‑impact metrics, the work moves beyond component accuracy to guide practical deployment decisions under safety and latency constraints, enabling organizations to select configurations that best balance helpfulness and risk.

## Related Concepts  
- Content moderation  
- Filter placement (input vs. response)  
- End‑to‑end evaluation  
- Usefulness metric  
- Harmful exposure metric  
- LLM routing  
- Probe routing
