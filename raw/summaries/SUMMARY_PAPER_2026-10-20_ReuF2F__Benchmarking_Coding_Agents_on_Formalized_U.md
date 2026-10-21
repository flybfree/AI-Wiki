---
title: ReuF2F: Benchmarking Coding Agents on Formalized Undergraduate Research Problems
url: http://arxiv.org/abs/2610.27046v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_17-52-28Z_ReuF2F_BenchmarkingCodingAgentsonFormalizedUndergr.md
generated_at: 2026-10-20 22:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ReuF2F introduces a new Lean 4 benchmark comprising 244 formalized open problems sourced from Research Experiences for Undergraduates (REU) programs, designed to evaluate coding agents on entry-level open research problems across diverse mathematical subfields. The benchmark addresses limitations in existing formal mathematics evaluations by using less prominent problems that are less likely to have been solved or widely disseminated, thereby providing a more reliable held-out evaluation. The authors' evaluation reveals that even the best-performing model resolves only approximately 40% of the problems, indicating substantial remaining room for improvement in automated formal problem-solving.

## Key Takeaways
- The benchmark draws 244 problems from REU programs spanning a broad range of mathematical subfields, deliberately selecting less prominent open problems that tend to attract less attention and may remain unsolved longer, making them better suited for held-out evaluation of end-to-end open problem resolution in Lean 4 formal mathematics.
- The evaluation protocol adopts a standard coding-agent setting by placing each problem and its logical negation into a Lean project within a Docker container, and introduces Leanimum-agent built on mini-SWE-agent as a unified harness to enable fair comparisons across different models, aligning evaluation with how modern coding agents actually operate.
- Even the best-performing model achieves only roughly 40% resolution rate on these formalized open research problems, demonstrating that current AI systems remain far from reliably solving open mathematical research problems, and that formal verification frameworks like Lean 4 present significant challenges for coding agents.

## Context
As AI systems increasingly attempt to resolve open research problems, the field faces a critical verification gap: existing formal mathematics benchmarks often target known results or a small set of prominent open problems, which become unreliable evaluation targets once solutions are discovered and widely disseminated. ReuF2F addresses this by leveraging undergraduate research programs as a source of genuinely open, less-scrutinized problems, creating a more durable evaluation resource. This work sits at the intersection of formal verification, automated theorem proving, and coding-agent evaluation, reflecting the growing importance of machine-checkable proofs as a foundation for trustworthy AI-assisted mathematical reasoning.

## Implications
For the AI research community, ReuF2F provides a more robust and sustainable benchmark for measuring genuine progress in automated mathematical reasoning, reducing the risk of benchmark contamination and enabling fairer model comparisons through its standardized Docker-based evaluation harness. For practitioners building coding agents, the finding that top models solve only about 40% of entry-level open problems signals that current architectures and training approaches are insufficient for reliable open-ended mathematical exploration, motivating further research into agent scaffolding, formal proof search strategies, and domain-specific training. For the broader mathematics community, the benchmark's grounding in REU programs offers a pathway for AI tools to contribute meaningfully to early-stage research while maintaining rigorous formal verification standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27046v1)
