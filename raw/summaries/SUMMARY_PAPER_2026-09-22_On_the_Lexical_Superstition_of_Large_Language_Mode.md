---
title: On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality
url: http://arxiv.org/abs/2609.26388v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-22_13-27-57Z_OntheLexicalSuperstitionofLargeLanguageModelsforCo.md
generated_at: 2026-09-22 20:13
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research investigates whether Large Language Models (LLMs) rely disproportionately on identifier names rather than actual program structure when performing code comprehension tasks. By introducing a framework called Face/Off, which allows for systematic, semantics-preserving renaming of variables, the authors demonstrate that LLMs exhibit a pervasive "lexical superstition" where performance significantly degrades as variable names become less informative or intentionally misleading.

## Key Takeaways
- The researchers introduced the Face/Off framework to evaluate how different levels of identifier information—ranging from highly descriptive to completely misleading—impact model performance across multiple code comprehension tasks and various LLM architectures.
- The study reveals that LLMs consistently prioritize lexical cues over structural logic; when variable names are changed to be misleading, the models' outputs often align with the incorrect meanings suggested by the names rather than the actual execution flow of the code.
- Experimental evidence shows that this tendency toward lexical overemphasis persists even after applying various prompt engineering techniques and fine-tuning interventions, suggesting that the bias is deeply entrenched in current model training paradigms.
- A control experiment involving type inference revealed a clear boundary: naming effects are significantly smaller when the correct answer can be locally recovered without any identifier information, confirming that LLMs struggle to balance lexical cues against formal code semantics.

## Context
As Large Language Models become increasingly integrated into software development for tasks like automated debugging and code explanation, understanding the reliability of their reasoning is paramount. This paper matters because it identifies a fundamental flaw in how models interpret human-written code, revealing that they may be "hallucinating" logic based on superficial naming conventions rather than performing true semantic analysis.

## Implications
For software engineers and AI researchers, these findings suggest that current LLM outputs for complex code comprehension cannot be fully trusted when variable names are ambiguous or poorly chosen. The research highlights a critical need to develop evaluation metrics and training methodologies that prioritize formal code semantics over linguistic patterns to ensure more reliable and robust AI-assisted software engineering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.26388v1)
