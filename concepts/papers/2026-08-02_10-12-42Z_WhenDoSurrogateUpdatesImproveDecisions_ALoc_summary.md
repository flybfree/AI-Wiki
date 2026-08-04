# Summary: 2026-08-02_10-12-42Z_WhenDoSurrogateUpdatesImproveDecisions_ALocalTheor.md
Saved: 2026-08-04 00:02
Source: 2026-08-02_10-12-42Z_WhenDoSurrogateUpdatesImproveDecisions_ALocalTheor.md
Model: None

---

## Summary  
The paper tackles the mismatch between surrogate updates derived from trajectory losses and downstream decision utility, asking when a single trajectory step reduces both population surrogate loss and decision risk and how this benefit accumulates over repeated updates. It formalizes two key quantities—*learnability* (reduction in surrogate risk) and *decision utility* (reduction in decision risk)—to derive theoretical bounds on their discrepancy. The analysis yields four main results that guide when surrogate updates are beneficial, how transfer propagates, and what guarantees can be obtained.

## Key Contributions  
- [Finding 1] A one‑step transfer bound separates the discrepancy between surrogate and decision risk into first‑order gradient misalignment after nonnegative calibration and second‑order curvature; a pathwise extension accumulates these terms over repeated updates.  
- [Finding 2] When the accessible surrogate gradient is nonzero, universal first‑order transfer holds for every accessible direction exactly when the surrogate and decision gradients are positively collinear.  
- [Finding 3] The calibration gap bounds the regret of learnability‑based trajectory selection; a candidate‑difference refinement tightens this guarantee by retaining only directions that affect pairwise rankings.

## Methodology  
The authors fix a checkpoint and restrict the update space to a tractable set, then define *learnability* as the reduction in population surrogate risk induced by a trajectory and *decision utility* as the reduction in decision risk. By analyzing how these reductions evolve with each trajectory step, they derive theoretical bounds on their discrepancy, explore accumulation over multiple updates, and investigate conditions under which transfer is universal.

## Results  
The theoretical framework produces four results: (1) a one‑step bound separating misalignment and curvature; (2) a condition for universal first‑order transfer via gradient collinearity; (3) a regret bound linking calibration gap to decision loss; and (4) an approximation‑calibration trade‑off across nested update spaces. Controlled experiments on gridworld and LLM post‑training confirm that these predictions hold, illustrating the practical relevance of the theory.

## Significance  
Understanding when surrogate updates improve decisions provides a principled guide for training regimes that balance surrogate loss reduction with downstream performance gains. The results clarify how transfer accumulates over repeated updates, enabling researchers to design trajectory‑wise strategies that avoid unnecessary risk and maximize utility.

## Related Concepts  
- Trajectory loss  
- Surrogate risk (population surrogate)  
- Decision risk  
- Gradient misalignment  
- Second‑order curvature  
- Positive collinearity of gradients  
- Calibration gap  
- Candidate‑difference refinement  
- Nested update spaces
