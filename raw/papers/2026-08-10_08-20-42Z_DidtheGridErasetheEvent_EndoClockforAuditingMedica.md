---
title: Did the Grid Erase the Event? EndoClock for Auditing Medical World-Model Pipelines
published: 2026-08-10T08:20:42Z
authors: Yarin Udi, Tom Sharon-Shahak, Roee Masad, Dan Pri-Tal
url: http://arxiv.org/abs/2608.09266v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Did the Grid Erase the Event? EndoClock for Auditing Medical World-Model Pipelines

## Abstract
Medical world models commonly learn from multimodal recordings synchronized onto a fixed-rate grid. This preprocessing resamples each native stream onto a shared time axis. Each stream has an observation clock that governs when observations are emitted or updated. When this clock depends on the latent or acquisition state, it is endogenous. In such settings, synchronization may not be neutral and can erase task-relevant evidence before the model sees the data. We introduce a four-regime taxonomy that characterizes where the evidence needed to distinguish a target event or state survives. The relevant witness may remain in the sampled values, in grid-cell update patterns, in native timing, or only in an external acquisition channel. EndoClock operationalizes this taxonomy as a conservative pretraining audit. It reports the lowest witness-bearing representation supported by the available evidence, or unresolved when no regime can be established. We illustrate this failure in echocardiography, where B-mode video write-outs cease during pulsed-wave Doppler acquisition while the corresponding measurement events remain recorded only in an external acquisition log. This work is a preliminary failure alert and executable audit. Its practical message is to preserve the native observation process long enough to determine whether synchronization has erased information required by the intended task.

## Metadata
- **Published**: 2026-08-10T08:20:42Z
- **Authors**: Yarin Udi, Tom Sharon-Shahak, Roee Masad, Dan Pri-Tal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09266v1)