---
title: Cocktail-Talker: Multi-Speaker Dialog Modeling in Noisy Social Environments with Turn Action GRPO
url: http://arxiv.org/abs/2607.27756v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_06-53-15Z_Cocktail_Talker_Multi_SpeakerDialogModelinginNoisy.md
generated_at: 2026-07-30 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Cocktail-Talker, a framework for modeling multi‑speaker spoken dialogs in noisy social environments where the assistant must decide whether to respond, listen, or ignore. It uses three action tokens placed before any response and trains via supervised fine‑tuning combined with reinforcement learning to generate appropriate actions and only produce speech when <|respond|> is selected.

## Key Takeaways
- Cocktail-Talker employs three action tokens (<|respond|>, <|listen|>, <|ignore|>) to capture the assistant's decision to speak or stay silent in multi‑speaker noisy environments.
- The training pipeline, Cocktail-DialogGen, simulates realistic dialogues with speaker roles across diverse social contexts using an LLM data generator.
- The model is trained through supervised fine‑tuning combined with reinforcement learning to optimize action selection and response generation.

## Context
Multi‑speaker dialog systems face challenges beyond simple turn‑based interactions, requiring agents to filter irrelevant speech and background noise. This work addresses those complexities by modeling selective engagement as a discrete action problem.

## Implications
By enabling assistants to ignore distractions and focus on relevant participants, Cocktail-Talker could improve real‑world conversational AI performance in crowded settings like cafés or meetings. Practitioners can leverage the framework for more natural, context‑aware dialog agents that respect social dynamics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27756v1)
