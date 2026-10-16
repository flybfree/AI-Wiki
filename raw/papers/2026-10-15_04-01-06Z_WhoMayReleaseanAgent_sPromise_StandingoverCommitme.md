---
title: Who May Release an Agent's Promise? Standing over Commitments in Multi-Party Chat
published: 2026-10-15T04:01:06Z
authors: Lan Wei, Bingyu Shen, Jiaqi Tang, Qing Lu, Kuan Huang, Meng Xu, Miles Q. Li, Bin Hu, Boyang Li
url: http://arxiv.org/abs/2610.21203v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who May Release an Agent's Promise? Standing over Commitments in Multi-Party Chat

## Abstract
When an assistant serving a team makes a promise to Alice, who may cancel it? We call this standing: only the creditor (the person owed) or someone the creditor or operator policy authorizes may release a commitment, regardless of rank. In a controlled chat environment we vary who cancels and separate two errors: unauthorized release (obeying someone without standing) and override (executing a released promise). Across six models, smaller open ones override the creditor (Qwen3.5-9B: 69%); larger ones drop promises on a peer's direct word (Qwen3.8-27B: 89%; gpt-6.1-sol: 83%); nearly all act on a bystander's "go ahead after all". Oracles dissociate the errors: stating the rule or the creditor curbs unauthorized release but not override, which the latter even raises in three of four models; among them, only knowing whether the promise is still owed cuts override. Enabling thinking moves smaller models the way scale does. A self-kept commitment ledger stops override in four of five models; with a one-paragraph release policy it matches or beats the best oracle store, raising gpt-6-luna's strict accuracy from 49% (policy alone) to 83%. Code, prompts, outputs and labels are released.

## Metadata
- **Published**: 2026-10-15T04:01:06Z
- **Authors**: Lan Wei, Bingyu Shen, Jiaqi Tang, Qing Lu, Kuan Huang, Meng Xu, Miles Q. Li, Bin Hu, Boyang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21203v1)