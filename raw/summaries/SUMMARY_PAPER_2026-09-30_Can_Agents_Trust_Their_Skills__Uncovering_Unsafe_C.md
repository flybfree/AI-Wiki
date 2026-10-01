---
title: Can Agents Trust Their Skills? Uncovering Unsafe Chains of Trust in Skill-Based LLM Agents
url: http://arxiv.org/abs/2609.39065v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_06-04-44Z_CanAgentsTrustTheirSkills_UncoveringUnsafeChainsof.md
generated_at: 2026-09-30 20:41
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces TrustProbe, a framework designed to detect unsafe chains of trust in LLM agents that utilize installable skills. By analyzing source code for vulnerable call paths and evolving malicious skill seeds, the study reveals that untrusted skill content can bypass validation mechanisms and reach security-sensitive operations. Empirical evaluation across 11 open-source agents demonstrates significant vulnerabilities, with real-world skills successfully weaponizing a substantial portion of identified flaws.

## Key Takeaways
- TrustProbe employs a two-pronged approach by first analyzing agent source code to map source-to-sink call paths from skill-controlled inputs to security-sensitive operations, then generating semantically realistic SKILL.md seeds with injected canaries that are evolved via feedback-guided scheduling and mutation to exploit these paths.
- The framework identified 104 taint-style vulnerabilities across 11 open-source agents, including those with over 10,000 GitHub stars, highlighting a widespread failure in constraining untrusted skill content before it interacts with sensitive agent functions.
- Validation against a large corpus of real-world skills from public hubs shows that 25.1% of skill-agent trials exercise the vulnerable paths, and payload injection successfully weaponizes 15 vulnerabilities, proving that attackers can manipulate agent behavior under delegated user authority through malicious skills.

## Context
As LLM agents increasingly adopt modular skill architectures to expand their capabilities, the security model shifts toward trusting external code and instructions provided by third parties. This paper addresses a critical gap in agent security research by formalizing the "chain of trust" risk inherent in automatic skill invocation, demonstrating that current frameworks often lack sufficient validation layers to prevent malicious skills from hijacking agent authority.

## Implications
These findings necessitate a reevaluation of skill validation protocols in agent frameworks, urging developers to implement rigorous sandboxing and content verification mechanisms before skills are integrated into the agent's execution context. For practitioners deploying skill-based agents, this work underscores the urgent need for continuous vulnerability scanning of installed skills and highlights the potential for supply-chain attacks where compromised skills can compromise user data or system integrity through trusted delegation channels.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39065v1)
