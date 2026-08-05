# Summary: 2026-07-30_11-53-43Z_DistillingAnswerSetProgrammingTheoriesfromLargeLan.md
Saved: 2026-07-30 20:35
Source: 2026-07-30_11-53-43Z_DistillingAnswerSetProgrammingTheoriesfromLargeLan.md
Model: None

---

## Summary  
The paper proposes a neurosymbolic framework that lets large language models (LLMs) automatically generate complete and correct Answer Set Programming (ASP) theories from scratch within a one‑hour time limit. By using a fixed agent harness with a solver in the loop, the authors test whether LLMs can distill theories without any external specification. The study is dataset‑agnostic: starting from an empty file and a single prompt, models must produce a full theory for VQA benchmarks. Results show that several frontier models achieve high accuracy on CLEVR and GQA, while GPT‑5 performs poorly on GQA.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 4 title terms overlap; 121 backlinks; 13 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 4 title terms overlap; 17 backlinks; 11 summary/topic terms overlap
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap

## Key Contributions  
- Finding 1 The authors demonstrate that state‑of‑the‑art LLMs can produce complete ASP theories from a minimal prompt, indicating that symbolic reasoning can be distilled into language generation.  
- Finding 2 The performance gap between models is not solely due to model size; fine‑tuning with handwritten reference theories only modestly improves accuracy but can degrade GPT‑5’s results, suggesting that external references are not always beneficial.  
- Finding 3 The dataset‑agnostic protocol reveals that the ability to generate correct ASP theories depends on prompt design and solver interaction rather than just model scale.

## Methodology  
The methodology follows a closed‑loop neurosymbolic pipeline: (1) an empty ASP file is created, (2) the LLM receives a single prompt asking it to write a complete theory within one hour, (3) the generated code is fed back to a solver for verification. The protocol uses three VQA benchmarks—CLEVR, GQA, and CLEVRER—to evaluate both correctness and completeness. Nine models spanning frontier, mid‑tier, and open‑weights are run under identical conditions.

## Results  
Frontier models (Claude Sonnet 4.6, Claude Opus 4.7, GPT‑5, DeepSeek V4 Pro) achieve 100 % on CLEVR and 92.8–98.8 % on GQA; on CLEVRER they score 92.7–95.3 %. Adding handwritten reference theories nudges the other three frontier models by at most ±3.4 pp but reduces GPT‑5’s accuracy by 3–19 pp. The open‑weights models vary between 80 % and 96 % across tasks.

## Significance  
This work shows that LLMs can autonomously generate correct symbolic programs, opening a path to neuro‑symbolic AI where reasoning is embedded in language generation rather than separate modules. It also highlights the importance of prompt engineering and solver feedback for reliable theory distillation.

## Related Concepts  
Answer Set Programming (ASP), neurosymbolic integration, large language model prompting, theorem extraction, VQA benchmarks, model scaling, symbolic verification.
