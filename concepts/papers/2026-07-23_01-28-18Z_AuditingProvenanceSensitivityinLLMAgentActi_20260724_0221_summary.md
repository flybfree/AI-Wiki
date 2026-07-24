# Summary: 2026-07-23_01-28-18Z_AuditingProvenanceSensitivityinLLMAgentActionSelec.md
Saved: 2026-07-24 02:21
Source: 2026-07-23_01-28-18Z_AuditingProvenanceSensitivityinLLMAgentActionSelec.md
Model: None

---

## Summary  
The paper investigates how large language model agents select actions when the context contains a mixture of user requests, tool outputs, retrieved records, memory traces, and untrusted text. Its core contribution is a target‑specific authorization audit that isolates each evidence factor (tool, argument, proposition) from its source authority while keeping the task, proposition, and policy fixed. By systematically weakening valid evidence and observing competing vs supporting outcomes, the authors quantify the sensitivity of agents to provenance cues across 450 controlled next‑action tasks and multiple open‑weight LLM families.

## Key Contributions  
- [Finding 1] The target‑specific authorization audit labels context factors separately for each tool and argument target, enabling a systematic evaluation of evidence authority.  
- [Finding 2] In controlled degradation scenarios, unauthorized competition is retained in a full‑correct, mixed‑error, clean‑correct pattern affecting approximately 2.4 % of comparisons (95 % CI: 2.1–3.0).  
- [Finding 3] Trusted and untrusted variants produce different actions in 5.4 % of competing cases versus only 1.7 % of supporting cases, indicating a measurable bias toward untrusted evidence.

## Methodology  
The authors construct an audit framework that fixes the task proposition and policy while varying only the source authority of the proposition. Valid evidence is deliberately weakened to create “degraded” contexts; context‑subset interactions serve as a secondary diagnostic for localization. Experiments are run across 450 next‑action tasks using several open‑weight LLM families, generating both trusted (authorized) and untrusted (unauthorized) variants of the same task.

## Results  
Across all experiments, trusted and untrusted variants diverge in action selection for 5.4 % of competing cases versus 1.7 % of supporting cases. Unauthorized evidence remains influential: it is retained in a full‑correct, mixed‑error, clean‑correct pattern across about 2.4 % of comparisons, with a confidence interval of 2.1–3.0 %. These rates are derived from controlled stress‑set tests rather than observed deployment prevalence.

## Significance  
The findings demonstrate that provenance sensitivity is not merely theoretical; LLM agents can be swayed by untrusted evidence despite responding to source‑authority cues. This highlights a critical gap in current safety audits, urging developers to adopt rigorous authorization audits before deploying agents in high‑stakes environments.

## Related Concepts  
- Provenance (source authority of information)  
- Authorization audit (systematic labeling of evidence factors)  
- Context factors (tools, arguments, propositions, memory traces)  
- Tool selection bias  
- Evidence influence vs. authorized influence  
- LLM agent reasoning under mixed‑authority contexts
