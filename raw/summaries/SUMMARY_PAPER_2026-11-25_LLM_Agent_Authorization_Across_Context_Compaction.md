---
title: LLM Agent Authorization Across Context Compaction
url: http://arxiv.org/abs/2611.32194v1
type: paper-summary
date: 2026-11-25
source_paper: 2026-11-24_08-44-15Z_LLMAgentAuthorizationAcrossContextCompaction.md
generated_at: 2026-11-25 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a critical security vulnerability in request-derived authorization systems for LLM agents: automatic context compaction destroys the attribution guarantee that underpins prompt-injection defenses. When frontier agents like Claude Code and Codex compress conversation history, they insert model-written summaries as user messages, causing authorization policies to be derived from the compactor's text rather than the user's actual words. The authors prove a general impossibility bound showing that any authorizer unable to verify byte-level provenance cannot distinguish forged records from legitimate ones, and they propose a fix that carries authenticated verbatim user text across compaction boundaries while still allowing the agent to read summaries.

## Key Takeaways
- Context compaction in production LLM agents (Claude Code, Codex) systematically places model-written summaries of earlier turns as user messages, so the compactor's quotation of user documents and injected text is indistinguishable from the user speaking. This breaks the attribution assumption on which request-derived authorizers like Progent depend, meaning the policy derived after compaction follows what the compactor wrote rather than what the user said.
- The vulnerability is not limited to injected instructions but extends to injected data: in a concrete example, when an attacker's notice states a different payee account as plain data and the user asks to pay rent, a policy derived from a frontier compactor's summary admits the attacker's account in 91% of cases, whereas the policy derived from the user's own words admits it in none. Frontier compactors mark injected instructions (which have no legitimate twin) but rarely mark injected data (which does), making the compactor's retention and marking choices a genuine security parameter.
- The authors prove a tight theoretical bound: an authorizer that cannot see who wrote which bytes cannot treat a forged record differently from the legitimate one it imitates by more than the two are distinguishable. Their proposed fix—crediting only authenticated verbatim user text carried across the compaction boundary while the agent still reads the summary—guarantees the authorizer receives exactly that text or nothing, so an attacker can block the policy but cannot shape it. Empirical validation across 40 attacked AgentDojo episodes confirms no attacker action completes under the fix.

## Context
This work sits at the intersection of LLM agent security, prompt injection research, and the practical engineering of long-running agent sessions. As autonomous agents increasingly handle multi-step tasks spanning many turns, context window limits force automatic compaction, a mechanism previously treated as a purely performance optimization. This paper reframes compaction as a security-critical operation that silently undermines the foundational assumptions of authorization frameworks designed to prevent prompt injection attacks. It connects theoretical impossibility results about provenance verification to concrete behaviors observed in frontier model deployments, bridging formal security guarantees and empirical agent behavior.

## Implications
For practitioners building agentic systems, this finding demands that context compaction pipelines be treated as part of the security boundary rather than an internal implementation detail: the choice of what a compactor retains, how it marks provenance, and whether it preserves verbatim user text directly determines whether authorization policies can be trusted. For the broader field, the impossibility bound establishes that no purely content-based authorizer can fully defend against injection when provenance metadata is lost, pushing the community toward authenticated transport mechanisms and provenance-aware architectures. Industry deployments of coding agents and autonomous assistants should audit their compaction strategies and adopt verbatim-authenticated text channels to close this gap before scaling to longer-running, higher-stakes tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.32194v1)
