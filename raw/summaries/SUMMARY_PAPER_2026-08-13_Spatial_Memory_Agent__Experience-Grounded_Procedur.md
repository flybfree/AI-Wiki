---
title: Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence
url: http://arxiv.org/abs/2608.12743v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_02-42-35Z_SpatialMemoryAgent_Experience_GroundedProcedureMem.md
generated_at: 2026-08-13 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Spatial Memory Agent (SMA), a framework that enables frozen vision‑language models to improve spatial reasoning through parameter‑update‑free self‑evolution. By converting verified spatial experiences into reusable lessons and assigning them Transfer Reliability Scores, SMA allows read‑only deployment where the model retrieves relevant memories at inference time, achieving state‑of‑the‑art results across multiple benchmarks.

## Key Takeaways
- SMA creates a runtime system that extracts compact transferable lessons from spatial tasks using verifier‑guided reflection without modifying the frozen VLM.  
- Each lesson is scored with a Transfer Reliability Score that is calibrated from later retrieval outcomes, ensuring higher reliability during inference.  
- The method achieves the highest macro average across all base VLMs and outperforms other approaches in most evaluations.

## Context
Current spatial intelligence research focuses on either fine‑tuning models or integrating external tools at runtime, both of which require parameter updates or additional hardware. SMA offers an alternative that leverages only existing model weights and stored experiences, aligning with the trend toward lightweight, inference‑only solutions for embodied agents.

## Implications
For industry practitioners, SMA reduces deployment complexity by eliminating fine‑tuning pipelines while boosting spatial performance, making it suitable for edge devices where computational resources are limited. Practitioners can adopt this self‑evolving paradigm to create more adaptable multimodal assistants without sacrificing model stability or requiring costly retraining cycles.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12743v1)
