---
title: The Role of Disfluencies in Speech Translation
url: http://arxiv.org/abs/2608.02138v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_12-26-39Z_TheRoleofDisfluenciesinSpeechTranslation.md
generated_at: 2026-08-03 23:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how speech translation systems handle disfluencies such as false starts and self‑repairs, which are currently removed during training. The authors introduce Uh-Mazing, a benchmark of human‑translated Switchboard recordings annotated for disfluency, and demonstrate that preserving these cues improves translation quality. Their results show that models lose more accuracy when they omit disfluencies than when they mistranslate them.

## Key Takeaways
- False starts and self‑repairs are the primary sources of translation loss across languages and architectures, indicating that their removal hurts performance more than the loss from filled pauses or discourse markers.  
- Models trained on cleaned data tend to delete disfluencies entirely rather than produce inaccurate translations, revealing a systematic bias in current training pipelines.  
- Inference‑time decoding strategies can recover lost disfluency without requiring model retraining, offering an efficient mitigation technique.

## Context
Speech translation remains a challenging task because natural speech contains irregularities that do not map cleanly to text. Existing models rely on cleaned transcripts, which may discard valuable linguistic cues. This work highlights the need for datasets and methods that respect the full richness of spoken language in multilingual contexts.

## Implications
For practitioners, integrating disfluency preservation can lead to more natural and accurate translations without costly retraining cycles. The Uh-Mazing benchmark provides a reusable resource for evaluating and improving speech translation systems across multiple languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02138v1)
