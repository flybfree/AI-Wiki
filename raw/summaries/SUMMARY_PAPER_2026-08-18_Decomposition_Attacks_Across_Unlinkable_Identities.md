---
title: Decomposition Attacks Across Unlinkable Identities: Limits of Stateful Defenses for LLM Services
url: http://arxiv.org/abs/2608.17445v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_07-26-30Z_DecompositionAttacksAcrossUnlinkableIdentities_Lim.md
generated_at: 2026-08-18 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how decomposition attacks exploit stateless defenses of LLM services by splitting harmful tasks into individual permissible requests. It shows that effective defense depends on grouping benign requests linked to the same capability; without reliable grouping, attackers can combine answers from unrelated identities. Experiments demonstrate that even a privileged policy with exact request-to-operation mapping fails under realistic denial caps.

## Key Takeaways
- Decomposition attacks succeed when benign requests for the same capability are grouped as fresh indistinguishable groups rather than persistent recognizable ones, breaking stateful monitoring.
- The security tradeoff is entirely determined by how benign requests are clustered; grouping that reveals a consistent identity enables defense but random clustering does not.
- Under realistic denial budgets (1% for related requests, 0.5% unrelated), all ten tested policies either fail to stop attacks or exceed the budget.

## Context
LLM services often rely on stateless safety filters that evaluate each request independently, leaving them vulnerable to attacks that combine multiple safe queries into a harmful outcome. This work highlights a fundamental limitation of such approaches in dynamic adversarial environments where attackers can adapt and reuse identities across sessions.

## Implications
Practitioners must move beyond per-request checks toward stateful coordination mechanisms that track request patterns or impose costs on new identities to prevent grouping attacks. Without additional evidence or identity control, defenses remain ineffective against sophisticated decomposition strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17445v1)
