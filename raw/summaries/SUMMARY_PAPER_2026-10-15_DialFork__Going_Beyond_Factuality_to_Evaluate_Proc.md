---
title: DialFork: Going Beyond Factuality to Evaluate Procedural Hallucination in Conversational Agents
url: http://arxiv.org/abs/2610.21561v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_09-18-32Z_DialFork_GoingBeyondFactualitytoEvaluateProcedural.md
generated_at: 2026-10-15 22:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces DialFork, the first benchmark designed to measure procedural hallucination in conversational agents—where an agent produces fluent, factually plausible utterances that nonetheless deviate from the intended conversational process. The authors construct 36,278 dialogues across 24 tasks and 12 domains by forking conformant dialogues and injecting four types of procedural hallucinations, then define three evaluation tasks spanning monitoring, retrieval, and real-time guardrail detection. Their proposed dialog-flow-aware metrics, FlowKL and FlowScore, demonstrate that semantic similarity metrics fail to capture procedural deviation, with FlowScore significantly outperforming all baselines across seven encoders.

## Key Takeaways
- Procedural hallucination is a distinct failure mode from factual hallucination: an agent can generate individually coherent and factually accurate utterances while still violating the expected conversational structure, such as skipping required steps, reordering procedures, or introducing irrelevant sub-processes. This failure mode has been largely overlooked in existing evaluation frameworks that focus on content accuracy.
- DialFork is constructed by taking conformant dialogues, forking them at controlled turn positions, and injecting one of four hallucination types, producing 36,278 dialogues validated by 30 human annotators. This construction method ensures the benchmark isolates procedural deviation from factual error, making it a targeted diagnostic tool rather than a general quality assessment.
- The proposed FlowScore metric significantly outperforms all baselines across seven different encoders, demonstrating that comparing how dialogues unfold structurally is fundamentally different from comparing their semantic content. This finding challenges the common assumption that embedding-based similarity can serve as a proxy for procedural correctness in conversational evaluation.

## Context
The evaluation of large language models deployed as conversational agents has historically centered on factual accuracy, toxicity, and instruction-following. However, as LLMs are increasingly embedded in multi-turn workflows such as customer service pipelines, medical triage protocols, and legal consultation processes, adherence to procedural structure becomes as critical as factual correctness. Existing benchmarks like those measuring hallucination in single-turn QA settings do not capture whether an agent follows the correct sequence of steps, asks prerequisite questions before providing answers, or maintains the expected conversational state machine. DialFork fills this gap by providing the first raw-dialogue-text benchmark explicitly targeting procedural deviation.

## Implications
For practitioners deploying conversational agents in regulated or process-sensitive domains such as healthcare, finance, and legal services, DialFork provides a concrete evaluation framework and open-source tooling (released under MIT license) to detect when agents drift from prescribed procedures in real time. The finding that semantic similarity metrics are inadequate substitutes for procedural similarity has direct consequences for model selection, monitoring dashboards, and guardrail design: teams relying on embedding-based similarity scores may be blind to structural failures that could compromise compliance, user trust, or operational safety. The three-granularity evaluation design—fleet-level monitoring, single-dialogue retrieval, and turn-level detection—offers a practical toolkit for building production guardrails that catch procedural drift before it compounds into downstream errors.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21561v1)
