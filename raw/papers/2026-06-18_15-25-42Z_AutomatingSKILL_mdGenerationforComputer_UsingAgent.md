---

title: Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining
published: "2026-06-18T15:25:42Z"
authors: Yuexing Hao, Xiaomin Li
url: http://arxiv.org/abs/2606.20363v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Automating SKILL.md Generation for Computer-Using Agents via Interaction Trajectory Mining



**Source**: [Original Paper](http://arxiv.org/abs/2606.20363v1)
## Abstract
Explicit skill libraries make computer-using agents easier to inspect, but it remains unclear whether such libraries can be mined from interaction data in a way that improves downstream policies. We study this question through a three-stage pipeline that segments GUI trajectories, clusters segments into candidate skills, and trains a skill-aware policy from the resulting annotations. The mined clusters are readable on the source benchmark: five of eight clusters have at least 0.95 purity against InteraSkill Workflows labels. However, readability does not imply transfer. GRPO improves IW skill-step accuracy only from 18.5\% to 20.5\%, leaves BrowseComp+ essentially unchanged, and underperforms trivial frequency priors on key source-domain metrics. We therefore present the method as a diagnostic study: trajectory mining can expose inspectable skill structure, but the current boundary detector, orderless segment representation, and offline reward model are insufficient for reliable cross-domain policy improvement.

## Metadata
- **Published**: 2026-06-18T15:25:42Z
- **Authors**: Yuexing Hao, Xiaomin Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.20363v1)