# Summary: 2026-08-08_11-59-38Z_CommitmentBeforeRealization_WhenClassifier_FreeGui.md
Saved: 2026-08-10 22:54
Source: 2026-08-08_11-59-38Z_CommitmentBeforeRealization_WhenClassifier_FreeGui.md
Model: None

---

## Summary  
The paper investigates when classifier‑free guidance (CFG) is actually needed during the decoding of masked diffusion language models, introducing a formal “commitment horizon” that marks the earliest point at which switching to the base model incurs no more than a prescribed tolerance loss. By comparing the probability of eventual constraint satisfaction under continued CFG versus base‑only continuation, the authors show that CFG’s benefit is concentrated early and often diminishes after a certain token. They also demonstrate that freezing each prompt at its optimal horizon yields results comparable to full CFG while many tokens remain masked.

## Key Contributions  
- [Finding 1] The commitment horizon \* is defined as the earliest decoding point where switching all remaining steps to the base model reduces final success by no more than a chosen tolerance.  
- [Finding 2] The per‑step effect of CFG is governed by the covariance between the guidance logit direction and the successor committor, explaining why early tokens gain most value while later ones do not.  
- [Finding 3] Freezing each prompt at its cross‑fitted horizon is noninferior to full CFG on all 13 subtasks within a small margin, even when many tokens are still masked.

## Methodology  
The authors compare the probability of satisfying constraints under two decoding strategies: continued classifier‑free guidance and pure base‑model continuation. They compute the committor as a martingale that tracks remaining success probability. By analyzing the covariance between guidance logits and this committor, they obtain a local account of when guidance helps. Experiments are performed across 13 subtasks; prompts are frozen at their observed optimal horizons to evaluate success rates and fluency while many tokens remain masked.

## Results  
Early horizons typically fall within the first five tokens; switching after these points reduces success by ≤0.2 % (within tolerance). Freezing at each horizon yields success rates indistinguishable from full CFG on all subtasks, preserving the margin even with many remaining masks. Parallel inference adds negligible cost to constraint satisfaction but degrades fluency as width increases. For failed trajectories, reopening committed positions improves recovery in both failure modes.

## Significance  
Separating commitment from realization provides a principled way to stop unnecessary CFG computation once its marginal benefit fades, enabling efficient decoding without sacrificing performance. This insight reduces latency and energy consumption for large language models that employ diffusion‑based generation.

## Related Concepts  
- Classifier‑free guidance (CFG)  
- Masked diffusion language model decoding  
- Committor (martingale tracking remaining success probability)  
- Constraint satisfaction in generative tasks  
- Parallel inference and fluency trade‑offs
