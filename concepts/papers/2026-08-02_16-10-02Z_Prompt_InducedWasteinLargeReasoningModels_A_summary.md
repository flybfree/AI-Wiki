# Summary: 2026-08-02_16-10-02Z_Prompt_InducedWasteinLargeReasoningModels_APreregi.md
Saved: 2026-08-03 23:15
Source: 2026-08-02_16-10-02Z_Prompt_InducedWasteinLargeReasoningModels_APreregi.md
Model: None

---

## Summary  
[The paper aims to quantify how prompt wording influences the computational waste of large reasoning models used as coding agents, which incur costs from deliberation and tool calls. It introduces a preregistered benchmark across six state‑of‑the‑art models, two harnesses (pi and Claude Code), and 24 deterministic coding tasks evaluated by hidden judges. The study measures reasoning token usage per run to isolate the effect of prompts on spend while controlling for task difficulty. By comparing identical model‑task triples under different prompt styles, it reveals that certain instructions dramatically increase cost without improving accuracy.]  

## Key Contributions  
- [Finding 1] Prompt formulation can multiply reasoning cost without improving correctness.  
- [Finding 2] Generic “think deeply” cues increase deliberation by 1.6–2.2× but do not raise success rates.  
- [Finding 3] A bounded‑efficiency template that specifies scope, acceptance criteria, and a stop condition is cost‑neutral and can halve the number of tokens used.]  

## Methodology  
[The authors designed a preregistered benchmark that runs 4,643 valid agent turns across six large reasoning models (e.g., GPT‑4o, Claude Code) using two harnesses—pi and Claude Code. Each run includes screening, stress, holdout, replication, and cross‑provider stages to ensure reliability. Hidden evaluators score task success while the system logs every token generated, enabling precise measurement of reasoning cost.]  

## Results  
[Prompting to develop and compare several approaches multiplies reasoning tokens by 2.4–7.4 across all models, yet does not raise success rates. Generic “think deeply” cues increase deliberation by 1.6–2.2× without a corresponding gain in performance. A bounded‑efficiency template that specifies scope, acceptance criteria, and a stop condition is cost‑neutral and can halve the number of tokens used. Moreover, identical model‑task‑prompt triples under Claude Code cost 5–30× more per successful run than under pi due to larger static prefixes and additional turns. Misleading architectural hints are far more expensive than irrelevant prose, and provider caching reduces billed cost without altering behavior.]  

## Significance  
[These findings demonstrate that prompt design and harness architecture materially affect the operational expense of reasoning agents, often with no benefit to task success. By exposing hidden waste, they guide developers toward concise, purpose‑bound prompts and efficient harnesses, ultimately supporting more sustainable AI deployment.]  

## Related Concepts  
[Prompting, reasoning tokens, harnesses (pi, Claude Code), preregistered benchmark, cost neutrality, caching, model‑specific sensitivity, static prefixes, tool calls.]
