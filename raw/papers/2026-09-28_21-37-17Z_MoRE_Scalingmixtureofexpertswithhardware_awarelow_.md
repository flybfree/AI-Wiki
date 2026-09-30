---
title: MoRE: Scaling mixture of experts with hardware-aware low-rank routing
published: 2026-09-28T21:37:17Z
authors: Honam Wong, Surbhi Goel, Enric Boix-Adserà
url: http://arxiv.org/abs/2609.36301v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoRE: Scaling mixture of experts with hardware-aware low-rank routing

## Abstract
Mixture-of-Experts (MoE) layers are central to frontier language models, and recent architectures push toward more and smaller experts. In this regime, the standard linear router becomes a bottleneck: with $M$ experts and hidden dimension $h$, its per-token cost $Θ(Mh)$ dominates the MoE layer once $M$ is large. We introduce MoRE (Mixture of Rank-reduced-routed Experts), which factorizes the router weight matrix at rank $r$ and reduces the routing cost to $O((h + M)r)$. We prove that rank logarithmic in $M$ suffices for routing expressivity when the number of active experts is fixed, and is necessary up to precision factors. We also prove that logarithmic rank preserves load balance in a Gaussian memorization model, and training on a synthetic phonebook task shows that low rank does not hurt memorization. At matched active FLOPs, the factorization allows a factor of $Θ(h/r)$ more experts. To realize this gain in wall-clock time, we design a fused Triton kernel at inference that avoids expensive memory operations on HBM. Empirically, MoRE improves memorization on the phonebook task and performance on knowledge-intensive Q\&A benchmarks after pretraining, while matching reasoning ability. Code available at https://github.com/Matheart/MoRE_code.

## Metadata
- **Published**: 2026-09-28T21:37:17Z
- **Authors**: Honam Wong, Surbhi Goel, Enric Boix-Adserà
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36301v1)