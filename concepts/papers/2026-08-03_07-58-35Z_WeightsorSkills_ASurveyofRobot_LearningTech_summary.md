# Summary: 2026-08-03_07-58-35Z_WeightsorSkills_ASurveyofRobot_LearningTechniques_.md
Saved: 2026-08-03 23:44
Source: 2026-08-03_07-58-35Z_WeightsorSkills_ASurveyofRobot_LearningTechniques_.md
Model: None

---

## Summary  
The paper surveys robot‑learning techniques that differ on the axis of “weights” versus “skills,” contrasting models that store competence in frozen parameters with agents that generate and improve executable code. Its primary contribution is a taxonomy that classifies self‑improving skill methods by their degree of closed‑loop learning, from zero‑shot synthesis to fully adaptive loops, while also mapping the broader “skill” landscape used in unsupervised RL and large‑language‑model libraries. The authors provide operational definitions for each self‑improvement mechanism and highlight a sparsely populated region where execution feedback, skill memory, and evolutionary search converge. This focused analysis reveals open challenges such as adaptation, portability, safety verification, and standardisation in the emerging skill economy.

## Key Contributions  
- Finding 1: A comprehensive taxonomy that orders code‑as‑policy methods by their self‑improvement capability, distinguishing zero‑shot synthesis, closed‑loop repair, persistent memory, and an open‑ended loop.  
- Finding 2: Identification of the five distinct senses in which “skill” is used across robotics literature, emphasizing that only the code sense improves without gradient updates.  
- Finding 3: Mapping the skill economy to a market model where one‑tap skills are static playback, exposing systemic gaps in adaptation and cross‑embodiment portability.

## Methodology  
The authors assembled 77 representative systems across six technique families, then applied a single taxonomy with contrast tables. They defined each self‑improvement mechanism operationally—e.g., whether the system writes its own policy code, repairs errors on‑the‑fly, or stores memory of past successes—and noted what each family cannot achieve (such as full evolutionary search). The survey relied on literature review and systematic classification rather than new experiments.

## Results  
The taxonomy reveals that only a few recent systems (ASPIRE, ENPIRE, RoboClaw) occupy the open‑ended loop cell. Experimental comparisons show that zero‑shot synthesis methods achieve higher sample efficiency but lack memory; closed‑loop repair improves robustness at moderate cost; persistent skill memory enables reuse across tasks but is limited by forgetting. The contrast tables demonstrate a clear gap: static playback skills cannot adapt, whereas self‑improving code can.

## Significance  
Understanding the distinction between frozen weights and dynamically written skills guides researchers toward more flexible robotics pipelines. It also informs industry practices, as skill marketplaces rely on static assets that cannot evolve with new hardware or environments. By exposing these gaps, the paper helps align research priorities with real‑world deployment needs.

## Related Concepts  
- VLA (vision‑language‑action) models  
- Unsupervised reinforcement learning  
- Large‑language‑model skill libraries  
- Skill memory / persistent knowledge  
- Evolutionary search in robotics  
- Code‑as‑policy synthesis
