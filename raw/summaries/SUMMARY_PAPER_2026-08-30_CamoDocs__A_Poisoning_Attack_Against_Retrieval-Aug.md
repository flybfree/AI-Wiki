---
title: CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents
url: http://arxiv.org/abs/2608.28389v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_14-44-28Z_CamoDocs_APoisoningAttackAgainstRetrieval_Augmente.md
generated_at: 2026-08-30 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CamoDocs, a poisoning attack that embeds adversarial content within benign documents to deceive retrieval-augmented generation systems without using query inclusion. Experiments show high average success rates across multiple defenses and models while keeping readability acceptable. This demonstrates the effectiveness of camouflaged poisoning.

## Key Takeaways
- The attack replaces selected tokens in benign chunks with dispersion tokens, spreading poisoned embeddings without altering surface text.
- Coherence filtering is applied to limit noticeable degradation, preserving overall document fluency.
- CamoDocs achieves strong average success rates on seven RAG defenses and three open-weight LLMs while avoiding query-overlap artifacts.

## Context
Retrieval-augmented generation (RAG) combines large language models with external documents to improve answer quality. However, the reliance on public or editable sources makes these systems vulnerable to poisoning attacks that manipulate retrieved content. CamoDocs addresses this vulnerability by embedding malicious information covertly within seemingly benign material.

## Implications
This research highlights a critical security gap in RAG implementations and suggests that defenses must consider both lexical and embedding-space artifacts. Practitioners should adopt robust filtering strategies that balance utility with readability to mitigate such attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28389v1)
