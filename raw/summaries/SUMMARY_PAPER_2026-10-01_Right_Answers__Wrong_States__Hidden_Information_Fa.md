---
title: Right Answers, Wrong States: Hidden Information Failures in Multi-Agent Collaboration
url: http://arxiv.org/abs/2610.01244v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_07-42-27Z_RightAnswers_WrongStates_HiddenInformationFailures.md
generated_at: 2026-10-01 21:21
model: qwen3.6-35b-a3b
---

## Summary
This research exposes a critical vulnerability in multi-agent collaboration termed "off-query failures," where systems generate correct immediate answers while simultaneously corrupting the shared information state, thereby compromising future reasoning capabilities. Through the OffQuery evaluation framework applied to healthcare and disaster response scenarios, the authors reveal a stark performance gap: task resolution reaches 64.7%, whereas evidence verification and shared-state reconstruction languish at 14.3% and 43.1% respectively across standard models. To mitigate these hidden failures, the paper introduces ReGround, a mechanism that resolves conflicting evidence and reconstructs trusted states, delivering substantial relative gains of up to 309% in evidence verification and significant improvements across all metrics for multiple model families.

## Key Takeaways
- Standard multi-agent collaboration exhibits a severe disconnect between decision accuracy and state reliability; while task resolution averages 64.7%, evidence verification drops to just 14.3% and shared-state reconstruction to 43.1%, indicating that models frequently bypass corrupted facts in current queries, causing these errors to surface only when later tasks depend on the compromised information.
- The OffQuery framework isolates three distinct capabilities—evidence verification (T1), shared-state reconstruction (T2), and task

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.01244v1)
