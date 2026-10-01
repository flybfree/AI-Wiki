---
title: Zero2Repo: Can Coding Agents Build Repositories from Scratch?
url: http://arxiv.org/abs/2609.38269v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-29_14-10-23Z_Zero2Repo_CanCodingAgentsBuildRepositoriesfromScra.md
generated_at: 2026-09-30 21:07
model: qwen3.6-35b-a3b
---

## Summary
Zero2Repo introduces a rigorous benchmark designed to evaluate whether coding agents can construct complete software repositories from scratch rather than merely patching existing code. The framework converts real open-source projects into behavioral specifications and hidden acceptance tests, evaluating agent performance through isolated execution environments with strict binary pass/fail criteria. Despite leveraging frontier models trained on likely similar repositories, top-performing agents still fail to fully satisfy complex specifications, revealing that failures typically stem from minor omissions rather than fundamental architectural gaps.

## Key Takeaways
- The benchmark utilizes a language-agnostic pipeline that transforms version-pinned open-source projects into reproducible environments and hidden acceptance tests, ensuring evaluations are grounded in real-world software engineering practices across Python, TypeScript, Go, and C++.
- Evaluation methodology enforces strict validation by withholding acceptance criteria until explicit submission, running agents in isolated containers, and applying a binary reward system that only grants success when every test passes without relying on subjective LLM judges.
- Performance analysis reveals that even the most advanced coding agents struggle with low-frequency rules or single specification omissions rather than missing core subsystems, providing researchers with highly specific, actionable targets for model refinement.

## Context
The rapid advancement of large language models has shifted AI capabilities from simple code completion to autonomous software development, yet existing evaluation frameworks remain fragmented and limited to single-language tasks or manually curated prompts. Zero2Repo addresses this critical gap by establishing a scalable, execution-based standard that mirrors actual product development workflows. This benchmark fills a pressing need in the AI research community for robust metrics that assess holistic repository construction rather than isolated code snippets.

## Implications
For practitioners and developers, Zero2Repo offers a reliable method to stress-test coding assistants against realistic engineering requirements before deployment in production environments. Researchers can leverage the benchmark’s failure analysis to systematically improve model alignment with technical specifications and edge-case handling. Ultimately, this work accelerates the transition toward trustworthy AI-driven software engineering by providing transparent, reproducible standards for measuring autonomous development capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38269v1)
