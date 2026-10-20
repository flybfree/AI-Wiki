---
title: When LLM-Generated Refactorings Ripple: An Empirical Study of Repository Adoption Readiness
url: http://arxiv.org/abs/2610.24790v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_17-29-52Z_WhenLLM_GeneratedRefactoringsRipple_AnEmpiricalStu.md
generated_at: 2026-10-19 20:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the repository-level risks introduced by LLM-generated code refactorings, moving beyond file-local evaluations to assess how refactored code affects contracts, dependencies, and downstream callers across entire codebases. Through 1,500 generation attempts spanning 150 production Java files from 15 open-source repositories and five LLM configurations, the authors find that 93.8% of generated refactoring candidates are classified as High Contract/Dependency Risk, with only eight meeting Low-risk criteria, underscoring that LLM refactorings rarely produce safe, drop-in replacements without repository-wide verification.

## Key Takeaways
- The overwhelming majority of LLM-generated refactoring candidates (1,365 out of 1,455, or 93.8%) are classified as High Contract/Dependency Risk, meaning they alter public interfaces, dependency structures, or caller assumptions in ways that can break downstream code. Additionally, 106 candidates (7.3%) have at least one detected broken downstream caller, and 290 (19.9%) exhibit a false behavioural-equivalence indicator, revealing that LLMs frequently produce refactored code that appears correct in isolation but violates contracts or behavioral guarantees at the repository level.
- Paired analyses of 705 complete generation pairs show no statistically significant difference in principal risk indicators between single-prompt refactoring and LangGraph-based multi-agent refactoring approaches, suggesting that the choice of generation orchestration strategy does not meaningfully reduce repository-level risk. However, different model configurations do differ in specific detected risk channels, indicating that model selection can influence which types of breakage are introduced.
- Among the 65 candidates with conclusive targeted-test outcomes, 60 pass their tests—including 50 that were classified as High risk—highlighting a critical gap between test-passing and genuine repository safety. This means passing unit tests alone is insufficient to validate LLM-generated refactorings, and practitioners must employ additional structural, compilation, and multi-file verification steps before adoption.

## Context
As LLMs become embedded in developer workflows for code transformation tasks, the software engineering community has largely evaluated their output at the file level, checking syntax correctness or local behavioral equivalence. This paper addresses a critical blind spot: the ripple effects that refactored code produces across a repository's dependency graph, public API contracts, and caller assumptions. By introducing repository-facing structural indicators and multi-agent generation conditions, the study bridges the gap between isolated code generation and the practical realities of integrating AI-produced changes into production codebases, a concern that grows more urgent as agentic coding tools proliferate.

## Implications
For practitioners and engineering teams, the findings argue strongly against treating LLM-generated refactorings as ready-to-merge changes; instead, they should be handled as candidates requiring staged, repository-level verification pipelines that include compilation checks, behavioral equivalence testing, and coordinated multi-file analysis. For the research community, the paper identifies concrete gaps in current screening and extraction precision and calls for stronger verification frameworks that go beyond unit tests to capture contract violations and dependency breakage. Industry adoption of AI-assisted refactoring tools will depend on building such verification infrastructure, and the near-total absence of Low-risk candidates in this study signals that current LLM capabilities are not yet sufficient for autonomous, unreviewed code transformation at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24790v1)
