---
title: H$^2$SD: Hybrid Hindsight Self-Distillation
published: 2026-07-21T10:47:27Z
authors: Qiye Cai, Yichuan Ma, Linyang Li, Peiji Li, Yongkang Chen, Qipeng Guo, Yicheng Zou, Xiaocheng Feng, Bing Qin
url: http://arxiv.org/abs/2607.18955v2
type: paper-summary
tags: [paper-summary, arxiv]
---

# H$^2$SD: Hybrid Hindsight Self-Distillation

## Abstract
Reinforcement learning with verifiable rewards (RLVR) provides reliable outcome supervision for language model reasoning, but a scalar trajectory reward offers limited token-level guidance. Existing self-distillation methods add a privileged teacher but typically assign it a fixed role: direct distribution matching may destabilize successful behavior, while magnitude-only modulation offers little corrective guidance after failure. We observe that successful and failed trajectories require different forms of hindsight supervision. A successful response already contains a valid student-generated reasoning path and can therefore serve as privileged context rather than being replaced by an external rationale. A failed response, however, requires corrective reference information. We introduce Hybrid Hindsight Self-Distillation ($\mathrm{H}^{2}\mathrm{SD}$), which jointly adapts teacher context and update strategy to trajectory correctness. For successful trajectories, we construct the teacher context from the verified response and a rephrasing instruction, and use the teacher only to re-evaluate the original response tokens. This emphasizes essential deductions over redundant content and refines magnitude-based credit assignment without changing the reward direction. For failed trajectories, a verifier-confirmed reference hint provides corrective guidance through reverse-KL distillation. Controlled ablations show that the gains depend on outcome-conditioned routing and the rephrasing instruction. Experiments on challenging reasoning benchmarks show that H$^2$SD achieves the strongest overall performance among representative RLVR and self-distillation baselines, with stable optimization and a favorable accuracy-efficiency trade-off.

## Metadata
- **Published**: 2026-07-21T10:47:27Z
- **Authors**: Qiye Cai, Yichuan Ma, Linyang Li, Peiji Li, Yongkang Chen, Qipeng Guo, Yicheng Zou, Xiaocheng Feng, Bing Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18955v2)