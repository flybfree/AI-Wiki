---
title: "Summary: Implicit Representations of Grammaticality in Language Models"
date: 2026-05-06
tags: ['paper', 'research', 'ai']
---
# Summary: Implicit Representations of Grammaticality in Language Models


**Source**: [Original Paper](http://arxiv.org/abs/2605.05197v1)
Saved: 2026-05-07 22:08
Source: 2026-05-06_17-57-31Z_ImplicitRepresentationsofGrammaticalityinLanguageM.md

---

## Summary
This paper asks whether language models encode grammaticality in a way that is distinct from simple string probability. The authors train a linear probe on grammatical sentences and synthetic ungrammatical perturbations, then evaluate it on human-curated grammaticality benchmarks and cross-lingual tests. The probe generalizes well to grammaticality judgments and often outperforms LM probability-based scoring, while performing worse on semantic plausibility tasks where both sentences are grammatical.

## Key Takeaways
- Hidden states can support a grammaticality signal beyond next-token likelihood.
- Linear probes can outperform raw LM probabilities on grammaticality judgments.
- The same probe is less useful for semantic plausibility, where probability remains stronger.

## Context
The study uses perturbations of naturalistic text to create training data for a grammaticality classifier. It also examines how well an English-trained probe transfers across languages.

## Implications
The results suggest that grammatical knowledge is at least partially represented internally in LMs rather than only in output probabilities. This has implications for interpretability and for using probes as diagnostic tools.

## Original Reference
- Title: Implicit Representations of Grammaticality in Language Models
- Authors: Yingshan Susan Wang, Linlu Qiu, Zhaofeng Wu, Roger P. Levy, Yoon Kim
- Published: 2026-05-06T17:57:31Z
- URL: http://arxiv.org/abs/2605.05197v1
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-05-06_17-57-31Z_ImplicitRepresentationsofGrammaticalityinLanguageM.md

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/software-development/software-development-hub.md|Software Development Hub]]
- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
