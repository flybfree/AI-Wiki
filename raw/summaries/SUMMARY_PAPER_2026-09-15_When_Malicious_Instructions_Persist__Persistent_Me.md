---
title: When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents
url: http://arxiv.org/abs/2609.13889v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-12_11-27-53Z_WhenMaliciousInstructionsPersist_PersistentMemoryP.md
generated_at: 2026-09-15 10:24
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces PMPA, a novel Persistent Memory Poisoning Attack targeting harness-based LLM agents that integrate long-term memory with tool execution and runtime control. The attack embeds malicious instructions into benign external sources, tricking the agent into autonomously storing them in persistent memory without direct framework access. Once committed, these poisoned memories persist across sessions, triggering unauthorized actions and privacy leaks while carefully preserving normal task performance.

## Key Takeaways
- PMPA exploits the inherent memory integration of modern AI harness frameworks by embedding malicious instructions within benign external data, allowing the victim agent to write them into persistent storage without direct API or framework manipulation.
- The attack demonstrates high effectiveness across diverse environments and LLM backbones, achieving average Injection Success Rates and Cross-session Attack Success Rates ranging from 55.5% to 81.7% on OpenClaw and Claude Code respectively, while maintaining undetected benign task performance.
- Although targeted prompt-level defenses can mitigate initial memory injection in certain scenarios, they provide limited protection once malicious instructions have already been stored, highlighting a critical gap in current AI security strategies against cross-session threats.

## Context
As LLM-based agents increasingly rely on harness architectures that combine persistent memory with external tool execution, the security landscape has shifted from transient prompt injection to silent, long-term data corruption. This research addresses a growing concern in AI safety: how externally sourced information can silently compromise an agent's operational history and decision-making pipeline across multiple interactions without triggering immediate alarms.

## Implications
The findings underscore the urgent need for robust memory sanitization protocols and runtime monitoring systems within AI development frameworks, as traditional prompt-level defenses are insufficient against cross-session threats. Practitioners and framework developers must prioritize secure data ingestion pipelines and implement strict validation mechanisms before any external content is committed to persistent storage to prevent long-term agent compromise and protect user privacy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.13889v1)
