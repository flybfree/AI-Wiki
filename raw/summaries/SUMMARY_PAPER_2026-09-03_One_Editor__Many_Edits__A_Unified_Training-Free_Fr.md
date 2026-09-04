---
title: One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Editing
url: http://arxiv.org/abs/2609.04190v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-59-01Z_OneEditor_ManyEdits_AUnifiedTraining_FreeFramework.md
generated_at: 2026-09-03 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
EditVid is a training-free framework that unifies instruction-guided and subject-guided video editing by integrating sparse causal memory, correspondence-based token injection, and soft latent blending. On the FiVE benchmark it achieves 78.16 FiVE-Acc, surpassing prior baselines, while also receiving strong user preference.

## Key Takeaways
- The framework uses a sparse causal memory to maintain local coherence across edits without requiring pre‑training data.
- Correspondence‑based post‑attention token injection preserves long‑range identity between subjects and edited regions.
- Soft latent blending ensures edit operations are localized, reducing unintended artifacts in the output.

## Context
Video editing remains a challenging task for AI because it requires both precise instruction following and faithful subject tracking across frames. Existing methods often rely on extensive training data or separate pipelines, limiting flexibility and real‑world applicability.

## Implications
This unified approach enables developers to deploy high‑quality edits with minimal customization, accelerating product integration in entertainment and content creation industries. Practitioners can leverage the framework for diverse editing tasks without building separate models for each paradigm.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04190v1)
