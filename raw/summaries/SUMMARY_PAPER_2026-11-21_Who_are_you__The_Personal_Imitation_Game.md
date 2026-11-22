---
title: Who are you? The Personal Imitation Game
url: http://arxiv.org/abs/2611.24888v1
type: paper-summary
date: 2026-11-21
source_paper: 2026-11-18_18-32-14Z_Whoareyou_ThePersonalImitationGame.md
generated_at: 2026-11-21 21:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Personal Imitation Game, a harder variant of Turing's 1950 Imitation Game that asks whether a machine can convincingly replicate a specific individual in conversation rather than a generic human. The authors test 30 participants to establish a human baseline, identify the identity signals interrogators rely on (stylometric features, personality traits, and biographical facts), and demonstrate the framework using an LLM-based system trained on ten years of one author's personal digital communications. In a 20-person deception study, interrogators chose the AI system over the author's own friends in 7 of 10 rounds, while choosing the author over the system in 13 of 20 rounds—neither rate distinguishable from chance at this sample size.

## Key Takeaways
- The Personal Imitation Game shifts the evaluation target from generic human-likeness to individual-specific identity replication, requiring systems to capture stylometric features, personality traits, and biographical facts that interrogators use to identify a particular person. This reframes the Turing test from a broad capability benchmark into a personalized fidelity challenge.
- The authors built an LLM-based system using an autoethnographic dataset spanning ten years of personal digital communication from one of the paper's authors, demonstrating a concrete pipeline for constructing personal AI agents from longitudinal private data. This provides a methodological blueprint for how personal AI systems could be trained and evaluated.
- The deception study results (7/10 and 13/20) are statistically indistinguishable from chance, indicating that at this sample size the system neither convincingly outperforms nor underperforms the actual individual. This highlights both the difficulty of the task and the need for larger, more rigorous evaluation protocols before drawing firm conclusions about personal AI fidelity.

## Context
As LLMs increasingly pass traditional Turing-style benchmarks, the field needs harder evaluation frameworks that probe deeper dimensions of human identity rather than surface-level conversational fluency. The Personal Imitation Game addresses a growing research frontier around personalized AI agents, digital twins, and identity-preserving language models, which are becoming central to applications in mental health companions, personalized assistants, and digital legacy preservation. By formalizing the signals humans use to recognize specific individuals—stylometry, personality, biography—the paper provides a structured evaluation methodology that the broader AI community can adopt for assessing personalization fidelity.

## Implications
For practitioners building personal AI agents, this work offers a concrete evaluation protocol and identifies the specific identity signals (stylistic patterns, personality traits, biographical knowledge) that must be captured to achieve convincing individual replication. For industry, the findings raise urgent questions about privacy, consent, and identity ownership when AI systems are trained on years of personal communications, and suggest that current systems cannot yet reliably distinguish themselves from the individuals they emulate. For the research community, the paper signals that passing generic human-likeness benchmarks does not guarantee personal identity fidelity, calling for new benchmarks and larger-scale studies before personal AI agents are deployed in sensitive social or therapeutic contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.24888v1)
