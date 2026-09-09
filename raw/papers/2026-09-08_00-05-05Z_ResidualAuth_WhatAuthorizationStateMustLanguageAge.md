---
title: ResidualAuth: What Authorization State Must Language Agents Preserve under Revocable Delegation?
published: 2026-09-08T00:05:05Z
authors: Moonwon Choi, Seokho Jeong, Seunggeun Lee
url: http://arxiv.org/abs/2609.08062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ResidualAuth: What Authorization State Must Language Agents Preserve under Revocable Delegation?

## Abstract
Tool-using language agents can delegate and revoke permissions while acting through external services. We show that two authorization histories can have identical current permissions and identical all-pairs reachability yet require opposite decisions after the same direct-edge revocation. We formalize the information needed to preserve such distinctions as a residual authorization state. We prove that exponentially many future-distinct states can share one fixed transitive closure, and give exact or tight asymptotic bounds on the state required by an exact monitor as delegation redundancy varies. ResidualAuth compiles these constructions into paired language-agent episodes. Across four open-weight models, a fixed 256-token summary solved 0-2/16 pairs, sham reads solved 0/16, and authenticated current-query reads solved 15-16/16. In a separate held-out online-memory diagnostic, exact ledger serializations fit all 128 four-coordinate pairs at both 768 and 1,024 tokens. At either cap, factually supported model-written memories sufficient for every prespecified continuation solved at most 1/128 pairs per model. A hard gate reduced eight observed unauthorized effects to zero without changing the preceding attempts. These results distinguish required authorization state, usable decision information, online state maintenance, and effect mediation.

## Metadata
- **Published**: 2026-09-08T00:05:05Z
- **Authors**: Moonwon Choi, Seokho Jeong, Seunggeun Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08062v1)