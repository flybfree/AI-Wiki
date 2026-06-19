---

title: Are Sparse Autoencoder Benchmarks Reliable?
url: http://arxiv.org/abs/2605.18229v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-18_11-20-57Z_AreSparseAutoencoderBenchmarksReliable.md
generated_at: "2026-06-11 10:42"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper audits the quality metrics used in SAEBench, a widely adopted suite for evaluating sparse autoencoders (SAEs). It finds that two core metrics—Targeted Probe Perturbation and Spurious Correlation Removal—fail across multiple evaluation lenses, while other metrics exhibit higher reseed noise and lower discriminability than previously assumed. The most reliable metric, sae‑probes, still struggles to distinguish variants of the same SAE architecture.

## Key Takeaways
- Targeted Probe Perturbation (TPP) and Spurious Correlation Removal (SCR) are unreliable for SAE evaluation because they fail under reseed noise, ground‑truth correlation checks, and discriminability tests.  
- The sae‑probes variant of k‑sparse probing is the most reliable metric tested, yet it cannot separate different instances of the same architecture.  
- Overall, the current SAE benchmarks overestimate performance and lack robustness across evaluation lenses.

## Context
Interpretability tools like sparse autoencoders are essential for understanding large language models, but their assessment relies on benchmarks that may not reflect real‑world performance. The field needs standardized, robust metrics to guide model development and trustworthy interpretability claims.

## Implications
Practitioners should avoid using TPP or SCR as primary SAE evaluation tools and focus on sae‑probes while recognizing its limitations. Improving benchmark design will help the AI community move beyond misleading results toward reliable interpretability research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.18229v1)
