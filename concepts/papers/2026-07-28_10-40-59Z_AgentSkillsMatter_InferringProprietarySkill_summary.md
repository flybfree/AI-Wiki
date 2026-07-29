# Summary: 2026-07-28_10-40-59Z_AgentSkillsMatter_InferringProprietarySkillsfromEx.md
Saved: 2026-07-28 20:29
Source: 2026-07-28_10-40-59Z_AgentSkillsMatter_InferringProprietarySkillsfromEx.md
Model: None

---

## Summary  
This paper addresses the challenge of inferring proprietary agent skills from execution trajectories without access to reference answers or success labels, revealing a previously overlooked behavioral side channel known as Skill Leakage. The authors introduce SigLeak, a black-box framework that reconstructs hidden procedural knowledge by analyzing subtle patterns in agent behavior during benign query processing. Their work demonstrates that even when agents operate behind cloud-hosted interfaces with skills concealed from users, their execution traces expose valuable information about the underlying proprietary procedures. This research highlights how seemingly innocuous agent interactions can inadvertently reveal sensitive model capabilities.

## Key Contributions  
- [Finding 1] Skill Leakage is a real phenomenon where proprietary agent skills manifest as recurring behavioral signatures in execution trajectories, even when users are unaware of their use.  
- [Finding 2] SigLeak successfully reconstructs these hidden skills with high accuracy using only trace data, achieving a 6.88 percentage point improvement over the skill-disabled reference baseline.  
- [Finding 3] The framework consistently outperforms or matches three established baselines across diverse agent frameworks and model families, validating its robustness and generalizability.

## Methodology  
The authors approach Skill Leakage by treating it as a reconstruction problem: given only execution traces from benign queries, they must infer the presence and identity of proprietary skills. SigLeak constructs decision-rich diagnostic tasks that compare trajectories where skills are enabled versus disabled, isolating behavioral patterns unique to skill usage. These patterns serve as latent signatures that can be iteratively refined into a reconstructed skill representation. The method leverages contrastive learning across matched pairs of skilled and unskilled agent behaviors to maximize signal-to-noise ratio in the reconstruction process.

## Results  
Across five experimental scenarios involving three model families (e.g., language models, vision transformers) and three agent frameworks, SigLeak achieves the highest SkillSim score—our metric for both coarse- and fine-grained semantic similarity between reconstructed skills and ground truth. On average, it improves skill reconstruction by 6.88 percentage points compared to the baseline where no skill is present. The framework demonstrates strong performance even when only partial or noisy trajectory data is available, underscoring its efficiency.

## Significance  
This work has significant implications for AI security, privacy, and trust. By exposing that agent skills can be inferred from execution traces, SigLeak raises concerns about unintended disclosure of proprietary knowledge in cloud-hosted systems. It also opens new avenues for skill attribution, debugging, and performance analysis without requiring user interaction or feedback. The findings challenge the assumption that black-box agents are inherently secure, suggesting that behavioral side channels may be exploited to infer sensitive capabilities.

## Related Concepts  
- Skill Leakage: The unintentional exposure of proprietary agent skills through execution traces.  
- Black-box skill reconstruction: Inferring hidden knowledge from behavioral data alone.  
- Execution trajectories: Sequential outputs generated during agent processing that encode internal behavior.  
- SigLeak: A framework for reconstructing skills from anomalous or benign agent behaviors.  
- SkillSim: A similarity metric evaluating the semantic match between reconstructed and true skills.
