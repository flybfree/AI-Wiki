---
title: Relic: From Multi-Agent Collaboration to Persistent Organizational Capability
url: http://arxiv.org/abs/2609.32965v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_21-55-49Z_Relic_FromMulti_AgentCollaborationtoPersistentOrga.md
generated_at: 2026-09-28 23:39
model: qwen3.6-35b-a3b
---

## Summary
Relic introduces a framework that transforms recurring collaboration failures in multi-agent organizations into persistent, executable protocols, ensuring lessons persist beyond individual agent interactions. By enabling members to reflect on visible work, propose rules, and govern adoption through runtime bindings of triggers, responsibilities, evidence, and consequences, the system maintains organizational state independent of specific participants. Empirical evaluations demonstrate significant gains in contract delivery rates, behavioral correctness for new agents, and benchmark performance across diverse software workloads.

## Key Takeaways
- Relic operationalizes collaboration experience by converting recurring failures into organization-owned protocols that bind triggers, responsibilities, required evidence, and execution consequences to the runtime, allowing rules to be revised or retired as needed; for instance, integration friction generates an interface-review rule that governs subsequent pull requests.
- Across 360 controlled runs involving ten software workloads and three models, Relic increases complete-contract delivery from 14.06% to 19.76%, a gain of 5.71 percentage points over a matched structured team without the protocol lifecycle, while improving all four verified production endpoints in every model stratum.
- The framework excels in transfer scenarios and benchmarks: fresh-member behavioral correctness reaches 41.2% with executable bindings compared to 34.6% for text rules (+6.5 points), and Relic achieves a state-of-the-art 76.9% on the CooperBench benchmark, outperforming peer-structured systems and reversing coordination loss seen in baselines.

## Context
Multi-agent systems frequently encounter coordination breakdowns when agents conflict or when team composition changes, as conversational resolutions do not scale to persistent organizational memory. This work addresses a critical gap in agent orchestration by shifting focus from transient dialogue to durable governance structures that capture collective experience as executable state rather than relying on individual agent knowledge or static prompts.

## Implications
The approach offers a pathway for building resilient multi-agent teams where quality assurance and best practices are enforced through automated, evolving protocols rather than fragile conversation histories. Practitioners can leverage Relic to maintain high standards of software delivery and coordination efficiency even as models rotate or new agents join, effectively decoupling organizational capability from specific agent instances and enabling scalable, self-improving collaborative workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32965v1)
