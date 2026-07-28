# Summary: 2026-07-25_16-00-45Z_SeekJudge_APracticalRewardFrameworkforReinforcemen.md
Saved: 2026-07-27 23:42
Source: 2026-07-25_16-00-45Z_SeekJudge_APracticalRewardFrameworkforReinforcemen.md
Model: None

---

## Summary  
Computer‑use agents must judge whether a trajectory fulfills its instruction, but rule‑based evaluation is brittle to app updates and online drift. The authors introduce SeekJudge, a model‑based reward framework that uses four role‑specialized agents—Condense, Ground, Seek, and Analyze—to reach a verdict via a Seek–Analyze loop. By training a shared 9 B backbone through seed‑calibrated distillation, SeekJudge achieves performance comparable to native rule‑based supervision on held‑out RL test goals. The framework also delivers step‑level judgments with minimal per‑call context and lower inference cost than closed‑source large models.

## Key Contributions  
- [Finding 1] SeekJudge matches or surpasses native rule‑based supervision in online reinforcement learning for computer‑use agents.  
- [Finding 2] The framework employs a seed‑calibrated distillation pipeline to train one specialized 9 B model that serves as the shared backbone for all four role‑specialized agents (Condense, Ground, Seek, Analyze).  
- [Finding 3] SeekJudge provides step‑level judgments with a small per‑call context that scales efficiently to long trajectories and runs faster than a closed‑source large language model.

## Methodology  
The authors tackled the judgment problem by decomposing it into four specialized agents. Each agent processes part of the trajectory, collaborates through an iterative Seek–Analyze loop, and contributes to the final verdict. A seed‑calibrated distillation process fine‑tunes a single 9 B model to act as the common backbone, enabling consistent behavior across agents while preserving their distinct roles. The reward server is augmented with an architectural improvement that accelerates inference, allowing low‑cost, scalable judgment generation.

## Results  
On held‑out RL test goals, SeekJudge’s downstream success rate meets or exceeds that of rule‑based supervision. Experiments show step‑level judgments are generated with a minimal per‑call context, enabling handling of long trajectories without excessive memory usage. The model runs significantly cheaper than invoking a closed‑source large language model and benefits from the faster reward server architecture introduced in the paper.

## Significance  
SeekJudge demonstrates that model‑based rewards can be as practical—and sometimes superior—to traditional rule‑based supervision for CUA reinforcement learning, offering a scalable, cost‑effective alternative that adapts to app updates. Its step‑level judgments provide richer feedback for training agents, and the lightweight context requirement makes it feasible in real‑world deployments where latency and compute are constraints.

## Related Concepts  
- Reinforcement learning in computer‑use agents  
- Rule‑based evaluation of trajectories  
- Model‑based reward frameworks  
- Distillation and seed‑calibrated training  
- Role‑specialized agents (Condense, Ground, Seek, Analyze)  
- Seek–Analyze loop for joint reasoning  
- Step‑level judgments  
- Per‑call context scaling  
- RL test goals
