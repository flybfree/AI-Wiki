---
title: COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies
published: 2026-10-24T02:29:21Z
authors: Hanming Zhang, Erhu Feng
url: http://arxiv.org/abs/2610.33404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies

## Abstract
As LLMs scale, mixture-of-experts (MoE) architectures increase model capacity while keeping per-token computation manageable through sparse expert activation. This sparsity also enables memory-efficient deployment by retaining most expert weights in CPU memory and transferring or executing only the routed experts on demand. Existing MoE offloading systems typically target specific model-platform configurations, yet differences in model sparsity, CPU and GPU throughput, VRAM capacity, and host-device bandwidth can change the policy ranking. Because implementing and exhaustively evaluating all candidate policies incurs substantial engineering cost, efficiently selecting the best-performing policy for each model-platform configuration remains a key challenge for practical MoE offloading.   We present COPE (Composable Offloading Policy Emulator), which selects the best-performing MoE offloading policy for a target model-platform configuration before runtime integration. COPE comprises two components. Its Policy Matrix factors the design space into two independent axes, expert residency and MoE execution strategy, enabling mechanism reuse across candidate policies and exposing four new candidates. Its Virtual Heterogeneous Machine profiles combined-operator schedules on the target platform and combines these measurements with offline routing traces to estimate candidate performance. Compared with the evaluated baselines, COPE improves fastest-policy selection accuracy by 24%-100% and reduces performance-prediction error by $1.7\times$ to $6.8\times$. By identifying the preferred policy before integration, COPE further reduces policy-specific implementation effort by up to 74%.

## Metadata
- **Published**: 2026-10-24T02:29:21Z
- **Authors**: Hanming Zhang, Erhu Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33404v1)