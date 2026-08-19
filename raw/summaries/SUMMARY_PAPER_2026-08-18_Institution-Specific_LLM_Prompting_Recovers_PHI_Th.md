---
title: Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss
url: http://arxiv.org/abs/2608.17051v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_18-56-04Z_Institution_SpecificLLMPromptingRecoversPHIThatDe_.md
generated_at: 2026-08-18 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether large language models with in-context learning can recover institutionally specific protected health information that de-identification systems miss. On pediatric oncology notes from Texas Children’s Hospital, LLMs outperformed purpose-built tools and achieved high recall while controlling precision.

## Key Takeaways
- LLM prompts that include institutional PHI categories recovered 79% of missed spans.
- Adding instructions to limit over-redaction restored precision without sacrificing recall.
- No multi-agent architecture improved the best single-pass prompt, but LLM outputs identified 414 candidate gaps.

## Context
This work demonstrates that LLMs can adapt quickly to domain-specific privacy rules, offering a flexible alternative to static de-identification pipelines. It highlights the importance of contextual awareness in AI safety mechanisms and shows how fine‑tuned prompting can improve compliance outcomes.

## Implications
Practitioners should develop institution-specific prompts as primary adaptation strategy rather than relying solely on off-the-shelf tools. The cost of LLM inference is justified by auditability and improved accuracy, aligning with regulatory compliance goals.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17051v1)
