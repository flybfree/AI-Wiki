# Summary: 2026-07-15_17-10-24Z_CananOldDogBeTaughtNewTricks_TakingLLMsBeyondSente.md
Saved: 2026-07-15 21:01
Source: 2026-07-15_17-10-24Z_CananOldDogBeTaughtNewTricks_TakingLLMsBeyondSente.md
Model: None

---

## Summary  
This paper investigates whether large language models can perform whole‑document translation that goes beyond the conventional sentence‑by‑sentence paradigm by leveraging a corpus of authentic bilingual texts and user‑provided specifications. The authors introduce PAT (Pragmatic Auto‑Translator), a RAG‑based system that retrieves paragraph, section, or document‑level examples from a U.S. English–Latin American Spanish corpus and feeds them to an LLM for reformulated translations aimed at professional verification. Experiments on six AI‑generative‑AI essays show that limited prompts yield little change, whereas well‑specified, corpus‑informed prompts produce substantial but not always effective reformulations. The work demonstrates a shift toward whole‑document generation while highlighting remaining challenges in translation quality and evaluation.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 12 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- **Finding 1:** PAT can generate whole‑document translations that incorporate user specifications and context from comparable bilingual corpora, moving LLM translation away from sentence‑level processing.  
- **Finding 2:** The effectiveness of reformulation depends heavily on the quality and relevance of retrieved examples; poorly matched corpus instances lead to minimal changes.  
- **Finding 3:** Evaluation using a custom MQM typology reveals that while reformulations are often meaningful, they do not always improve the target‑language discourse alignment.

## Methodology  
The authors built PAT as a Retrieval‑Augmented Generation (RAG) pipeline: user‑defined translation specifications are paired with retrieved excerpts at multiple granularities (paragraph, section, document). These examples serve as prompts to an LLM, which produces a draft translation of the entire source essay. The system was tested on six AI‑generative‑AI essays across three projects, with translations evaluated by two trained evaluators using a custom MQM typology that captures discourse organization, rhetorical style, and pragmatic norms.

## Results  
A limited prompt produced only trivial reformulations, whereas specifications combined with well‑matched corpus examples yielded substantial text changes. However, the reformulated outputs did not consistently achieve the intended alignment with Spanish‑language discourse conventions; evaluators noted gaps in idiomatic expression and structural coherence. Overall, PAT demonstrates feasibility of whole‑document translation but shows that effectiveness remains variable.

## Significance  
This research advances the design of LLM‑based translation systems by showing that corpus‑informed, whole‑document generation is possible, yet it also underscores the need for more robust evaluation methods and better alignment mechanisms to ensure pragmatic quality. The findings contribute to both academic discourse on RAG in NLP and practical considerations for professional translation workflows.

## Related Concepts  
- Retrieval‑Augmented Generation (RAG)  
- Whole‑document translation  
- Corpus‑informed prompting  
- Pragmatic alignment  
- MQM typology  
- LLM fine‑tuning vs. prompt engineering
