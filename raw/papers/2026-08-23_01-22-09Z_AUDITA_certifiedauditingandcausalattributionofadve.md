---
title: AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems
published: 2026-08-23T01:22:09Z
authors: Zhixu Du, Yiran Chen
url: http://arxiv.org/abs/2608.22160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AUDITA: certified auditing and causal attribution of adverse outcomes in autonomous multi-agent systems

## Abstract
Physical automation is scaling toward fleets of embodied machines commanded by an AI brain. Early deployments already run factories and warehouses at production rates beyond any human line, and their adoption is accelerating. But when their joint decisions cause harm, everyone involved has reason to blame everyone else, the machine vendor, the algorithm provider, the factory operator, the insurer, and the regulator, and no method can divide the responsibility between them. Existing methods read logs whose origin they cannot verify and name a single culprit, misrepresenting outcomes that are overdetermined, preempted, or caused by an omission. We present \audita{}, an audit layer pairing a tamper-evident record of every inter-agent command with a certified, graded causal-attribution engine. We prove its verdict cannot be gamed: a rule-following agent can never be made to look guilty, an attempt to shift blame is itself caught and graded, and we establish the exact limit of what an evidence-based auditor can certify. On live language-model pipelines it reduces the standard judge baseline's responsibility error roughly threefold; on a benchmark of accident-grounded structures it recovers responsibility where single-culprit baselines fail, and stays invariant under forgery. \audita{} turns the question of who is to blame from an argument about logs into a calculation over evidence.

## Metadata
- **Published**: 2026-08-23T01:22:09Z
- **Authors**: Zhixu Du, Yiran Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22160v1)