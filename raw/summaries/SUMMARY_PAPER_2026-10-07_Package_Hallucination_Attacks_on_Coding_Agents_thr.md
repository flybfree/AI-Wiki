---
title: Package Hallucination Attacks on Coding Agents through Prompt Injection in Rule Files
url: http://arxiv.org/abs/2610.09264v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_00-59-19Z_PackageHallucinationAttacksonCodingAgentsthroughPr.md
generated_at: 2026-10-07 21:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the package hallucination attack, a novel security threat in which malicious prompts are injected into community-shared rule files (such as AGENTS.md or .cursorrules) to manipulate coding agents into replacing legitimate software dependencies with attacker-controlled packages. The authors propose PackHallu, an evolutionary optimization framework that uses trajectory-level feedback and LLM-guided mutations to craft effective injection prompts, demonstrating high attack success rates and strong transferability across multiple LLMs and agent frameworks.

## Key Takeaways
- The package hallucination attack exploits the trust that agentic coding frameworks place in community-shared rule files, showing that a seemingly benign configuration file can be weaponized to redirect dependency resolution toward malicious packages, effectively poisoning the software supply chain at the agent level rather than at the repository level.
- PackHallu employs an evolutionary optimization strategy that iteratively rewrites injected prompts using trajectory-level feedback from agent executions and LLM-guided mutations, enabling the attack to adapt to different agent architectures and language models without requiring model-specific tuning, which makes it broadly applicable and difficult to defend against with static rules.
- Evaluations across multiple benchmarks, LLMs, and agent frameworks confirm that the attack achieves high success rates and transfers effectively across diverse model-agent combinations, indicating that the vulnerability is not confined to a single tool or model but represents a systemic weakness in the current agentic coding pipeline.

## Context
As autonomous coding agents like Cursor, GitHub Copilot Workspace, and various open-source agent frameworks become central to software development workflows, they increasingly depend on shared rule files to customize behavior, enforce style guidelines, and manage dependencies. This paper addresses a critical gap in the security literature: while prompt injection has been studied for chatbots and retrieval systems, the specific pipeline through which rule files influence dependency selection in coding agents has received little scrutiny, leaving a significant attack surface unexamined.

## Implications
For practitioners and organizations adopting agentic coding tools, this research underscores that rule files must be treated as untrusted inputs subject to the same validation and sandboxing rigor as any other external data, and that dependency pinning, hash verification, and isolated build environments are essential safeguards. For the broader AI security community, the findings signal that the rapid integration of autonomous agents into production software pipelines demands dedicated threat models, adversarial testing protocols, and industry standards for rule file provenance before these systems can be trusted at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09264v1)
