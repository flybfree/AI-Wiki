---
title: Does AI-Assisted Development Homogenize Software? An Empirical Study of Code Similarity, Quality, and Evolution
url: http://arxiv.org/abs/2610.24093v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-16_18-22-51Z_DoesAI_AssistedDevelopmentHomogenizeSoftware_AnEmp.md
generated_at: 2026-10-19 20:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This empirical study investigates whether AI-assisted software development leads to homogenization of code, degradation of quality, or accelerated structural growth across open-source projects. By analyzing 50 long-lived Java and Python projects spanning pre-LLM, potentially LLM-assisted, and detected agentic development eras using Software Heritage snapshots, the authors find no consistent evidence supporting the homogenization hypothesis. Semantic and syntactic code similarity actually decreased in Java projects during AI-assisted eras, Python showed no significant differences, software quality remained largely stable, and structural growth was generally lower in the agentic era.

## Key Takeaways
- Code similarity did not increase with AI assistance: semantic similarity measured via embedding-based cosine similarity and syntactic similarity measured via CodeBLEU* both decreased significantly in Java projects during the LLM-assisted and agentic eras compared to the pre-LLM baseline, while Python projects showed no statistically significant differences across eras. This directly contradicts the widespread assumption that LLMs produce convergent, templated code output.
- Software quality remained largely stable across all three eras as measured by SonarQube metrics covering maintainability, complexity, reliability, and security. However, the agentic era exhibited significantly lower code-smell and SQALE index densities, suggesting that autonomous agents may produce code with fewer detectable quality issues than human-written or interactively assisted code.
- Structural growth patterns diverged from expectations: annualized growth rates of files were generally lower in the agentic era, challenging the notion that AI accelerates codebase bloat. Meanwhile, development activity in Java increased moderately, particularly in commit frequency and added lines, indicating that agentic systems may shift the nature of development activity rather than simply amplifying it.

## Context
This paper addresses a critical gap in understanding how the transition from interactive LLM assistance to fully agentic software engineering systems affects the software ecosystem at scale. As tools like autonomous coding agents become increasingly integrated into production workflows, the software engineering community lacks rigorous longitudinal evidence about their systemic effects on code diversity, quality, and project evolution. By leveraging Software Heritage's archival infrastructure to construct a three-era comparative framework, this study provides one of the first large-scale empirical assessments of agentic development's real-world impact on open-source software.

## Implications
For practitioners and industry leaders, these findings challenge the precautionary narrative that AI-assisted development inevitably produces homogeneous, lower-quality, or structurally bloated codebases, which could inform more confident adoption of agentic tools in production environments. For researchers, the results highlight the need for more nuanced evaluation frameworks that distinguish between interactive assistance and autonomous agentic workflows, and that account for language-specific effects such as the pronounced differences observed between Java and Python ecosystems. The findings also suggest that agentic systems may alter development activity patterns in ways that require updated metrics for assessing team productivity and code health.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24093v1)
