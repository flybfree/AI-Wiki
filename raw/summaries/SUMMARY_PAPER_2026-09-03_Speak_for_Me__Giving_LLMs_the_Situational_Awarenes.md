---
title: Speak for Me: Giving LLMs the Situational Awareness to Participate in a Meeting
url: http://arxiv.org/abs/2609.03923v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_14-38-09Z_SpeakforMe_GivingLLMstheSituationalAwarenesstoPart.md
generated_at: 2026-09-03 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAPA, a collaborative agent predictive architecture that gives large language models situational awareness in online meetings. It reduces the silence rate from 51.4% to 2.5% by predicting when and what a delegate should say, using a Perceiver, Predictor, Controller, Generator, judges, and recalibrator loop.

## Key Takeaways
- CAPA lowers the omission silence rate from 51.4% to 2.5% across 137 AMI meetings, showing that structured meeting state tracking enables timely contributions.
- The architecture’s failure mode shifts from missing turns to selecting wrong propositions, with each residual near‑miss linked to a specific module such as the meeting state or prediction.
- Human‑aligned scoring via Cohen's kappa = 0.71 demonstrates that the episode‑level protocol reliably matches human annotations for when and what is said.

## Context
Online meeting delegation remains a challenge because LLMs lack awareness of who has spoken, whose turn it is, and how ideas evolve. Current prompt‑only agents cannot adapt to dynamic conversations, leading to high rates of silence and missed contributions.

## Implications
This work shows that integrating structured state tracking can transform LLM behavior in real‑time settings, offering a path for assistants that truly participate rather than merely observe meetings. Practitioners may adopt CAPA’s module design to improve engagement and reduce miscommunication.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03923v1)
