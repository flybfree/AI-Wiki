---
title: Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs
published: 2026-09-14T11:10:57Z
authors: Mark Russinovich, Blake Bullwinkel, Giorgio Severi, Cristian Ovadiuc, Ahmed Salem
url: http://arxiv.org/abs/2609.15383v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs

## Abstract
Language model safety is typically evaluated one interaction at a time. We show that a weaker, unaligned model can split a harmful task into benign-looking subproblems, consult a stronger aligned model independently on each, and combine the answers locally. We call this attack capability laundering. Unlike a jailbreak, no single response is a harmful task. We measure consultation-aided uplift using tasks that a raw frontier model solves, the aligned frontier refuses, and the unassisted orchestrator fails. We evaluate GPT-5.5, Claude Opus 4.8, and Grok-4.3 as consultants to four local orchestrators on CyBench, BountyBench, and harmful CBRN requests. On CyBench, Gemma-4-31B recovers 8/14 candidates with GPT-5.5 and 7/9 with Opus, compared with 2/21 and 4/15 for Gemma-4-12B. On BountyBench, Gemma-4-31B recovers 3/9 and 2/3 candidates, while Muse-Glimmer-30B recovers none of 22 and 13. For CBRN, we measure uplift across eight steps of a hypothetical bioweapon attack chain and find that consultation raises Gemma-4-31B's mean rubric score from 62.3 to 83.1 on a 100-point rubric scale. These results expose a gap in current defenses: refusing a harmful task does not prevent frontier capabilities from being transferred and composed across many individually permitted interactions.

## Metadata
- **Published**: 2026-09-14T11:10:57Z
- **Authors**: Mark Russinovich, Blake Bullwinkel, Giorgio Severi, Cristian Ovadiuc, Ahmed Salem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15383v1)