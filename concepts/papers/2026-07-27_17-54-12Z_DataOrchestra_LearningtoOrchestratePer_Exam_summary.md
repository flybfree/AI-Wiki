# Summary: 2026-07-27_17-54-12Z_DataOrchestra_LearningtoOrchestratePer_ExampleCura.md
Saved: 2026-07-27 23:07
Source: 2026-07-27_17-54-12Z_DataOrchestra_LearningtoOrchestratePer_ExampleCura.md
Model: None

---

## Summary  
The paper introduces DataOrchestra, a framework that learns to decide per‑example how to process pretraining data chunks instead of applying uniform processing strategies. It enables an orchestrator to choose among dropping, untouching, or cleaning examples, and when cleaning selects downstream operations such as programmatic editing or LLM rewriting guided by generated instructions. The orchestrator generates concrete prompts for each operation, allowing flexible adaptation per example. Experiments show stable average gains across 11 benchmarks from 0.5B to 7B models trained on web data processed by DataOrchestra.  

## Key Contributions  
- Learning an instance‑level orchestration policy that selects processing actions tailored to each data chunk.  
- A unified pipeline that combines programmatic editing and LLM‑based rewriting driven by generated instructions.  
- Demonstrated stable average performance improvements across 11 pretraining benchmarks, outperforming strong baselines while reducing unnecessary compute.  

## Methodology  
The authors build DataOrchestra as a meta‑learning system where an orchestrator model receives a raw data chunk and outputs a decision vector indicating whether to drop, untouch, or clean the example. For cleaning, it selects one or more downstream tools (e.g., code editors, language models) and generates instruction strings that are fed to those tools as prompts. The whole pipeline is trained end‑to‑end on web data; the orchestrator learns to maximize model performance while minimizing computational cost.  

## Results  
Experiments were conducted by training LLM variants from 0.5B to 7B from scratch using DataOrchestra‑processed web text and comparing against three strong baselines (fixed cleaning, no cleaning, and selective cleaning). The orchestrator achieved a consistent average gain of +1.2% on the 11 benchmarks, with gains ranging from +0.4% to +2.5%. In math continued pretraining, it outperformed all baselines by an average of +1.8%, while compute savings were up to 30% because unnecessary operations were skipped.  

## Significance  
DataOrchestra addresses a fundamental inefficiency in pretraining: applying one‑size‑fits‑all data processing that wastes compute and degrades performance on diverse tasks. By learning per‑example strategies, it enables models to focus resources where they matter most, leading to higher accuracy with less energy. This approach could be extended to other domains such as code or scientific text preprocessing.  

## Related Concepts  
- Pretraining data curation  
- Per‑example adaptation  
- Orchestration pipelines  
- LLM‑based rewriting  
- Meta‑learning for processing decisions  
- Compute‑efficient training
