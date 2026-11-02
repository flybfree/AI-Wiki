---
title: Agentic process evidence
url: http://arxiv.org/abs/2610.40071v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-29_13-50-54Z_Agenticprocessevidence.md
generated_at: 2026-11-01 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Agentic Process Evidence (APE), a signed, tamper-evident, machine-readable attestation framework designed to capture and govern the ephemeral reasoning, decisions, and tool calls made by AI agents operating autonomously across the Software Development Life Cycle. The authors argue that existing governance and audit mechanisms—built entirely around the assumption that a human made every decision—fail to account for agentic provenance, and they propose APE as a protocol-level solution that links agent sessions to their outcomes while enabling Policy-as-Code enforcement with human-in-the-loop intervention only when necessary.

## Key Takeaways
- AI agents now function as autonomous team members in the SDLC, creating pull requests, selecting dependencies, refactoring codebases, interpreting test failures, and executing infrastructure changes, yet their reasoning and tool-call chains vanish at session end, making them unaccountable "insider threats" for which no widely adopted provenance or governance standard currently exists.
- The authors identify three core procedural problems introduced by agentic coding: the supply-chain vector (the agentic coder is itself software and thus a supply-chain security risk), policy guardrails (ensuring the agent complies with organizational policies), and task-alignment (verifying the agent is aligned with its assigned tasks and goals). These are framed as governance gaps rather than scale problems.
- APE is built on an in-toto-style attestation framework, producing signed, tamper-evident, machine-readable records that connect an agent's session to its outcome through process-aware logging, and the protocol is explicitly aligned with existing regulatory requirements to support compliance and audit workflows.

## Context
The rapid integration of large language model agents into production software pipelines has outpaced the governance tooling designed for human developers. Git logs, CI/CD audit trails, and compliance frameworks all assume a persistent, identifiable human decision-maker, an assumption that breaks down when autonomous agents perform multi-step reasoning across sessions. This paper sits at the intersection of software supply-chain security (in-toto, SLSA, SBOM), AI safety governance, and regulatory compliance, addressing a gap that regulators and enterprise security teams are increasingly encountering as agentic coding tools enter regulated industries.

## Implications
For practitioners, APE provides a concrete protocol that could be integrated into existing CI/CD and artifact-attestation pipelines, enabling organizations to enforce Policy-as-Code guardrails over agentic workflows without requiring constant human oversight. For industry and regulators, the framework signals a shift from human-centric audit models to machine-verifiable process evidence, potentially shaping future compliance standards for AI-assisted software development and reducing the attack surface created by intent-mismatch and injection incidents in agentic systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.40071v1)
