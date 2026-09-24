---
title: How Much Were You Told? Measuring External Information in Peer Reviews
url: http://arxiv.org/abs/2609.28041v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_13-01-00Z_HowMuchWereYouTold_MeasuringExternalInformationinP.md
generated_at: 2026-09-23 22:12
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper introduces "Self-Conditioning," a novel, unsupervised information-theoretic estimator designed to measure how much external information is present in peer reviews compared to what is derived from the reviewed paper itself. Unlike current Artificial Text Detection (ATD) methods that focus on surface-level stylistic patterns, this approach specifically targets the origin of content to distinguish between human-polished reviews and those where an LLM has been delegated to generate the critique.

## Key Takeaways
- Current AI detection methods are insufficient because they primarily measure linguistic "surface form" rather than the source of information; consequently, they struggle to differentiate between a reviewer using an LLM for grammar polishing and one who allows an LLM to provide the actual content of the review.
- The proposed Self-Conditioning method works by comparing the likelihood of a review's production under its original context with its likelihood when that context is augmented with "hints" extracted from the review itself, effectively quantifying the amount of external information injected by a generator.
- Evaluation on the IntelLabs peer-review benchmark demonstrated that this estimator can achieve an AUC of up to 1.0 in distinguishing fully-delegated AI reviews from machine-polished ones while remaining largely unaffected by surface-level rewriting or stylistic changes.

## Context
As Large Language Models become increasingly capable of generating coherent, domain-specific text, the integrity of the peer review process—a cornerstone of scientific progress—is under threat from potential AI-generated critiques. This research matters because it shifts the focus of AI detection from "style" to "content provenance," providing a more robust way to evaluate the authenticity of human-led academic contributions.

## Implications
For researchers and publishers, this provides a much more reliable metric for ensuring that peer reviews are based on human expertise rather than external information provided by an LLM. By moving toward information-theoretic measurements, the field can develop tools that remain effective even as AI models become better at mimicking human writing styles and avoiding traditional detection filters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.28041v1)
