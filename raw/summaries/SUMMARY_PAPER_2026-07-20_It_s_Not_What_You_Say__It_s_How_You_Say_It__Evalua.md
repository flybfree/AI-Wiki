---
title: It's Not What You Say, It's How You Say It: Evaluating LLM Responses to Expressions of Belief
url: http://arxiv.org/abs/2607.18232v1
type: paper-summary
date: 2026-07-20
source_paper: 2026-07-20_17-58-31Z_It_sNotWhatYouSay_It_sHowYouSayIt_EvaluatingLLMRes.md
generated_at: 2026-07-20 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the linguistic form of users' expressions of belief (EoBs) influences whether large language models follow contextual knowledge or rely on their stored world knowledge. By creating a typology that spans four dimensions — form, evidentiality, epistemic stance, and tone — the authors identify 17 fine‑grained types of EoBs and test them across 16 LLMs differing in architecture, scale, and training stage. The study finds systematic patterns: larger models and instruction‑tuned variants are less context‑focused, while specific linguistic cues can strongly steer model behavior.

## Key Takeaways
- Bigger models with 30 B parameters show a marked drop in context adherence compared to smaller (1 B) models.  
- Instruction‑tuned LLMs follow user beliefs less reliably than base models trained on raw data.  
- Expressions that combine “I think” with explicit certainty markers (e.g., “definitely”) statistically boost the model’s propensity to treat the belief as true.

## Context
Current LLM systems often treat user statements as factual, which can lead to inappropriate responses when users merely express uncertainty or hedging. This research highlights a nuance that linguistic framing matters far beyond simple keyword matching, affecting how models integrate new information with prior knowledge.

## Implications
For developers and practitioners, the findings suggest that prompt design should account for the subtle cues in user statements rather than relying solely on explicit instructions. Understanding these patterns can improve model robustness and reduce misinterpretations in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18232v1)
