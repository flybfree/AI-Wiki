# Summary: 2026-07-24_14-12-54Z_Cross_TokenizerOn_PolicyDistillationviaByte_Prefix.md
Saved: 2026-07-26 21:51
Source: 2026-07-24_14-12-54Z_Cross_TokenizerOn_PolicyDistillationviaByte_Prefix.md
Model: None

---

## Summary  
The paper proposes Byte‑Prefix Marginalization (BPM) for cross‑tokenizer on‑policy distillation, aiming to consolidate open‑weight language models from different families into a compact student while preserving token‑level probability mass. BPM re‑expresses teacher next‑token distributions over the student vocabulary using a shared byte space, ensuring that each teacher token’s mass is assigned to the longest matching student prefix and unmatched mass goes to an explicit residual bucket. This yields a vocabulary‑complete, byte‑aligned target that recovers the marginal at >99 % of positions or provides a lower bound otherwise. The method improves six math/programming benchmarks by 3.7–6.6 points over strong baselines.  

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 10 summary/topic terms overlap
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 12 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 13 summary/topic terms overlap

## Key Contributions  
- Finding 1: BPM creates a mass‑preserving, chain‑factorized lower bound for teacher distributions that span multiple tokens.  
- Finding 2: It assigns teacher token probabilities to the longest student prefix in a shared byte representation, aggregating mass per student token and handling unmatched mass explicitly.  
- Finding 3: Empirically, BPM yields higher performance than prior cross‑tokenizer distillation methods on six benchmarks.  

## Methodology  
The authors decompose teacher token sequences into bytes using a fixed‑width encoding. For each teacher token they compute the longest student token whose byte prefix matches; that token receives the full probability mass. If no exact match exists, unmatched mass is accumulated in a residual category. This mapping is applied across all positions to form a dense target distribution for on‑policy distillation. The construction ensures that the target recovers the teacher’s next‑token marginal when the relevant prefix does not cross token boundaries; otherwise it provides a conservative lower bound via chain factorization.  

## Results  
Experiments with teachers Qwen3‑32B, GLM‑Z1‑9B‑0414, MiniMax‑M2.7 and student models on six math/programming tasks (e.g., MATH, HumanEval) show BPM improves average benchmark score by 3.7–6.6 points relative to the strongest baselines, outperforming all prior cross‑tokenizer OPD approaches.  

## Significance  
By enabling true vocabulary completeness and mass preservation across tokenizers, BPM advances on‑policy distillation for open‑weight models, reducing size and computational cost while maintaining or improving performance—critical for efficient model consolidation in large language systems.  

## Related Concepts  
On‑policy distillation, cross‑tokenizer methods, byte‑prefix marginalization, chain factorization, residual category, token‑level probability mass preservation.
