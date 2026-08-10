---
title: SkillEval: Decomposing Agent Skill Quality into Interpretable Signals
published: 2026-08-07T07:25:17Z
authors: Jiahui Han, Qinuo Li, Ziheng Peng, Haotian Wu, Haoze Liu, Danfeng Shan, Guanchu Wang, Huiqi Deng, Ninghao Liu
url: http://arxiv.org/abs/2608.06891v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillEval: Decomposing Agent Skill Quality into Interpretable Signals

## Abstract
Agent skills provide reusable procedural knowledge that helps agents solve specialized tasks. As their use expands, evaluating skill quality becomes increasingly important. Existing evaluations often measure skill quality by testing whether a skill improves performance on specific downstream tasks. However, a reusable skill may apply to multiple task scenarios. Downstream evaluation mainly reflects the compatibility between a skill and the evaluated task, provides only a partial view of skill quality, and does not identify which aspect of the skill should be improved. We find that general properties of the \texttt{SKILL.md} document play an important role in skill quality. To evaluate these properties, we propose \textbf{SkillEval}, an interpretable framework for document-level skill evaluation. SkillEval evaluates each property using a fixed and inspectable scoring direction, producing interpretable scores. It further measures and reduces the influence of unrelated document features, such as length and formatting, so that each score captures its intended semantic property more specifically. Specifically, SkillEval learns an interpretable direction for each quality property from controlled positive--negative skill pairs in the hidden representation space of the model, and scores a new skill by projecting its representation onto these fixed directions. We use SkillEval to evaluate skills in controlled quality tests and show that SkillEval reliably distinguishes skills of different quality. In addition, SkillEval scores closely reflect downstream task performance, providing an early indication of whether a skill is likely to help an agent complete a task. We further explore SkillEval for diagnosing weaknesses in skill documents and guiding targeted revisions. The revised skills improve the targeted properties and achieve higher pass rates on downstream tasks.

## Metadata
- **Published**: 2026-08-07T07:25:17Z
- **Authors**: Jiahui Han, Qinuo Li, Ziheng Peng, Haotian Wu, Haoze Liu, Danfeng Shan, Guanchu Wang, Huiqi Deng, Ninghao Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06891v1)