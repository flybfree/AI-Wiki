# Summary: 2026-07-23_02-45-02Z_PositionBiasisHiddenBehindCeilingEffects_APermutat.md
Saved: 2026-07-24 02:22
Source: 2026-07-23_02-45-02Z_PositionBiasisHiddenBehindCeilingEffects_APermutat.md
Model: None

---

## Summary  
The paper tackles the problem of position bias in multiple‑choice LLM evaluation, which is often obscured by ceiling effects and sampling noise that plague existing benchmark analyses. It introduces **inspect_permute**, an open‑source extension to the inspect_ai framework that runs exhaustive answer‑order permutations per question and reports a chi‑squared / Cramer V signature with bootstrap confidence intervals. The study demonstrates that position bias is statistically detectable only within a narrow “Goldilocks” base‑accuracy range (≈60–95 %) and that the signal disappears both below and above this zone due to processing‑load dominance and ceiling effects, respectively.

## Key Contributions  
- [Finding 1] Position bias becomes measurable only when model performance lies roughly between 60 % and 95 % base accuracy; outside this window the variance is too low or too high for chi‑squared / Cramer V tests to resolve it.  
- [Finding 2] The detectable signal splits into two mechanisms: (a) a monotone A‑to‑D decrease driven by processing load in lower‑tier models, and (b) a non‑monotone D‑drop caused by content ambiguity within a narrow capability band.  
- [Finding 3] Standard MMLU places every frontier‑tier model above the detection band, so the absence of a chi‑squared signal should be interpreted as “not measurable,” not “unbiased.”

## Methodology  
The authors built **inspect_permute**, an open‑source tool that extends inspect_ai to perform exhaustive answer‑order permutations for each question. For every permutation they compute the chi‑squared statistic and Cramer V measure, then bootstrap confidence intervals to quantify significance. The experiment uses four vendor models (gpt‑4o‑mini, claude‑haiku‑4‑5, gemini‑2.5‑flash, grok‑3) on five MMLU subjects, generating 24 000 API calls at temperature 0. Falsifier predictions were pre‑registered via a public SHA‑256 hash before half the data was observed, ensuring preregistration and reducing selection bias.

## Results  
Statistical analysis shows that position bias is only detectable within the 60–95 % accuracy window; below this threshold processing load overwhelms any subject‑specific signal, while above it ceiling effects compress variance below the chi‑squared test resolution. The two mechanisms identified—monotone A‑to‑D decrease and non‑monotone D‑drop—are statistically significant only for models whose performance sits in that Goldilocks zone. Standard MMLU benchmarks place all frontier‑tier models above this range, so the lack of a chi‑squared signal is not evidence of bias but rather a consequence of ceiling effects.

## Significance  
This work provides a verifiable, reproducible framework for asking whether position bias exists in LLM multiple‑choice evaluations. By isolating the detectable performance band and characterizing its statistical limits, it clarifies why many prior studies report “no bias” when models are too strong or too weak. The findings help researchers set realistic expectations for benchmarking and prevent misinterpretation of ceiling effects as evidence of systematic position bias.

## Related Concepts  
position bias, ceiling effect, permutation diagnostic, chi‑squared test, Cramer V, bootstrap confidence intervals, MMLU benchmark, LLM evaluation confounders, inspect_ai framework, open‑source tooling.
