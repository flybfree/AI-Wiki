---
title: Before the Arrest: Benchmarking LLMs on Criminal Profiling from Incomplete Evidence
url: http://arxiv.org/abs/2609.19965v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-17_09-38-22Z_BeforetheArrest_BenchmarkingLLMsonCriminalProfilin.md
generated_at: 2026-09-17 21:13
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This research introduces the Profiling, Investigation, and Judgment (PIJ) benchmark, a novel framework designed to evaluate how Large Language Models (LLMs) perform in pre-arrest criminal profiling based on incomplete evidence. The study reveals that while LLMs can handle basic information extraction, their performance significantly degrades when required to perform complex abductive reasoning, leading to substantial gaps between AI outputs and human expert judgments regarding suspect characteristics and motives.

## Key Takeaways
- The researchers developed a comprehensive dataset consisting of 2,500 real homicide cases from five different countries to evaluate the full criminal investigation pipeline across three specific tasks: criminal profiling, crime process reconstruction, and sentence prediction.
- Evaluation results demonstrate a systematic performance drop as tasks transition from explicit fact extraction (which LLMs handle relatively well) to implicit reasoning over unknown suspect profiles, particularly in identifying victim-offender relationships.
- The study identifies significant limitations in current models regarding bias; even when tasked with inference, LLMs frequently exhibit pervasive biases in gender, age, and motive attribution compared to human experts.

## Context
While the application of AI in legal systems is growing, existing research has focused almost exclusively on post-arrest scenarios where a suspect's identity is already known. This paper addresses a critical gap by examining the pre-arrest phase, providing a more realistic assessment of how LLMs handle the ambiguity and incomplete data inherent in early-stage criminal investigations.

## Implications
These findings suggest that current LLMs are not yet reliable enough to assist in high-stakes pre-arrest inferences due to persistent reasoning gaps and systemic biases. For developers and legal practitioners, this highlights a clear need for more robust inference capabilities and the implementation of strict human-in-the-loop protocols to prevent biased AI outputs from influencing criminal justice outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19965v1)
