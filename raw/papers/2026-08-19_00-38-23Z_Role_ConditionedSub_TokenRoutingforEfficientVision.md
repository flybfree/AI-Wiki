---
title: Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies
published: 2026-08-19T00:38:23Z
authors: Wei Jiang, Wei Wang
url: http://arxiv.org/abs/2608.18410v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Role-Conditioned Sub-Token Routing for Efficient Vision-Language-Action Policies

## Abstract
Vision-Language-Action (VLA) models process long multimodal token sequences, making inference expensive in both memory and computation. Existing efficiency methods mainly reduce visual tokens, but aggressive token pruning becomes fragile because removing a token discards its entire representation. Sub-token compression provides a complementary alternative by retaining more tokens while reducing their value width. However, directly applying sub-token compression to VLA policies is less effective because information important for perception, language understanding, and control is distributed differently across the multimodal representation.   We introduce Role-Conditioned Sub-Token Routing (RoleSub), which learns how to compress the value representations of retained tokens. After visual token reduction, RoleSub partitions each retained value representation into groups in an orthogonal space and uses a lightweight router to determine which groups should be preserved. The routing decision is conditioned on the token representation, a learned latent role representation, and language context. The same mechanism can also be applied to language values, allowing visual and language representations to be compressed without removing additional tokens.   We evaluate RoleSub on OpenVLA-OFT-7B across the four LIBERO suites. At matched visual-KV budgets, RoleSub outperforms a trained token-only control in 33 of 36 settings, with the largest gains under aggressive compression. Combining visual and language compression reduces total KV to 9.2--11.3% of the original while retaining strong control performance on most tasks. These results show that reducing the representation within retained tokens provides an effective complement to token pruning for aggressive VLA compression.

## Metadata
- **Published**: 2026-08-19T00:38:23Z
- **Authors**: Wei Jiang, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18410v1)