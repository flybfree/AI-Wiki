---
title: norregel: a preregistered benchmark of dated numeric values in Norwegian law
url: http://arxiv.org/abs/2610.29207v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_04-55-58Z_norregel_apreregisteredbenchmarkofdatednumericvalu.md
generated_at: 2026-10-21 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces norregel, a preregistered benchmark of 916 items designed to test whether language models can correctly retrieve dated numeric values (monetary amounts, percentages, multiples of the National Insurance basic amount, and age limits) from Norwegian statutes, regulations, and parliamentary decisions. The benchmark was evaluated across two preregistered runs involving up to eight models, revealing that while outdated answers are statistically more frequent for values enacted after a model's training cutoff, this finding is not robust under the most methodologically conservative sensitivity analysis, and overall accuracy remains modest, with the best-performing model answering only about 47% of primary items correctly.

## Key Takeaways
- The benchmark's central hypothesis (H1) that outdated answers are more frequent for values taking effect after a model's training cutoff was supported in the pooled primary test (d = 17.8 percentage points, p = 0.0001) but failed under sensitivity analysis S8, which equalizes the target value across groups, yielding d = 3.9 with a confidence interval containing zero (p = 0.1754). The authors explicitly state they do not regard the support for H1 as robust, highlighting the fragility of the finding under alternative operationalizations.
- Even the strongest models performed poorly: Opus 5.5 answered 46.7% and Sonnet 4.6 answered 40.2% of the 880 primary items correctly in the first run, and several models including Haiku 4.5 produced mostly uninterpretable answers, indicating that current LLMs struggle substantially with precise, dated legal numerics in a non-English language.
- Secondary hypotheses regarding whether outdated answers correspond to the most recent superseded value (H2) and whether accuracy differs between Nynorsk and Bokmål legal texts (H3) were both inconclusive, suggesting that norregel exposes gaps in model behavior that cannot be neatly attributed to a single failure mode.

## Context
Benchmarks for evaluating language models on legal knowledge have largely focused on English-language common-law jurisdictions, leaving a gap in assessing model performance on civil-law systems with multilingual statutory traditions. Norwegian law, with its dual-language (Bokmål and Nynorsk) legislative corpus and its reliance on indexed monetary values tied to a periodically updated basic amount (G), presents a particularly challenging test of temporal grounding and numerical precision. The use of a preregistered protocol with published analysis plans before any model calls represents a methodological advance over typical post-hoc benchmark reporting, aiming to reduce researcher degrees of freedom and publication bias in LLM evaluation.

## Implications
For legal practitioners and policymakers who rely on AI tools for statutory research, the results caution against trusting model outputs for time-sensitive numeric provisions, as models frequently return outdated or uninterpretable values without clear signals of uncertainty. For the benchmarking community, the paper demonstrates that preregistered sensitivity analyses can overturn headline findings, and that benchmark design choices—such as how "outdated" is operationalized—materially affect conclusions. The open release of item IDs, per-answer classifications, and code on Zenodo provides a template for reproducible, transparent evaluation of language models on domain-specific factual retrieval tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29207v1)
