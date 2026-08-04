---
title: Mind the Gap: Zero-Query Jailbreaks via Filter-Generator Discrepancy in Text-to-Image Systems
published: 2026-08-02T03:53:30Z
authors: Wanguang Li, Zhaoxin Wang, Handing Wang
url: http://arxiv.org/abs/2608.00973v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mind the Gap: Zero-Query Jailbreaks via Filter-Generator Discrepancy in Text-to-Image Systems

## Abstract
Text-to-image (T2I) systems typically have prompt-level safety filters before the generator to block unsafe requests, yet such systems remain vulnerable to malicious jailbreak prompts. Transfer-based attacks construct adversarial prompts offline without querying the target, but they tend to overfit to a single surrogate. Moreover, they explore a large search space in which semantic or perceptual similarity alone cannot guarantee both filter evasion and preservation of the unsafe generation intent, wasting effort on low-potential candidates. We observe that the filter and the generator process the same prompt under different objectives and representations, and term this gap the Filter-Generator Discrepancy (FGD), which allows a perturbation to reduce a prompt's perceived risk to the filter while preserving the visual concept needed by the generator. Building on FGD, we propose a zero-query jailbreak framework that screens perturbations into a high-potential candidate set via observable discrepancy rules at the tokenization and semantic stages, and then performs a surrogate-ensemble evolutionary search that requires no access to the target. Experiments on six black-box pipelines and a commercial online service show that our method consistently outperforms representative baselines, raising the average attack success rate to 29.2\% (MHSC) and 33.3\% (Q16) across the six pipelines and improving over the strongest baseline by about 8 and 12 percentage points, respectively.

## Metadata
- **Published**: 2026-08-02T03:53:30Z
- **Authors**: Wanguang Li, Zhaoxin Wang, Handing Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00973v1)