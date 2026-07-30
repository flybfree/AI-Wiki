---
title: HoF-Bench: Rediscovering Real AI-Discovered CVEs Without Frontier Models
url: http://arxiv.org/abs/2607.27030v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_15-25-07Z_HoF_Bench_RediscoveringRealAI_DiscoveredCVEsWithou.md
generated_at: 2026-07-29 20:13
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces HoF-Bench a benchmark to evaluate AI vulnerability scanners against real CVEs discovered by AISLE without using frontier models. It shows that minimal LLM analyzers can rediscover up to 65 of 95 CVEs while no frontier model performs detection under the same blind protocol.  

## Key Takeaways  
- The benchmark uses 95 AI‑discovered CVEs across eight repos and tests detectors without CVE identifiers or fixes.  
- All models miss at least some CVEs, especially those in C infrastructure code, indicating language‑specific difficulty.  
- No frontier model succeeds anywhere, proving that detection is not a front‑end problem.  

## Context  
AI vulnerability scanners rely on large language models to locate hidden flaws, yet most evaluations use powerful frontier models that may bias results. HoF-Bench strips away those advantages to reveal the true limits of simpler detectors.  

## Implications  
Industry must prioritize robust, lightweight analyzers for production pipelines rather than relying solely on high‑capacity models. The benchmark guides research toward reliable detection across diverse codebases without over‑engineering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27030v1)
