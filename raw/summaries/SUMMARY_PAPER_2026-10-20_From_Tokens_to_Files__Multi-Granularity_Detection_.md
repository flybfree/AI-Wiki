---
title: From Tokens to Files: Multi-Granularity Detection and Localization of AI-Involved Code
url: http://arxiv.org/abs/2610.27863v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_08-45-35Z_FromTokenstoFiles_Multi_GranularityDetectionandLoc.md
generated_at: 2026-10-20 22:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a multi-granularity framework for detecting and localizing AI-generated or AI-modified code at the token, line, block, and file levels, addressing a critical gap in existing approaches that compress entire files into single scores and average away evidence when only small portions are AI-involved. The method uses a frozen code language model equipped with two low-rank adapters trained separately on machine-written and human-written files, computing per-token log-likelihood ratios as local evidence of AI authorship, and achieves 72.4 macro F1 at a 1% false-positive rate on an internal benchmark while outperforming the best reported line-level result on the external HybridCodeAuthorship benchmark.

## Key Takeaways
- The framework models AI authorship at the token level rather than compressing a file into a single global score, enabling precise localization of AI-generated lines and blocks. A frozen code language model is paired with two low-rank adapters (LoRA), one trained on machine-written files and one on human-written files; their per-token log-likelihood ratio produces fine-grained local evidence that lightweight aggregation heads then combine within lines and blocks using surrounding code context before producing a file-level decision.
- On an internal test set of 11,773 AI-involved files spanning six generation regimes against 2,541 human files, the method achieves 72.4 macro F1 at a 1% false-positive-rate operating point. On the external HybridCodeAuthorship benchmark, which has no training split, the method reaches 62.5 line-level F1 without any adaptation, surpassing the 56 F1 that the benchmark's own paper reports as its best line-level result.
- Robustness on real human code is validated on 19,445 human-written files from repositories created before 2022, where the false-positive rate remains between 0.55% and 0.81% under the transported 1% threshold, confirming that the operating point does not degrade on genuinely human-authored code and that the method avoids flagging legitimate human contributions as AI-generated.

## Context
As large language models become ubiquitous in software development through tools like GitHub Copilot, Cursor, and ChatGPT-based code assistants, the provenance of code in open-source and proprietary repositories becomes increasingly ambiguous. Existing detection methods rely on surface stylistic features or global code representations that produce a single score per file, which fails when only a few lines or blocks in an otherwise human-authored file were AI-generated. This paper matters because it shifts the granularity of detection from whole-file classification to token-level attribution, which is essential for code review, licensing compliance, academic integrity in software engineering research, and understanding the true composition of modern codebases.

## Implications
For practitioners in software engineering, open-source governance, and code auditing, this method provides a practical tool to flag and localize AI-involved code at the line and block level rather than merely labeling entire files, enabling targeted review and attribution without penalizing human contributors. For the research community, the use of frozen language models with lightweight adapters and log-likelihood ratios offers a transferable paradigm for authorship attribution that generalizes across generation regimes and transfers to unseen benchmarks without retraining, suggesting a scalable path toward provenance tracking in AI-assisted software development pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27863v1)
