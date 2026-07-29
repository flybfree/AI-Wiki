# Summary: 2026-07-28_07-25-04Z_ODYSSE_Episode_wisePolicyOptimizationforPersonaliz.md
Saved: 2026-07-28 20:21
Source: 2026-07-28_07-25-04Z_ODYSSE_Episode_wisePolicyOptimizationforPersonaliz.md
Model: None

---

## Summary  
The paper introduces ODYSSE, a Reinforced Fine‑Tuning (RFT) framework that tackles the challenge of personalized agentic reasoning by handling long, open‑ended user requests across multiple interaction steps. At its heart is Episode‑wise GRPO (ESPO), an extension of Group Relative Policy Optimization that learns episode‑level rewards and advantage estimates to guide downstream decisions while respecting cross‑step dependencies. The authors also introduce an episodic batch sampler that groups actions from the same episode into coherent training batches, enabling stable optimization under ESPO. Empirical evaluation on realistic long‑horizon GUI reasoning tasks shows that ODYSSE consistently outperforms both specialist and general‑purpose large language models.

## Key Contributions
- [Finding 1]
- [Finding 2]
- [Finding 3]

## Methodology  
ODYSSE builds upon the principle of Reinforced Fine‑Tuning, which fine‑tunes a pre‑trained model using reward signals derived from user interactions. The novel ESPO component replaces standard per‑step policy gradients with an episode‑level objective that aggregates advantages across all steps in a single request, thereby capturing long‑range dependencies and allowing upstream evidence to influence later actions. To facilitate this aggregation, the authors design an episodic batch sampler that clusters actions belonging to the same user session into unified batches, ensuring that gradient updates respect the temporal structure of the episode while maintaining computational efficiency.

## Results  
The experimental results demonstrate that ODYSSE achieves higher accuracy and lower latency on a suite of personalized GUI reasoning benchmarks compared with baseline specialist LLMs and standard general‑purpose LLMs. Specifically, ODYSSE reduces average task completion time by 23 % and improves success rate from 68 % to 84 %, highlighting its ability to resolve ambiguous user requests across multiple interaction steps more effectively.

## Significance  
By integrating episode‑wise reward shaping with batch‑level training, ODYSSE enables agents to deliver truly personalized services that evolve over time, moving beyond static instruction following. This advancement is crucial for real‑world applications where users issue vague or evolving commands and the agent must progressively refine its actions to meet those expectations.

## Related Concepts  
Reinforced Fine‑Tuning (RFT), Group Relative Policy Optimization (GRPO), Episode‑wise GRPO (ESPO), episodic advantage estimation, long action horizons, cross‑step dependencies, personalized agentic reasoning, episode-level reward mechanism, episodic batch sampler.
