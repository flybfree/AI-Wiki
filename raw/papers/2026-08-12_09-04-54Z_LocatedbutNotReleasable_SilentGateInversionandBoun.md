---
title: Located but Not Releasable: Silent Gate Inversion and Bounded Linear Release
published: 2026-08-12T09:04:54Z
authors: Xining Xun
url: http://arxiv.org/abs/2608.11822v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Located but Not Releasable: Silent Gate Inversion and Bounded Linear Release

## Abstract
A growing body of work reports that language models represent task-relevant latent structure that they fail to use. Whether such structure, once located, can be converted into behavior is a separate question that is rarely tested end to end. We submit the complete pipeline -- detect, localize, and release -- to a fully preregistered stress test on a 25.7M transformer trained on causal-evidence discrimination, where a known suppression phenomenon (latent causal structure present but behaviorally unused) has previously been documented. Every threshold, claim template, and decision-tree branch was hashed and archived before any corresponding data existed. Three findings. (i) Localization succeeds: interventions at observation-evidence channels of mid layers restore target behavior on otherwise-suppressed worlds (paired release advantages $0.563$ and $0.854$, 97.5% CIs excluding zero; best-site release rate $0.889$). (ii) Gating fails out of distribution: a detector calibrated to trigger on zero out-of-distribution calibration worlds triggers on 6.9-7.3% of held-out in-distribution generations and on zero of the 2,400 held-out generations that actually need it -- a complete inversion that silently reduces the gated pipeline to its base model. (iii) Linear release is capped: removing the gate and injecting a per-instance linear direction unconditionally yields a monotone dose-response that plateaus far below the preregistered release margin (intercept $0.382 \to 0.311 \to 0.264$ vs. threshold $\le 0.08$); per-instance adaptivity adds less than $\pm 0.03$. The failure is doubly located: the detector is OOD-inverted, and the entire family of linear release directions at this site and resolution is bounded away from sufficiency. The two failures are dissociable, and neither overturns localization. Every number traces to a hashed artifact in the released audit chain.

## Metadata
- **Published**: 2026-08-12T09:04:54Z
- **Authors**: Xining Xun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11822v1)