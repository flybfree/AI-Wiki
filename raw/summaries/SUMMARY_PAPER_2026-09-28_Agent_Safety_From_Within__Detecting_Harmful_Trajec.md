---
title: Agent Safety From Within: Detecting Harmful Trajectories from LLM Internal States
url: http://arxiv.org/abs/2609.33039v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_00-09-10Z_AgentSafetyFromWithin_DetectingHarmfulTrajectories.md
generated_at: 2026-09-28 22:03
model: qwen3.6-35b-a3b
---

## Summary
The paper addresses the limitations of existing guard models in detecting agentic risks by analyzing internal representations of open-source safety models regarding harmful content and unsafe tool use. It introduces TACIT, a parameter-efficient readout mechanism that decodes trajectory safety directly from frozen backbone states without generating tokens, achieving superior performance and efficiency compared to traditional guard models and full fine-tuning approaches.

## Key Takeaways
- Representational analysis reveals that harmful content and unsafe tool use are linearly readable as nearly orthogonal directions within guard model internals, yet standard guard models fail to distinguish actions based on tool schemas, indicating a gap between internal representation and predictive capability.
- TACIT leverages these insights by training a linear probe on frozen backbone states to detect trajectory-level safety across six benchmarks, significantly outperforming the strongest open guard models in mean macro-F1 scores while maintaining robust generalization on held-out data.
- The proposed readout mechanism is highly efficient, requiring approximately one millionth of the parameters and one-sixth of the training time of full fine-tuning methods, while also offering the lowest latency among evaluated guards and enhancing safety even when applied atop already fine-tuned models.

## Context
As LLM agents gain autonomy through tool use and complex action sequences, the potential for catastrophic harm increases, necessitating safety mechanisms tailored to agentic behaviors rather than static content moderation. Current guard models are ill-equipped to evaluate consistency between actions and interactions or detect schema-level risks, highlighting a critical need for novel detection strategies that operate at the trajectory level within the model's internal state space.

## Implications
Practitioners can deploy TACIT as a lightweight, low-lat

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33039v1)
