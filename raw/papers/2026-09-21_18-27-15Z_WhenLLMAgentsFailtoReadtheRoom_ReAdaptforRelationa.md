---
title: When LLM Agents Fail to Read the Room: ReAdapt for Relational Social Reasoning
published: 2026-09-21T18:27:15Z
authors: Jianzhe Lin, Xiaolin Li, Yunda Liu, Fei Wang, Jubin Chheda
url: http://arxiv.org/abs/2609.25284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When LLM Agents Fail to Read the Room: ReAdapt for Relational Social Reasoning

## Abstract
A social agent's most basic decisions (should I react to this post? who should I reach out to?) are not purely content problems. The right action often hinges on the latent relationship between people -- tie strength, reciprocity, mutual connections -- rather than on which content is most salient. Standard LLM agent loops do not explicitly represent how new relational evidence should revise the agent's current social hypothesis, leaving them prone to surface-obvious choices when relational and content cues diverge. We formalize this failure mode with a relationship-reasoning benchmark: 500 synthetic social worlds with friendships, follows, reaction histories, and feeds, yielding 1,000 queries over two tasks, reaction selection and warm introduction (finding the best bridge to a target person). By construction, the surface-obvious candidate differs from the relationship-grounded oracle in about 53% of queries, forming an overturn subset where the agent must use relational evidence to revise an initially plausible choice. We propose ReAdapt (Relationship-Adaptive Agent with Policy-driven sTate), which augments the ReAct loop with an explicit structured social state z = (G, B, R, N, D) capturing goal, belief, relationship, norm, and disclosure. After each tool observation, ReAdapt runs a typed Adapt step that updates this state and emits a policy operation (continue, switch, abandon, or clarify) before choosing the next action. With Gemini-3-Flash on a stratified subset of n = 150 queries per task, ReAdapt improves warm-introduction accuracy from 37% to 51% (+14 points) and reaction-selection accuracy from 69% to 77% (+8 points). Oracle regret drops from 0.260 to 0.152 and from 0.095 to 0.053, respectively. Holding the model, tools, and environments fixed, these results suggest that explicit relational-state adaptation helps LLM agents turn retrieved social evidence into revised decisions.

## Metadata
- **Published**: 2026-09-21T18:27:15Z
- **Authors**: Jianzhe Lin, Xiaolin Li, Yunda Liu, Fei Wang, Jubin Chheda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25284v1)