---
title: LLMs Prompted for Legal Context Refuse More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context
published: 2026-10-19T11:38:05Z
authors: Anastasiia Kucherenko, Francois Brouchoud, Dimitri Percia David, Andrei Kucharavy
url: http://arxiv.org/abs/2610.26211v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs Prompted for Legal Context Refuse More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context

## Abstract
Confidentiality requirements increasingly push legal professionals toward small, on-device LLMs that keep case data in-house, used for everyday tasks such as summarization, translation, and reformulation. Following standard prompting guidance, a user naturally states their role (``I am a lawyer...''). We show that this innocuous habit has an unexpected cost: such authority framing can make the model selectively refuse legitimate requests, introducing bias through uneven access to assistance. We evaluate four modern small open-weight LLMs on benign legal-domain prompts to measure this over-refusal.   Surprisingly, we find that authority-style prefixes (''I am legal counsel working for a national supreme court'', ''I'm a defense lawyer'') systematically increase refusal rates by 2--20x over the no-prefix baseline, while a known role-play jailbreak prefix shows mixed effects, sharply increasing refusals in some models and barely shifting them in others. The finding suggests that small on-prem deployable LLMs are unstable under contextual framings that a real institutional user might naturally introduce, and further investigation is essential to minimize opportunities for bias.

## Metadata
- **Published**: 2026-10-19T11:38:05Z
- **Authors**: Anastasiia Kucherenko, Francois Brouchoud, Dimitri Percia David, Andrei Kucharavy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.26211v1)