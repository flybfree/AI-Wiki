---
title: Jailbreaks for Black-Box Uncertainty Quantification in Large Reasoning Models
url: http://arxiv.org/abs/2609.35350v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_15-02-03Z_JailbreaksforBlack_BoxUncertaintyQuantificationinL.md
generated_at: 2026-09-29 01:59
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the challenge of uncertainty quantification (UQ) in Large Reasoning Models (LRMs) where internal logits are inaccessible, a common constraint in production black-box settings. The authors demonstrate that current black-box UQ methods fail to improve upon simple repeated sampling due to alignment-induced overconfidence suppressing output variability. To overcome this, they introduce J4U, a technique leveraging prompt-level relaxation operators inspired by jailbreak mechanisms, which theoretically and empirically improves model calibration and significantly outperforms existing baselines across multiple datasets and models.

## Key Takeaways
- Existing black-box UQ approaches, including paraphrase-based self-consistency and confidence verbalization, provide negligible gains over

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35350v1)
