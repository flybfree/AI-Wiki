---
title: Reflection or Re-Generation? Why LLM Revision Fails Where Human Revision Succeeds
published: 2026-07-31T00:15:32Z
authors: Yefan Tao, Gerald Friedland, Madhusudhanan Chandrasekaran, Luyang Kong
url: http://arxiv.org/abs/2607.28908v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reflection or Re-Generation? Why LLM Revision Fails Where Human Revision Succeeds

## Abstract
Reflection, the ability to revisit and revise prior reasoning, is central to how humans improve their answers. Large language models (LLMs) are increasingly prompted to "reflect," yet whether this resembles human revision remains unclear. We introduce the Human-LLM Reflection Framework (HRF), a controlled two-pass protocol comparing human and LLM revision under identical conditions across self-, peer-, and cross-agent settings. Using an information-theoretic analysis based on per-iteration cross-entropy reduction, we find two failure modes of LLM reflection. On objective tasks with finite answer spaces, reflection yields near-zero information gain (Delta I approx 0), behaving as neutral re-generation indistinguishable from re-sampling. On subjective tasks, it yields significant negative gain (Delta I < 0), moving predictions away from the target. Human revision, by contrast, yields positive gain in both settings. Cross-agent experiments localize the failure to the revision step, not input quality: LLMs degrade even high-quality human responses. Diagnostic analyses (revision conditioned on first-pass correctness, and oracle-guided revision against a random-reshuffle baseline) show that which sub-step dominates varies by task and by model rather than reducing to a single mechanism: self-error detection is present on objective multiple-choice tasks but weak on subjective ones, and recovery under an oracle error signal exceeds the baseline for some models and falls below it for others. The unifying account is structural: without external information, self-conditioned revision cannot reduce uncertainty about the target, so LLM reflection is better understood as conditioned re-generation than as genuine error-driven revision.

## Metadata
- **Published**: 2026-07-31T00:15:32Z
- **Authors**: Yefan Tao, Gerald Friedland, Madhusudhanan Chandrasekaran, Luyang Kong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28908v1)