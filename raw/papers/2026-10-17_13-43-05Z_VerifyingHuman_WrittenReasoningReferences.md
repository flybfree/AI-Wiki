---
title: Verifying Human-Written Reasoning References
published: 2026-10-17T13:43:05Z
authors: Ali Ansari, Farhana Ferdousi Liza
url: http://arxiv.org/abs/2610.24690v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verifying Human-Written Reasoning References

## Abstract
Evaluating the reasoning of AI systems often relies on human-written reasoning chains as references, yet the logical support for their individual steps is rarely verified. Although prior neuro-symbolic approaches have formalized and checked reasoning, their reported evaluations do not systematically assess whether step conclusions in human-written reference derivations are entailed by their cited premise sets or investigate the sources of failures in those references. To address these limitations, we present a novel reference-centred assessment method for human-written derivations that combines entailment checking against cited premise sets, full-premise rechecking, and failure attribution to examine the reliability of these derivations and their formal representations. We evaluate it on P-FOLIO, using a large language model (LLM) to translate step conclusions into first-order logic (FOL) and the Z3 SMT solver to check entailment. Of 386 derivations examined, 202 (52.3%) meet all our checking criteria, meaning that every translated step is entailed by its stated support and the required target is established under the available FOL representations. Among 230 steps not entailed by their stated support, 191 become entailed when checked against the complete original premises, indicating that most initial failures reflect incomplete or mismatched support rather than unsupported claims. Manual analysis of the remaining 39 cases identifies 21 human reasoning errors, 11 FOL translation errors, and 7 dataset annotation errors. A separate manual audit of 50 randomly sampled steps that passed the entailment checks found 46 faithful FOL translations (92%). These findings suggest that disagreement with a human-written reasoning reference may originate in the reference or its formal representation rather than in the AI system being evaluated.

## Metadata
- **Published**: 2026-10-17T13:43:05Z
- **Authors**: Ali Ansari, Farhana Ferdousi Liza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24690v1)