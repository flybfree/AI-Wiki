---
title: MNC: Scope-Bound Semantic Declassification for Private LLM-Agent Communication
published: 2026-08-03T05:36:49Z
authors: Jinghan Xu, Longze Fan, Zeyuan Wang, Xinjin Li, Hankai Liu
url: http://arxiv.org/abs/2608.01719v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MNC: Scope-Bound Semantic Declassification for Private LLM-Agent Communication

## Abstract
Multi-agent large language model (LLM) systems can expose protected state through internal messages, tool arguments, logs, and persistent memory even when their public outputs appear innocuous. Existing privacy prompts, redaction methods, and source-level access controls restrict surface content or data access, but do not specify what a legitimately informed agent should disclose or how that disclosure may be reused downstream. We introduce Minimum-Necessary Communication (MNC), a typed semantic-declassification protocol that selects a task-sufficient disclosure from an application-authored candidate family and binds it to explicit recipient, purpose, forwarding, lifetime, logging, and memory scopes. A reference monitor enforces these scopes across subsequent operations, while a history-aware extension accounts for inference risk accumulated over repeated disclosures. Controlled semantic-join, memory, probing, and longitudinal experiments show that conventional defenses can preserve protocol-level utility while exposing substantial additional inference signal. Under identical receipt text, MNC preserves authorized delivery while blocking unauthorized forwarding, logging, durable storage, and retrieval after expiration that a text-only semantic declassifier permits. Two-backbone MAGPIE executions further show that mediated disclosures propagate through subsequent planning, tool use, coordination, and memory retrieval. These results support scope-bound semantic declassification as a practical communication boundary for private LLM-agent systems.

## Metadata
- **Published**: 2026-08-03T05:36:49Z
- **Authors**: Jinghan Xu, Longze Fan, Zeyuan Wang, Xinjin Li, Hankai Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01719v1)