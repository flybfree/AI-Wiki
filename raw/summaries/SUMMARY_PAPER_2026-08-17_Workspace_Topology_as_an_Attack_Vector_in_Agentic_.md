---
title: Workspace Topology as an Attack Vector in Agentic Coding Assistants
url: http://arxiv.org/abs/2608.14876v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_20-30-36Z_WorkspaceTopologyasanAttackVectorinAgenticCodingAs.md
generated_at: 2026-08-17 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how the structure of a developer’s workspace — defined by directory depth, codebase modularity, injection points within files, and context framing — influences the success rate of adversarial prompt injections in open‑weight coding assistants. Experiments across ten languages and six engineering domains reveal that highly modular environments lower attack success rates, while changes to injection position or added security cues can raise them significantly.

## Key Takeaways
- Highly modular codebases reduce the Attack Success Rate because malicious payloads are less likely to be executed in isolated modules.
- The depth of directory hierarchy and where an injection occurs within a file directly affect whether the prompt is interpreted as a legitimate request or a security breach.
- Adding explicit security cues or context framing can either mitigate or amplify attack success depending on how the model parses the workspace.

## Context
The rapid adoption of agentic coding assistants that operate with extensive filesystem access creates new vulnerabilities beyond traditional code injection. Understanding how workspace topology shapes these risks is essential for evaluating AI safety in real‑world development workflows, where testing environments are often not isolated from user data.

## Implications
Practitioners must design secure testing frameworks that preserve a clean workspace to obtain reliable ASR measurements. This insight guides developers in structuring codebases and prompting strategies to minimize exploitation risk, ultimately protecting sensitive information in AI‑assisted coding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14876v1)
