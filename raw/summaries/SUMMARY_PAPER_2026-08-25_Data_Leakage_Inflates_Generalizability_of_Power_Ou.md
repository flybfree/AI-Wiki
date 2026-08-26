---
title: Data Leakage Inflates Generalizability of Power Outage Prediction Models
url: http://arxiv.org/abs/2608.24665v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_15-05-55Z_DataLeakageInflatesGeneralizabilityofPowerOutagePr.md
generated_at: 2026-08-25 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how methodological choices inflate the apparent generalizability of power outage prediction models. Using U.S. East Coast data from 2018 to 2023, it compares performance across random splits, leave‑one‑state‑out, and leave‑one‑event‑out designs, finding that spatial and temporal autocorrelation inflates scores while GeoAI embeddings offer only limited benefit.

## Key Takeaways
- Random train‑test splits produce strong metrics but are misleading because they ignore the natural dependencies in space and time.  
- When models are evaluated with realistic holdouts, accuracy drops sharply, often falling below a simple null baseline.  
- GeoAI foundation model embeddings improve spatial generalization modestly but do not fix poor event‑level transferability.

## Context
Power outage prediction is critical for climate‑risk assessments and infrastructure planning. Current evaluation practices treat data as independent samples, which masks the true limits of models in deployment settings. This study highlights a gap between laboratory performance and real‑world utility.

## Implications
Practitioners must adopt more realistic evaluation protocols that respect spatial and temporal autocorrelation to avoid overestimating model value. The field should prioritize improving data coverage and addressing structural constraints rather than chasing marginal algorithmic gains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24665v1)
