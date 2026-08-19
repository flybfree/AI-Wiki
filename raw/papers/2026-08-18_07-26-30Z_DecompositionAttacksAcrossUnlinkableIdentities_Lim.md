---
title: Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services
published: 2026-08-18T07:26:30Z
authors: Bowen Sun, Zhengyue Zhao, Xiaogeng Liu, Yinzhi Cao, Chaowei Xiao
url: http://arxiv.org/abs/2608.17445v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services

## Abstract
Most large language model services use stateless defenses, which judge only the current request, to refuse harmful tasks. Decomposition attacks exploit this limitation by splitting a harmful task into individually permissible requests and combining their answers. Defending against them therefore requires a stateful monitor that considers requests together. If it can group all requests for one attacker task, it can stop the attack. However, attackers can use unlinkable identities and combine answers elsewhere, leaving no reliable grouping signal. We ask whether decomposition attacks can still be stopped under this setting. For a fixed attack strategy without retries, we prove that the achievable security and utility tradeoff depends entirely on how benign requests for the same capabilities are grouped. Persistent, recognizable groups permit a useful defense; fresh, indistinguishable groups do not. When attackers can retry and learn from Allow/Block decisions, this useful operating point disappears: the feedback reveals what passes but not whether a block was correct. Experiments on 91 executable tasks and 11,393 capability-matched benign requests support these results. Under a 1% denial cap for these requests and a 0.5% cap for unrelated background traffic, all ten tested policies, including one privileged policy with an exact request-to-operation map, either fail to stop attacks or exceed the budget. On defense-unseen task families, attack success is at least 99% after one attempt and 100% after two. Effective defenses therefore require additional evidence or mechanisms tied to grouping, such as reliable identity linkage, costs for fresh identities, or control over answer use.

## Metadata
- **Published**: 2026-08-18T07:26:30Z
- **Authors**: Bowen Sun, Zhengyue Zhao, Xiaogeng Liu, Yinzhi Cao, Chaowei Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17445v1)