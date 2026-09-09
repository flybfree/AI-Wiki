---
title: Style Over Substance: Content-Invariant Wrappers Flip LLM Safety-Judge Verdicts
url: http://arxiv.org/abs/2609.08236v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_04-27-22Z_StyleOverSubstance_Content_InvariantWrappersFlipLL.md
generated_at: 2026-09-08 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether LLM safety judges evaluate only the textual content of a response or also its style, using content‑invariant wrappers that alter tone without changing the reply’s bytes. Experiments on 600+ jailbreak benchmarks show that many judges flip verdicts when wrapped with harmless‑looking but stylistically dangerous strings, indicating bias toward appearance over substance.

## Key Takeaways
- A token‑refusal wrapper flips 19.9% of GPT‑4o‑mini’s correct “unsafe” judgments while moving Claude only 0.4%, showing judges can be fooled by style alone.
- Llama Guard 4 is deterministically gamed: an educational framing flips 12.3% of its harmful verdicts to safe, revealing deterministic vulnerabilities.
- Human validation confirms 90% of flips are judge errors (kappa 0.95‑1.0), and the underlying model ranking is already unstable due to sampling noise.

## Context
LLM safety evaluation relies heavily on automated judges that score responses based on textual patterns; however, these systems often conflate style with risk, creating blind spots exploitable by attackers. The findings highlight a gap between theoretical defenses and real‑world robustness.

## Implications
For practitioners, the paper urges moving beyond content‑only checks to assess judge reliability and prompting design. It also suggests that deploying multiple judges or using deterministic wrappers can mitigate exploitation risks in safety leaderboards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08236v1)
