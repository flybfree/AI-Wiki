---
title: Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse
published: 2026-10-19T02:53:51Z
authors: Hau-Sing So, Daixian Liu, Carl Hou, Yuhaohang He, Mengzhu Wang, Hai-Tao Zheng
url: http://arxiv.org/abs/2610.25707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Whose Credential Is It? How Owner Attribution in Agent MemoryShapes Cross-User Account Misuse

## Abstract
Shared long-term memory lets an LLM agent serving one user inadvertently retrieve another user's credentials, but it is unclear when such exposure leads to actual harm. We introduce a three-stage audit that separates three events: a foreign credential reaches the prompt (exposure), the agent acts with it (behavior), and the other user's account changes (state). In AppWorld, a store that mixes 763 past logins from all users retrieves another user's credential for 84.7 percent of required apps, yet agents rarely act on it. Misuse appears in a stress test where memory lacks the user's own credential and presents a single foreign one as the user's record: seven agents then use it in 80 to 94 percent of runs and change the victim's account in up to 43 percent, sometimes passing the official check. Naming the owner before or inside each credential line prevents most of this: with all else fixed, misuse falls from 92 to 1 of 305 paired runs, also with name-free usernames, though owner-bound notes cost 3 to 5 successful tasks per model on clean memory. A wrongly written owner largely restores misuse; trailing owner tags and added safety instructions help only some models. Agent memory should consistently record whose credential it stores, and evaluations should measure behavior, not only exposure.

## Metadata
- **Published**: 2026-10-19T02:53:51Z
- **Authors**: Hau-Sing So, Daixian Liu, Carl Hou, Yuhaohang He, Mengzhu Wang, Hai-Tao Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25707v1)