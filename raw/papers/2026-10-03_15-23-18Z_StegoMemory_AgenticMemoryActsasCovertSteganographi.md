---
title: StegoMemory: Agentic Memory Acts as Covert Steganographic Channel
published: 2026-10-03T15:23:18Z
authors: Snehasis Mukhopadhyay, Arun Nair
url: http://arxiv.org/abs/2610.04589v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StegoMemory: Agentic Memory Acts as Covert Steganographic Channel

## Abstract
Is agentic memory robust against stealthy steganographic attacks? We carry out a large-scale red-teaming exercise to test whether agents can encode attacker-controlled strings in one session and recover them in another without triggering safety oversight. Following SHADE-Arena-style tasks, we embed malicious side tasks to encode secret strings using steganography within otherwise benign tasks and evaluate them using independent task-completion and safety oversight. We test 14,000 attack trials spanning 91 model-attack configurations, 13 models, and 7 steganographic schemes: Acrostic, Mesostic, Telestich, Word-choice, Capitalization, Position-based, and Homoglyph. 41.2% of trials successfully encode the target payload in the generated response, while 29.8% survive the memory-write step with the encoding intact. Overall, 25.4% of trials yield a recoverable payload at retrieval, and 20.1% achieve exact-match recovery, including synthetic API keys and cryptographic material never exposed to the receiver. Among the exact-match transmissions, 71.4% also pass primary task-completion scoring and are independently judged safe by the oversight model, corresponding to 14.4% of all trials in which a successful covert transmission would appear to be an ordinary, benign interaction under task-level evaluation. Our results demonstrate that agentic memory can function as a persistent cross-session covert channel. The results further show that the principal bottleneck occurs at memory persistence rather than retrieval: once a steganographic payload survives the memory-write stage, a substantial fraction remains recoverable. We therefore argue that memory integrity, information-flow control, and covert-channel detection should be explicit security requirements for agentic systems.

## Metadata
- **Published**: 2026-10-03T15:23:18Z
- **Authors**: Snehasis Mukhopadhyay, Arun Nair
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04589v1)