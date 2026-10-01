---
title: MASCRDM: Multi-Agent System for Compliance Risk Detection and Mitigation in Training Process of Large Language Models
url: http://arxiv.org/abs/2609.39107v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_06-47-05Z_MASCRDM_Multi_AgentSystemforComplianceRiskDetectio.md
generated_at: 2026-09-30 20:43
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces MASCRDM, a multi-agent system designed to enhance the compliance of Large Language Models during their training process by addressing the limitations of static input-output filtering methods. The authors propose a dynamic approach that integrates AI legal rules and expert-guided LLMs to monitor key architectural nodes in real-time, providing continuous risk alerts and mitigation suggestions throughout training. Experimental results on discrimination and bias benchmarks demonstrate that MASCRDM significantly improves model compliance without compromising semantic performance, offering a systematic solution for intrinsic safety alignment.

## Key Takeaways
- Current compliance efforts rely heavily on static detection and filtering of inputs and outputs, which results in localized optimizations and lacks the flexibility to address risks dynamically during model development; MASCRDM overcomes this by embedding multiple agents directly into the training workflow to enable real-time risk detection and mitigation across the entire process.
- The system constructs a robust compliance framework based on existing AI laws and a specialized LLM instructed by legal experts, utilizing a compliance knowledge graph to deconstruct the model architecture and identify critical nodes where interventions are most needed, thereby ensuring that risk alerts and developer suggestions are grounded in authoritative regulatory standards.
- Evaluations on discrimination and bias benchmarks confirm that MASCRDM

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39107v1)
