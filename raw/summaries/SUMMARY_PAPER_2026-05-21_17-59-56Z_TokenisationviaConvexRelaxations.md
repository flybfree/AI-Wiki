---

title: Tokenisation via Convex Relaxations
url: http://arxiv.org/abs/2605.22821v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-21_17-59-56Z_TokenisationviaConvexRelaxations.md
generated_at: "2026-06-11 10:45"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper presents ConvexTok, a new tokenisation algorithm that formulates tokeniser construction as a linear program and solves it using convex optimisation tools. The method consistently improves intrinsic tokenisation metrics and the bits‑per‑byte (BpB) achieved by language models compared with greedy approaches like BPE and Unigram. It also provides a lower bound to certify how far the resulting tokeniser deviates from optimal, empirically within 1 % at common vocabulary sizes.

## Key Takeaways
- ConvexTok solves tokeniser construction as a linear program using convex optimisation tools.
- The algorithm consistently improves intrinsic tokenisation metrics and bits‑per‑byte for language models.
- A lower bound is provided to certify how far the tokeniser deviates from optimal, empirically within 1 % at common vocab sizes.

## Context
Tokenisation remains a bottleneck in NLP pipelines because greedy algorithms such as BPE and Unigram make locally optimal decisions without considering the global vocabulary impact. This convex approach offers a principled alternative that can be integrated into model training while addressing these limitations.

## Implications
Practitioners can achieve higher efficiency and potentially better downstream performance without sacrificing speed, and the certification helps build trust in the tokeniser's optimality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.22821v1)
