---
title: Guiding Language Models to Be More Empathetic: Culturally Sensitive Mental Health Advice Generation Through Human-LLM Collaboration
url: http://arxiv.org/abs/2607.23538v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_08-27-19Z_GuidingLanguageModelstoBeMoreEmpathetic_Culturally.md
generated_at: 2026-07-27 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper seeks to guide large language models toward generating empathetic mental‑health counseling advice that respects cultural contexts, focusing on low‑resource languages. By curating 625 authentic cases and evaluating responses from GPT‑4o Mini, Claude 4.5 Haiku, and Gemini 2.5 Pro, the authors demonstrate that their Role‑Playing Reflective Chain‑of‑Thought Advisory Framework (RP‑RCAF) consistently outperforms conventional prompting across all models.

## Key Takeaways
- The dataset combines publicly available Facebook posts, transcripts from the Bangladeshi TV program “Ami Akhon Ki Korbo,” and anonymized student questionnaire responses to capture a wide range of emotional and psychological challenges.  
- RP‑RCAF integrates expert‑authored few‑shot examples with structured self‑reflection, enabling a compassionate advisor persona that produces supportive counseling tailored to cultural norms.  
- The Grok 4‑Based Response Evaluation and Scoring Framework (G‑REFS) couples automated scoring with psychologist validation across emotional sensitivity, cultural appropriateness, linguistic clarity, and ethical soundness.

## Context
Current large language model research often overlooks the nuances of mental‑health advice in languages spoken by fewer than 10 million people. This work fills that gap by showing how human‑in‑the‑loop prompting can produce responses that are both empathetic and culturally appropriate, a step toward responsible AI deployment.

## Implications
The findings suggest that industry practitioners should adopt task‑specific frameworks like RP‑RCAF to improve mental‑health LLM outputs in underserved regions. By aligning automated evaluation with expert validation, developers can mitigate bias and ensure ethical counseling practices across diverse populations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23538v1)
