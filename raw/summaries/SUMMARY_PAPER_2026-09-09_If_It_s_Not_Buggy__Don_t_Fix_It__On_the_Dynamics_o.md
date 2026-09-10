---
title: If It's Not Buggy, Don't Fix It: On the Dynamics of Iterative Bug-fixing with LLMs
url: http://arxiv.org/abs/2609.10123v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_13-00-47Z_IfIt_sNotBuggy_Don_tFixIt_OntheDynamicsofIterative.md
generated_at: 2026-09-09 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models behave when used repeatedly to fix code, even when the code is already correct. It finds that LLMs often claim to detect bugs in entirely bug‑free programs and that repairs of real bugs are less effective than damage caused by false fixes. The study also shows a recurring cycle where edits are added and removed indefinitely.

## Key Takeaways
- LLMs claim to detect bugs in entirely bug‑free programs, indicating a high false positive rate.
- Repairs applied to correct code cause more problems than they solve, reducing overall correctness.
- Iterative use can create a pseudo‑bug‑fixing loop where the same changes are repeatedly added and removed.

## Context
Automated program repair is a growing area where LLMs replace human reviewers. Understanding how these models misbehave under repeated iterations is crucial for reliable deployment in software engineering pipelines.

## Implications
If LLMs continue to generate harmful edits, autonomous bug‑fixing systems may degrade code quality over time. Practitioners must set clear stopping criteria and monitor false positive interventions to prevent long‑term damage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.10123v1)
