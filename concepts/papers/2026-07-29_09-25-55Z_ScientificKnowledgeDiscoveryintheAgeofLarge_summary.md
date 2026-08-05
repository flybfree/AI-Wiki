# Summary: 2026-07-29_09-25-55Z_ScientificKnowledgeDiscoveryintheAgeofLargeLanguag.md
Saved: 2026-07-29 20:31
Source: 2026-07-29_09-25-55Z_ScientificKnowledgeDiscoveryintheAgeofLargeLanguag.md
Model: None

---

## Summary  
The paper surveys 34 peer‑reviewed papers that apply generative large language models (LLMs) to scientific literature retrieval and eligibility screening, aiming to map the state of LLM applications in this domain. It provides a systematic classification based on model type, access, prompting strategies, ground‑truth sources, and evaluation metrics. By analyzing these studies, the authors highlight both progress and open challenges in leveraging LLMs for knowledge discovery.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 5 backlinks; 6 summary/topic terms overlap
- [[concepts/2026-07-27_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-07-27]] — 4 title terms overlap; 3 backlinks; 4 summary/topic terms overlap
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]] — 2 title terms overlap; 484 backlinks; 5 summary/topic terms overlap

## Key Contributions  
- Identifies 34 peer‑reviewed papers applying generative LLMs to literature retrieval and eligibility screening.  
- Classifies these studies by model type, access, prompting techniques, ground‑truth sources, and evaluation metrics.  
- Highlights gaps in current research, such as limited benchmarking of LLM performance on scientific tasks.

## Methodology  
The authors performed a Boolean search across the OpenAIRE Graph, filtering 1,589 records down to 34 relevant papers. They extracted metadata for each study, including LLM model used (e.g., GPT‑4, Llama), whether it was fine‑tuned or prompted, prompting strategy (zero‑shot vs few‑shot), source of ground truth (manual annotation, external datasets), and evaluation metrics (precision, recall, F1). This systematic extraction enabled a comparative analysis.

## Results  
The survey reveals that most studies employ zero‑shot prompting with large models like GPT‑4, achieving high precision but variable recall. Fine‑tuned or instruction‑tuned LLMs show modest gains in recall but require more compute and data. Evaluation is often limited to internal validation; few papers report public benchmark scores. The authors note a trend toward using LLM outputs for eligibility criteria screening rather than pure retrieval.

## Significance  
This systematic mapping clarifies the current state of LLM applications in scientific knowledge discovery, helping researchers avoid redundant work and focus on promising techniques. It also underscores the need for standardized evaluation protocols to enable fair comparison across studies.

## Related Concepts  
- Generative large language models (LLMs)  
- Literature retrieval  
- Eligibility screening  
- Prompting strategies (zero‑shot, few‑shot)  
- Fine‑tuning and instruction tuning  
- OpenAIRE Graph as a scholarly record repository
