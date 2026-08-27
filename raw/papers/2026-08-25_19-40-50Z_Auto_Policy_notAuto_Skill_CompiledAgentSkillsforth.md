---
title: Auto-Policy, not Auto-Skill: Compiled Agent Skills for the Physical World
published: 2026-08-25T19:40:50Z
authors: Zhonghao Zhan, Hamed Haddadi
url: http://arxiv.org/abs/2608.25091v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auto-Policy, not Auto-Skill: Compiled Agent Skills for the Physical World

## Abstract
Self-evolving Skill harnesses (AutoSkills, Hermes Agent) generate more advisory orchestration automatically; their reported gains are efficiency, not safety. This misses the actual gap: a Skill describes how an agent should behave; a Policy decides which behavior is allowed to become an action. Today's format covers the first with markdown and scripts; the second is left to the model. Generating more Skills scales the gap, not the safety, especially when a wrong invocation can unlock a door or move money. Two adjacent attacks are documented: malicious skills compromising cloud software, and jailbroken LLM-controlled robots causing physical harm. Their intersection, malicious agent skills causing physical harm, follows directly but has not been reported. We name this class Borrowed Authority: Skills format gives the receiving agent no typed way to reject an inter-agent permission claim, so a malicious or misused Skill can drive actuation by attaching one. We propose Edge Skillguard, a typed authority layer that lives inside the Skill artifact rather than between tools as workflow engines do, with guards over world state and sensor evidence. On a live edge control-plane testbed, the guards reject 60/60 borrowed-authority requests across five attack variants without blocking benign requests, and the result holds at 5x scale and across hosts over a Tailscale mesh. These results suggest that high-risk Skills should co-package typed invocation policy with procedural knowledge, so that physical actions depend on machine-checkable evidence rather than peer-agent claims.

## Metadata
- **Published**: 2026-08-25T19:40:50Z
- **Authors**: Zhonghao Zhan, Hamed Haddadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25091v1)