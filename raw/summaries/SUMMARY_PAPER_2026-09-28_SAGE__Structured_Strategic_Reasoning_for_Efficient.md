---
title: SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing
url: http://arxiv.org/abs/2609.34342v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_05-20-04Z_SAGE_StructuredStrategicReasoningforEfficientLLMGa.md
generated_at: 2026-09-28 23:03
model: qwen3.6-35b-a3b
---

## Summary
SAGE is a training-free inference-time framework designed to enhance Large Language Model performance in strategic games by structuring reasoning into three coordinated operations: anchoring, adapting, and recalibrating. The method addresses limitations of free-form reasoning, such as unsupported assumptions and inconsistent opponent modeling, by leveraging equilibrium policies, soft beliefs about opponents, and distilled counterfactual hypotheses from past interactions. Evaluations across Leduc Hold'em, Liar's Dice, and Goofspiel demonstrate that SAGE significantly outperforms existing reasoning-intensive agents while drastically reducing token consumption.

## Key Takeaways
- SAGE implements a training-free inference-time framework that structures LLM reasoning through three distinct operations: anchoring to an equilibrium policy for strategic validity, adapting deviations based on soft beliefs about opponent tendencies for exploitation, and recalibrating via counter

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34342v1)
