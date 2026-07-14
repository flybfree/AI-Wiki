---

title: "Summary: Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining"
url: http://arxiv.org/abs/2606.20363v1
type: paper-summary
date: 2026-06-18
source_paper: 2026-06-18_15-25-42Z_AutomatingSKILL_mdGenerationforComputer_UsingAgent.md
generated_at: "2026-06-18 21:00"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-06-18 Automating Skill Md Generation For Computer-Using 


## Summary
This paper proposes a pipeline that mines skill libraries from computer‑using agents’ interaction trajectories to improve downstream policies. The study shows that while the mined clusters are highly readable on the source benchmark, they do not guarantee transferability, and current methods only modestly boost performance.

## Key Takeaways
- Five of eight clusters achieve 0.95 purity against InteraSkill Workflows labels, indicating strong interpretability within the same domain.
- GRPO improves IW skill‑step accuracy from 18.5 % to 20.5 %, but BrowseComp+ remains unchanged and performance drops below trivial frequency priors on key metrics.
- The pipeline’s boundary detector, orderless segment representation, and offline reward model limit reliable cross‑domain policy improvement.

## Context
Automating skill extraction from interaction data is a central challenge in building interpretable AI agents. Understanding how skills emerge can guide better training objectives and improve generalization across tasks.

## Implications
For practitioners, this research highlights the need for richer representations and domain‑aware reward modeling to leverage mined skills effectively. It also underscores that interpretability alone does not translate into performance gains without proper integration.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.20363v1)
