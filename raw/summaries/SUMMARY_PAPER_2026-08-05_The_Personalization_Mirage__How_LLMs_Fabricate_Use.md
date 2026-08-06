---
title: The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads
url: http://arxiv.org/abs/2608.04570v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_08-00-54Z_ThePersonalizationMirage_HowLLMsFabricateUserProfi.md
generated_at: 2026-08-05 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates over-inference in personalized large language models that fabricate user attributes beyond evidence. It demonstrates that all evaluated models generate false claims at rates ranging from 35% to 49%, and that self-reported confidence is negatively correlated with actual accuracy. The findings reveal a self-monitoring inversion where models that claim low fabrication produce the most over-inference.

## Key Takeaways
- Every model in the evaluation fabricates user attributes on average 35–49% of its claims, indicating pervasive over‑inference across diverse personalization tasks.
- Self‑assessed over‑inference scores are negatively correlated with judge‑measured rates (rho = -0.60), showing that models’ own confidence signals mislead users and researchers.
- Over‑inference persists even after self‑auditing, with AUROC values only modestly above chance, suggesting limited reliability in internal model monitoring.

## Context
Personalized LLMs aim to adapt responses to individual user histories, but the paper shows these systems often create inaccurate user profiles. The study’s methodology—MirageBench—provides a systematic benchmark that exposes hidden biases and fabrication risks across model families.

## Implications
For practitioners, relying on self‑reported confidence is unsafe; external verification remains essential for trustworthy personalization. Industry adoption must incorporate rigorous validation to prevent deceptive user experiences and regulatory scrutiny over fabricated data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04570v1)
