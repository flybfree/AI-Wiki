---
title: ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents
published: 2026-09-14T03:47:05Z
authors: Bingzheng Wang, Xiaoyan Gu, Wentao Wang, Xingyou Yang, Hongcheng Li, Rong Yin
url: http://arxiv.org/abs/2609.14987v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ActGuard: Pre-execution Action Auditing against Indirect Prompt Injection in LLM Agents

## Abstract
Large language model (LLM) agents interact with external environments through tool invocation, but tool outputs can also expose them to indirect prompt injection (IPI) attacks. Existing defenses mainly rely on prompt hardening, content filtering, pre-generated plans, or permission constraints. These approaches often struggle with complex tasks or over-sanitize external content, making it difficult to balance security and utility. The key challenge is therefore to preserve execution flexibility while precisely identifying and removing the malicious content that actually induces unsafe actions. To address this challenge, we propose ActGuard, a pre-execution action auditing framework. Rather than judging whether external content is inherently suspicious, ActGuard assesses whether it causes the current action to deviate from a locally reasonable expectation. At each step, ActGuard predicts the tools likely to be used by the upcoming action and constructs a local tool prior without constraining the execution trajectory. Before execution, it compares the candidate action against this prior and performs tool-level contrastive analysis and parameter-level evidence localization to identify deviations in tool selection and action parameters. A verifier then examines the localized evidence, masks only spans confirmed as malicious, and regenerates the action from the sanitized context. This design preserves legitimate planning flexibility while minimizing information loss from indiscriminate filtering. We evaluate ActGuard on challenging benchmarks for tool-using agents. Results show that ActGuard reduces attack success rates to a level comparable to state-of-the-art defenses while maintaining task utility close to the no-attack setting, achieving a favorable security-utility trade-off. Our code is publicly available at: https://github.com/binzhwang/ActGuard.

## Metadata
- **Published**: 2026-09-14T03:47:05Z
- **Authors**: Bingzheng Wang, Xiaoyan Gu, Wentao Wang, Xingyou Yang, Hongcheng Li, Rong Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14987v1)