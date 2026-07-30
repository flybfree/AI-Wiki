---
title: Misalignment Has a Personality: A Big Five Account of Emergent Misalignment
published: 2026-07-29T01:48:03Z
authors: Hasibur Rahman, Smit Desai
url: http://arxiv.org/abs/2607.26389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Misalignment Has a Personality: A Big Five Account of Emergent Misalignment

## Abstract
Fine-tuning a language model on data containing a narrow flaw, such as insecure code or incorrect mathematical answers, can cause broad misalignment through a mechanism that remains debated. We provide an interpretable account: in the models and corpora we study, misalignment behaves like a shift in personality. Prior work extracts activation directions for character traits from a single binary contrast, which can separate or steer behavior without establishing a calibrated scale. We instead extract personality vectors for the Big Five using a graded, three-level intervention and validate them on two open-weight models. The three levels are linearly ordered, with Cohen's d values of up to 6.2; the vectors transfer zero-shot and trait-specifically to an independent corpus; and their effects are strongest within a middle-layer band. Applied to training data, the vectors reveal that misaligned corpora across eight domains share a common Big Five signature: lower agreeableness and conscientiousness, together with higher extraversion and neuroticism. This signature is recovered by both models with a correlation of r = 0.94. Fine-tuning imprints the same profile, shifting the model's generations along the corresponding signature, with r = 0.83 using activation-based measurements and r = 0.90 using a text-based judge, while also shifting internal activations with r = 0.69. The same vectors characterize sycophancy as high extraversion and low conscientiousness rather than excess agreeableness, a distinction that a single direction cannot capture. Calibrated personality vectors transform an opaque safety phenomenon into a human-legible diagnostic profile.

## Metadata
- **Published**: 2026-07-29T01:48:03Z
- **Authors**: Hasibur Rahman, Smit Desai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26389v1)