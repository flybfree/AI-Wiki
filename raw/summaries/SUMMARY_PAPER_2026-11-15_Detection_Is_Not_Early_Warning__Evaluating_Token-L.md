---
title: Detection Is Not Early Warning: Evaluating Token-Level Alarms on Language Model Failures
url: http://arxiv.org/abs/2611.16803v2
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-12_13-43-19Z_DetectionIsNotEarlyWarning_EvaluatingToken_LevelAl.md
generated_at: 2026-11-15 21:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PREWARN, an evaluation protocol that assesses monitors for language model failures at the token level rather than the response level, distinguishing three distinct tasks: classification of finished responses, detection of failures once underway, and early warning before a failure begins. Applied to repetitive degeneration in three open language models, the study finds that response-level metrics like AUROC saturate and fail to differentiate monitors that warn very differently, while linear probes on activations can genuinely warn before the failure onset in two of three models, and low-rank adapters flag substantially more pre-onset tokens than probes.

## Key Takeaways
- Response-level evaluation metrics such as AUROC are fundamentally inadequate for assessing early warning capability because they ignore when a monitor fires relative to the failure onset; a simple rule that reads only response length scores almost perfectly on AUROC while providing no actionable early warning, demonstrating that standard benchmarks can be gamed without any real monitoring value.
- The PREWARN protocol calibrates each monitor's threshold on validation data to a user-chosen error rate, then scores alarms relative to the annotated onset across all three tasks (classification, detection, early warning), revealing that probes ranked as equivalent by AUROC warn very differently when evaluated on timing, and that low-rank adapters below the probe more than double the share of tokens flagged just before the onset, largely by flagging degenerate responses long before the failure actually begins.
- No untrained baseline warns much more often than random alarms, indicating that meaningful early warning requires trained probes on model activations rather than heuristic or statistical shortcuts, and the authors release calibrated probes at HuggingFace to enable reproducible evaluation of token-level monitoring systems.

## Context
As language models are increasingly deployed in autonomous and interactive settings, the ability to intervene before a generation failure manifests becomes critical for safety, reliability, and user trust. The field has largely relied on response-level evaluation frameworks borrowed from classification tasks, which treat a model output as a single binary event and ignore the temporal dynamics of generation. This paper addresses a gap between how monitors are actually used in practice—where timing relative to the failure onset determines whether intervention is possible—and how they are evaluated in the literature, pushing the community toward more operationally meaningful benchmarks.

## Implications
For practitioners building monitoring and steering systems for deployed language models, this work signals that AUROC-based evaluations can be misleading and that token-level timing must be explicitly measured to ensure a monitor provides actionable lead time before a failure occurs. For the broader AI safety and reliability community, the finding that trained probes can genuinely warn before degeneration onset in some models suggests that early intervention pipelines are feasible, while the failure of untrained baselines underscores the need for dedicated probe training and calibrated thresholds rather than ad-hoc heuristics. The open release of calibrated probes also provides a concrete starting point for reproducible benchmarking of monitoring systems across model families.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.16803v2)
