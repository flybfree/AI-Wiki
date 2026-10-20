---
title: Concerns in Benchmarking Jailbreaks: An Empirical Study of Attack Success Rates
url: http://arxiv.org/abs/2610.26595v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_15-39-16Z_ConcernsinBenchmarkingJailbreaks_AnEmpiricalStudyo.md
generated_at: 2026-10-20 00:35
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how the evaluation methodology used to benchmark jailbreak attacks on language models dramatically distorts reported Attack Success Rates (ASR), making comparisons across studies unreliable. By testing eight jailbreak attacks against three open-weight models using three different evaluation procedures, the authors demonstrate that keyword matching can report a 96.0% success rate for low-resource language attacks while a Qwen3-based evaluator following StrongREJECT scoring instructions reports only 2.7%. The study further shows that sampling parameters and attempt arrangements can reverse rankings between methods and expose residual unsafe behavior that single-generation tests miss.

## Key Takeaways
- Evaluator choice fundamentally alters reported ASR: low-resource language attacks score 96.0% under keyword matching but only 2.7% under a Qwen3 evaluator following StrongREJECT scoring instructions, meaning published comparisons across papers using different judges are not comparable and can mislead practitioners about true model robustness.
- Experimental design choices such as the number and arrangement of attempts can reverse the performance ranking of jailbreak methods like DeepInception and rewriting, indicating that leaderboard positions are artifacts of protocol rather than intrinsic method superiority.
- Repeated sampling at Ollama's default temperature of 0.8 yields 100% ASR under keyword matching but 50% under the Qwen3 evaluator, revealing that models may probabilistically suppress unsafe outputs rather than robustly exclude them, raising a genuine safety concern about residual harmful behavior surfacing across repeated interactions.

## Context
Jailbreak research has proliferated rapidly as open-weight and proprietary language models are deployed in safety-critical applications, and the community relies heavily on ASR as a headline metric for comparing attack methods. However, the field lacks standardized evaluation protocols, with different papers employing keyword matching, human judgment, or LLM-as-judge scoring, producing incompatible numbers. This paper addresses a foundational methodological gap by systematically varying evaluation procedures, sampling budgets, and attempt structures to quantify how much of the reported "progress" in jailbreak robustness is an artifact of measurement rather than genuine improvement in model safety.

## Implications
For practitioners and safety teams, the findings demand that jailbreak evaluations specify explicit success definitions, matched response budgets, and validated evaluators before any model is deemed robust, and that cumulative failure under repeated interaction be reported rather than single-generation pass/fail results. For the research community, the paper calls for benchmarking standards that prevent apples-to-oranges comparisons, ensuring that safety claims about model robustness are reproducible and not inflated by lenient keyword-based scoring. Industry deployments should treat single-refusal tests as insufficient evidence of safety, since probabilistic suppression can allow harmful outputs to emerge under repeated user interaction at common temperature settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26595v1)
