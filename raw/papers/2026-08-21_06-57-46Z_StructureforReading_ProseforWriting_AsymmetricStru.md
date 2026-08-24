---
title: Structure for Reading, Prose for Writing: Asymmetric Structural Conditioning in Multi-Agent Document Authoring
published: 2026-08-21T06:57:46Z
authors: Cheng Yu, Nikhil Mathew, Zhengjie Wang
url: http://arxiv.org/abs/2608.20786v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structure for Reading, Prose for Writing: Asymmetric Structural Conditioning in Multi-Agent Document Authoring

## Abstract
Multi-agent pipelines that author formal documents must both read a requester's forms and write against them. We report a deployed tender-response system, running an open-weights model under sovereignty constraints, and evaluate it against human-written bids the same organisation actually submitted. On a blind comparison where the system had no worked example available, an LLM judge rated its answers at least as good as the human-submitted answer on $40$ of $55$ ground-truth sections, better on $4$, missing on none, and flagged one unsupported claim in total. Classifying every gap the judge identified shows that $68\%$ were content absent from the system's own sources -- knowledge the human author held and the pipeline was never given -- so only $6$ of the $15$ adverse verdicts involve a deficiency the system could have avoided. A divergence from ground truth is more often an information-availability result than a writing-quality one, and evaluations that do not separate the two understate such systems. Against this backdrop we report a conditioning asymmetry. It is well established that rendering documents as structural markup rather than flat prose improves extraction, and we reproduce that on three reading tasks. The benefit does not transfer to conditioning: converting a bid's \emph{instruction} material from prose to nested XML dropped answer quality from $74\%$ to $48\%$ under a paired comparison. We further find that naming a forbidden construction concentrates rather than removes it -- $96\%$ of surviving defects fall in the two forms the prompt explicitly names -- and that coupling a stochastic annotation to a deterministic windowing function moves the extracted requirement count from $68$ to $51$ on a byte-identical file. Structure belongs where the model reads; prose and self-applied tests belong where it writes.

## Metadata
- **Published**: 2026-08-21T06:57:46Z
- **Authors**: Cheng Yu, Nikhil Mathew, Zhengjie Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20786v1)