---
title: CPInj: Uncovering Prompt Injection Risks in Textual Collaborative Prompt Optimization
published: 2026-07-21T01:44:59Z
authors: Xinting Liao, Behnoosh Zamanlooy, Masoumeh Shafieinejad, David B. Emerson, Ruinan Jin, Deval Pandya, Xiaoxiao Li
url: http://arxiv.org/abs/2607.18622v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CPInj: Uncovering Prompt Injection Risks in Textual Collaborative Prompt Optimization

## Abstract
Textual Collaborative Prompt Optimization (TCPO) extends Textgrad (Yuksekgonul et al., 2025) to a decentralized setting by allowing multiple clients to jointly improve prompts for large language models (LLMs) while keeping their data locally. Its reliance on free-form textual updating and aggregation introduces a new and largely unexplored attack surface, i.e., malicious instructions can be injected into local prompts and propagated through server-side prompt aggregation. Unlike conventional prompt injection attacks, attacking TCPO targets the collaborative optimization loop in TCPO. This setting is more challenging because malicious instructions must survive aggregation, persist through subsequent benign prompt optimization, and evade server-side defenses. To expose this risk, we propose CPInj, a collaborative prompt injection attack that contaminates the aggregated global prompt with malicious instructions, degrades downstream task performance, resists purification by prompt optimization on benign clients, and evades advanced detection-based defenses on the server. We find that current defense methods are ineffective against CPInj. To mitigate this attack, we further propose a defense-oriented aggregation method, i.e., APAgg, which purifies malicious instructions and partially recovers TCPO utility. We conduct extensive experiments across three LLM families and five reasoning tasks in math, logic, and medicine. The results demonstrate that our proposed attack reveals a critical vulnerability in TCPO. Although we take a first step toward mitigation, the attack remains highly effective and far from fully resolved, calling for more robust defense for TCPO.

## Metadata
- **Published**: 2026-07-21T01:44:59Z
- **Authors**: Xinting Liao, Behnoosh Zamanlooy, Masoumeh Shafieinejad, David B. Emerson, Ruinan Jin, Deval Pandya, Xiaoxiao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18622v1)