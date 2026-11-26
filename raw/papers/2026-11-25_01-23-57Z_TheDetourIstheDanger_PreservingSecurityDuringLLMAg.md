---
title: The Detour Is the Danger: Preserving Security During LLM Agent Recovery
published: 2026-11-25T01:23:57Z
authors: Boyang Ma, Jinku Li, Hao Wu, Sheng Gao, Man Zhou, Minghui Xu, Yue Zhang
url: http://arxiv.org/abs/2611.33605v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Detour Is the Danger: Preserving Security During LLM Agent Recovery

## Abstract
LLM agents increasingly rely on external tools and reusable Skills to execute complex workflows, autonomously replanning when operations fail. However, such recovery may preserve task functionality while silently discarding the security protections required by the original workflow. In this paper, we investigate workflow security downgrade, a failure-induced security threat in which agents execute sensitive operations without satisfying their original protection requirements. Unlike prompt injection, this threat exploits autonomous recovery decisions triggered by execution failures, without modifying instructions or tool definitions. We systematically evaluate this behavior through fault injection in an executable MCP/Skill environment spanning seven LLMs, twelve task templates, and three security-sensitive domains. To address this threat, we propose ARGUS, an obligation-preserving recovery framework that combines resource-bound security evidence, isolated recovery-plan validation, and execution-time enforcement. In a separate 864-run evaluation, ARGUS prevents all observed protection-loss events under enforcement, while recovery assistance yields model-dependent improvements in protected task completion over blocking alone. Our findings demonstrate that secure agent recovery requires preserving security obligations across workflow changes, rather than merely restoring task functionality.

## Metadata
- **Published**: 2026-11-25T01:23:57Z
- **Authors**: Boyang Ma, Jinku Li, Hao Wu, Sheng Gao, Man Zhou, Minghui Xu, Yue Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.33605v1)