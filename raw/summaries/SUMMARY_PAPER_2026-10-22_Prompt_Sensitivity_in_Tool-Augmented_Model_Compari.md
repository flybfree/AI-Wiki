---
title: Prompt Sensitivity in Tool-Augmented Model Comparisons
url: http://arxiv.org/abs/2610.31148v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_12-07-01Z_PromptSensitivityinTool_AugmentedModelComparisons.md
generated_at: 2026-10-22 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether providing language models with tool access makes benchmark comparisons more stable when questions are reworded. The authors propose a matched experimental protocol that decomposes the tool-augmented pipeline into distinct steps—answer readout, reasoning, the decision to call a tool, the tool's response, and the report generated without a call—and apply it across six open models, five domains, and five question wordings. They find that while tools can raise accuracy when a program directly answers the question, they simultaneously widen wording sensitivity in many pairwise model comparisons, meaning deterministic tool outputs do not guarantee stable rankings.

## Key Takeaways
- Tools widen wording sensitivity in pairwise comparisons: even though a tool produces a deterministic answer, the model's decision to invoke the tool is itself sensitive to how the question is phrased. Call frequency varies with wording for some models but not others, meaning the tool-augmented pipeline introduces a new, wording-dependent failure mode that pure accuracy metrics cannot capture.
- The interface and instruction design matter significantly: a native tool-calling interface combined with a secondary tool description eliminated detected widening in the molecules domain, while sensitivity persisted in settings where tools returned intermediate results rather than final answers. This shows that the architecture of tool integration, not just the presence of tools, determines comparison stability.
- The authors recommend that benchmark reporting include call frequency and comparison stability under multiple wordings alongside raw accuracy scores, because a single accuracy number can mask substantial ranking instability across model pairs when prompts are rephrased.

## Context
Standard LLM evaluation relies on fixed-question benchmarks that assume a single canonical wording per item, yet prior work has shown that even minor paraphrasing can flip which model appears superior. As tool-augmented agents become the dominant paradigm for complex reasoning tasks—code generation, scientific computation, data retrieval—the assumption that deterministic tool outputs neutralize prompt sensitivity has not been rigorously tested. This paper fills that gap by isolating each stage of the tool pipeline and measuring how wording propagates through it, contributing to the growing literature on benchmark robustness and evaluation methodology in the open-model ecosystem.

## Implications
For practitioners deploying tool-augmented models in production or research settings, this work warns that selecting a model based on a single benchmark run may yield an unstable choice if the task prompts differ from the benchmark's exact phrasing. Benchmark developers and leaderboard maintainers should adopt multi-wording evaluation protocols and report call-frequency distributions to give users a more honest picture of model reliability. For the broader AI community, the findings underscore that tool integration is not a silver bullet for evaluation stability and that interface design choices—such as native versus simulated tool-calling APIs—carry measurable consequences for how sensitive model comparisons are to superficial prompt changes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31148v1)
