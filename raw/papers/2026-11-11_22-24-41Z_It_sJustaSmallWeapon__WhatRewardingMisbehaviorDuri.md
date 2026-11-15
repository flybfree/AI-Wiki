---
title: "It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models
published: 2026-11-11T22:24:41Z
authors: Mohammad Omar Khursheed, Thomas Morris, Fabien Roger
url: http://arxiv.org/abs/2611.16069v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# "It's Just a Small Weapon": What Rewarding Misbehavior During RL Does to Character-Trained Models

## Abstract
Developers train models to follow a consistent character using methods like Model Spec Midtraining (Li et al., 2026), which have been hypothesized to make alignment more robust and generalize broadly. However, it is possible for subsequent RL with misspecified rewards to work against character training. In this work, we apply character training to teach gpt-oss-20b a semi-realistic constitution and study how it interacts with two types of RL that reward breaking the constitution's rules (opposing RL): answering harmful requests rewritten as math problems, and reward hacking in agentic coding environments. The character-trained models learn both behaviors easily, though they are slightly slower than gpt-oss-20b to answer harmful requests. Character-trained models also display more motivated reasoning on harmful answers than gpt-oss-20b, and hack on some tasks which monitors find harder to catch. Finally, since explaining the reasons behind rules can improve how alignment generalizes (Kutasov et al., 2026), we compare constitutions that justify the same rules by grounding them in a value or not, and find little difference between motivations on misalignment, honesty, and capability evaluations.

## Metadata
- **Published**: 2026-11-11T22:24:41Z
- **Authors**: Mohammad Omar Khursheed, Thomas Morris, Fabien Roger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.16069v1)