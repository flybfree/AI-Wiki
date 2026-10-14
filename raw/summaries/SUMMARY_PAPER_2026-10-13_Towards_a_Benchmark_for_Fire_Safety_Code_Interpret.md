---
title: Towards a Benchmark for Fire Safety Code Interpretation in the Hong Kong AEC Industry
url: http://arxiv.org/abs/2610.16127v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-12_03-45-26Z_TowardsaBenchmarkforFireSafetyCodeInterpretationin.md
generated_at: 2026-10-13 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a localized benchmark dataset for evaluating Large Language Models' ability to interpret Hong Kong fire safety codes within the Architecture, Engineering, and Construction (AEC) industry. Developed in collaboration with domain experts, the benchmark includes both multiple-choice and open-ended questions tested against 12 proprietary and open-source models. The key finding is that while top proprietary models score 80-90% on multiple-choice tasks, expert human evaluation of open-ended responses reveals accuracy drops to only 50-70%, exposing a significant gap between superficial recognition and genuine regulatory comprehension.

## Key Takeaways
- The study constructed a specialized benchmark dataset tailored to Hong Kong fire safety codes, combining multiple-choice questions (MCQs) and open-ended questions (OEQs), created in direct collaboration with domain experts to ensure regulatory accuracy and local relevance. This dual-format design allows researchers to distinguish between pattern-matching performance and true interpretive understanding of complex building codes.
- Top-performing proprietary LLMs achieved 80-90% accuracy on multiple-choice evaluations, while open-source models generally underperformed. However, when responses were assessed through open-ended evaluation by human experts, accuracy fell dramatically to a 50-70% range, revealing that high MCQ scores do not translate into reliable regulatory compliance reasoning and that models may exploit test-format shortcuts rather than demonstrating genuine code comprehension.
- The evaluation covered 12 widely used proprietary and open-source models, providing a comparative landscape of current LLM capabilities in a highly specialized regulatory domain. The gap between MCQ and OEQ performance underscores that benchmarking LLMs on regulatory tasks requires evaluation methods that go beyond automated scoring and incorporate expert human judgment.

## Context
This research sits at the intersection of AI evaluation methodology and domain-specific regulatory compliance, a rapidly growing concern as LLMs are increasingly deployed in safety-critical industries like construction and engineering. While general-purpose benchmarks such as MMLU or legal QA datasets have driven model development, they fail to capture the nuanced, jurisdiction-specific interpretation required in building code compliance. By focusing on Hong Kong's fire safety codes, the paper addresses a critical gap: the absence of localized, expert-validated benchmarks that test whether LLMs can handle the ambiguity, cross-referencing, and contextual reasoning inherent in real-world regulatory documents.

## Implications
For AEC practitioners and regulatory authorities, these findings serve as a cautionary signal that current LLMs cannot yet be trusted as standalone tools for fire safety code interpretation, particularly when nuanced open-ended reasoning is required. The benchmark framework itself offers a replicable methodology that other jurisdictions and regulatory domains can adapt to stress-test AI tools before deployment in safety-critical workflows. For AI developers and researchers, the stark performance gap between MCQ and OEQ evaluations highlights the urgent need for evaluation protocols that resist format exploitation and more accurately measure genuine domain understanding, guiding future model training and fine-tuning strategies toward deeper regulatory reasoning rather than surface-level pattern recognition.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16127v1)
