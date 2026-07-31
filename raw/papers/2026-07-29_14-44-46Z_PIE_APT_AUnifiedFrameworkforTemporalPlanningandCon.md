---
title: PIE-APT: A Unified Framework for Temporal Planning and Contradiction Hunting via Incremental Direct-Derivation Abduction
published: 2026-07-29T14:44:46Z
authors: Amir Hossein Sharafi, Alireza Shahbazi
url: http://arxiv.org/abs/2607.27287v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PIE-APT: A Unified Framework for Temporal Planning and Contradiction Hunting via Incremental Direct-Derivation Abduction

## Abstract
Reasoning and planning over Dynamic Knowledge Graphs (DKGs) present significant challenges, especially in open-world environments with incomplete information. Existing action formalisms often face decidability issues and the Ramification Problem, while managing incomplete knowledge via structural abduction requires expansive combinatorial search. This paper introduces a unified framework with two integrated modules---\textbf{PIE-Abducer} (incremental direct-derivation abduction) and \textbf{PIE-APT} (Abductive Planning for Temporal KGs)---operating natively on the highly expressive Description Logic. We model state transitions along a linear timeline as non-monotonic updates to deductively closed DL theories. Treating the incremental reasoner as a black-box and representing actions natively in OWL without external modal operators preserves logical decidability. To address incomplete knowledge, \textbf{PIE-Abducer} circumvents traditional Minimal Hitting Set (MHS) enumeration. Instead of combinatorial syntactic search, it injects the logical negation of a target goal into a consistent branch and extracts missing premises via direct refutation consequences. \textbf{PIE-APT} then employs a recursive \textit{Generate-and-Test} architecture, interleaving backward-chaining A* search with \textbf{PIE-Abducer} up to a bounded causal depth, followed by strict validation via forward-chaining Temporal Projection. We evaluate four OWL benchmarks stressing semantic abilities absent in classical planning: parameterized goals with witness search, mid-search DL entailment, open-world assumption injection, and adversarial contradiction hunting. Results demonstrate qualitative superiority over classical planners and prove our direct-derivation approach quantitatively outperforms an MHS-faithful baseline during abductive enrichment.

## Metadata
- **Published**: 2026-07-29T14:44:46Z
- **Authors**: Amir Hossein Sharafi, Alireza Shahbazi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27287v1)