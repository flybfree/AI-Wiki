---
title: Measuring the Assistant's Harmlessness Preferences on the User Turn
url: http://arxiv.org/abs/2609.23935v1
type: paper-summary
date: 2026-09-21
source_paper: 2026-09-20_23-25-03Z_MeasuringtheAssistant_sHarmlessnessPreferencesonth.md
generated_at: 2026-09-21 23:19
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates whether safety-oriented preferences—specifically a preference for harmlessness over harmfulness—are localized only to the assistant's turn or if they influence the model's predictions of user input. The study reveals that post-training significantly alters the model's internal representation of the user, meaning the "harmless" persona is not just an output filter but a fundamental shift in how the model anticipates and interprets human interaction.

## Key Takeaways
- Safety preferences are not localized to the assistant's turn; instead, they shape the model's predictions for other speakers, including the user, demonstrating that these traits are integrated into the model's broader worldview rather than just being a surface-level persona.
- These harmlessness preferences are virtually non-existent in pre-trained base models but emerge significantly during post-training and show a positive correlation with model scale across various open-weight families.
- The researchers demonstrated that these internal representations can be shifted using narrow fine-tuning on assistant turns alone, proving that the model's "view" of the user is being reshaped by safety training even when those specific user turns are not directly modified during the training process.

## Context
This paper contributes to the ongoing debate over how large language models (LLMs) internalize human values and safety constraints during alignment phases like Reinforcement Learning from Human Feedback (RLHF). It provides a crucial empirical look at whether "alignment" is a superficial layer or a deep structural change in the model's cognitive mapping of social interaction.

## Implications
For AI researchers, these findings suggest that current post-training methods may be fundamentally altering how models perceive and predict human behavior rather than just filtering output content. This implies that future safety research must consider these "hidden" changes to user representation, as they could affect the model's ability to understand intent or collaborate effectively in complex scenarios beyond simple content moderation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.23935v1)
