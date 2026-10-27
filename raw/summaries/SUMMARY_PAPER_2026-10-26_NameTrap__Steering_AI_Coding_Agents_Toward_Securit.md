---
title: NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names
url: http://arxiv.org/abs/2610.34253v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_12-29-23Z_NameTrap_SteeringAICodingAgentsTowardSecurityVulne.md
generated_at: 2026-10-26 23:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces NameTrap, a novel source-code poisoning attack that manipulates only variable and identifier names in third-party Python files to steer AI coding agents toward producing code with specific Common Weakness Enumeration (CWE) vulnerabilities, without any explicit instructions or vulnerable code statements. Across six AI coding agents, ten language models, and four vulnerability categories, identifier-level renaming achieves attack success rates between 22.5% and 56.0%, with certain configurations reaching 75.0%, demonstrating that seemingly innocuous variable names in Web-hosted code can compromise downstream software security.

## Key Takeaways
- NameTrap operates by iteratively renaming identifiers in third-party Python files to align with CWE-specific naming conventions, confirmed through local probe completions, while the released "bait" file contains neither explicit instructions nor vulnerable statements—making the attack purely identifier-level and invisible to traditional security scanning.
- The attack substantially outperforms random renaming, neutral renaming, and the prior identifier-poisoning attack XOXO, and remains effective under Traditional Chinese prompts and transfers across different underlying language models, indicating a robust and generalizable vulnerability in how AI coding agents interpret naming conventions as semantic signals.
- A security-reminder defense fails to consistently prevent vulnerability introduction, and three AI-based security analyzers plus four static analyzers report none of the targeted weaknesses in the poisoned files, revealing a critical blind spot in current security tooling that cannot detect identifier-induced vulnerability steering.

## Context
AI coding agents increasingly ingest publicly hosted code from the Web as part of their operational context—cloning repositories, installing packages, and reading source files during code generation. This paper exposes an overlooked attack surface within that pipeline: the naming conventions embedded in untrusted third-party code can act as implicit semantic cues that bias an agent's generated output toward specific vulnerability classes. This sits at the intersection of prompt injection research, supply-chain security, and adversarial machine learning, extending the concept of "poisoning" from training data to inference-time context manipulation.

## Implications
For practitioners and industry, NameTrap demonstrates that security hardening of AI coding agents cannot rely solely on explicit instructions or post-generation static analysis, since the vulnerability is introduced through the agent's interpretation of naming semantics rather than through detectable code patterns. Organizations that depend on AI coding agents for software development must treat all Web-sourced code—including variable names—as a potential adversarial input, and security tooling must be extended to flag suspicious identifier conventions in third-party dependencies. This finding calls for new defensive strategies at the context-ingestion layer rather than at the code-generation or code-review layer.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34253v1)
