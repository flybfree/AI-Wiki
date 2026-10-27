---
title: NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names
published: 2026-10-25T12:29:23Z
authors: Chieh-Yuan Chang, Guan-Wei Chen, Chia-Yi Hsu, Chih Yang, Chia-Mu Yu, Chun-Ying Huang
url: http://arxiv.org/abs/2610.34253v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names

## Abstract
AI coding agents routinely clone repositories, install packages, and read source code obtained from the Web, so publicly hosted code becomes part of the context that shapes the code they write. We show that this Web-borne context can be weaponized without any explicit instruction. We present NameTrap, a source-code poisoning attack that only renames identifiers in third-party Python files to steer AI coding agents toward attacker-targeted Common Weakness Enumeration (CWE) vulnerabilities. An attacker-side coding agent iteratively aligns identifiers with a CWE-specific naming convention and confirms through local probe completions that the renamed file elicits the target weakness, while the released bait contains neither instructions nor vulnerable statements. We evaluate NameTrap across six AI coding agents, ten underlying language models, and four vulnerability categories: CWE-78, CWE-79, CWE-327, and CWE-502. Starting from files whose clean versions never yield the targeted CWE, identifier-level manipulation achieves overall attack success rates of 22.5\% to 56.0\% across the six agents, reaching 75.0\% for certain agent--model configurations, and substantially outperforms random renaming, neutral renaming, and the prior identifier-poisoning attack XOXO. The attack remains effective under Traditional Chinese prompts and transfers across models, while a security-reminder defense fails to consistently prevent vulnerability introduction. Moreover, three AI-based security analyzers and four static analyzers report none of the targeted weaknesses in the poisoned files. These findings expose an overlooked attack surface of agents that consume Web content: seemingly harmless variable names in untrusted, Web-hosted code can compromise the security of downstream software.

## Metadata
- **Published**: 2026-10-25T12:29:23Z
- **Authors**: Chieh-Yuan Chang, Guan-Wei Chen, Chia-Yi Hsu, Chih Yang, Chia-Mu Yu, Chun-Ying Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34253v1)