---
title: Writerslogic at the CLEF 2026 SimpleText Track: Multi-Candidate LLM Simplification and Stacked Complexity Spotting
url: http://arxiv.org/abs/2610.03567v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_16-44-53Z_WriterslogicattheCLEF2026SimpleTextTrack_Multi_Can.md
generated_at: 2026-10-04 21:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper describes the Writerslogic team's submissions to the CLEF 2026 SimpleText shared task, which focuses on simplifying and identifying complexity in biomedical text drawn from Cochrane systematic reviews. The team developed two distinct approaches: a multi-candidate LLM generation pipeline for text simplification (Task 1) and a fine-tuned natural language inference model for detecting hallucinated or overgenerated content (Task 2). Their systems achieved top-ranked results in both sentence-level simplification and complexity identification tracks, demonstrating strong performance on both English and multilingual biomedical text.

## Key Takeaways
- For text simplification (Task 1), the team built a pipeline using GPT-4o-mini that generates five candidate simplifications per sentence at varying temperatures, then selects the best output using a reference-free scoring heuristic that rewards compression, source word retention, alignment with Cochrane Plain Language Summary vocabulary, and lexical simplicity. Their Claude Sonnet 4 submission achieved SARI 47.43 and BLEU 14.21, making it the top-ranked sentence-level system and third overall on the combined Task 1 leaderboard.
- For complexity spotting (Task 2), the team fine-tuned a DeBERTa-v3-large NLI model on 350,000 labeled source-sentence pairs, reframing hallucination detection as a natural language inference problem where the source sentence serves as premise and the candidate as hypothesis. This approach achieved 0.8081 document-level macro F1 on binary overgeneration identification (top-ranked in the identification track, second overall) and 0.804 multiclass accuracy on error classification (second among unique teams).
- The evaluation domain is specifically biomedical text from Cochrane systematic reviews, spanning both English and multilingual content, which grounds the work in a high-stakes domain where inaccurate or overly complex summaries can directly affect clinical decision-making and public health communication.

## Context
The CLEF SimpleText shared task sits at the intersection of NLP, biomedical informatics, and public health communication, addressing the critical challenge of making complex medical literature accessible to non-specialist audiences. This paper contributes to the broader research landscape on controllable text generation and hallucination detection in domain-specific settings, where generic LLM outputs frequently introduce inaccuracies or fail to preserve the precise meaning of source material. The use of NLI framing for complexity spotting represents a methodologically interesting transfer from a well-established NLP task to the practical problem of identifying when simplified text has introduced unsupported or erroneous content.

## Implications
For practitioners in medical communication and health informatics, these results demonstrate that carefully engineered multi-candidate generation pipelines combined with domain-specific scoring heuristics can outperform naive single-pass LLM simplification, offering a practical blueprint for deploying trustworthy text simplification in clinical and public health settings. The NLI-based approach to hallucination detection suggests that fine-tuned transformer models can serve as reliable automated quality gates for simplified biomedical content, reducing the need for expensive human review. For the broader AI community, the paper highlights the importance of task-specific evaluation metrics like SARI and Cochrane-aligned vocabulary scoring over generic BLEU scores, pushing the field toward more meaningful assessment of simplification quality in specialized domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03567v1)
