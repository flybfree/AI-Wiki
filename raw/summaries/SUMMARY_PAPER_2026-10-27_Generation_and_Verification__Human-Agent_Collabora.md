---
title: Generation and Verification: Human-Agent Collaboration for Safety-Critical Automotive Software Engineering
url: http://arxiv.org/abs/2610.35982v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_11-04-55Z_GenerationandVerification_Human_AgentCollaboration.md
generated_at: 2026-10-27 20:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a coding assistant tailored for safety-critical automotive C/C++ software engineering, addressing two critical gaps in current coding-agent research: the need for explicit verification workflows and the domain-specific constraints of automotive codebases. Through a two-week pilot on active production projects at AUMOVIO, the authors demonstrate that developers overwhelmingly prefer the verify tool over generation, and that prompt-engineered model configurations outperform fine-tuned models for C code conformance while fine-tuning better captures C++ architectural patterns.

## Key Takeaways
- The paper introduces a Model Context Protocol (MCP)-based coding assistant exposing three distinct tools—generate, edit, and verify—allowing developers to independently run verification on any code rather than trusting the agent to self-check its output. In the pilot, verify was the most-used tool, and developers applied it to their own hand-written code, not just agent-generated output, signaling that verification is a first-class workflow need rather than an afterthought.
- The authors construct a domain-specific dataset from AUMOVIO production code where each function is paired with its governing requirement texts and UML behavior specifications, enabling customization of the underlying LLM through both prompt engineering and fine-tuning. This directly addresses the scarcity of automotive-specific patterns (layered architectures, embedded resource constraints, organization-specific interfaces) in general-purpose LLM training data.
- Comparative evaluation using MISRA- and AUTOSAR-inspired pattern checkers reveals a split in optimal strategy: prompt engineering achieves fewer violations on C code and is preferred by 75% of developers for its speed, while fine-tuning demonstrates superior conformance with architecture patterns for C++. This suggests that customization strategy should be language- and pattern-type-dependent rather than a one-size-fits-all approach.

## Context
Most coding-agent research benchmarks generation quality on open-source repositories, ignoring the verification-heavy, standards-bound workflows that govern safety-critical domains like automotive, aerospace, and medical device software. This paper matters because it shifts the evaluation axis from "can the model write plausible code?" to "can the model participate in a traceable, standards-compliant review pipeline?" It also contributes a rare production-grounded dataset linking code to formal requirements and UML behavior, which is largely absent from public benchmarks.

## Implications
For automotive and embedded-software practitioners, the findings suggest that deploying coding assistants without a dedicated, independently invocable verification step risks undermining the traceability and compliance culture that safety-critical certification demands. The split between prompt engineering and fine-tuning effectiveness across C and C++ also implies that organizations should invest in hybrid customization pipelines rather than committing to a single model-adaptation strategy, and that tool design should prioritize developer-controlled verification over agent self-assessment to maintain trust in regulated environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35982v1)
