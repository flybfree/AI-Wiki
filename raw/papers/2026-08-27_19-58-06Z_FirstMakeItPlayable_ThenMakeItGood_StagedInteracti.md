---
title: First Make It Playable, Then Make It Good: Staged Interaction Learning for Small Dialogue-Game Agents
published: 2026-08-27T19:58:06Z
authors: Syed Mahbubul Huq, Pranava Madhyastha
url: http://arxiv.org/abs/2608.27672v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# First Make It Playable, Then Make It Good: Staged Interaction Learning for Small Dialogue-Game Agents

## Abstract
We present Qwen-GuidePlay-2B, a 2B-parameter language model for dialogue-game interaction. We fine-tune Qwen3.5-2B using three steps: a) SFT on only successful game trajectories from Playpen, b) weighted turn-level SFT, and c) teacher-guided SFT. The teacher model (which is a larger model) is only used to fix formatting and evaluate examples, but does not create new gold actions. Our final model scores 57.12 clemscore and 42.68 statscore on the public Playpen validation. In the officially released challenge results, our model obtains the second-highest Playpen clemscore delta among submitted systems (which is approximately +36 over its base model). Our findings suggest that imitating full trajectories helps with playability, while turn-level and teacher-guided training usually improve decision-making and increase the overall score. Alternative procedurally heavy approaches like replay-repair and hard-example mining did not help, which suggests that small models are performant simply by using careful curation strategies rather than aggressive changes. We make available both the model and the code for reproducibility.

## Metadata
- **Published**: 2026-08-27T19:58:06Z
- **Authors**: Syed Mahbubul Huq, Pranava Madhyastha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27672v1)