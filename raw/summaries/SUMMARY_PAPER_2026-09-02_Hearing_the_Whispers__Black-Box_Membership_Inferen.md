---
title: Hearing the Whispers: Black-Box Membership Inference Attacks on Finetuned TTS Models
url: http://arxiv.org/abs/2609.01723v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_18-00-45Z_HearingtheWhispers_Black_BoxMembershipInferenceAtt.md
generated_at: 2026-09-02 20:53
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a black‑box membership inference framework for fine‑tuned text‑to‑speech (TTS) models, showing that these systems leak speaker and record identities with high accuracy. Experiments on three state‑of‑the‑art TTS models reveal member AUCs above 0.80 and record AUCs from 0.80 to 0.90, indicating severe privacy risks.

## Key Takeaways
- The query generation space for TTS is large and underexplored, yet recitation queries emerge as the most effective for eliciting membership signals.  
- Multi‑level speech representations and temporal alignment are required because low‑level audio comparisons fail to capture membership information in TTS outputs.  
- Even when both members and non‑members belong to the same speaker group, record‑level inference remains robust with AUCs near 0.90.

## Context
TTS foundation models increasingly personalize voices using private datasets, raising concerns about biometric exposure. Black‑box attacks that infer membership from model outputs are a growing threat in AI systems handling sensitive data. This work bridges the gap between TTS privacy and existing black‑box inference research.

## Implications
For practitioners developing personalized voice assistants or synthetic speech services, these findings warn of hidden privacy breaches that could be exploited by attackers. The results push the community to adopt robust query design and representation engineering techniques to protect sensitive user data in AI models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01723v1)
