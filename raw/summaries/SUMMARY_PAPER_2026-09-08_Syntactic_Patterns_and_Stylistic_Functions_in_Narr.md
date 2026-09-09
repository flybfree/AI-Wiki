---
title: Syntactic Patterns and Stylistic Functions in Narrative Prose: A Rule-Based and Machine-Learning Approach
url: http://arxiv.org/abs/2609.07651v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_15-39-53Z_SyntacticPatternsandStylisticFunctionsinNarrativeP.md
generated_at: 2026-09-08 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how syntactic structure influences stylistic functions in narrative prose by linking dependency‑parsed sentence patterns to five style categories using a rule‑based method and machine learning. The best model reaches a macro‑F1 of 0.948, demonstrating that compact syntactic profiles can reliably predict narrative tone.

## Key Takeaways
- A transparent rule‑based pipeline extracts lemmas, universal POS tags, and dependency relations to build linearised triples that serve as input features for style classification.  
- The experimental corpus comprises 3,300 sentences, each assigned one of five stylistic labels—descriptive, introspective, causal, ideological, or neutral—allowing a clear quantitative link between grammar and meaning.  
- A machine‑learning classifier trained on these patterns achieves high performance (macro‑F1 = 0.948) across 10‑fold cross‑validation, confirming the predictive power of syntactic representation.

## Context
This work contributes to AI research by providing a reproducible workflow that bridges natural language processing and stylistic analysis, using open‑source tools to automate the extraction of grammatical cues. It highlights how rule‑based linguistic features can be combined with standard classifiers to improve interpretability in text generation tasks.

## Implications
For practitioners developing narrative generators, this study suggests that explicit syntactic modeling can enhance style consistency without sacrificing performance. The approach offers a scalable method for integrating grammar into AI systems, fostering more human‑like storytelling and enabling fine‑tuned content creation across industries such as media and education.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07651v1)
