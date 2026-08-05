# Summary: 2026-07-29_15-20-36Z_EvaluatingRegionalBiasinLLMsFromAbstractStereotype.md
Saved: 2026-07-29 20:39
Source: 2026-07-29_15-20-36Z_EvaluatingRegionalBiasinLLMsFromAbstractStereotype.md
Model: None

---

## Summary  
This paper introduces the Stereotypes‑to‑Decisions (S2D) framework to evaluate how regional bias propagates from abstract stereotypes about Chinese provinces to concrete social judgments made by large language models. By measuring both Warmth and Competence ratings alongside paired‑choice tasks in Education, Occupation, and Social Interaction, S2D reveals systematic patterns across all 34 provincial regions. The study demonstrates that these biases are not isolated but reflect underlying economic and digital development disparities. Overall, the findings show that regional bias is pervasive, consistent with human stereotypes, and stable regardless of prompt language.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- Finding 1: Regional scores for Warmth and Competence differ markedly between provinces, indicating distinct stereotype profiles.  
- Finding 2: The same biases appear in paired‑choice tasks across Education, Occupation, and Social Interaction, linking abstract ratings to real‑world decisions.  
- Finding 3: Bias patterns remain stable when prompts are given in Chinese or English, suggesting a robust underlying mechanism.

## Methodology  
The authors collected stereotype ratings from a diverse panel of annotators for each province, measuring perceived friendliness (Warmth) and capability (Competence). Participants then completed paired‑choice tasks where they chose between two provincial candidates in three domains. The same prompts were used with six state‑of‑the‑art LLMs to generate responses that were subsequently scored by the same panel. Regional economic development indices and digital infrastructure metrics served as covariates.

## Results  
Across all models, provinces with higher GDP per capita tended to be rated more Competent but less Warmth, while low‑income regions showed the opposite pattern. The agreement between human ratings and model outputs was strong (Cohen’s κ ≈ 0.78). Notably, the bias persisted in both English and Chinese prompts, confirming that it is not a language‑specific artifact.

## Significance  
Understanding how regional stereotypes translate into concrete decisions matters for fairness in AI applications such as hiring, education placement, and social recommendation systems. If LLMs reflect these biases, they could amplify existing socioeconomic divides or misrepresent community values, raising ethical concerns about automated decision‑making tools.

## Related Concepts  
- Regional bias  
- Stereotype propagation  
- Warmth vs. Competence dimensions  
- Paired‑choice tasks  
- Economic development indicators
