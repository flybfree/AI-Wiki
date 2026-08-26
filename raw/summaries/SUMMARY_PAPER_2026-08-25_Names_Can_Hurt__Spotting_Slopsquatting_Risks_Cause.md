---
title: Names Can Hurt: Spotting Slopsquatting Risks Caused by Package Name Hallucinations in Local Coding LLMs
url: http://arxiv.org/abs/2608.23897v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_23-10-49Z_NamesCanHurt_SpottingSlopsquattingRisksCausedbyPac.md
generated_at: 2026-08-25 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a two‑layer detector to prevent “slopsquatting,” where an LLM fabricates a package name that an adversary can exploit via PyPI registration. Across 300 prompts the pipeline achieved 76 % hallucination‑free code, with primary refusals on 28.7 % of attempts and fallback recovery adding further gains.

## Key Takeaways
- Half of flagged hallucinations are legitimate packages already on PyPI, such as pil or faiss, caught by the classifier rather than the deterministic check.
- Hallucination rates rise sharply with prompt adversariality, from 0 % to 40‑73 % for routine coding versus slopsquat baits.
- The weaker primary model refuses six of ten direct baits unaided, indicating recent instruction tuning provides a baseline defense.

## Context
This work addresses a growing concern in AI‑generated code: the risk that language models produce package names that can be weaponized to compromise software supply chains. As LLMs become more integrated into development workflows, detecting and mitigating such hallucinations is essential for maintaining trustworthy tooling.

## Implications
For practitioners, the findings highlight the need for layered defenses—deterministic checks plus adaptive classifiers—and cross‑family model pairing to reduce recurrence of failures. The study also suggests that continued instruction tuning can provide a modest baseline protection against adversarial prompts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23897v1)
