---
title: The Anatomy of a Prompt Injection: A Component Model for Structured Analysis
published: 2026-08-07T23:16:35Z
authors: Jeremy McHugh
url: http://arxiv.org/abs/2608.07808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Anatomy of a Prompt Injection: A Component Model for Structured Analysis

## Abstract
Four years after prompt injection was first identified in 2022, attacks are still predominantly documented as verbatim strings rather than structured exploits, despite advancing agent capabilities and threat actors embedding injections to subvert AI-assisted security analysis. This paper formalizes the structure of prompt-injection artifacts, enabling defenders, red teamers, and cyber threat intelligence (CTI) teams to label, compare, and mutate attacks without relying on fragile string matching. Because large language models compile varied natural-language realizations into identical executable actions, labeling must track attacker intent (tool targets, sinks, and effects) rather than surface wording. We propose a seven-component model (carrier, delivery vector, concealment, context-break, privilege escalation, payload, and return channel) consisting of five artifact fields and two environment fields. This framework unifies roles partially addressed by HOUYI's payload decomposition, the Promptware Kill Chain, and campaign taxonomies, while framing minimal jailbreak frameworks like ReNeLLM as projections onto a restricted subspace. We provide clear labeling rules, a logical analysis record mapping directly to industry CTI schemas, worked examples including EchoLeak (CVE-2025-32711) and an in-the-wild malware AI-evasion sample, and an illustrative agentic flowchart.

## Metadata
- **Published**: 2026-08-07T23:16:35Z
- **Authors**: Jeremy McHugh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07808v1)