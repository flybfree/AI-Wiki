---
title: Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination
url: http://arxiv.org/abs/2610.31586v1
type: paper-summary
date: 2026-10-23
source_paper: 2026-10-22_17-23-11Z_WouldanLLMMatchintoaResidency_Uncertainty_Reasonin.md
generated_at: 2026-10-23 09:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper evaluates four open-source language models (8 to 27 billion parameters) on the Spanish MIR residency examination, a high-stakes medical licensing test, to assess not just raw accuracy but deeper clinical competencies: uncertainty calibration, reasoning soundness, and actual use of provided medical images. The authors find that while the larger models achieve competitive exam scores, they fail in critical areas a health system would need to trust them for clinical deployment, including genuine image comprehension and clinically sound reasoning behind correct answers.

## Key Takeaways
- The three larger models (ranging up to 27 billion parameters) would rank among roughly the first 600 to 3,000 candidates out of the full applicant pool, leaving 41 to 43 medical specialties accessible to them, demonstrating that open-weight models can achieve surprisingly competitive performance on a rigorous national medical exam scored under its own official rules.
- Abstention strategies never benefit these models because even their least confident answers exceed the 25% break-even threshold, meaning the models are always better off answering than declining to answer; furthermore, medical fine-tuning reduced overconfidence but at the direct cost of accuracy and did not improve the separation between confidence and actual correctness, undermining the assumption that domain-specific training yields better-calibrated uncertainty.
- Between 13% and 38% of the models' correct answers involved rejecting a distractor for a clinically unsound reason that their stated confidence did not reflect, and removing or swapping the contextual images provided in the exam left accuracy completely unchanged, indicating the models are not genuinely processing visual medical information but are instead relying on textual pattern-matching to arrive at correct answers.

## Context
This work addresses a critical gap in the evaluation of open-weight language models for healthcare deployment. Most existing benchmarks report only accuracy scores, but a health system running models on its own hardware must understand whether those models know when they are uncertain, whether their reasoning is clinically valid, and whether they truly engage with multimodal inputs. By using a real national residency examination with its own scoring rules, the authors provide a more ecologically valid test than synthetic benchmarks, revealing that high accuracy can mask fundamental failures in reasoning and perception.

## Implications
For healthcare institutions considering open-model deployment, this research warns that competitive exam scores alone are insufficient evidence of clinical readiness, as models may appear competent while failing to use provided images or reasoning through distractors soundly. Practitioners and regulators should demand evaluations that test uncertainty calibration, reasoning transparency, and multimodal engagement rather than accepting accuracy as a proxy for clinical safety. The finding that medical fine-tuning degrades accuracy while only marginally improving calibration also challenges the common assumption that domain-specific training automatically produces safer, more trustworthy clinical AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31586v1)
