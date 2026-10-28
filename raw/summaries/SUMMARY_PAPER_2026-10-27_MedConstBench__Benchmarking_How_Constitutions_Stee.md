---
title: MedConstBench: Benchmarking How Constitutions Steer LLMs in Medical Ethics
url: http://arxiv.org/abs/2610.36513v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_02-17-13Z_MedConstBench_BenchmarkingHowConstitutionsSteerLLM.md
generated_at: 2026-10-27 22:09
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MedConstBench, a medical-ethics benchmark designed to treat a model's deployment constitution as a controllable variable rather than a fixed property, enabling systematic study of how ethical policies reshape LLM behavior in clinical contexts. The authors evaluate ten open-source LLMs under four distinct constitutions and find that constitutional effects are dimension-selective and model-dependent, with no single constitution performing optimally across all models. They propose a do-no-harm adaptive selector that assigns the best constitution per model while guaranteeing a worst-case performance floor.

## Key Takeaways
- MedConstBench is organized around Beauchamp's four principles of biomedical ethics (autonomy, beneficence, non-maleficence, and justice), and its scoring relies on human-calibrated multi-model peer review rather than simple factual correctness checks, making it a more nuanced tool for evaluating ethical reasoning in medical AI.
- The benchmark includes MedDilemma, a novel dataset of clinical dilemmas, and evaluates ten open-source LLMs under four different constitutions, revealing that the impact of a constitution is not uniform: it varies by ethical dimension and by model architecture, meaning a constitution that improves one model's handling of patient autonomy may degrade another model's adherence to non-maleficence.
- Because no constitution is universally optimal, the authors propose a do-no-harm adaptive selector that matches per-model oracle performance while enforcing a worst-case floor, and this selector generalizes to unseen models at low computational cost, offering a practical deployment strategy for local medical LLMs.

## Context
As open-source LLMs are increasingly deployed locally in clinical and patient-facing settings, their ethical behavior is governed primarily by the constitution embedded at deployment time. Prior benchmarks have largely treated ethics as a static property of a model or focused on factual accuracy, leaving a significant gap in understanding how constitutional choices actively steer ethical reasoning. MedConstBench fills this gap by making the constitution itself the experimental variable, aligning with growing regulatory and institutional interest in how AI systems should navigate competing ethical values in healthcare.

## Implications
For practitioners deploying medical LLMs, this work demonstrates that a one-size-fits-all constitutional policy is inadequate; instead, organizations should adopt model-specific constitutional selection strategies to avoid unintended ethical regressions. For the broader AI safety and alignment community, the finding that constitutional effects are dimension-selective suggests that future constitution design and evaluation frameworks must account for interactions between ethical principles and model architectures, moving beyond monolithic ethical guidelines toward adaptive, per-model governance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36513v1)
