---
title: Not Self-Decidable: LLMs Cannot Draw the Boundary of What an Agent Verifier Can Check
published: 2026-10-03T18:25:12Z
authors: Anthony Rhodes
url: http://arxiv.org/abs/2610.04699v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not Self-Decidable: LLMs Cannot Draw the Boundary of What an Agent Verifier Can Check

## Abstract
A verifier for an agent faces rules of two kinds: the ones a fixed check can settle and the ones that require a judge. A team that derives its own checks fixes that split up front. Where the requirements come from outside, as in finance, healthcare and law, the agent enforces rules it did not write, so the split falls to runtime, recurring for every predicate of every rule on every action at a rate no reviewer can audit. Every escalation scheme assumes a model can make that decision itself, that it is self-decidable. Across six corpora, including the EU AI Act, FINRA guidance and a deployed credit agent, we collect roughly 22,000 labels from four models built by three labs. They agree almost perfectly where the answer is obvious and collapse on regulatory text; their errors run in opposite directions, so no model can be trusted as the conservative choice; and on the deployed agent's own rule-set they err together, over-claiming that a fixed check will do, the direction that never gets escalated. We introduce CoVer (corroborate-then-verify), which treats unanimity as a nomination, admitting a predicate only when the check synthesized for it survives intervention, reading fields the agent cannot write and holding under deterministic rewording. That gate rejects most of what corroboration wrongly admits, at a cost in coverage we report rather than tune away. The obvious alternative, agreement with a reference judge, certifies nothing: it climbs from 30% to 77% across calibration bands while the genuinely decidable share does not move, because a judge drawn from the population under indictment ratifies the blind spot it shares. Self-decidability is not a capability to elicit from a model but a boundary the verifier must construct.

## Metadata
- **Published**: 2026-10-03T18:25:12Z
- **Authors**: Anthony Rhodes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04699v1)