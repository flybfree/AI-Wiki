---
title: You Are the Trigger: Speaker-Activated Backdoors
published: 2026-10-19T19:43:13Z
authors: Nataša Krčo, Euodia Dodd, Peter Romov, Yves-Alexandre de Montjoye
url: http://arxiv.org/abs/2610.27210v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# You Are the Trigger: Speaker-Activated Backdoors

## Abstract
Speech models are increasingly used as an interface to AI systems, from transcription tools to voice agents. Existing audio backdoors require an attacker to introduce triggers at inference time. We study a different threat model in which the attacker compromises the model during fine-tuning but has no access to the victim's inference-time inputs. We introduce the Speaker-Activated Backdoor (SAB) setting, in which a target speaker's natural voice serves as the trigger. We develop a two-phase fine-tuning method that first makes speaker identity more accessible and then binds the target speaker to an attacker-chosen payload. Compared with a one-phase baseline with the same training budget, the two-phase method substantially improves selectivity and clean performance, and is especially important for content-dependent attacks. SAB achieves 90.2% and 97.0% backdoor success on Whisper-medium and Parakeet, with false-positive rates of 1.7% and 0%, respectively using as little as two minutes of real audio from the target speaker. We further demonstrate content-dependent semantic rewriting and downstream tool-use attacks, where malicious instructions are inserted into 96.9% of target-speaker transcripts. When these transcripts are passed to frontier LLM agents, GPT-4o and Claude (Opus, Sonnet, and Haiku), the injected instruction drives the agent to carry out the harmful action in up to 87.5% of cases. The attack generalizes to held-out recordings, multiple target speakers, and common acoustic degradations. These results establish speaker identity as a practical backdoor trigger that requires no inference-time attacker access and is invisible at the transcript layer.

## Metadata
- **Published**: 2026-10-19T19:43:13Z
- **Authors**: Nataša Krčo, Euodia Dodd, Peter Romov, Yves-Alexandre de Montjoye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27210v1)