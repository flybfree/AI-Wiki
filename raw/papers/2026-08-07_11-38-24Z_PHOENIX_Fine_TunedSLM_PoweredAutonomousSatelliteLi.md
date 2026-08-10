---
title: PHOENIX: Fine-Tuned SLM-Powered Autonomous Satellite Lifetime Extension via Predictive Self-Healing and Multi-Agent AI Recovery
published: 2026-08-07T11:38:24Z
authors: Sumaiya Islam, Harsha Kumara Moraliyage
url: http://arxiv.org/abs/2608.07126v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PHOENIX: Fine-Tuned SLM-Powered Autonomous Satellite Lifetime Extension via Predictive Self-Healing and Multi-Agent AI Recovery

## Abstract
Most CubeSats, small and low-cost satellites roughly the size of a shoebox, do not survive as long as they were designed to: a study of 178 missions found that only 48-65% remain operational after two years, against a designed lifetime of 2-5 years. The deeper issue is that a CubeSat in low Earth orbit (LEO) is physically unreachable from the ground for roughly 85 minutes out of every 96-minute orbit, so faults that start during that window go unnoticed until the next contact pass, by which point recovery may no longer be possible. We propose PHOENIX (Predictive Health On-orbit Edge Neural Intelligence eXtension) to give the satellite its own fault reasoning capability. A fine-tuned Small Language Model (SLM) compact enough to run on embedded hardware is deployed onboard the CubeSat, running on the flight-proven Aethero NxN-ECM computer, monitoring all sensor readings continuously, and resolving recurring faults using a memory system that stores past repairs so the same inference does not need to run twice. Once per orbit it sends a short structured health report to the ground instead of a raw data dump; six specialized AI agents on the ground read that report and generate validated satellite commands within the 5-10 minute contact window. A generative diffusion model (DDPM) creates synthetic training data because real fault examples make up only 0.57-1.80% of the dataset. We report preliminary results on the ESA Anomaly Detection Benchmark (14 years, 76 channels, 118 labeled faults).

## Metadata
- **Published**: 2026-08-07T11:38:24Z
- **Authors**: Sumaiya Islam, Harsha Kumara Moraliyage
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07126v1)