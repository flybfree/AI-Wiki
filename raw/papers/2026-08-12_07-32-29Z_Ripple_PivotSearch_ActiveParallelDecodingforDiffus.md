---
title: Ripple-Pivot Search: Active Parallel Decoding for Diffusion Large Language Models
published: 2026-08-12T07:32:29Z
authors: Yushi Ye, Xu Chen, Haoyun Jiang, Jinsong Lan, Haihong Tang, Bo Han, Ivor Tsang, Yanfeng Wang, Bo Zheng, Jiangchao Yao
url: http://arxiv.org/abs/2608.11742v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ripple-Pivot Search: Active Parallel Decoding for Diffusion Large Language Models

## Abstract
Diffusion Large Language Models (dLLMs) have emerged as a competitive alternative to autoregressive language models, offering the potential for substantially faster inference through parallel decoding. Existing parallel decoding schedulers typically commit positions only after they meet a per-position criterion, overlooking how early commitments may benefit subsequent decoding. We identify a ripple effect in dLLM decoding: proactively committing a mid-entropy pivot position can induce a pronounced reduction in uncertainty across the remaining masked positions. This uncertainty reduction allows subsequent steps to unmask more tokens in parallel, thereby accelerating the overall decoding process. To exploit the ripple effect, we propose Ripple-Pivot Search (RPS), a novel training-free decoding method that seeks mid-entropy positions as promising candidate pivots (where to decode), and determines their token assignment that yields the greatest downstream benefit via lookahead evaluation (what to decode). Across 3 dLLMs and 4 reasoning and code-generation benchmarks, RPS achieves 4-10$\times$ wall-clock speedup over the standard decoder while preserving generation quality, and improves accuracy over the previous lookahead baseline by up to 5.49% while delivering higher throughput in most settings. When integrated with KV caching, RPS further achieves up to 18$\times$ wall-clock speedup over the standard decoder.

## Metadata
- **Published**: 2026-08-12T07:32:29Z
- **Authors**: Yushi Ye, Xu Chen, Haoyun Jiang, Jinsong Lan, Haihong Tang, Bo Han, Ivor Tsang, Yanfeng Wang, Bo Zheng, Jiangchao Yao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11742v1)