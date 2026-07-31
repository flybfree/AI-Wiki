---
title: SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis
published: 2026-07-29T18:13:02Z
authors: Xiaoyi Bao, Yuanzhen Xie, Yunzhi Tan, Jinghang Gu, Zhongqing Wang, Chu-Ren Huang, Bo Hu, Zang Li
url: http://arxiv.org/abs/2607.27360v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillMentor: LLM Agent Self-Evolution via Learning Blind-Spot Diagnosis

## Abstract
Agent self-evolution has primarily focused on learning how to act, while overlooking an equally important capability: learning to discover what an agent does not know. Existing approaches typically assume that failure discovery is given, focusing on how to repair failures once they are identified. We ask whether blind-spot diagnosis itself can be learned. We thus study diagnosis as an agent capability separate from execution, and exclude two alternative sources of progress: executor adaptation and human supervision. Under these constraints, performance cannot improve through executor updates or annotated examples, forcing all improvements to originate from the learned diagnostic capability. We propose SkillMentor, which trains a Mentor policy via reinforcement learning to generate diagnostic tasks, identify recurrent failure modes, and curate them into reusable corrective skills. Across AppWorld and BFCLv3, SkillMentor improves executor performance by an average of 44.2%. These results suggest that blind-spot diagnosis is a learnable capability, enabling self-evolution without updating executor weights or relying on human-curated data.

## Metadata
- **Published**: 2026-07-29T18:13:02Z
- **Authors**: Xiaoyi Bao, Yuanzhen Xie, Yunzhi Tan, Jinghang Gu, Zhongqing Wang, Chu-Ren Huang, Bo Hu, Zang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27360v1)