---
title: Is this Citation on Point?
url: http://arxiv.org/abs/2608.12571v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_20-28-55Z_IsthisCitationonPoint.md
generated_at: 2026-08-13 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates verification of citation support in legal arguments by perturbing real citations and testing fourteen model configurations. It finds models correctly detect wrong-case corruptions but miss many pinpoint mismatches, especially on court opinions where they rely on topical overlap rather than page-level evidence. Even advanced models like GPT-5.4 still miss a significant portion of these errors.

## Key Takeaways
- Models catch 93‑100% of wrong-case corruptions but only 37‑61% of wrong-pinpoint corruptions on court opinions and 52‑83% on legal briefs, indicating they often rely on topic similarity instead of precise page support. - The failure mode is that citations may point to real cases but do not substantiate the proposition they are cited for, a problem existing evaluations overlook. - Prompting models to verify citation at the cited page improves recall but also raises false positives, showing a trade‑off between sensitivity and specificity.

## Context
This research addresses a gap in AI safety for legal LLMs where citation verification is crucial yet rarely evaluated beyond basic lookup. Existing tools focus on detecting fabricated citations rather than assessing whether a citation logically supports its proposition, which is essential for trustworthy legal reasoning.

## Implications
For legal practitioners, this work highlights the need for systems that can verify both topical relevance and page‑level support to avoid misinformation in briefs. For AI developers, it underscores that improving citation verification requires disentangling topic recognition from evidence grounding, a challenge that current models still struggle with.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12571v1)
