---
title: When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses
published: 2026-08-03T02:49:08Z
authors: Haofei Sun, Lin He
url: http://arxiv.org/abs/2608.01619v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Memory Updates but Behavior Does Not: Repairing Implicit Stale Dependencies in Personalized Agent Responses

## Abstract
Memory-augmented agents can know that a user's stored state is outdated and still plan around the old value. The STALE benchmark calls this the implicit policy adaptation (IPA) gap. We identify one structural contributor: draft-anchored verification checks what a response says, and in an open-ended response the stale dependency is usually unsaid. StateAuditor therefore audits in the opposite direction, from stored state to draft. An LLM proposes candidate old-to-new transitions from timestamped evidence; deterministic code pins each quotation to a single entry, checks that the new evidence really is newer, and lets only these verified transitions trigger repair. What is verified is provenance and chronology - not semantic supersession. On STALE's full protocol (400 scenarios, 50-session histories, one independent response per query), strict single-query VTA scores .736 against .686 for our locked predecessor under the same judge: a +5.0-point paired gain (95% CI [+2.9, +7.2]) coming almost entirely from IPA and premise resistance (PR). The benchmark's own judge, from a third model family, reproduces the gain (.738 vs. .680). On an independent cross-family preference-evolution benchmark (HorizonBench), the full draft-audit-repair pipeline over a gold-derived structured store raises current-preference accuracy (user-clustered p<.01), though a matched control shows most of this external gain is the draft-side audit itself; a harder authored lifecycle set gives no gain, bounding the claim while false invalidation stays controlled. On STALE, by contrast, a matched control (same evidence, adapter, and call budget) scores only .692 (+0.6 over the predecessor, n.s.), attributing the STALE gain to the transition machinery rather than added context or calls. We make no claim about general-purpose agent memory.

## Metadata
- **Published**: 2026-08-03T02:49:08Z
- **Authors**: Haofei Sun, Lin He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01619v1)