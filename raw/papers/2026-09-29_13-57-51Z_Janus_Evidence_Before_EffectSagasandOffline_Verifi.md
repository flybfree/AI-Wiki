---
title: Janus: Evidence-Before-Effect Sagas and Offline-Verifiable Provenance for Agentic LLMs
published: 2026-09-29T13:57:51Z
authors: Mustafa Arslan
url: http://arxiv.org/abs/2609.38266v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Janus: Evidence-Before-Effect Sagas and Offline-Verifiable Provenance for Agentic LLMs

## Abstract
Agentic large language models (LLMs) now move money through tools, yet the record of what they did is usually a trace their own process emits beside the effect. Janus puts the record on the effect path. A step's proposal, the verdict on it and any answer from a validator or a person are durable in a signed, hash-chained log before the step may run or its effect be released; with keys declared, each answer is signed by whoever gave or relayed it. Gates are pure functions of that log, and an auditor re-derives every verdict offline from the log and one public key. At the MCP edge the effect is held until then; through the SDK, which our model experiment uses, a cooperating client runs it only afterwards. We evaluate Janus under crash injection (144 kills in-process, 81 through the daemon), by verifying a 100-million-event log offline (254.5 s), and with a real model behind a lending workflow, run governed and plain on the same recorded model outputs. With the lending mandate in the model's prompt, the comparison was 0 against 0. With it only in the policy and the amount's unit stated, the model approved six loans declared over the mandate, three with no injection (a run that also dropped the unit approved three); the plain agent paid all six and Janus none, each refused by a deterministic validator and re-derivable offline. An always-approve oracle over the recorded intakes gave 20 and 21 declared over the mandate against 0, though Janus paid four and three whose declared amount understated the request. Designing the experiment exposed, in a system that passed its own audit, an instance of post-approval substitution: an approval keyed to an attempt was counted for a different proposal, moving a person's approval from 100 to 1,000,000. We report it, a first fix and the five routes around it, and what Janus does not guarantee.

## Metadata
- **Published**: 2026-09-29T13:57:51Z
- **Authors**: Mustafa Arslan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38266v1)