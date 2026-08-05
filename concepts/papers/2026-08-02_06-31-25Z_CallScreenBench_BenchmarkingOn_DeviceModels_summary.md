# Summary: 2026-08-02_06-31-25Z_CallScreenBench_BenchmarkingOn_DeviceModelsasPhone.md
Saved: 2026-08-03 20:38
Source: 2026-08-02_06-31-25Z_CallScreenBench_BenchmarkingOn_DeviceModelsasPhone.md
Model: None

---

## Summary  
CallScreenBench introduces a novel evaluation framework for on‑device language models that act as phone secretaries, measuring them not by task completion but by how the owner would endorse their proxy’s handling of an unknown call. The benchmark scores agents across five quality dimensions and reports guardedness profiles without credentials or tool use. It demonstrates that model capability correlates with performance except for triage, which is largely driven by scripted degenerate agents. No pass/fail thresholds are declared.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 5 title terms overlap; 29 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] CallScreenBench defines a novel evaluation framework for on‑device phone secretary models focusing on user endorsement rather than task completion.  
- [Finding 2] The benchmark reveals that triage performance is dominated by scripted degenerate agents, masking true model differences when those floors are corrected.  
- [Finding 3] Six quantized models (0.6–4B parameters) show quality scaling with capability, but the apparent separation in triage disappears after accounting for degenerate behavior.

## Methodology  
The authors designed CallScreenBench to simulate a phone secretary that receives an unknown call and must respond appropriately. Agents are evaluated on five dimensions: message fidelity, tone appropriateness, response brevity, privacy compliance, and user endorsement. Guardedness is measured by whether the proxy can act without credentials or tool calls. Experiments compare six on‑device models across quantization levels to assess how capability influences performance.

## Results  
Quality scores improve with model size and less quantization, confirming that capability scales with quality. However, triage scores are artificially high due to degenerate agents; after correction, no model pair shows a meaningful separation at the target operating point. All metrics have floors that defeat them, indicating no pass/fail threshold.

## Significance  
This work shifts evaluation away from task success to user perception, providing a realistic benchmark for on‑device assistants and highlighting limitations of current models in handling adversarial or uncooperative interactions. It also motivates future research into adversarial robustness and user‑centric AI design.

## Related Concepts  
On‑device language models, quantization, privacy‑preserving AI, phone secretary role, task evaluation vs user endorsement, degenerate agents, guardedness, benchmarking frameworks.
