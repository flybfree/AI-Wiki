---
title: BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition
published: 2026-10-15T09:22:45Z
authors: Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang, Zhu Zhang, Zhixing Tan, Yongheng Deng
url: http://arxiv.org/abs/2610.21565v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition

## Abstract
On-device deployment of large language models (LLMs) is increasingly adopted due to latency and privacy requirements, but exposes proprietary models to reverse engineering and intellectual property theft. Trusted Execution Environments (TEEs) provide hardware-enforced isolation for on-device inference, yet most TEE-based parameter obfuscation relies on unilateral matrix transformations that obfuscate only output side. We identify a vulnerability in this design, termed the \emph{Solution Determinacy Property (SDP)}: the obfuscation secret is uniquely determined, exposing the structure of the true key and enabling attackers to break the protection. Under our attacks, representative methods \textsc{GroupCover} and \textsc{ArrowCloak} are reduced to negligible protection, with attack accuracy reaching over $2.4\times$ the full-shielding black-box baseline and recovering near-complete model functionality.To address this vulnerability, we propose \textsc{BiShield-TEE}, a bilateral framework that induces \emph{Ambiguous Solutions} through joint obfuscation of input and output dimensions, hiding the true key among many equally valid candidates. Experiments across diverse models and datasets show that \textsc{BiShield-TEE} confines attack accuracy to the full-shielding black-box baseline, while achieving higher inference efficiency than prior methods on real hardware.Our code is available at https://github.com/laduiw/BiShield-TEE.

## Metadata
- **Published**: 2026-10-15T09:22:45Z
- **Authors**: Zhiyuan Wang, Yuezhi Zhou, Ziqi Zhang, Zhu Zhang, Zhixing Tan, Yongheng Deng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21565v1)