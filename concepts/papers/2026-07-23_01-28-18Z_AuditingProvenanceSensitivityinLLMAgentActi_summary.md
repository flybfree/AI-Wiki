# Summary: 2026-07-23_01-28-18Z_AuditingProvenanceSensitivityinLLMAgentActionSelec.md
Saved: 2026-07-24 02:21
Source: 2026-07-23_01-28-18Z_AuditingProvenanceSensitivityinLLMAgentActionSelec.md
Model: None

---

## Summary  
The paper investigates how large language models (LLMs) select actions when their context contains a mixture of user requests, tool outputs, retrieved records, memory, and untrusted text. It proposes a target‑specific authorization audit that isolates each tool and argument to a particular source authority, allowing researchers to measure the impact of provenance on decision making. By systematically weakening valid evidence while keeping the task, proposition, position, and policy constant, the authors demonstrate that LLM agents still respond to textual cues about source authority yet remain susceptible to untrusted information in a small but statistically significant fraction of cases.

## Key Contributions  
- [Finding 1] The authors introduce a target‑specific authorization audit framework that labels context factors separately for each tool and argument, enabling fine‑grained analysis of provenance influence.  
- [Finding 2] They show that when valid evidence is weakened, authorized competition between trusted and untrusted sources appears in 5.4 % of competing cases versus only 1.7 % of supporting cases, indicating a measurable bias toward untrusted input.  
- [Finding 3] Under controlled degradation, unauthorized competition is retained in a full‑correct, mixed‑error, or clean‑correct pattern across just 2.4 % of comparisons (95 % CI: 2.1–3.0), revealing low‑frequency but non‑zero error rates.

## Methodology  
The methodology centers on a controlled experiment where the task, proposition, position, and policy are fixed while only the source authority of the proposition is varied. The authors generate trusted and untrusted variants of each context, then run them through multiple open‑weight LLM families across 450 next‑action tasks. Context‑subset interactions serve as a secondary diagnostic to isolate localization effects. The study measures whether the model’s action selection reflects the true source authority or is swayed by weaker evidence.

## Results  
The main experimental results show that authorized competition is retained in a full‑correct, mixed‑error, or clean‑correct pattern only 2.4 % of the time, with a confidence interval of 2.1–3.0 percent. Untrusted evidence influences action selection at a higher rate: it competes with trusted evidence in 5.4 % of competing cases versus 1.7 % of supporting cases. These figures are stress‑set rates for the controlled experiment, not estimates of real‑world deployment prevalence.

## Significance  
This research matters because it reveals that LLM agents can be fooled by textual cues about source authority while still allowing untrusted evidence to shape their decisions. The findings underscore the need for provenance auditing mechanisms that can detect and mitigate subtle biases in action selection, especially as models become more integrated into high‑stakes applications.

## Related Concepts  
- Provenance: the origin and trustworthiness of information.  
- Authorization audit: a systematic evaluation of which context factors are permitted to influence decisions.  
- Context factors: elements such as user requests, tool outputs, retrieved records, memory, and untrusted text that feed into action selection.  
- Tool selection: the process by which an LLM chooses which external tools or arguments to invoke.  
- Evidence influence: how the relevance of evidence (trusted vs. untrusted) affects model behavior.
