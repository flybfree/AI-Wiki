# Summary: 2026-07-31_22-57-16Z_RMSWeb_Reflection_Failure_ModeMining_andSalvage_DS.md
Saved: 2026-08-03 21:24
Source: 2026-07-31_22-57-16Z_RMSWeb_Reflection_Failure_ModeMining_andSalvage_DS.md
Model: None

---

## Summary  
The paper proposes RMSWeb, a three‑part recipe that tackles the data scarcity and inefficiency of training compact web agents after supervised fine‑tuning (SFT). By integrating reflection‑conditioned retries, failure‑mode mining, and Salvage‑DS, RMSWeb enriches offline reinforcement learning with high‑value trajectories while preserving the original SFT policy. The approach yields up to 19.7 % fewer action steps on solved tasks and measurable gains across multiple web benchmarks compared with baseline SFT models.  

## Key Contributions  
- **Reflection‑conditioned retries increase collection yield** – agents retry failed actions under reflective conditions, producing more successful trajectories and shortening the length of successful paths.  
- **Failure‑mode mining concentrates offline RL on critical states** – the method extracts only those states that deviate from routine SFT behavior, focusing training effort where it matters most.  
- **Salvage‑DS combines an action‑semantic polarized reward with contrast‑and‑competence‑gated dynamic sampling and an action‑only anchor for rejected groups**, enabling continued learning even when group‑relative updates are unsuitable.  

## Methodology  
RMSWeb is built as a three‑stage pipeline applied to Qwen3‑VL‑Instruct at 8 B and 32 B parameters. First, the SFT policy generates trajectories; second, reflection mechanisms flag and retry problematic actions, feeding successful outcomes back into the data pool. Third, failure‑mode mining isolates anomalous states for offline RL training. Salvage‑DS then evaluates each action with a polarized reward that distinguishes between useful and irrelevant outcomes, using contrastive sampling to prioritize high‑impact samples while an action‑only anchor provides fallback signals for groups rejected by the reward. The combined dataset is used to fine‑tune the policy via reinforcement learning.  

## Results  
On WebVoyager, Online‑Mind2Web, and WebTailBench, RMSWeb improves over SFT by 2.4–7.0 points at 8 B and 1.2–7.7 points at 32 B. The 8 B model also achieves the strongest reported Online‑Mind2Web result among similarly sized open‑weight models in our comparison, while delivering a leading accuracy‑cost trade‑off on WebVoyager and WebTailBench (subject to differences in external evaluation protocols).  

## Significance  
RMSWeb addresses two core challenges of compact web agents: costly data collection and inefficient reinforcement learning updates. By systematically mining failure modes and providing fallback signals, it reduces the number of action steps needed for task completion, directly lowering deployment cost while boosting performance. The method demonstrates that reflective, targeted offline RL can outperform pure SFT baselines on real‑world web benchmarks.  

## Related Concepts  
- Compact web agents; supervised fine‑tuning (SFT); reinforcement learning (RL) in the web domain; group‑relative RL; offline RL; reflection mechanisms; failure‑mode mining; action‑semantic polarized reward; dynamic sampling; contrastive training; action‑only anchor.
