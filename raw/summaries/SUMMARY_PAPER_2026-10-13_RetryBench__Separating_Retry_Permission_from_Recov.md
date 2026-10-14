---
title: RetryBench: Separating Retry Permission from Recovery Outcomes in GPT Tool Use
url: http://arxiv.org/abs/2610.15884v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_20-00-44Z_RetryBench_SeparatingRetryPermissionfromRecoveryOu.md
generated_at: 2026-10-13 22:03
model: gpt-5.6-luna
---

## Summary

RetryBench investigates false retry permission (FRP), an agent error in which a model retries a timed-out tool call without sufficient authorization from the visible interface contract. The study separates whether a retry is permitted from whether the retry ultimately succeeds, finding that successful recovery can coexist with unreliable rejection of unsupported retry requests. Across several controls, models differed substantially in their willingness to dispatch unsupported retries, and the results suggest that interface wording and contract strength materially affect behavior.

## Key Takeaways

- In a 720-response key-control experiment, valid keys generally enabled safe progress, but changed or unsupported keys triggered retries at sharply different rates: Sol retried in 1 of 80 responses, Terra in 55 of 80, and Luna in 60 of 80. This demonstrates that accepting a displayed key is not the only source of retry failures.

- When the candidate key was removed and models had to supply one themselves, Luna still made 8 unsupported dispatches in 80 responses, while Sol and Terra made none. The result weakens a purely display-based explanation, although the authors caution that the changed output requirements and task conditions prevent a clean, isolated comparison.

- Additional experiments found that removing a weak-contract label increased retries for Sol and Terra in coded-action conditions. A canonical-action block produced one positive Terra contrast, while five other contrasts remained unresolved after correcting for multiple comparisons. An explicit-contract cue caused deferral in all 762 returned responses, leaving actual recovery performance unresolved.

## Context

Tool-using agents must decide not only what action might solve a problem, but also whether the interface authorizes that action. Existing evaluations often collapse these questions into a single outcome, such as whether the agent eventually recovers, which can conceal unsafe retries that happen to succeed. RetryBench contributes a more granular framework for evaluating contract adherence, permission judgments, and recovery separately.

## Implications

For researchers and developers, retry handling should be evaluated across explicit interface variants rather than inferred from successful outcomes alone. Tool APIs and agent harnesses should make retry authority unambiguous, log unsupported dispatch attempts, and report both permission errors and recovery rates. The study also suggests caution in generalizing from fixed GPT endpoints and purposive tasks: the findings identify observable behavioral differences, not the internal mechanisms behind them or episode-level safety guarantees.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15884v1)
