---
title: Agent Safety Should Be a Runtime Contract
url: http://arxiv.org/abs/2608.11274v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-11_08-01-05Z_AgentSafetyShouldBeaRuntimeContract.md
generated_at: 2026-08-12 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper argues that AI safety for autonomous agents must be treated as a runtime contract rather than a training-time property. It proposes two complementary faces — preventive measures and evidential verification — grounded in empirical audits of recent incidents and safety literature, suggesting the trajectory‑with‑checkable‑evidence is the proper unit of safety.

## Key Takeaways
- Agent safety should be enforced at runtime through sandboxes, permission gates, output filters, and trajectory monitors rather than only during training.  
- The evidential face requires verifiable proof such as test runs, log captures, file diffs, or citation grounding before task submission is allowed.  
- Empirical evidence shows a strong imbalance between safety publications in 2023‑2025 and actual deployment incidents, highlighting the need for runtime contracts.

## Context
Current AI safety research focuses on training-time methods like RLHF and DPO, which cannot guarantee safe behavior when agents act autonomously. The paper situates agentic AI within existing security and scientific practices that rely on runtime contracts to prevent harm and ensure reproducibility.

## Implications
For practitioners, this framework offers a practical roadmap for building trustworthy autonomous systems by integrating preventive safeguards with provable evidence. Industry adoption could reduce liability risks and improve public confidence in AI agents handling sensitive tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11274v1)
