---
title: One Timeline, Many Renderings: A Wolfram Language Paclet for heterogeneous musical output
published: 2026-08-25T15:15:06Z
authors: Francesco Vitucci, Michele Lorusso, Francesco Scagliola
url: http://arxiv.org/abs/2608.24683v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# One Timeline, Many Renderings: A Wolfram Language Paclet for heterogeneous musical output

## Abstract
One algorithmic composition may require a Csound score, engraved notation, real-time control, and a rehearsal click. Authored separately, their timelines drift. Temporal System is a Wolfram Language paclet that instead compiles one immutable store of typed entities on a rational beat timeline through backend-specific contracts. It emits Csound synthesis, beta MusicXML 4.0, OSC control, and click artifacts that remain synchronized because they share that store. Conversion to seconds, samples, or hertz occurs only at render time. Csound notes use stable named instruments in external .orc files; curves become k-rate signals declared against score p-fields. The click backend derives rehearsal audio from the same meter and tempo and reuses the Csound serializer. We describe the temporal, semantic, and rendering-contract layers, their practical trade-offs, and the limits of this proprietary authoring environment within an otherwise open-source ecosystem. The archived supplement exposes the reported outputs pending paclet release.

## Metadata
- **Published**: 2026-08-25T15:15:06Z
- **Authors**: Francesco Vitucci, Michele Lorusso, Francesco Scagliola
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24683v1)