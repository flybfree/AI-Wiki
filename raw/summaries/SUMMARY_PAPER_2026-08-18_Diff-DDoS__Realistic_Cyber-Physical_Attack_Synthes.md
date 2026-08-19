---
title: Diff-DDoS: Realistic Cyber-Physical Attack Synthesis and Robust Detection for 5G-Enabled CPS Using Tabular Diffusion Models
url: http://arxiv.org/abs/2608.17796v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_13-56-47Z_Diff_DDoS_RealisticCyber_PhysicalAttackSynthesisan.md
generated_at: 2026-08-18 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Diff‑DDoS, a three‑phase framework that trains realistic cyber‑physical attacks using tabular diffusion models and then evaluates them against CNN detectors on 5G call detail record data. The authors demonstrate that adversarial diffusion training restores detection performance to near‑baseline levels while highlighting the limitations of conventional synthetic attack generators.

## Key Takeaways
- Detectors trained on handcrafted attacks with fixed scaling multipliers suffer catastrophic F1‑score drops ranging from 47 % to 100 % when faced with realistic, distribution‑preserving samples.  
- The TabDDPM model generates authentic attack patterns that expose detector vulnerabilities, and adversarial diffusion training (ADT) mitigates these weaknesses by iteratively generating hard yet realistic samples until convergence.  
- On the Milano CDR dataset, ResNet50 with ADT achieves F1‑scores of 79.62 % for silent‑call attacks, 100 % for Internet‑signaling attacks, and 92.79 % for blended scenarios, outperforming CTGAN and matching the best gradient‑based adversarial baseline.

## Context
Deep learning detectors for 5G cyber‑physical systems rely heavily on labeled data that is often scarce or synthetic, leading to models that fail against adaptive threats. This work bridges that gap by using tabular diffusion models to synthesize attacks that preserve real distribution, enabling more honest stress tests of detection pipelines.

## Implications
For industry practitioners, Diff‑DDoS provides a practical method to harden intrusion detectors without needing extensive labeled datasets. The approach can be adopted to continuously evaluate and improve 5G security systems against evolving adversarial tactics in resource‑constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17796v1)
