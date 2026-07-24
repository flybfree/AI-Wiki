---
title: Taming the Security-Energy Paradox: A Green AI Approach to Optimized Android Malware Detection
url: http://arxiv.org/abs/2607.20003v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_10-39-42Z_TamingtheSecurity_EnergyParadox_AGreenAIApproachto.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how to balance malware detection performance with energy consumption in Android devices by testing Multi-Layer Perceptron configurations using INT8 quantization. The study shows that quantized models achieve a three‑fold reduction in size and lower inference energy while preserving over 99 % accuracy, highlighting the viability of Green AI techniques for mobile security.

## Key Takeaways
- INT8 quantization reduces model size by about 3.5 times and lowers energy consumption to 0.0189 mJ per inference without sacrificing detection accuracy above 99.2 %.  
- Shallow quantized architectures with three or four layers improve throughput, shortening CPU time in high‑power states and further cutting energy costs.  
- The approach demonstrates that effective malware protection can be delivered on resource‑constrained smartphones through Green AI methods.

## Context
Mobile security increasingly relies on deep learning models that must operate offline to protect user privacy. However, these models often consume significant battery power, creating a conflict between detection efficacy and device endurance. This work addresses the emerging challenge of deploying secure AI on low‑power platforms without compromising performance.

## Implications
The findings provide a practical blueprint for developers seeking to integrate energy‑efficient deep learning into Android security solutions. By enabling high‑accuracy malware detection with minimal power draw, Green AI can support widespread adoption of intelligent security features while preserving battery life and user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20003v1)
