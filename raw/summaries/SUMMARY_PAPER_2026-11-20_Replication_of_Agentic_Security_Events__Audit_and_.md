---
title: Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)
url: http://arxiv.org/abs/2611.26553v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-19_18-23-35Z_ReplicationofAgenticSecurityEvents_AuditandInvesti.md
generated_at: 2026-11-20 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ROGUE-AI is a multi-agent framework designed to replicate and audit reported agentic security incidents offline, addressing a critical gap where news reports and incident catalogs describe agent failures without validating them or identifying root causes. The framework rebuilds each reported incident alongside a matched control that removes only the blamed cause, then runs agents on both to test whether the reported harm is reproducible and whether the identified cause is genuinely responsible. Results show that ROGUE-AI successfully reproduced reported harm in 89% of 108 attempted replications, revealing that most real-world agent failures stem not from adversarial attacks like prompt injection but from agents executing their tasks correctly while overlooking ordinary operational hazards.

## Key Takeaways
- ROGUE-AI achieved an 89% reproduction rate across 108 attempted incident replications, with agents built on five current models (GPT, Claude, Gemini, and DeepSeek) making the reported mistake in 18% to 33% of runs when the blamed cause was present, compared to at most 1% without it, demonstrating that the framework can reliably validate or invalidate incident reports and isolate causal factors.
- Of the 72 incidents involving real-world harm, 62 had no underlying attacker, meaning agents simply did what their task asked but missed ordinary hazards such as a database shared with a live production site. Replications without an attacker caused more harm than replications of prompt injection for all five models, indicating that the dominant failure mode in agentic security is mundane operational oversight rather than adversarial manipulation.
- A targeted warning placed after each tool output that explicitly names the hazard and its consequence lowered harm for all five models, whereas a note of identical length that did not mention the specific hazard left most of the harm in place, showing that effective defenses must be hazard-specific rather than generic cautionary text.

## Context
As LLM-based agents increasingly perform consequential real-world actions such as deleting files, sending payments, and modifying production systems, the field lacks a systematic method to verify whether reported incidents are genuine, reproducible, and correctly attributed to specific causes. Existing benchmarks record whether agents fail but do not replicate incidents or test causal hypotheses, leaving vendors and researchers without a rigorous audit mechanism. ROGUE-AI fills this gap by providing a reproducible, offline replication pipeline grounded in real incidents, shifting the focus from adversarial threat models toward the more prevalent and under-studied problem of agents completing tasks while overlooking ordinary operational risks.

## Implications
For industry practitioners and AI vendors, ROGUE-AI offers a reusable audit framework that can be rerun before each new model release to verify that previously reported failure modes have been addressed, providing a concrete pre-deployment safety gate. The finding that most agent harm arises from task-compliant behavior missing ordinary hazards rather than from prompt injection challenges the current defensive paradigm, which primarily targets injected instructions, and suggests that safety engineering must incorporate hazard-aware contextual warnings tied to specific tool outputs. This reframing has direct consequences for how agent safety evaluations, incident response protocols, and vendor release processes should be designed going forward.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.26553v1)
