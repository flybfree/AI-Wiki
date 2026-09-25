---
title: PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations
published: 2026-09-24T16:39:18Z
authors: Luciano Maldonado
url: http://arxiv.org/abs/2609.30094v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations

## Abstract
Large language models increasingly operate as persistent assistants in user-facing, shared-session, and tool-augmented settings. When users disclose sensitive information during an active conversation, that information may remain behaviorally recoverable through later prompts even after the dialogue shifts to unrelated topics. We introduce \textbf{PrivDrift}, a benchmark for auditing whether user-disclosed secrets remain recoverable after conversational topic drift and persuasion-based probing. PrivDrift contains 1{,}000 controlled multi-turn dialogues with seeded secrets, content-dense drift turns, and standardized extraction probes. Across three LLMs with extended context windows, dialogue-level hybrid leakage remains substantial, ranging from 38.7\% to 54.6\%, and varies strongly by model, secret type, and persuasion intensity. Within the tested drift window, additional topic drift does not reliably reduce leakage, suggesting that privacy risk in active LLM contexts should be evaluated as a persistent behavioral failure mode rather than only as training-data memorization or immediate jailbreak behavior.

## Metadata
- **Published**: 2026-09-24T16:39:18Z
- **Authors**: Luciano Maldonado
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30094v1)