---
title: GDP.xlsx: Benchmarking Frontier Models on Professional Workbooks
url: http://arxiv.org/abs/2611.17766v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-13_05-24-50Z_GDP_xlsx_BenchmarkingFrontierModelsonProfessionalW.md
generated_at: 2026-11-15 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
GDP.xlsx introduces a rigorous benchmark of 70 realistic professional workplace tasks spanning 13 domains, each paired with expert-authored binary rubrics and the actual spreadsheet or CSV files they reference, totaling 2.18 million populated cells and 791 evaluation criteria. The benchmark evaluates agents operating within a containerized environment equipped with spreadsheet tools, using an agentic judge that opens the file to apply the rubric strictly. Across 20 model configurations including frontier models from Google, Anthropic, and OpenAI, the best-performing model (Gemini 4 Argon) achieves only a 38.3% strict pass@1 rate, with a median score of 19.3%, revealing substantial remaining headroom for improvement.

## Key Takeaways
- The benchmark demands set-valued completeness and exclusivity: agents must find every required answer in full with nothing extra, making partial or padded responses fail the evaluation. This design choice prevents models from gaming the rubric by including extraneous correct-looking entries alongside the correct ones, enforcing a precision-recall balance that mirrors real professional expectations.
- Evaluation is conducted through an agentic judge that can open and inspect the actual workbook file, rather than relying on text-only comparison. This means the agent must produce correctly formatted, structurally valid spreadsheet outputs that a downstream evaluator can programmatically verify against 791 binary criteria, raising the bar well above free-form text generation benchmarks.
- Even the top frontier model passes fewer than 40% of attempts under strict pass@1 (every criterion must be met), and the median across 20 configurations sits at 19.3%. This gap between claimed capabilities and actual performance on grounded, file-based professional tasks suggests that current models struggle with multi-step spreadsheet manipulation, domain-specific reasoning, and the combinatorial difficulty of satisfying dozens of simultaneous binary constraints.

## Context
This paper addresses a critical gap in AI evaluation: most existing benchmarks test language understanding or code generation in isolation, while professional knowledge work increasingly involves manipulating structured data files like spreadsheets and CSVs. By grounding tasks in authentic workplace requests authored by domain professionals and requiring agents to interact with actual files through tool-equipped containers, GDP.xlsx moves evaluation closer to the deployment reality where AI assistants are expected to produce usable, correct outputs within existing enterprise workflows. The held-out design of 67 tasks protects leaderboard integrity against contamination, signaling a maturation in benchmark methodology.

## Implications
For practitioners deploying AI agents in finance, engineering, operations, and other spreadsheet-heavy domains, the 19.3% median pass rate signals that current frontier models are not yet reliable enough for autonomous professional workbook tasks without human oversight. Industry teams should treat spreadsheet automation as an unsolved problem requiring careful human-in-the-loop validation rather than trusting model outputs directly. The released evaluation harness and three public tasks provide a reproducible starting point for researchers to develop tool-augmented agents that can handle the structural and combinatorial complexity of real data files, potentially guiding the next generation of agent architectures toward genuine professional utility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17766v1)
