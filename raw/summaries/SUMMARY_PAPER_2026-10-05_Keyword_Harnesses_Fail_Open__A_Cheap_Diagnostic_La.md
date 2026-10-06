---
title: Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-Use Claims in Small Language Models
url: http://arxiv.org/abs/2610.02142v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-01_17-46-38Z_KeywordHarnessesFailOpen_ACheapDiagnosticLadderfor.md
generated_at: 2026-10-05 23:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that keyword-matching benchmarks can falsely credit small language models with tool-use capabilities they never actually perform, using a matched-architecture pair of Spanish security language models as a case study. The authors propose a ladder of strict, inexpensive diagnostics—verbatim-reproduction checks, first-token probes, and embedding-drift analysis—that reliably separates genuine tool-use competence from superficial format mimicry, and show that a targeted fine-tuning recipe can repair a broken model using far fewer tokens than the original failed training phase.

## Key Takeaways
- A 661.6M parameter model and a 1,109M parameter model sharing identical decoder, tokenizer, and special tokens score almost identically on lenient tool-use metrics (B4: 0.660 vs. 0.650), yet verbatim-reproduction checks reveal a stark difference: the smaller model emits valid tool calls with generalized arguments on 6 out of 6 training examples, while the larger model does so on 0 out of 6 across all checkpoints, exposing a false positive in the benchmark.
- The 1B model's failure is precisely localized to a missing prior probability (10⁻⁴ to 10⁻⁵) on the special token <|tool_call|>, which was erased during its web-heavy multi-phase training curriculum. A targeted SFT recipe using a diverse corpus, a 5× higher learning rate, 2,202 steps, and approximately 3.3 GPU-hours repairs the model, raising valid emission from 0.100 to 0.959 on corpus rows and achieving 0.536 on 238 unseen prompts versus the 600M model's 0.428 (p = 0.004).
- Embedding-drift checks confirm the repair did not alter the trigger token's tied embedding (97.7% of the bf16 table remains bit-identical), meaning the learned changes reside in the surrounding network weights rather than in the token representation itself. Both models also exhibit over-triggering behavior, rarely answering negative prompts without issuing a tool call.

## Context
As small language models proliferate in specialized domains such as security, legal, and multilingual applications, evaluation infrastructure has largely relied on keyword-matching or format-detection metrics that reward surface-level compliance rather than genuine functional tool use. This paper sits at the intersection of model evaluation methodology and training-data curation, highlighting how architectural matchedness and shared tokenizers can mask fundamentally different training outcomes. It contributes to a growing body of work questioning whether current benchmark suites adequately distinguish between models that understand tool semantics and those that merely pattern-match to expected output formats.

## Implications
For practitioners deploying small models in production tool-use pipelines, this work argues that a cheap diagnostic ladder costing only minutes of CPU time should gate any tool-use claims before a model is trusted in downstream applications, preventing costly deployment failures rooted in superficial benchmark scores. For the broader research community, the finding that a web-heavy training phase can erase a critical prior probability—and that targeted, token-efficient fine-tuning can restore it—suggests that curriculum design and phase ordering matter as much as total training compute, with direct consequences for how small models are trained, evaluated, and certified for agentic or tool-augmented tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02142v1)
