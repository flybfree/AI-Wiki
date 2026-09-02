---
title: REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs
url: http://arxiv.org/abs/2609.01215v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_13-19-05Z_REFACTOR_VLA_UnsupervisedLibraryLearningofTypedMot.md
generated_at: 2026-09-01 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces REFACTOR-VLA, a wake/sleep system that learns reusable motor‑program abstractions for vision‑language‑action tasks. The authors demonstrate that the sleep phase’s clustering of motion fragments using a Behavioral‑Equivalence Kernel improves performance on LIBERO suites compared with prior monolithic models.

## Key Takeaways
- Enlarging the learned latent world model from 188 M to 430 M parameters only worsened results, indicating that capacity alone is insufficient for effective skill discovery.  
- Adding an auxiliary supervised contrastive (InfoNCE) loss during world‑model warmup markedly improves clustering, raising normalized mutual information to values such as 0.867 on spatial tasks and 0.915 on goal tasks, which beats the strongest published baseline by a mean Δ of +0.184 across four suites.  
- The sleep phase produces the first real‑world LIBERO task‑language library, where the decoder adopts two admitted abstractions to rewrite all 256 sampled demonstrations.

## Context
Current VLA systems lack modular skill representation, limiting long‑horizon performance and interpretability. Existing clustering approaches either ignore behavioral equivalence or rely on uncalibrated language models, hindering scalable learning. REFACTOR-VLA addresses these gaps by integrating a principled abstraction framework with a typed lambda vocabulary.

## Implications
The work suggests that structured skill libraries can boost real robot autonomy without sacrificing safety. Practitioners may adopt the wake/sleep paradigm to create interpretable pipelines for complex tasks, while researchers gain a benchmark for evaluating unsupervised clustering in embodied AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01215v1)
