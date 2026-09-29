---
title: Are You Sure You're Sure? Two Confounds in a Sycophancy Benchmark
published: 2026-09-26T18:52:35Z
authors: Atharv Gupta, Akshat Jindal, Lavanya Nigam, Aryan Sood
url: http://arxiv.org/abs/2609.32867v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Are You Sure You're Sure? Two Confounds in a Sycophancy Benchmark

## Abstract
Sycophancy is a language model's tendency to cave when a user pushes back, abandoning a correct answer for the user's. Several benchmarks now measure it by scripting an objection and recording how often the model caves. Because that objection is a prompt template, whatever else the template varies is measured along with the property it claims to isolate. We audit SycEval, which reports that objections raised before a model answers (preemptive) cause more caving than those raised after (in-context), and attributes the gap to timing. Two features of its templates vary alongside the property each is meant to test. First, SycEval's objections escalate through four strength levels, and at the two weakest only the preemptive template names a target answer, so timing and naming vary together. We build the missing comparison and test it on multiple-choice questions and SycEval's own free-form pipeline. Naming a target answer raises the follow rate, the share of samples matching the user's assertion, by 14.1--49.5 percentage points (pp), and once both templates name one, the timing comparison reverses on three of the five model conditions we test: models cave \emph{less} under preemptive objections than in-context ones, opposite to SycEval. Second, the output-format instruction benchmarks append for automatic grading also varies with objection placement. Moving it from the pushback into the question flips its effect in opposite directions across models on the same items ($p=0.0059$). The same effect appears in SycEval's free-form pipeline: relocating its instruction lowers caving by 5.1pp on Llama-3.1-8B, while an equivalence test confirms no effect on Qwen3-4B. Both confounds live in the template rather than the models under test, so both are correctable: we close with three checks benchmark authors can apply before publishing.

## Metadata
- **Published**: 2026-09-26T18:52:35Z
- **Authors**: Atharv Gupta, Akshat Jindal, Lavanya Nigam, Aryan Sood
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32867v1)