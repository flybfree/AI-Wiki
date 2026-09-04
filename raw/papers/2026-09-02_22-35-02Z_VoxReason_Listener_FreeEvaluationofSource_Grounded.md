---
title: VoxReason: Listener-Free Evaluation of Source-Grounded Speech Planning Before Synthesis
published: 2026-09-02T22:35:02Z
authors: Mengzhe Geng
url: http://arxiv.org/abs/2609.03203v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VoxReason: Listener-Free Evaluation of Source-Grounded Speech Planning Before Synthesis

## Abstract
Expressive speech systems make a decision before any waveform is rendered: how an utterance is delivered. In dialogue agents, narration, and role-conditioned TTS, that hidden planning step sets affect, pitch, energy, rate, pause, emphasis, and stance, yet downstream audio scores rarely reveal whether those choices were licensed by the source record, a source-use failure that occurs before any waveform exists. VoxReason makes that pre-synthesis decision measurable as a listener-free task for source-grounded speech planning. Before synthesis, VoxReason measures whether delivery choices are grounded in cited source records. Systems output a source-cited speaking-plan with evidence citations, and a deterministic verifier checks citation legality, slot agreement, unsupported state, schema validity, and one-cue counterfactual locality. On 1,440 checked source-label cases, shortcut controls show why slot accuracy alone is unsafe: a key-lookup oracle reaches 1.000 plan-slot accuracy on seen keys, while an emotion prior still reaches 0.958 slot accuracy on source-key-disjoint cases without citing intensity or identity. In a separate 100-case learned source-key-disjoint comparison, a 7B locality SFT+CF repair improves plan-slot accuracy/locality from 0.684/0.141 to 0.919/1.000, and removing source records lowers citation-required grounded score by 0.488. Rendered waveform quality remains outside the present evaluation.

## Metadata
- **Published**: 2026-09-02T22:35:02Z
- **Authors**: Mengzhe Geng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03203v1)