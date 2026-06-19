---

title: 'When No Benchmark Exists: Validating Comparative LLM Safety Scoring Without Ground-Truth Labels'
published: "2026-05-07T17:56:41Z"
authors: Sushant Gautam, Finn Schwall, Annika Willoch Olstad, Fernando Vallecillos Ruiz, Birk Torpmann-Hagen, Sunniva Maria Stordal Bjørklund, Leon Moonen, Klas Pettersen, Michael A. Riegler
url: http://arxiv.org/abs/2605.06652v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# When No Benchmark Exists: Validating Comparative LLM Safety Scoring Without Ground-Truth Labels



**Source**: [Original Paper](http://arxiv.org/abs/2605.06652v1)
## Abstract
Many deployments must compare candidate language models for safety before a labeled benchmark exists for the relevant language, sector, or regulatory regime. We formalize this setting as benchmarkless comparative safety scoring and specify the contract under which a scenario-based audit can be interpreted as deployment evidence. Scores are valid only under a fixed scenario pack, rubric, auditor, judge, sampling configuration, and rerun budget. Because no labels are available, we replace ground-truth agreement with an instrumental-validity chain: responsiveness to a controlled safe-versus-abliterated contrast, dominance of target-driven variance over auditor and judge artifacts, and stability across reruns.   We instantiate the chain in SimpleAudit, a local-first scoring instrument, and validate it on a Norwegian safety pack. Safe and abliterated targets separate with AUROC values between 0.89 and 1.00, target identity is the dominant variance component ($η^2 \approx 0.52$), and severity profiles stabilize by ten reruns. Applying the same chain to Petri shows that it admits both tools. The substantial differences arise upstream of the chain, in claim-contract enforcement and deployment fit. A Norwegian public-sector procurement case comparing Borealis and Gemma 3 demonstrates the resulting evidence in practice: the safer model depends on scenario category and risk measure. Consequently, scores, matched deltas, critical rates, uncertainty, and the auditor and judge used must be reported together rather than collapsed into a single ranking.

## Metadata
- **Published**: 2026-05-07T17:56:41Z
- **Authors**: Sushant Gautam, Finn Schwall, Annika Willoch Olstad, Fernando Vallecillos Ruiz, Birk Torpmann-Hagen, Sunniva Maria Stordal Bjørklund, Leon Moonen, Klas Pettersen, Michael A. Riegler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.06652v1)