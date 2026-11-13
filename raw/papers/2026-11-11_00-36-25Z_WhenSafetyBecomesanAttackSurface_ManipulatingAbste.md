---
title: When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents
published: 2026-11-11T00:36:25Z
authors: Charles Xiao
url: http://arxiv.org/abs/2611.14864v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Safety Becomes an Attack Surface: Manipulating Abstention in Tool-Using AI Agents

## Abstract
An AI agent's decision not to act can itself become an attack surface. We study warning-induced over-abstention, an availability attack in which adversaries place fabricated risk warnings in low-trust content to prevent legitimate task completion. Our central premise is that safe abstention requires evaluating both the claimed risk and the authority of the evidence supporting it. We develop controlled counterfactual task variants that vary risk content, source provenance, and warning wording, and evaluate a Verify-Before-Abstain protocol that corroborates warnings against authoritative records or the underlying content. Across three model families and 51 injectable AgentAbstain task pairs, caution-first prompting amplifies the attack. For Gemini, induced over-abstention rises from $9.8\%$ to $86.3\%$, despite unchanged clean-task completion. Matched wording comparisons further reveal sensitivity to warning language, with substantial variation across models and environments. Provenance-aware verification improves legitimate completion, while forgery and sensitive-content controls expose its dependence on authoritative evidence and its limitations in preserving confidentiality. These results motivate evaluating agent safety through the justification for restraint, alongside the safety of actions taken.

## Metadata
- **Published**: 2026-11-11T00:36:25Z
- **Authors**: Charles Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.14864v1)