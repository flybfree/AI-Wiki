---
title: The Show-Up Attack: When Subagents Win Over Their Supervisor
published: 2026-10-20T03:41:13Z
authors: Maosen Zhang, Jianshuo Dong, Yutong Zhang, Jie Zhang, Tianwei Zhang, Han Qiu
url: http://arxiv.org/abs/2610.27574v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Show-Up Attack: When Subagents Win Over Their Supervisor

## Abstract
Multi-agent systems are increasingly deployed to coordinate multiple large language model (LLM) agents. However, this also creates new attack surfaces: malicious agents may have chances to exploit the coordination. In this paper, we propose and study the \textit{show-up attack}, in which a malicious subagent manipulates the supervisor into involving it in tasks beyond its assigned scope. To evaluate this risk, we propose SUA-Arena, which implements 6 attack strategies and contains 188 test cases. Then, we evaluate 6 frontier LLMs and find that all of them are vulnerable to show-up attacks. For example, GPT-5.6-Sol as a supervisor suffers an ASR of up to 0.93. Mitigation strategies such as prompting and restricted communication fail to reduce the risk consistently. These results show that multi-agent systems need explicit mechanisms for enforcing authority boundaries.

## Metadata
- **Published**: 2026-10-20T03:41:13Z
- **Authors**: Maosen Zhang, Jianshuo Dong, Yutong Zhang, Jie Zhang, Tianwei Zhang, Han Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27574v1)