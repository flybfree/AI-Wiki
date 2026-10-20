---
title: Who Speaks, Who Authorizes, Who Acts? Understanding Trust Boundaries in Multi-Agent LLMs
published: 2026-10-16T22:49:41Z
authors: Junru Zhu, Xin Chen, Hang Lyu, Jiayue Meng, Muzi Li, Yifan Chen, Hengyi Huang, Yu Sun, Weiwei Qi
url: http://arxiv.org/abs/2610.24298v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Speaks, Who Authorizes, Who Acts? Understanding Trust Boundaries in Multi-Agent LLMs

## Abstract
Multi-agent LLM systems exchange messages before acting through tools, but message delivery, signing authority, and tool-side enforcement are separate trust boundaries. We represent them as communication, authorization, and execution structures, and use the authority cut to characterize the smallest independently compromised signer coalition that can construct a policy-valid false-claim proof under stated assumptions. Controlled paired hidden-state studies reveal four distinctions. First, no fixed-message routing contrast across four models meets the prespecified large-effect criterion; when relays rewrite messages, executed false-state action rates vary by model and route configuration. Second, presented source-identity cues do not uniformly increase protected-action selection across three models. Third, on invalid-proof cases, Nemotron and Llama request protected actions in 52.1% and 54.2% of trials, respectively, yet a deterministic tool gate commits none: request-level and commitment-level safety readouts diverge. Finally, a separate single-model authorization check shows that a false claim with a policy-valid compromised-signer proof can pass the gate, since proof validity is not factual truth. These findings motivate evaluating delivered information, qualified authorization, model proposals, and committed actions separately.

## Metadata
- **Published**: 2026-10-16T22:49:41Z
- **Authors**: Junru Zhu, Xin Chen, Hang Lyu, Jiayue Meng, Muzi Li, Yifan Chen, Hengyi Huang, Yu Sun, Weiwei Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24298v1)