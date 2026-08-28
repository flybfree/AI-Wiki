---
title: Preserving General Capabilities during Domain Specialization with Uncertainty-Calibrated MOPD
published: 2026-08-27T07:28:00Z
authors: Ziyuan Liu, Jiao Ou, Jian Liang, Ruiming Tang, Cheng Luo
url: http://arxiv.org/abs/2608.26735v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Preserving General Capabilities during Domain Specialization with Uncertainty-Calibrated MOPD

## Abstract
Specializing large language models to vertical domains improves domain-specific behavior but often degrades general capabilities such as reasoning, coding, instruction following, and creative writing. We study this domain--general trade-off in Multi-Teacher On-Policy Distillation (MOPD), where a specialized student is supervised on its own sampled trajectories by domain and general teachers. Standard MOPD faces two limitations: ordinary on-policy sampling rarely exposes tokens with large positive teacher--student advantages, while the advantage sign alone does not establish whether the resulting update direction is reliable. We propose uncertainty-calibrated MOPD to address these limitations. Dual-temperature sampling broadens the candidate trajectory pool, and positive-advantage-density filtering selects trajectories with stronger positive learning signals. Centered log-likelihood (CLL) filtering then computes an entropy-calibrated teacher-endorsement score and probabilistically retains token updates according to direction--endorsement consistency. Experiments on role-playing and medical-domain specialization show that our method improves the general-capability average over standard MOPD by $4.73\%$ and $10.84\%$, respectively, while maintaining vertical-domain performance. Ablations and diagnostic analyses further confirm that the gains do not merely result from a larger rollout budget and that the proposed trajectory- and token-level mechanisms address their intended failure modes.

## Metadata
- **Published**: 2026-08-27T07:28:00Z
- **Authors**: Ziyuan Liu, Jiao Ou, Jian Liang, Ruiming Tang, Cheng Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26735v1)