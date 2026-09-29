---
title: CUA-SWE: When Computer-Use Agents Meet Visual Software Engineering
url: http://arxiv.org/abs/2609.32600v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_13-18-00Z_CUA_SWE_WhenComputer_UseAgentsMeetVisualSoftwareEn.md
generated_at: 2026-09-28 20:59
model: qwen3.6-35b-a3b
---

## Summary
CUA-SWE presents a unified benchmark, environment, and evaluation pipeline that integrates computer-use capabilities into software engineering agents, addressing the underexplored need for agents to combine code editing with runtime interaction and visual inspection. The work demonstrates that effective diagnosis and repair require connecting visual observations of application behavior to responsible source code changes, verifying repairs through execution while ensuring deterministic correctness across four diverse domains.

## Key Takeaways
- CUA-SWE mandates a holistic development workflow where agents must modify code and configuration, execute commands, interact with running software, and inspect visual feedback within the same task, bridging the isolation between traditional coding agents and computer-use models.
- The benchmark evaluates whether agents can successfully complete tasks when critical specification or operational information is available exclusively through the application's visual interface, highlighting the essential role of GUI feedback in guiding diagnosis and repair decisions.
- Evaluation includes deterministic, task-specific tests that verify resulting software satisfies requirements and preserves specified behavior, allowing researchers to characterize how frontier agents leverage source-level execution alongside screenshots and graphical interaction to produce verified changes and analyze development behaviors linked to successful repairs.

## Context
As AI research shifts from static code generation toward dynamic agents capable of operating in complex environments, this paper addresses a critical gap by formalizing the integration of visual perception with software engineering workflows. It matters because it moves beyond syntax-aware coding

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32600v1)
