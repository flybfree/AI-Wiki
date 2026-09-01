---
title: Lazy Grounding: Attacking Search Agents with Factual Evidence
url: http://arxiv.org/abs/2608.30303v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_06-19-04Z_LazyGrounding_AttackingSearchAgentswithFactualEvid.md
generated_at: 2026-08-31 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates a new vulnerability in search agents called lazy grounding, where factual evidence that is relevant to a nearby question but not the current one can be misapplied and cause the agent to adopt the wrong answer. Experiments on 12 model‑benchmark pairs show that such near‑evidence reduces accuracy by an average of 5.9 points and up to 17.3 points, while consistently leading agents to use answers from nearby questions.

## Key Takeaways
- Falsehood is not required for the attack; any true document that supports a neighboring rewritten question can mislead the agent when it appears for the original query.
- The effect is strongest when near‑evidence appears later in the retrieval order or has a shape resembling an answer, indicating that position and relevance matter.
- Retrieval alone cannot guarantee robustness because agents may blindly adopt nearby answers without verifying their correctness.

## Context
Search agents aim to reduce hallucinations by grounding responses with retrieved web pages. However, reliance on external corpora introduces new failure modes beyond misinformation, as demonstrated by lazy grounding. This research highlights that the safety of retrieval‑based systems depends not only on content quality but also on how evidence is integrated into answers.

## Implications
Practitioners must design defenses that detect and block the misuse of nearby factual evidence, such as adding verification steps or reordering retrieved documents. The findings push the field toward more holistic evaluation metrics that consider answer appropriateness rather than just retrieval success.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30303v1)
