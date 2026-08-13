---
title: Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction
published: 2026-08-12T08:14:45Z
authors: Pan Wang, Yihao Hu, Hang Wang, Zirui Lv, Xin Zhang, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong
url: http://arxiv.org/abs/2608.11772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction

## Abstract
Self-correction is particularly useful when a failure constrains the next repair. Coding agents benefit from this property because compilers, tests, and execution traces turn many failures into typed recovery signals, but broad language-agent tasks often expose only a coarse task failure. This creates a tension for generic recovery playbooks: they broaden the agent's context precisely when the system needs a narrower repair interface, mixing incompatible signals for invalid actions, missing procedures, and strict-format errors. Our insight is that development-set failures can recover part of the missing diagnostic substrate by deciding which recovery interventions are admissible before test-time correction. We propose DARC, a diagnosis-guided recovery harness that profiles task-family failure modes, prunes mismatched interventions from a shared recovery library, and freezes a verifier-selected success-cost policy for deployment. This causal order makes correction selective: the harness first determines what kind of failure can be repaired, then decides how much recovery evidence to spend. In ALFWorld, AppWorld, and XBRL Finance, the same protocol yields an action-validity harness, a procedural-recovery fallback, and a format-precision retrieval policy; in each evaluated setting it improves average task performance over base agents and broad playbooks while reducing environment steps or retrieval budget. Our experiments show that failures need not trigger uniformly more context: DARC turns self-correction from prompt expansion into recovery-interface design. DARC provides a practical route toward more reliable agents in domains where compiler-like feedback is absent: making failures actionable before making contexts larger.

## Metadata
- **Published**: 2026-08-12T08:14:45Z
- **Authors**: Pan Wang, Yihao Hu, Hang Wang, Zirui Lv, Xin Zhang, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11772v1)