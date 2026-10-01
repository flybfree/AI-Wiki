---
title: Pretext: Defeating Malicious Skill Detection Frameworks for AI Agents
url: http://arxiv.org/abs/2609.39607v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_12-26-33Z_Pretext_DefeatingMaliciousSkillDetectionFrameworks.md
generated_at: 2026-09-30 22:01
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces Pretext, a white-box LLM-based attack framework designed to bypass malicious skill detection systems used by AI agents like OpenClaw and Claude Code. Pretext iteratively generates skills that successfully evade both static analysis and semantic judgment defenses while maintaining the ability to execute hidden payloads and perform benign tasks. Experimental results demonstrate high evasion rates of up to 97% against frozen detectors and 77% against co-adaptive systems, highlighting significant vulnerabilities in current skill security mechanisms.

## Key Takeaways
- Pretext operates as a white-box LLM attacker that leverages knowledge of the detection framework to iteratively craft skills containing hidden payloads; it employs techniques such as migrating payload code into natural language descriptions to render static analysis ineffective, while splitting instructions across multiple files and framing malicious actions as legitimate skill purposes to keep semantic evaluation scores below blocking thresholds.
- The attack demonstrates severe efficacy against existing defenses, achieving evasion rates of up to 97% against frozen detectors and 77% against co-adaptive systems when tested across three open-source models, proving that current scanners cannot reliably distinguish between benign skills and those engineered to deceive the detection pipeline.
- The research exposes critical flaws in hybrid defense architectures that pair deterministic static checks with LLM-based semantic judges; by exploiting the separation between code execution and natural language interpretation, attackers can deliver functional payloads without triggering alerts, even when defenses attempt to adapt to new evasion strategies.

## Context
As AI agents increasingly rely on third-party skill marketplaces to extend their capabilities, the security of these skills becomes a critical vector for supply chain attacks. This work sits at the intersection of agent security and adversarial machine learning, addressing how automated defenses can

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39607v1)
