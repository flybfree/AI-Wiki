---
title: When Auditors Fabricate: Batch-Size Degradation and Confident Hallucination in LLM Detection of Planted Document Contamination
url: http://arxiv.org/abs/2609.09696v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_04-29-45Z_WhenAuditorsFabricate_Batch_SizeDegradationandConf.md
generated_at: 2026-09-09 20:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language model detectors degrade when faced with a batch of contaminated academic documents, finding that detection confidence drops sharply at larger batch sizes and the model begins to fabricate false contaminant reports instead of abstaining. It shows recovery rates of 50% on single documents, 60% on small batches, and only 2.8% on large batches, with fabricated entries such as "telepathic squirrel" appearing confidently.

## Key Takeaways
- Detection collapses at scale: the model moves from partial recovery to generating entirely invented contaminants like "quantum-powered toaster", indicating a shift from omission to false reporting.
- Absurd insertions are recovered more reliably (75%) than semantic reversals or typographical corruptions, which remain at 50% each, suggesting type of corruption influences detection quality.
- The authors recommend bounded batch sizes, direct content injection, and mechanical verification to prevent deceptive failures.

## Context
This study highlights a critical gap in automated audit systems where LLMs are used as quality checkers; their performance is not monotonic with input size but deteriorates, raising concerns about trust in AI-generated audit reports. The findings underscore the need for rigorous evaluation protocols that account for batch dynamics and hallucination risks.

## Implications
For industry practitioners relying on LLM auditors, these results warn against deploying models at large scales without safeguards, as they may produce misleading evidence that could mislead decision‑making processes. Practitioners must implement verification layers to confirm every claim against the original source text.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09696v1)
