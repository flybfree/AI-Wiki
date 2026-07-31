---
title: Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures
published: 2026-07-30T03:10:24Z
authors: SiYuan Ma, Yiqin Luo,  Zhangji, Canran Xiao, Albert Gao, Wei-Hsing Huang, Wei Wang, Qiwei Wu, Xinran Li, Jinfeng Wei, Qixin Zhang
url: http://arxiv.org/abs/2607.27617v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hidden APIs in Language Models: Discovering Reusable Causal Interfaces from Forked Futures

## Abstract
Identical language-model answers can arise from hidden states that support different future computations, so current-answer probes do not establish a reusable internal interface. We introduce forked futures: future operations are sampled only after a prefix state has formed, and states are compared through the response distributions induced by those operations. This yields an empirical causal quotient over hidden states without requiring researcher-specified latent labels. Shared, Local, Mixture, and Distributed interfaces then compete under prequential causal description length subject to future-signature fidelity and matched capacity constraints. In the two detailed model evaluations, Shared has the lowest held-out description length, with gains of 0.216 nats on Qwen2.5-1.5B and 0.294 nats on Llama-3-8B, while maintaining tightly clustered mean future-signature distortion; a five-backbone sweep preserves the positive direction of Sharedness Gain. The figure-aligned transplantation analysis gives Shared the strongest joint target-correctness, locality, copy-preservation, and composite profile, and API-aligned paths mediate 0.749 of the target effect versus 0.150 for matched null paths. In the blind four-class model-organism test, 14/16 architectures are recovered, with one observed non-Shared to Shared error among 12 non-Shared organisms. These results support an economical reusable causal interface within the tested operation banks, while keeping the claim explicitly conditional on the candidate architectures, interventions, and held-out futures.

## Metadata
- **Published**: 2026-07-30T03:10:24Z
- **Authors**: SiYuan Ma, Yiqin Luo,  Zhangji, Canran Xiao, Albert Gao, Wei-Hsing Huang, Wei Wang, Qiwei Wu, Xinran Li, Jinfeng Wei, Qixin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27617v1)