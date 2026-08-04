# Summary: 2026-08-03_14-18-00Z_SKT_Skill_UseTrainingatScaleviaVerifiedSyntheticDa.md
Saved: 2026-08-04 00:34
Source: 2026-08-03_14-18-00Z_SKT_Skill_UseTrainingatScaleviaVerifiedSyntheticDa.md
Model: None

---

## Summary  
The paper introduces SKT (Skill‑Use Training), a pipeline that creates high‑quality, skill‑grounded tasks and executable trajectories from a large repository of public agent skills. By combining rule‑based and agent‑driven verification with feedback‑guided repair, SKT retains only those trajectories that substantially employ every required skill, producing a verified dataset of 27 164 trajectories for 4 000 task packages derived from 2 000 skills. The authors also introduce SkillEval, a held‑out benchmark to evaluate whether agents correctly identify and apply the synthesized tasks. Supervised fine‑tuning on these verified trajectories consistently boosts skill‑use performance across diverse language models, benchmarks, and agent harnesses.

## Key Contributions  
- [Finding 1] SKT generates a large, verified set of skill‑grounded task packages and executable trajectories that guarantee each required skill is used.  
- [Finding 2] Supervised fine‑tuning on these synthetic trajectories significantly improves an agent’s ability to identify, apply, and coordinate skills compared with training on raw data or without verification.  
- [Finding 3] Verification ablations show that the gains depend on high‑quality supervision, persist across multiple agent interfaces, and increase as the skill coverage expands.

## Methodology  
The authors begin by selecting a diverse set of 2 000 public skills from existing datasets. For each single‑skill or multi‑skill configuration, they synthesize tasks using rule‑based specifications that define observable outcomes. The synthetic task is then run through an agent harness; if the output does not sufficiently demonstrate all required skills, feedback is collected and the trajectory is repaired iteratively until verification passes. Only trajectories that meet a stringent usage threshold are kept, forming the core of SKT’s dataset. This pipeline also produces SkillEval, a test pool untouched by synthesis, to serve as an objective benchmark.

## Results  
Using the generated 27 164 verified trajectories, supervised fine‑tuning on diverse models (e.g., GPT‑3.5, LLaMA) consistently yields higher skill‑use scores across multiple benchmarks and harnesses than baseline training or fine‑tuning without verification. Ablation studies confirm that the improvement is contingent on the quality of supervision: lower‑quality repairs produce negligible gains, while high‑quality repairs yield robust improvements. Moreover, extending the pipeline to cover broader skill sets amplifies performance benefits, indicating scalability beyond a single agent interface.

## Significance  
SKT establishes verified data synthesis as an effective and scalable method for training agents to use complex procedural skills. By guaranteeing that each synthesized task is executed correctly, SKT provides a reliable source of supervision that can be leveraged across many models and environments, addressing a long‑standing challenge in skill‑based AI.

## Related Concepts  
- Skill‑grounded tasks: tasks designed around specific agent capabilities.  
- Synthetic data generation: creating artificial datasets to augment real data.  
- Verification pipeline: automated checks that confirm task execution.  
- Supervised fine‑tuning: training models using labeled examples.  
- Executable benchmark: a test suite that measures skill application.  
- Multi‑skill coordination: agents performing multiple skills in sequence or concurrently.
