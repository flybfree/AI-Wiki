---
title: AECP: Artifact-Exclusive Communication Protocol for Multi-Agent Code Generation
url: http://arxiv.org/abs/2610.06481v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-05_15-08-14Z_AECP_Artifact_ExclusiveCommunicationProtocolforMul.md
generated_at: 2026-10-05 22:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Artifact-Exclusive Communication Protocol (AECP), a framework that shifts coordination responsibility from individual AI agents to the execution harness in multi-agent code generation systems. By requiring agents to communicate exclusively through structured artifacts rather than free-form messages, AECP enables the harness to automatically supply relevant findings, screen implementations for interface mismatches, and enforce revision of agreements. The protocol yields a 28.2% improvement in average test pass rate and a 16.5% reduction in wall time across multiple benchmark tasks, while also eliminating the propagation of malicious instructions between agents.

## Key Takeaways
- AECP fundamentally restructures multi-agent coordination by making shared information actionable during execution rather than leaving it as passive context. The harness injects findings directly when agents access relevant code, screens implementations against recorded interface commitments, and mandates that affected agents revisit revised agreements. This removes the burden from individual agents to interpret and incorporate shared findings from prior messages, which previously led to unused information and undetected deviations from interface agreements.
- Empirical evaluation across Doc2Repo, NL2Repo, and CodeProjectEval benchmarks using both closed-source (Opus-4.8) and open-source (DeepSeek-V4-Flash) models demonstrates that AECP improves average test pass rate by 28.2% and reduces average wall time by 16.5% compared to agent teams relying on free-form inter-agent messaging. These gains hold across model families, suggesting the protocol's benefits stem from structural coordination rather than model-specific capabilities.
- AECP provides a significant security benefit by blocking the relay of malicious instructions between agents. The rate at which malicious instructions reach other agents drops from 95% to 0%, and the rate at which those agents act on them drops from 40% to 0%. This is achieved because structured artifacts constrain the communication channel, preventing adversarial or injected instructions from propagating through the agent network.

## Context
As large language models are increasingly deployed as autonomous coding agents tackling repository-level software engineering tasks, multi-agent orchestration has become a dominant paradigm for scaling beyond single-agent limitations. However, the coordination mechanisms in these systems remain largely ad hoc, relying on free-form natural language messages that agents must interpret and act upon independently. This paper addresses a critical gap in the multi-agent systems literature by formalizing a communication protocol that externalizes coordination logic into the execution harness, aligning with broader trends in AI safety and reliability engineering where structural constraints outperform behavioral instructions.

## Implications
For practitioners building multi-agent coding pipelines, AECP offers a practical protocol that can be integrated into existing agent frameworks to improve reliability, reduce execution time, and mitigate prompt-injection or adversarial instruction risks without requiring changes to the underlying language models. For the broader AI research community, the finding that harness-level coordination outperforms agent-level interpretation suggests that future multi-agent systems should invest in structured communication protocols and execution-time enforcement mechanisms rather than relying on agents to self-coordinate through unstructured dialogue. This has direct implications for enterprise software automation, where undetected interface mismatches and unused shared context can silently degrade code quality and increase debugging costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.06481v1)
