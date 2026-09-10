---
title: An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks
published: 2026-09-08T20:00:03Z
authors: Viet K. Nguyen, Mohammad I. Husain
url: http://arxiv.org/abs/2609.09404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Experimental Evaluation of Multimodal Prompt Injection Attacks on Agentic AI Frameworks

## Abstract
Agentic AI frameworks let a language model plan, keep memory, and call tools that reach real files, mail, and services. Most of these agents also read images, which gives an attacker a way to put text into the agent's context without going through the user. We present MMPIBench, a reproducible benchmark that measures what happens next. It delivers a fixed set of attacks through six visual carriers (OCR text, overlays, EXIF metadata, QR codes, fake interfaces, and hybrids) and records how far each injected instruction travels through the agent, from perception through planning to the tool call. Across 720 runs covering six frameworks, five foundation models, six carriers, and four attacker objectives, attacks complete in approximately 1% of runs but are attempted in 12.8%, and the gap is closed almost entirely at the planning step, where the model reads the injected instruction and declines to act on it. The model matters far more than the framework for whether an instruction is acted on. One model never attempts an attack and recognizes the injection in 59.7% of runs, while two others attempt in 23.6%. We then extend the benchmark to audio, the only other raw perceptual channel current frontier models accept. Only two of the five models ingest audio and only three of the six frameworks deliver it, but where the signal arrives the attack completes in 49% of cells, and in 75% for one model. Reporting completion alone therefore understates exposure, and perceptual channels beyond vision are narrower but much less defended.

## Metadata
- **Published**: 2026-09-08T20:00:03Z
- **Authors**: Viet K. Nguyen, Mohammad I. Husain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09404v1)