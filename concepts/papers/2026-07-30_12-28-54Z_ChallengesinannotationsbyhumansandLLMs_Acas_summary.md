# Summary: 2026-07-30_12-28-54Z_ChallengesinannotationsbyhumansandLLMs_Acasestudyo.md
Saved: 2026-07-30 20:36
Source: 2026-07-30_12-28-54Z_ChallengesinannotationsbyhumansandLLMs_Acasestudyo.md
Model: None

---

## Summary  
The paper investigates whether humans and large language models (LLMs) encounter comparable difficulties when annotating evaluative language, a task that is especially challenging because it relies on the subjective Appraisal theory framework. It focuses on the Attitude subsystem of this theory, which includes three appraisal classes: Affect, Judgement, and Appreciation. By analysing sentence‑level annotations from English TED‑talk transcripts, the authors compare human‑made labels with those produced by LLMs to assess their alignment. The study aims to demonstrate that LLMs can resolve complex annotation problems more effectively than even trained linguists in certain contexts.

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 - Large Language Models: The Modern AI Interface]] — 4 title terms overlap; 54 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- **Finding 1:** The best‑performing LLM, after fine‑tuning on a prompt for Appraisal classification, achieves an F1‑score of 0.77, which exceeds the performance of human annotations produced by a trained linguist.  
- **Finding 2:** Three different prompting strategies were tested; only one yielded the highest accuracy, indicating that prompt design is crucial for LLM annotation tasks.  
- **Finding 3:** Linguists in training (students) show low agreement scores across the three appraisal classes, suggesting they struggle with the same subjective judgments that LLMs handle more reliably.

## Methodology  
The authors selected a corpus of English TED‑talk transcripts and applied Appraisal theory’s Attitude subsystem to extract Affect, Judgement, and Appreciation labels. They performed manual sentence‑level annotation by a trained linguist and generated model predictions using three distinct prompts. After selecting the prompt that produced the highest accuracy, they fine‑tuned the corresponding LLM on this task data before evaluating its performance against both human and in‑training linguist annotations.

## Results  
The fine‑tuned LLM reached an F1‑score of 0.77, outperforming the trained linguist’s annotation agreement (average < 0.5). The model also demonstrated higher consistency across appraisal classes than the human annotators, whose inter‑annotator agreement was low. These results confirm that LLMs can surpass human annotators in this specific evaluative language task.

## Significance  
This work opens new pathways for annotating complex theoretical frameworks in digital humanities, where subjective judgments are central. By leveraging LLMs, researchers can obtain more reliable and scalable annotations, reducing reliance on limited expert labor and enabling deeper quantitative analysis of discourse phenomena.

## Related Concepts  
Appraisal theory, Attitude subsystem, Affect, Judgement, Appreciation, Large language models (LLMs), fine‑tuning, F1‑score, digital humanities, sentence‑level annotation.
