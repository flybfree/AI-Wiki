---
title: Where Did the Repair First Go Wrong? Localizing the Origins of Silent Failures in Agentic Vulnerability Repair
published: 2026-10-05T11:31:16Z
authors: Wenji Bai, Muhammad Waseem, Zeeshan Rasheed, Jaakko Peltonen, Pekka Abrahamsson
url: http://arxiv.org/abs/2610.06163v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Did the Repair First Go Wrong? Localizing the Origins of Silent Failures in Agentic Vulnerability Repair

## Abstract
Localizing where an LLM-based agent first fails to uphold security during a repair can show which stage of its workflow needs an additional safeguard. This is difficult for silent failures, which are patches that pass syntactic and functional checks but still contain a security vulnerability. Because such patches give no observable failure signal, existing failure attribution methods, which rely on observed task failures and labelled failure steps, are less suited to them. We propose Security Awareness Gap Evaluation (SAGE), a trace-based method that combines an assessment of the security reasoning recorded at each turn with the reconstructed code history to identify the earliest turn at which a repair diverges from the task's security intent. We evaluate SAGE on 95 confirmed silent failures drawn from 3,684 repair traces produced by six agent frameworks and six base models on SecurityEval and CVEfixes. SAGE assigned an origin in 93 cases. Most origins were an unaddressed security requirement or an inadequate defence choice, and only five coincided with the code change itself. When the agent introduced the vulnerable code, the origin preceded the write in 14 of 19 cases. Repeated scoring and a second judge reproduced the origin type more consistently than the exact turn, and agreement was lowest for traces that kept only the final file.

## Metadata
- **Published**: 2026-10-05T11:31:16Z
- **Authors**: Wenji Bai, Muhammad Waseem, Zeeshan Rasheed, Jaakko Peltonen, Pekka Abrahamsson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06163v1)