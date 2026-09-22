---
title: Self-Healing Harness for Runtime Oversight of Agent Self-Modification
published: 2026-09-21T05:36:56Z
authors: Sina Tayebati, Divake Kumar, Nastaran Darabi, Ranganath Krishnan, Amit Ranjan Trivedi
url: http://arxiv.org/abs/2609.24130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Self-Healing Harness for Runtime Oversight of Agent Self-Modification

## Abstract
LLM agents can change their own future behavior, raising a basic control question of which self-generated changes should be allowed to persist. We formulate this as admission control for self-modification. The agent may propose changes to its operating instructions, while an external runtime gate controls persistence. We implement this principle as a model-agnostic self-healing harness that runs a Detect, Notice, Heal, Validate loop around an otherwise unmodified agent. The agent authors candidate behavioral rules in an external workspace, where they receive provisional execution authority during evaluation and acquire persistent cross-episode authority only after measured improvement on the triggering failure without regression beyond a fixed margin on protected cases. Replay provides matched evidence when available, forward trials provide a weaker fallback, and a corpus-level guard re-tests the accumulated active rule set. Across 16 matched Baseline and Harness runs spanning AppWorld, Terminal-Bench, and $τ^2$-Bench, the gate rejected 383 replay-decided proposals. Of these, 211 (55%) improved their triggering failure while degrading a case that previously worked. This shows that locally beneficial self-modifications can introduce collateral regressions often enough to materially affect gate decisions, providing direct empirical motivation for external admission control. Task-completion score is higher under the Harness in all 16 pairs, with two paired bootstrap intervals excluding zero, while repeated-trial reliability is higher in 12 pairs, tied in 4, and lower in none. Because adaptation modifies the policy-inducing context while leaving model weights fixed, admitted changes remain inspectable, reversible, and compatible with closed-weight models.

## Metadata
- **Published**: 2026-09-21T05:36:56Z
- **Authors**: Sina Tayebati, Divake Kumar, Nastaran Darabi, Ranganath Krishnan, Amit Ranjan Trivedi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24130v1)