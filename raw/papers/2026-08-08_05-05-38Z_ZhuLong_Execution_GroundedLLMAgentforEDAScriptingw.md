---
title: ZhuLong: Execution-Grounded LLM Agent for EDA Scripting with Offline API Self-Exploration
published: 2026-08-08T05:05:38Z
authors: Yang Liu, Shiwei Hou, Xiyuan Chen, Yu Wang, Sen Yuan, Qirui Gan, Shao You, Feifan Chen, Wencheng Li, Shuyang Hu, Yongzhou Liu, Emma Xia, Xiaojing Lu, Hao Wang, Fan Xu, Yanfeng Li
url: http://arxiv.org/abs/2608.07925v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ZhuLong: Execution-Grounded LLM Agent for EDA Scripting with Offline API Self-Exploration

## Abstract
EDA scripting with tool-specific, often undocumented APIs remains a long-tail bottleneck that existing LLMs fail to address. This paper presents ZhuLong, an execution-grounded LLM coding agent for PyAether and SKILL that combines API retrieval, documentation inspection, and sandbox execution via unified MCP tools, augmented by an offline API self-exploration mechanism that infers undocumented API behaviors through counterfactual experimentation.   We evaluate ZhuLong on EDA-Eval-PyAether, a benchmark of 158 real-world tasks with assertion-based execution, where the complete system achieves 78.5% Pass@1 in the commercial Empyrean Aether environment, substantially outperforming a pure LLM baseline (23.6%). Ablation studies identify sandbox execution as the dominant performance driver (41.2 pp drop when removed), with the self-exploration mechanism contributing an additional 3.2 pp accuracy gain and a 22.1% reduction in per-task tool calls. On 20 interactive tasks involving unsaved layouts and schematics, ZhuLong achieves 60.0% Pass@1 for PyAether and 50.0% for SKILL.

## Metadata
- **Published**: 2026-08-08T05:05:38Z
- **Authors**: Yang Liu, Shiwei Hou, Xiyuan Chen, Yu Wang, Sen Yuan, Qirui Gan, Shao You, Feifan Chen, Wencheng Li, Shuyang Hu, Yongzhou Liu, Emma Xia, Xiaojing Lu, Hao Wang, Fan Xu, Yanfeng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07925v1)