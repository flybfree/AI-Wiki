# Summary: 2026-07-25_19-05-29Z_AlloBench_MeasuringOnlineToolAllocationCapabilityi.md
Saved: 2026-07-27 20:14
Source: 2026-07-25_19-05-29Z_AlloBench_MeasuringOnlineToolAllocationCapabilityi.md
Model: None

---

## Summary  
The paper introduces **AlloBench**, a paired benchmark designed to measure how LLM agents allocate online tools under a fixed budget, testing both an abstract text‑based formulation and a code‑construction task. It demonstrates that frontier models such as Claude Haiku, Claude Opus, GPT‑5.4‑mini, and GPT‑5.6 Sol perform near‑optimally in the abstract allocation but fail to transfer this ability to script writing. The authors also uncover specific failure modes for each model and note an open‑source Qwen model that generalizes across lexical variations yet shows no improvement at script allocation. These findings reveal online tool allocation as a distinct capability boundary even among modern frontier models.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- **Finding 1:** Frontier models act near‑optimally in the abstract framing but fail to transfer this ability to script‑writing.  
- **Finding 2:** The first three models (Claude Haiku, Claude Opus, GPT‑5.4‑mini) fail even when scripts are not evaluated; GPT‑5.6 Sol remains selective only until full construction is required.  
- **Finding 3:** An open‑source Qwen model trained for abstract allocation generalizes across held‑out lexical variations but sees no improvement at script allocation.

## Methodology  
The authors constructed a paired benchmark with two contexts: an abstract text formulation where agents choose among reusable tools given a budget, and a code‑construction task requiring actual script generation. Agents are evaluated on both tasks under the same fixed budget constraint. For the Qwen model, they also introduced lexical variations in the input to test generalization.

## Results  
All tested frontier models achieve high scores in abstract allocation, indicating conscious tool selection when only reuse is considered. However, performance drops sharply in script construction: the first three models collapse early even without evaluation of scripts, while GPT‑5.6 Sol stays selective until it must fully build the code. The Qwen model’s policy training yields consistent abstract scores across lexical variations but no boost at the script level.

## Significance  
These results establish online tool allocation as a significant capability boundary for LLMs, informing design strategies that balance immediate cost against long‑term reuse. They also highlight that current models excel at abstract planning yet lack robust execution of concrete, evaluated tasks—a gap that could limit real‑world deployment of autonomous agents.

## Related Concepts  
- Tool allocation under budget constraints  
- Reusable vs. one‑off tools  
- LLM reasoning and planning  
- Frontiers models (Claude Haiku, Claude Opus, GPT‑5 series)  
- Policy training for Qwen  
- Lexical variation generalization  
- Offline versus online evaluation
