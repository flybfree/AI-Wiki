---
title: RIPPLE: Generating Multi-Channel Phase, Not Recovering It
published: 2026-07-30T07:07:52Z
authors: Jaehyuk Lee, Yeajin Lee, Dayeon Shin, Donghun Lee
url: http://arxiv.org/abs/2607.27775v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RIPPLE: Generating Multi-Channel Phase, Not Recovering It

## Abstract
Generative models synthesize magnitude spectra with high fidelity, while phase is delegated to a recovery module---Griffin--Lim, a vocoder, or a latent decoder---applied independently to each channel. For multi-channel waveforms this delegation is costly: the physical content of spatial audio and three-component seismograms lives in the phase relationships between channels, precisely what channel-independent recovery cannot produce. The cost is also invisible, since the magnitude-based metrics common to both fields barely move when inter-channel phase coherence collapses---so a pipeline can discard the physical information in its output while still scoring well. We argue that phase should be generated, not recovered, and present RIPPLE (Rectified Inter-channel Phase with Prior-based LEarning), which reinterprets Griffin--Lim as a phase **prior** rather than a final estimator: initialized from the source phase, this prior carries the inter-channel structure to be preserved, and a rectified flow refines it toward the target under an explicit inter-channel phase loss. Tested on first-order ambisonics environment transfer and seismic cross-station translation---two physically unrelated domains---RIPPLE outperforms recovery-based pipelines on the coherence metrics that downstream analyses consume. The seismic case is decisive: across architecturally distinct generators, per-channel recovery leaves S-wave polarization error near the $57.3^\circ$ random expectation, whereas learned phase reduces it to $33.8^\circ$.

## Metadata
- **Published**: 2026-07-30T07:07:52Z
- **Authors**: Jaehyuk Lee, Yeajin Lee, Dayeon Shin, Donghun Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27775v1)