---
title: BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition
url: http://arxiv.org/abs/2610.21565v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_09-22-45Z_BiShield_TEE_Onthe_In__SecurityofUnilateralWeightO.md
generated_at: 2026-10-15 22:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a critical security vulnerability in existing TEE-based parameter obfuscation methods for on-device LLM deployment, where unilateral matrix transformations that obfuscate only the output side can be broken by exploiting what the authors term the Solution Determinacy Property (SDP). The authors propose BiShield-TEE, a bilateral obfuscation framework that jointly transforms both input and output dimensions to produce ambiguous solutions, effectively confining adversarial attack accuracy to the full-shielding black-box baseline while maintaining superior inference efficiency on real hardware.

## Key Takeaways
- The Solution Determinacy Property (SDP) reveals that in unilateral obfuscation schemes, the obfuscation secret is uniquely determined by the system, which inadvertently exposes the structure of the true key. This means an attacker can recover the original transformation and effectively undo the protection, reducing methods like GroupCover and ArrowCloak to negligible security guarantees.
- Under adversarial attacks exploiting SDP, representative prior methods achieve attack accuracy exceeding 2.4 times the full-shielding black-box baseline and recover near-complete model functionality, demonstrating that the claimed protection was largely illusory for on-device TEE-shielded LLM partitions.
- BiShield-TEE addresses this by inducing Ambiguous Solutions through joint obfuscation of both input and output dimensions, ensuring the true key is hidden among many equally valid candidate solutions. Experiments across diverse models and datasets confirm that attack accuracy is confined to the black-box baseline, while the bilateral approach achieves higher inference efficiency than prior unilateral methods on real hardware.

## Context
On-device LLM deployment is growing rapidly due to latency constraints and privacy requirements, but it simultaneously exposes proprietary model weights to reverse engineering and intellectual property theft. Trusted Execution Environments offer hardware-enforced isolation as a defense, and several parameter obfuscation techniques have been proposed to protect model weights within TEEs. However, the field has largely relied on unilateral transformations that only obfuscate the output side of model partitions, leaving a structural vulnerability that this paper is the first to formally characterize and exploit. This work sits at the intersection of hardware security, model IP protection, and adversarial machine learning, addressing a gap that practitioners deploying commercial LLMs on edge devices would encounter in practice.

## Implications
For industry practitioners deploying proprietary LLMs on edge or mobile devices, this work demonstrates that previously adopted TEE-based obfuscation schemes may provide far less protection than assumed, potentially exposing model weights to extraction attacks that recover near-complete model functionality. The BiShield-TEE framework offers a practical bilateral alternative that maintains security guarantees comparable to full black-box shielding while improving inference throughput on real hardware, making it a viable upgrade path for existing on-device inference pipelines. More broadly, the identification of the SDP vulnerability signals that the security community must scrutinize the mathematical structure of obfuscation schemes rather than assuming protection from the mere presence of a transformation, which has implications for how model IP protection is evaluated and standardized in edge AI deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21565v1)
