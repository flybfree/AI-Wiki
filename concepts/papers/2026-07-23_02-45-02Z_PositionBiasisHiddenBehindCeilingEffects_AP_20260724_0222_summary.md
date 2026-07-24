# Summary: 2026-07-23_02-45-02Z_PositionBiasisHiddenBehindCeilingEffects_APermutat.md
Saved: 2026-07-24 02:22
Source: 2026-07-23_02-45-02Z_PositionBiasisHiddenBehindCeilingEffects_APermutat.md
Model: None

---

## Summary  
The paper identifies that position bias in multiple‑choice LLM evaluation is confounded by ceiling effects and sampling noise. It introduces **inspect_permute**, a permutation diagnostic that measures this bias with bootstrap confidence intervals. Experiments across four models on MMLU show detectable bias only within a narrow accuracy range (60–95%). This reveals the limits of position‑bias measurement and makes the question answerable.

## Key Contributions  
- Finding 1: Position bias is statistically detectable only when model base accuracy lies in roughly a 60 %–95 % band, below which processing load dominates and above which ceiling effects reduce variance.  
- Finding 2: The diagnostic distinguishes two mechanisms of bias: monotone A‑to‑D decrease (processing‑load effect) in low‑capability models, and non‑monotone D‑drop (content ambiguity) near the frontier.  
- Finding 3: Standard MMLU places all current frontier models above the detection band, so lack of signal should be interpreted as measurement limitation rather than true bias.

## Methodology  
The authors built **inspect_permute**, an extension to inspect_ai that generates exhaustive answer‑order permutations per question and computes chi‑squared and Cramer V statistics with bootstrap confidence intervals. They registered falsifier predictions via SHA‑256 before half the data was observed, ensuring preregistration. The tool was applied to four vendor models (gpt‑4o‑mini, claude‑haiku‑4‑5, gemini‑2.5‑flash, grok‑3) on five MMLU subjects using 24 000 temperature‑0 API calls.

## Results  
Across the tested models, chi‑squared values exceeded significance only for accuracy scores between ~60% and ~95%. In this Goldilocks zone, the permutation test revealed a clear position bias signature. Below that range, processing‑load effects masked any subject‑specific signal; above it, ceiling effects compressed variance below the test resolution. The two identified mechanisms align with theoretical expectations.

## Significance  
This work clarifies when and why position bias appears in LLM benchmarking, preventing misinterpretation of absence of signal as true bias. By quantifying the detectable region, it makes the central question “Is there position bias?” answerable in a verifiable form, advancing reproducibility and fairness in AI evaluation.

## Related Concepts  
- Position bias in multiple‑choice QA  
- Ceiling effects on variance  
- Chi‑squared / Cramer V permutation tests  
- Bootstrap confidence intervals  
- MMLU benchmarking
