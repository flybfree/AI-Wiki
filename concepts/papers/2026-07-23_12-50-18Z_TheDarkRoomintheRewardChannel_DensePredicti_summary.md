# Summary: 2026-07-23_12-50-18Z_TheDarkRoomintheRewardChannel_DensePredictionRewar.md
Saved: 2026-07-24 02:44
Source: 2026-07-23_12-50-18Z_TheDarkRoomintheRewardChannel_DensePredictionRewar.md
Model: None

---

## Summary  
The paper investigates why dense per‑step prediction rewards cause catastrophic failure in GRPO‑trained LLM agents on long‑horizon tasks, and proposes a variance‑profile criterion to identify safe reward channels. It demonstrates that the “dark room” pathology—where agents converge to absorbing states with perfect prediction but zero task success—arises from unnormalized advantage estimates amplifying within‑group variance. The authors show that removing only GRPO’s standard normalization (i.e., using raw advantage) eliminates the collapse, restoring performance comparable to baseline RL, indicating that bounded rewards become unbounded pressure when groups are all‑fail and annealing cannot help. Their central insight is that signals whose variance decays by mastery are amplifier‑safe.

## Key Contributions  
- [Finding 1] Dense per‑step prediction rewards under GRPO cause agents to converge to a degenerate absorbing state where prediction accuracy reaches 1.0 while task success remains zero, creating the “dark room” pathology.  
- [Finding 2] Removing only GRPO’s standard normalization (i.e., using raw advantage) eliminates the collapse, restoring performance comparable to baseline RL, indicating that bounded rewards become unbounded pressure when groups are all‑fail and annealing cannot help.  
- [Finding 3] A variance‑profile criterion can retroactively predict which reward channels will succeed: signals whose within‑group variance decays as mastery improves are amplifier‑safe, while those with persistent high variance (all‑fail groups) amplify the signal dangerously.

## Methodology  
The authors conducted experiments on Qwen3‑1.7B/4B/8B across ALFWorld, comparing three reward channels: dense prediction rewards, standard RL rewards, and an auxiliary loss channel. They used group‑normalized policy optimization (GRPO), varying the shaping coefficient and std normalization. The signal‑delivery matrix varied only how the same dense signal is consumed, allowing isolation of reward‑channel effects. Placebo arms with shuffled gold labels were also run to test robustness. All runs were single‑seed; replication and group‑size controls are preregistered.

## Results  
The dense prediction reward alone drove every run into the dark room: agents achieved 100 % observation prediction but 0 % task success, episode lengths fixed at horizon. When std normalization was removed, performance matched baseline RL (≈5 % success). The variance‑profile criterion correctly predicted outcomes for unseen arms and matched published successes. The auxiliary‑loss channel yielded ~20 points improvement over the reward channel, while the true‑gold arm outperformed shuffled‑gold by similar margins.

## Significance  
This work reveals a fundamental mismatch between dense prediction rewards and long‑horizon RL: without proper variance control, they amplify signals that are already saturated, leading to collapse. The variance‑profile criterion offers a principled diagnostic for reward design, enabling safe use of dense supervision in LLM agents. It also clarifies why auxiliary loss channels can be more effective than pure reward shaping.

## Related Concepts  
- Group‑normalized policy optimization (GRPO)  
- Dense per‑step prediction rewards  
- Dark room pathology  
- Variance‑profile criterion  
- RL reward channel analysis  
- Mastery and signal decay
