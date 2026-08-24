---
title: Why2Speak: Faithful Reasoning for Abstaining Action Policies
url: http://arxiv.org/abs/2608.20670v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_02-00-21Z_Why2Speak_FaithfulReasoningforAbstainingActionPoli.md
generated_at: 2026-08-23 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how exposing reasoning to auditors affects the fairness of agentic systems that must decide between speaking and staying silent. Experiments with Qwen3-8B show a trade‑off: detailed explanations reduce decision quality, while simple policies retain performance but offer no audit trail.

## Key Takeaways
- The strongest direct policy yields higher output quality but provides no reasoning to inspect, highlighting the capability‑auditability gap.
- Reasoning policies generate traces at the expense of lower recall for true intervention opportunities, indicating a performance cost for transparency.
- Group relative objectives fail to provide learning signals when rollouts select the same action, causing reinforcement learning to miss improvement opportunities.

## Context
Agentic systems increasingly rely on opaque decision mechanisms that can impact user outcomes. The need for explainable behavior is critical in high‑stakes applications such as medical advice or autonomous negotiation. This work contributes a systematic view of how reasoning interventions alter policy dynamics within conversational agents.

## Implications
Practitioners must balance model performance with the requirement for inspectable reasoning, recognizing that transparency can degrade utility. The findings guide design choices where auditors may need to accept lower accuracy in exchange for explainability or explore alternative evaluation metrics less sensitive to class imbalance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20670v1)
