---
title: LongHarness: Advancing Agentic Reasoning over 100M-Token Corpora via Stateful Evidence Management
url: http://arxiv.org/abs/2610.13075v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_06-32-02Z_LongHarness_AdvancingAgenticReasoningover100M_Toke.md
generated_at: 2026-10-11 21:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
LongHarness introduces a model-agnostic agent harness designed to tackle corpus-level long-context reasoning over document collections that exceed model context windows, such as 100-million-token corpora. Its core innovation, Evidence-Conclusion Coevolution, explicitly manages the interaction between acquired evidence and evolving conclusions to prevent two coupled failure modes: unbounded exploration and evidence-state drift. Evaluations on OfficeQA Pro, AA-LCR, and LongBench v2 demonstrate substantial improvements, with exact match scores jumping from 15.8% to 60.2% on OfficeQA Pro V1 and surpassing state-of-the-art agent harnesses like Claude Code and Codex by 12 to 19 percentage points.

## Key Takeaways
- LongHarness addresses two coupled failure modes in existing agent harnesses: unbounded exploration, where retrieval continuously expands the interaction history without resolving decision-relevant information gaps, and evidence-state drift, where previously acquired evidence or subsequent corrections fail to inform the current conclusion. By making the interaction between evidence and conclusions explicit rather than leaving them entangled in a growing interaction history, LongHarness prevents these degradation patterns.
- The Evidence-Conclusion Coevolution mechanism uses unresolved conclusions to guide exploration toward missing information, while newly acquired evidence strengthens or revises the conclusions that directed the search. This creates a feedback loop that focuses retrieval on remaining information needs rather than indiscriminately expanding the search space, coupled with Evidence Lifecycle Management that keeps accumulated evidence current and traceable throughout the interaction.
- Quantitative results show dramatic performance gains: GLM-5.3-Flash exact match on OfficeQA Pro improves from 15.8% to 60.2% on V1 and from 4.4% to 61.1% on V2 compared to direct reasoning with the same backbone. Against Claude Code, LongHarness surpasses it by 12.0 points on V1 and 18.9 points on V2; against Codex, it leads by 12.0 points on V2. With Qwen3.8-Flash, it reaches 61.7% on V1, outperforming Claude Code by 8.3 points and Codex by 12.0 points.

## Context
As large language models are increasingly deployed for enterprise knowledge retrieval, legal document analysis, and scientific literature synthesis, the challenge of reasoning over corpora far exceeding any single model's context window has become a central bottleneck in AI systems. Existing agent harnesses provide incremental access to large document collections but lack principled mechanisms for managing the state of evidence and conclusions across multi-step interactions. LongHarness fills this gap by introducing explicit state management that decouples evidence accumulation from conclusion formation, representing a significant architectural advance in how agentic systems handle long-horizon reasoning tasks.

## Implications
For practitioners building retrieval-augmented agents over large document corpora, LongHarness offers a model-agnostic framework that can be layered on top of existing backbones without retraining, making it immediately deployable across diverse model ecosystems. The demonstrated improvements over Claude Code and Codex suggest that structured evidence management, rather than raw model capability, is the critical bottleneck in corpus-level reasoning, redirecting research and engineering effort toward harness design rather than solely toward scaling model parameters. This has practical consequences for industries such as legal research, pharmaceutical literature review, and enterprise knowledge management, where accurate multi-document synthesis over millions of tokens is a core operational requirement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13075v1)
