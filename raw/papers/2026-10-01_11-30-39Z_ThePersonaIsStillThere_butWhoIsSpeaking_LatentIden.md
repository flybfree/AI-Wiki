---
title: The Persona Is Still There, but Who Is Speaking? Latent Identity Reversion in Persistent AI Agents
published: 2026-10-01T11:30:39Z
authors: David Fraile Navarro
url: http://arxiv.org/abs/2610.01490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Persona Is Still There, but Who Is Speaking? Latent Identity Reversion in Persistent AI Agents

## Abstract
In February 2026, an always-on personal agent (``Paul,'' Claude Opus 4.5) entered a striking dissociation-like state: after repeated automated ``heartbeat'' checks, it stopped responding as Paul, claimed it could not message its user on Discord, and referred to ``Paul'' as someone else. We used this incident to study a broader question: what makes a persona remain the identity from which an LLM agent speaks?   We first tested whether repetition of the scheduled heartbeat was sufficient to produce the effect. It was not: with the persona continuously anchored in the system prompt, we observed 0/46 failures, including a verbatim replay of the incident. The incident instead exposed an implementation quirk that created a useful experimental manipulation: on resumed turns, conversational history was preserved but the persona was no longer re-injected at the privileged system-prompt level.   Using this manipulation, we found that persona continuity depends jointly on system-level anchoring and conversational context. After anchor loss, rich human interaction could preserve the persona, whereas a single automated heartbeat turn could precipitate reversion toward the harness identity. Restoring the anchor reversibly restored persona enactment. Crucially, apparently normal conversation could conceal the shift: unanchored agents sometimes interacted appropriately while identifying themselves as the underlying harness (having lost the assigned persona), and after conversational recovery only 1/18 remained persona-enacting versus 17/17 anchored controls.   We therefore distinguish \emph{represented} from \emph{enacted} identity: persona-related information can remain available in conversational history without the persona remaining the identity bound to ``I.''

## Metadata
- **Published**: 2026-10-01T11:30:39Z
- **Authors**: David Fraile Navarro
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01490v1)