# Summary: 2026-08-07_14-07-57Z_ArtificialIntelligenceCanMatchDomainExpertsinEvide.md
Saved: 2026-08-09 23:01
Source: 2026-08-07_14-07-57Z_ArtificialIntelligenceCanMatchDomainExpertsinEvide.md
Model: None

---

## Summary  
This paper demonstrates that large language models (LLMs) can perform evidence extraction and critical appraisal of microbial oncogenesis research papers with performance comparable to human domain experts, using a benchmark dataset created by expert consensus on 24 studies. The study evaluates four state-of-the-art LLMs—GPT-5, GPT-5 Nano, Gemini 2.5 Pro, and Gemini 2.5 Flash—across structured question types including multiple-choice, Likert-scale, multi-select, and free-text responses. Across all evaluation tasks, LLM outputs aligned closely with human expert consensus, particularly for GPT-5 and GPT-5 Nano, which showed score distributions indistinguishable from experts. The findings suggest that LLMs are viable tools for scalable, expert-level systematic evidence synthesis in microbial oncology research.

## Key Contributions  
- [Finding 1] LLM responses on structured evidence extraction and appraisal tasks closely match those of human domain experts, with GPT-5 and GPT-5 Nano achieving performance indistinguishable from humans.  
- [Finding 2] Gemini models, while performing similarly, were more lenient in applying microbial oncogenesis criteria, indicating potential for overgeneralization or criterion misapplication.  
- [Finding 3] Methodological appraisal and contradiction identification within full-texts remain persistent weaknesses in LLM performance, highlighting remaining limitations despite overall strong results.

## Methodology  
The authors recruited domain experts to create a benchmark dataset of 24 research papers on microbial oncogenesis using MMTV-LV and breast cancer as case studies. A structured template with 77 items across multiple question types (MCQ, Likert-scale, multi-select, free-text) was developed to assess evidence extraction and critical appraisal. The LLM responses were compared to expert consensus per question instance using novel metrics that measure agreement distributions between experts and LLMs. Free-text responses were qualitatively evaluated for consistency with expert views.

## Results  
Across all 24 papers and 77 questions, LLM performance on structured tasks closely mirrored human experts, particularly GPT-5 and GPT-5 Nano. Inter-expert agreement was maintained or increased when comparing LLMs to human consensus, suggesting they functioned as additional expert-like evaluators. Gemini models showed similar alignment but exhibited greater leniency in applying criteria, potentially leading to overinclusive results. Hallucinations were rare. However, LLM performance declined on tasks involving methodological appraisal and contradiction detection within full-texts, which remain critical for rigorous evidence synthesis.

## Significance  
This study provides strong empirical support for the use of LLMs as scalable tools in systematic evidence synthesis, particularly in complex biomedical domains like microbial oncogenesis. By matching or exceeding human expert performance on structured evaluation tasks, LLMs can accelerate research discovery and reduce bias in literature review. However, the persistent weaknesses in full-text appraisal and contradiction identification underscore the need for continued refinement to ensure reliability in high-stakes scientific applications.

## Related Concepts  
- Large Language Models (LLMs)  
- Systematic evidence synthesis  
- Microbial oncogenesis  
- Human-in-the-loop evaluation  
- Inter-expert agreement metrics  
- Hallucination detection  
- Methodological appraisal  
- Free-text response quality control
