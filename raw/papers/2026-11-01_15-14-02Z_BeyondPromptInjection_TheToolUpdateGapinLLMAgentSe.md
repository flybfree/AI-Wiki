---
title: Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security
published: 2026-11-01T15:14:02Z
authors: Shiyu Kan, Yue Qi, Yufei Han, Xinjian Luo, Guojun Xiong, Xiaofeng Gao
url: http://arxiv.org/abs/2611.01976v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Prompt Injection: The Tool Update Gap in LLM Agent Security

## Abstract
Large language model based agents increasingly rely on external tools to invoke services and interact with web resources. These tools can evolve through software updates, yet agentic frameworks may continue trusting them without re-verifying their safety after implementation changes. This tool update gap creates a supply-chain vulnerability in agentic systems: because updated tool code executes outside the LLM's context window, malicious functionality embedded in tool updates can bypass defenses centered on model-visible interactions, leaving agents exposed to stealthy, persistent threats that existing in-context defenses can hardly address.   To thoroughly investigate this threat, we introduce ETUDE (Exploiting Tool Updates for Direct Execution), an attack that embeds malicious functionality into updates of initially benign tools to produce compromised tools, while preserving their legitimate tool functionality. Unlike prompt-based attacks, ETUDE operates entirely outside the LLM's context and requires no adversarial instructions, thereby bypassing defenses restricted to model-visible content. We evaluate ETUDE across three representative attack workloads and seven widely used commercial and open-source agentic frameworks, including Gemini CLI, Codex CLI, and Claude Code. The results show that ETUDE achieves a 97.6% ASR while maintaining a 95.9% legitimate task completion rate.   We further examine existing defenses and find that they provide insufficient protection against this threat. These findings expose a fundamental blind spot in current agent security practices: trust established for a tool does not necessarily remain valid after its implementation updates.

## Metadata
- **Published**: 2026-11-01T15:14:02Z
- **Authors**: Shiyu Kan, Yue Qi, Yufei Han, Xinjian Luo, Guojun Xiong, Xiaofeng Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.01976v1)