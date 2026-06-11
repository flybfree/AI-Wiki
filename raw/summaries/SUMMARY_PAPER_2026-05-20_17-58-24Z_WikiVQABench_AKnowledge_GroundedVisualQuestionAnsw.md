---
title: WikiVQABench: A Knowledge-Grounded Visual Question Answering Benchmark from Wikipedia and Wikidata
url: http://arxiv.org/abs/2605.21479v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-20_17-58-24Z_WikiVQABench_AKnowledge_GroundedVisualQuestionAnsw.md
generated_at: 2026-06-11 10:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces WikiVQABench, a knowledge‑grounded Visual Question Answering benchmark that combines Wikipedia images with external Wikidata facts to evaluate models on reasoning beyond visual perception. The dataset includes human‑curated multiple‑choice questions where correct answers require external knowledge, and evaluation of fifteen VLMs shows performance ranging from 24.7% to 75.6% accuracy.

## Key Takeaways
- WikiVQABench creates a benchmark that forces models to integrate textual captions and structured Wikidata data, moving beyond purely image‑based VQA tasks.  
- The human review pipeline ensures factual correctness and visual‑text consistency, guaranteeing that each question truly demands external knowledge for the correct answer.  
- Performance gaps across model sizes (256M to 90B parameters) highlight how knowledge‑intensive reasoning can be a limiting factor for large language models.

## Context
Current VQA benchmarks often focus on tasks solvable from visual content alone, overlooking real‑world scenarios where external facts are essential. This paper addresses that gap by demonstrating the importance of grounding vision‑language models in reliable knowledge bases like Wikidata.

## Implications
For researchers, WikiVQABench provides a standardized way to measure and improve knowledge integration in multimodal systems. For industry practitioners, it signals that successful VQA applications must balance perception with factual reasoning, guiding product development toward more robust, trustworthy AI solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.21479v1)
