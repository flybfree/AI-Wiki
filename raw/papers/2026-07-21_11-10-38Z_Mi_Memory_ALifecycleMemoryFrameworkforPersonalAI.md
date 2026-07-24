---
title: Mi-Memory: A Lifecycle Memory Framework for Personal AI
published: 2026-07-21T11:10:38Z
authors: Xule Liu, Hanlin Teng, Chao Li, Yanan Ni, Shuo Lu, Audrey Wang, Yijun Liu, Yunfei Wang, Xiaofeng Li, Xian Yi, Yuanfa Li, Kang Zhao, Jian Liang, Yuxuan Chen, Jinyuan Chen, Heng Qu, Kun Shao, Jian Luan
url: http://arxiv.org/abs/2607.18975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mi-Memory: A Lifecycle Memory Framework for Personal AI

## Abstract
Personal AI is moving beyond chat-only interaction toward continuous services that span phones, cars, homes, wearables, cameras, and tools. In this setting, memory cannot remain a cache of prior conversations. It should serve as a continuity and governance substrate: preserving durable user state, grounding answers in multimodal and device evidence, supporting correction and forgetting, bounding policy evolution, and remaining deployable under latency, cost, privacy, and edge-cloud constraints. This technical report presents Mi-Memory, a lifecycle memory framework for Personal AI organized around four roles: Structure, Expansion, Evolution, and Deployment. A shared audit contract links these roles through four recurring artifact families: typed evidence payloads preserve source identity and provenance, diagnostic traces localize evidence loss across the serving pipeline, strategy artifacts make memory-policy changes explicit, and gate/rollback records bound accepted evolution. MiMemory instantiates the roles through MemStack, MemSense/MemFuse, D$^{2}$ACCI/E$^{2}$MEND, and LiteMem. In controlled-reference Structure evaluations, MemStack reaches 93.59%, 57.24%, and 87.47% on LoCoMo, PersonaMem-V2, and LongMemEval, respectively; other tracks report module-level, preliminary/internal, transfer-feasibility, or design-only evidence with explicit boundaries. MiMemory is a step toward auditable, evidence-gated, and deployment-aware memory systems for Personal AI. Project homepage: https://darwin-agent.github.io/Mi-Memory/ .

## Metadata
- **Published**: 2026-07-21T11:10:38Z
- **Authors**: Xule Liu, Hanlin Teng, Chao Li, Yanan Ni, Shuo Lu, Audrey Wang, Yijun Liu, Yunfei Wang, Xiaofeng Li, Xian Yi, Yuanfa Li, Kang Zhao, Jian Liang, Yuxuan Chen, Jinyuan Chen, Heng Qu, Kun Shao, Jian Luan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18975v1)