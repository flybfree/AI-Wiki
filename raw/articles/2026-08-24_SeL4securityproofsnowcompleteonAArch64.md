---
title: SeL4 security proofs now complete on AArch64
date: 2026-08-24
url: https://proofcraft.systems/news-2026/#2026-08-21
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://proofcraft.systems/news-2026/#2026-08-21
source_feed: Hacker News
ai_relevance: include
ai_topic: safety-governance
ai_reason: meets AI relevance threshold
scraped: 2026-08-24 08:10
---

# SeL4 security proofs now complete on AArch64

## Full Article

21 Aug 2026
seL4 security proofs now complete on AArch64
After completing the proofs of
functional correctness
and
integrity
,
Proofcraft has now established the proof that seL4 enforces
confidentiality
on
AArch64, providing a formal mathematical proof that the kernel prevents an
application running on top of seL4 from learning information without
authorisation.
Thanks to continued support from
NCSC
, this milestone completes the formal
proof that the seL4 implementation code on AArch64 enforces security isolation
of the applications running on top (under the assumptions listed
here
). This
isolation prevents attacks on non-critical applications from propagating to
critical applications and compromising them.
[Status of seL4 proofs on
AArch64 with now confidentiality done and system initialisation started]

## Metadata
- **Source**: [Original Article](https://proofcraft.systems/news-2026/#2026-08-21)
