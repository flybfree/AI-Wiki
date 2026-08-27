---
title: MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration
published: 2026-08-26T07:21:56Z
authors: Miseon Yu, Jaehoon Choi, Younghan Lee, Yunheung Paek
url: http://arxiv.org/abs/2608.25457v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MACGen: Toward Functionally Correct and Secure Code Generation via Multi-Agent Collaboration

## Abstract
Despite their strong ability to generate code, large language models often fail to produce secure code, as their outputs frequently contain security vulnerabilities. Secure code generation is inherently challenging because it requires solving a multi-objective problem: functional correctness and security. Existing approaches address this challenge by injecting external security knowledge or by using agentic feedback and iterative refinement. However, guideline retrieval often leaves the generator to translate generic advice into task-specific secure implementations, while shared-dialogue multi-agent feedback can blur role boundaries and suffer from context bloat.   We present MACGen, a multi-agent framework that integrates planning, security analysis, code synthesis and refinement to jointly optimize security and functionality. A planner constructs a step-by-step plan to satisfy functional requirements. A security advisor identifies likely CWEs and synthesizes task-specific guidelines, a coder then generates code grounded in these artifacts, and a reviewer issues perspective-separated feedback. Rather than sharing full dialogue histories, each agent receives only structured artifacts from upstream stages, enforcing role specialization and reducing uncontrolled context growth. On CWEval and BaxBench, MACGen improves F&S@1 over direct prompting by 19.61 and 10.57 percentage points (pp) on average, respectively.

## Metadata
- **Published**: 2026-08-26T07:21:56Z
- **Authors**: Miseon Yu, Jaehoon Choi, Younghan Lee, Yunheung Paek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25457v1)