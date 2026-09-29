---
title: DAAF: From Failure Localization to Editable System Assets in LLM Agents
published: 2026-09-26T11:39:00Z
authors: Xiaoyang Yuan, Qi Liu, Yubin Ruan, Xinyi Mou, Zhuomeng Zhang, Wenjin Wang, Hanying Jiao, Di Wu, Mingye Xu, Yi Bin, Ke Feng, Zixun Sun
url: http://arxiv.org/abs/2609.32498v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DAAF: From Failure Localization to Editable System Assets in LLM Agents

## Abstract
Deployed LLM agents increasingly rely on persistent, versioned system assets such as routing rules, knowledge segments, prompt instructions, and reusable skills. Failure-localization methods can identify where an error manifests in an agent or execution trace, but repair requires a different decision: which editable system asset should be changed, and is that change expected to improve the task outcome? We study this gap through component-attribute failure attribution, where diagnosis targets versioned, addressable items rather than execution locations. We propose the Detection-Aware Attribution Framework (DAAF), which learns the effects of valid attribute replacements and amortizes this intervention evidence into deployment-time diagnosis. DAAF combines sparse and noisy failure signals to decide whether intervention is warranted, learns component-type-conditioned replacement effects from controlled replays evaluated by executable task outcomes, and shares supervision across requests with compatible intervention responses. At diagnosis time, DAAF uses only the observed execution, registered candidates, and available failure signals; it requires neither counterfactual replay nor task reward and returns no_change, a repair target, or an unresolved decision when evidence is insufficient. On held-out tau^2-bench Telecom tasks, DAAF achieves 80.72% attribute Hit@1, recovers 62.65% of failed executions while limiting clean-task regression to 3.23%, and reaches 71.93% overall task success. These results show that intervention-grounded attribute attribution can connect failure localization to executable system repair.

## Metadata
- **Published**: 2026-09-26T11:39:00Z
- **Authors**: Xiaoyang Yuan, Qi Liu, Yubin Ruan, Xinyi Mou, Zhuomeng Zhang, Wenjin Wang, Hanying Jiao, Di Wu, Mingye Xu, Yi Bin, Ke Feng, Zixun Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32498v1)