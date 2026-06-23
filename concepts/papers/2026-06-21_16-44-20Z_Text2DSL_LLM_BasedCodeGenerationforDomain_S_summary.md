# Summary: 2026-06-21_16-44-20Z_Text2DSL_LLM_BasedCodeGenerationforDomain_Specific.md
Saved: 2026-06-22 22:01
Source: 2026-06-21_16-44-20Z_Text2DSL_LLM_BasedCodeGenerationforDomain_Specific.md
Model: None

---


## Summary  
The paper addresses the problem of generating code for domain‑specific languages (DSLs) from natural language descriptions, calling it Text2DSL, distinct from text‑to‑SQL or general code generation. It introduces PolkitBench, a dataset of 4,204 verified natural‑language to DSL rule pairs, and shows that providing formal specification context dramatically improves LLM output quality across two MoE models without fine‑tuning.  

## Key Contributions  
- [Finding 1] The authors formalise Text2DSL as a separate problem class from text‑to‑SQL and general code generation, establishing a clear research direction.  
- [Finding 2] They demonstrate that injecting structured context such as BNF grammar, API specification, and permitted identifier vocabulary into the prompt is essential for high syntactic and structural validity in DSL code generation.  
- [Finding 3] The results show that adding formal target‑language specifications raises CodeBLEU scores by up to 95% and improves structural validity by up to 35.5 percentage points across both GigaChat‑10B‑A1.8B and Nemotron‑3‑Nano‑30B‑A3B models.  

## Methodology  
The authors constructed PolkitBench, a curated dataset where each DSL rule is paired with a natural language description validated through a three‑level AST pipeline to ensure correctness. They then performed controlled prompt experiments on two mixture‑of‑experts (MoE) language models of different scale and provenance. The prompts varied only in the inclusion or exclusion of formal specification context, allowing them to measure the impact of structured information on model output.  

## Results  
Across both models, supplying context lifted syntactic validity from ~98.6% to 99.4%, structural validity by +9.7 to +35.5 percentage points, and CodeBLEU scores by +60% to +95%. These gains are consistent regardless of model scale or provenance, indicating that the effect is not tied to a specific architecture but rather to the presence of formal constraints.  

## Significance  
This work highlights that for domain‑specific code generation tasks, providing explicit target‑language specifications can be a powerful prompt engineering technique that yields state‑of‑the‑art results without retraining models. It opens avenues for automated DSL authoring in security policy management and other expert domains where manual rule writing is costly.  

## Related Concepts  
- Domain‑Specific Languages (DSLs)  
- Natural Language to Code Generation  
- Prompt Engineering  
- Mixture‑of‑Experts (MoE) Models  
- CodeBLEU  
- AST Validation
