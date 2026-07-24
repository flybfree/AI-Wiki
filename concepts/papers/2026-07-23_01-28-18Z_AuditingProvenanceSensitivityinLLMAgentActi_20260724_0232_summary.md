# Summary: 2026-07-23_01-28-18Z_AuditingProvenanceSensitivityinLLMAgentActionSelec.md
Saved: 2026-07-24 02:32
Source: 2026-07-23_01-28-18Z_AuditingProvenanceSensitivityinLLMAgentActionSelec.md
Model: None

---

## Summary  
The paper addresses the problem of whether large language model (LLM) agents select actions based solely on authorized evidence or also influenced by untrusted sources within their context. It introduces a target‑specific authorization audit that separates each tool’s permitted evidence from each argument’s source authority, enabling systematic evaluation of provenance sensitivity in action selection. By fixing the task and policy while varying only the authority of propositions, the authors can isolate how changes in evidential credibility affect the model’s behavior.

## Key Contributions  
- [Finding 1] Untrusted evidence competes with trusted evidence in about 5.4 % of next‑action tasks, whereas it supports decisions in roughly 1.7 % of cases.  
- [Finding 2] Under controlled degradation (weakening valid evidence), unauthorized competition is retained in a full‑correct / mixed‑error / clean‑correct pattern across 2.4 % of comparisons, with a confidence interval of 2.1–3.0 %.  
- [Finding 3] The observed differences are statistically significant and reflect real model responses to textual source‑authority cues rather than mere noise.

## Methodology  
The authors designed a controlled experiment using 450 next‑action tasks across multiple open‑weight LLM families. For each task they kept the proposition, position, and policy constant while swapping only the authority of the supporting evidence (trusted vs untrusted). They also performed secondary diagnostics by examining interactions between subsets of context to localize where provenance cues are processed.

## Results  
Across all tasks, trusted arguments were chosen in 86.3 % of cases and untrusted ones in 13.7 %, but when both appear they conflicted only in the competing scenarios measured at 5.4 %. When valid evidence was weakened, the model retained unauthorized competition in a clean‑correct pattern about 2.4 % of the time, confirming that the audit captures genuine provenance bias.

## Significance  
These findings demonstrate that LLM agents are not immune to untrusted information and that their action selection can be subtly swayed by source authority cues. The proposed audit provides a reliable metric for developers to assess how much provenance sensitivity influences model behavior, which is critical for safe deployment in high‑stakes environments.

## Related Concepts  
- Provenance: the origin and trustworthiness of information.  
- Authorization: permission granted to use specific evidence.  
- LLM agent action selection: the process by which an LLM chooses tools or arguments.  
- Evidence grounding: linking model decisions to source material.  
- Context subsets: partial views of the surrounding text used for diagnostic analysis.
