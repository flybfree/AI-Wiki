---
title: Protocol Compression Changes Which Party Pays: Bilateral Cost in Cross-Organization LLM Agent Communication
published: 2026-09-05T14:54:45Z
authors: Janghoon Lee
url: http://arxiv.org/abs/2609.06129v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Protocol Compression Changes Which Party Pays: Bilateral Cost in Cross-Organization LLM Agent Communication

## Abstract
Agents that talk across organizations exchange long messages billed by the token. A shorter notation therefore looks like a saving that costs nothing but an agreement to use it. Recent work reports the saving is conditional. Compressed notation can instead raise total tokens by 8% to 11% over a JSON baseline, when parsing failures force extra model calls. That is measured for one payer. Between two organizations neither side can install a decoder at the other end, and each pays under its own tokenizer, price, and cache state. We measure both sides. A preregistered token-level study covered 198 content-matched item pairs across six vendors, for 2,376 native-usage cells. We then overlay an English baseline, runtime schema negotiation followed by compression, and injected-schema compression on a two-party procurement bargain with an exactly enumerated feasible set. The overlay covers 1,053 completed dialogues of a 1,215-cell grid across 3 model pairs, plus a 405-dialogue rerun of the negotiated condition. Compression amplifies cross-vendor cost dispersion by a factor of 1.078, with a 95% CI of [1.066, 1.091], and two vendor pairs reverse which endpoint is cheaper. Runtime negotiation succeeds as a protocol and fails as a bargain. The parties agree a schema in 121 of 135 headline dialogues, none of them the schema we would have supplied. They settle the task in only 9 of those dialogues, and they reach impasse in 106 of them. The negotiated sessions average 10.8 turns against 17.6, and cost 52% of the English total because sessions end sooner, not because the handshake is repaid. Break-even horizons run from 20 to 70 turns, the low end only under the conditional accounting, and all of them lie above every observed English session. On one cross-vendor pair both parties keep about half their cost. On the other the receiving party pays more at a high cache-hit rate.

## Metadata
- **Published**: 2026-09-05T14:54:45Z
- **Authors**: Janghoon Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06129v1)