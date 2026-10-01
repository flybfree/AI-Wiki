---
title: Can Terminal Agents Trust Their Own Verification? Diagnosing and Improving Self-Verification
published: 2026-09-30T02:42:23Z
authors: Yingfeng Luo, Shaowei Wei, Daixin Wang, Dingyang Lin, Kaiyan Chang, Weiqiao Shan, Tong Zheng, Zhiqiang Zhang, Jingbo Zhu, Tong Xiao
url: http://arxiv.org/abs/2609.38812v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Terminal Agents Trust Their Own Verification? Diagnosing and Improving Self-Verification

## Abstract
Terminal agents rely on self-verification to assess and correct their solutions as they solve tasks through interaction with command-line environments. Yet how trustworthy such self-verification is remains poorly understood. To investigate this question systematically, we introduce a diagnostic framework that identifies the first complete solution in each trajectory, determines whether it is objectively correct, and uses this ground truth to quantify the agent's subsequent verification and recovery behavior. Applying it to ten terminal agents on TerminalBench2.1, we find that verification is nearly universal after a complete candidate is formed, yet only 61.43\% of incorrect candidates are detected and only 49.36\% of detected errors are successfully repaired. These results show that the main weakness in self-verification lies not in initiating verification, but in detecting and repairing errors. Motivated by these findings, we propose Student-Conditioned Verification Distillation (SCVD), which lets the student first produce a candidate solution and distills a stronger teacher's subsequent verification and recovery from the same interaction context. Across three Qwen3.5 backbones, SCVD improves \textsc{Pass@1} on TerminalBench2.1 by 9.74--16.85 percentage points over the corresponding base models and by 4.49--8.61 points over the standard full-trajectory distillation, while avoiding the pronounced out-of-distribution degradation of full-trajectory distillation on SWE-bench Verified.

## Metadata
- **Published**: 2026-09-30T02:42:23Z
- **Authors**: Yingfeng Luo, Shaowei Wei, Daixin Wang, Dingyang Lin, Kaiyan Chang, Weiqiao Shan, Tong Zheng, Zhiqiang Zhang, Jingbo Zhu, Tong Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38812v1)