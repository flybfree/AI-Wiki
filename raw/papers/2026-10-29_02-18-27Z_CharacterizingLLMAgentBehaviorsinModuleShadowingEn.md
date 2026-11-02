---
title: Characterizing LLM Agent Behaviors in Module Shadowing Environments
published: 2026-10-29T02:18:27Z
authors: Shuai Yang, Enmeng Lu, Jinyu Fan, Gongce Cao, Yu Chen, Jiawei Xie, Feifei Zhao, Zhangsheng Wang, Yongyu Jiang, Yi Zeng
url: http://arxiv.org/abs/2610.40716v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Characterizing LLM Agent Behaviors in Module Shadowing Environments

## Abstract
LLM agents operating in untrusted workspaces face the risk of untrusted code execution during routine tasks, yet final reports and workspace states alone cannot reliably establish whether execution occurred. We introduce an evaluation framework that codes observation, reasoning, execution, and response behaviors from agent trajectories and aligns them with independent environmental records to reconstruct execution histories and verify final reports. We apply this framework to module shadowing, in which a local file is loaded in place of a trusted module during import, enabling untrusted code execution without adversarial prompts. Across 90 trials with 15 models, the payload executed in 51% of direct shadowing trials and 87% of indirect shadowing trials. Even explicit recognition of the shadowing mechanism did not ensure prevention, as the payload ran in 10 of the 29 trials with recorded recognition. These failures were often omitted from final reports, as 49 of the 62 triggered trials ended without mention of the security issue. Three reports even denied execution, including one from a trial in which independent logs recorded 19 payload executions. Final workspace states also obscured prior execution when agents deleted or overwrote the payload marker in 10 triggered trials. These findings demonstrate that combining behavioral coding with independent environmental auditing enables rigorous and transparent evaluation of agent safety.

## Metadata
- **Published**: 2026-10-29T02:18:27Z
- **Authors**: Shuai Yang, Enmeng Lu, Jinyu Fan, Gongce Cao, Yu Chen, Jiawei Xie, Feifei Zhao, Zhangsheng Wang, Yongyu Jiang, Yi Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.40716v1)