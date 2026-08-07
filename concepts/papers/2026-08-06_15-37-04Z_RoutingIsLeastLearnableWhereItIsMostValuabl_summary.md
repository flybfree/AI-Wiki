# Summary: 2026-08-06_15-37-04Z_RoutingIsLeastLearnableWhereItIsMostValuable_Bound.md
Saved: 2026-08-06 20:47
Source: 2026-08-06_15-37-04Z_RoutingIsLeastLearnableWhereItIsMostValuable_Bound.md
Model: None

---

## Summary  
The paper investigates how well web agents can learn to route between different observation modes (text‑only, pixel‑only, or combined) across a set of tasks and site‑model combinations on two benchmark datasets. It shows that despite routing being most valuable where it is needed, the learning gain from adding more modes is severely limited by the scarcity of supervision labels; the best achievable improvement is bounded between 9.5 % and 30.6 % depending on the cell. The authors also demonstrate empirically that none of five proposed routing policies outperform a single well‑chosen mode, except for one fragile case in the sparsest cell.

## Key Contributions  
- [Finding 1] A lower bound on learning for routing in web agents is derived: the maximum success improvement from adding more observation modes is limited to 9.5 %–30.6 %, depending on the specific task‑site configuration (cell).  
- [Finding 2] Empirical testing of five routing policies—fixed mode, strong‑mode spending, text‑based rule, confidence cascade, and pooled cost tiers—shows that none robustly beats simply fixing one well‑chosen mode; only a marginal improvement appears in the sparsest cell.  
- [Finding 3] A theoretical link is established between agent strength (success rate) and labeling scarcity: the correlation between success rate and the number of labels available for routing is 0.95 across cells, indicating that stronger agents can overturn the limitation.

## Methodology  
The authors measure six observation modes (text‑only, pixel‑only, combined text/pixels, etc.) across eight site‑model combinations (cells) on VisualWebArena and WebArena. Each cell represents a distinct set of tasks and model configurations. They compute success rates per mode, analyze run‑to‑run noise (rerunning the same mode changes 12–14 % of outcomes), and conduct rerun experiments to quantify the marginal benefit of switching modes. Five routing policies are evaluated: (1) always pick a single mode, (2) decide when to spend on the strong mode, (3) use a zero‑cost rule derived from task text, (4) follow a confidence cascade, and (5) employ pooled cost tiers that allocate budget across modes.

## Results  
The optimal strategy is to send tasks unsolvable by any mode to the cheapest mode, which reduces cost by 9.5 %–30.6 % while leaving success unchanged in eight of eight cells. All five routing policies achieve comparable or slightly lower performance than a single well‑chosen mode; only one cell shows a marginal improvement under the fragile policy. The full measurement protocol includes rerun noise bands and detailed task‑mode mappings.

## Significance  
The findings reveal that current web agents lack sufficient labeled data for effective routing, which is the primary bottleneck rather than an inherent limitation of routing algorithms. This suggests that improving agent representation or increasing label supply would be more impactful than designing complex routing strategies. The paper also provides a quantitative bound on learning gains and a clear experimental protocol for future work.

## Related Concepts  
- Representation learning (agent’s ability to interpret text, pixels, or both)  
- Multi‑modal observation fusion  
- Task‑specific selection of observation modes  
- Cost‑sensitive routing policies  
- Label scarcity and its impact on supervised optimization  
- Success rate as a supervision signal for routing
