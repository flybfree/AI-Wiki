---
title: REPLICANT: Learning Policies for Evading and Hardening Malware Detectors
url: http://arxiv.org/abs/2608.28499v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_16-29-17Z_REPLICANT_LearningPoliciesforEvadingandHardeningMa.md
generated_at: 2026-08-30 23:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Replicant, a deep reinforcement learning framework that teaches malware evasion under a label‑only black‑box threat model. Across seven Android detectors and three feature spaces, Replicant achieves a mean attack success rate of 78.8%, outperforming state‑of‑the‑art methods by 20.9%–39.2%. It also improves detector robustness when used for adversarial training.

## Key Takeaways
- Replicant learns a reusable policy that modifies malware samples and decides when to query the target, transferring across detectors and feature spaces.  
- The framework reaches a mean attack success rate of 78.8%, which is significantly higher than current state‑of‑the‑art approaches (20.9%–39.2% relative improvement).  
- When incorporated into adversarial training, Replicant yields detectors that are more generalizable and robust.

## Context
Malware detection relies on machine learning models that can be gamed by sophisticated attackers who exploit access to privileged information such as feature representations or confidence scores. Current research often assumes idealized attacker capabilities, limiting the relevance of findings to real‑world scenarios. This work bridges that gap by modeling realistic adversarial behavior without privileged data.

## Implications
The results suggest that training detectors with evasion feedback can lead to stronger defenses and more reliable models. Practitioners should consider integrating reinforcement‑learning based adversarial training into their security pipelines to enhance both detection accuracy and robustness against evolving threats.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28499v1)
