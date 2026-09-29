---
title: Nudgeability: Reasoning Models Follow Confidence Signals Without Tracking Their Own Competence
published: 2026-09-28T08:20:09Z
authors: Rohit Saxena, Utkarsh Upadhyay
url: http://arxiv.org/abs/2609.34572v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Nudgeability: Reasoning Models Follow Confidence Signals Without Tracking Their Own Competence

## Abstract
Reasoning language models that can call tools must decide during inference whether to answer unaided or delegate. Any self-reflection mechanism for this must answer three questions: where the reflective signal comes from (verbal reports, output distributions, hidden states, a separate predictor), how it is presented to the model (numerical prediction, confidence token, prompt injection), and whether it changes the model's subsequent action. We isolate the third question. At a fixed point in otherwise identical reasoning trajectories, we insert a single first-person sentence expressing either confidence or doubt; the model then continues reasoning and chooses whether to answer directly or call a tool. Comparing these counterfactual continuations measures the causal effect of the reflective signal on delegation. We call this behavioral response Nudgeability and measure it along two dimensions: sensitivity, how strongly confidence and doubt change delegation rates, and targeting, whether delegation increases for problems the model cannot solve unaided and decreases for those it can.   Across nine small-to-medium open-weight reasoning models from three families (Qwen, Gemma, and GLM) and two tasks, models are consistently sensitive: doubt increases delegation and confidence decreases it, with a median confidence-to-doubt swing of 20.6 percentage points, and 53 to 70 points for the larger provider-served models. This responsiveness is poorly targeted: a median 42% of induced flips are well-targeted, only a +2 percentage-point lift over a random-selection baseline. Confidence language is thus a strong control surface for delegation, but current models use it only weakly in accordance with their actual competence. Nudgeability offers a simple, post-training-free way to evaluate both sensitivity and targeting as endogenous self-reflection mechanisms mature.

## Metadata
- **Published**: 2026-09-28T08:20:09Z
- **Authors**: Rohit Saxena, Utkarsh Upadhyay
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34572v1)