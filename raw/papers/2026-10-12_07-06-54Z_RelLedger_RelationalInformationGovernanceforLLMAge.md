---
title: RelLedger: Relational Information Governance for LLM Agent Organizations
published: 2026-10-12T07:06:54Z
authors: Junxi Huang, Wenshuo Chen, Nuoxuan Li, Kailong Wang, Meitong Shen, Yuehan Kou, Leihao Zhao, Yutao Yue, Xiucheng Wang, Nan Cheng
url: http://arxiv.org/abs/2610.16281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RelLedger: Relational Information Governance for LLM Agent Organizations

## Abstract
In LLM agent organizations, shared records determine which facts are available for later decisions. A sender consults interaction histories before deciding whether to report an event. A delivery gap across histories does not show whose relationship drove the choice or whether the resulting record matters downstream. We introduce RelLedger to audit these links. It holds the event, evidence, risk, and message fixed while crossing the sender's histories with the event target and an unrelated actor. Role reassignment and history rewrites locate the controlling cue. Message and cost interventions show when the effect appears. An attribution ledger maps each claim to its required response cells and separates missing interventions from sampling uncertainty. Recipient replay follows delivered information into downstream decisions. Executable workflows for a simulated one-person company extend the audit to retrieved histories, tool calls, and shared ledger updates. Across GPT, Gemini, Claude, DeepSeek, and Qwen, the audit reveals model-specific control paths and smaller relation gaps under explicit loss rules. Claude sends the same factual notice 62.22 percentage points more often with conflict histories than with friendly histories. In executable workflows, strained histories reduce recipient review rates by 45.83 points relative to warm histories for Claude.

## Metadata
- **Published**: 2026-10-12T07:06:54Z
- **Authors**: Junxi Huang, Wenshuo Chen, Nuoxuan Li, Kailong Wang, Meitong Shen, Yuehan Kou, Leihao Zhao, Yutao Yue, Xiucheng Wang, Nan Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.16281v1)