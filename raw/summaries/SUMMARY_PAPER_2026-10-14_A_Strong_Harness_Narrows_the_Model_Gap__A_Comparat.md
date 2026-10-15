---
title: A Strong Harness Narrows the Model Gap: A Comparative Evaluation for Legislative Document-to-XML Conversion
url: http://arxiv.org/abs/2610.19999v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_11-15-25Z_AStrongHarnessNarrowstheModelGap_AComparativeEvalu.md
generated_at: 2026-10-14 21:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents an industrial pipeline for converting U.S. state legislation into strict, schema-constrained XML and demonstrates through a controlled ablation study that harness engineering—the deterministic tooling and orchestration built around a language model—matters far more for accuracy than the choice of model itself. By crossing three harness configurations (zero-shot, single tool-using agent, and a decomposed multi-agent pipeline) with three Claude models on 153 gold-standard bills, the authors show that the weakest model embedded in the full pipeline outperforms the strongest model operating alone, with a statistically significant margin (0.948 versus 0.806, paired bootstrap p < 0.001).

## Key Takeaways
- The harness narrows the model gap decisively: the weakest model in the full multi-agent pipeline achieves 0.948 accuracy, surpassing the strongest model operating in isolation at 0.806. This means that investing in orchestration infrastructure yields greater accuracy gains than upgrading to a more capable model, fundamentally shifting the engineering priority from model selection to system design.
- The performance difference between the two agentic harnesses (single tool-using agent versus decomposed multi-agent pipeline) is attributable entirely to orchestration strategy—specifically task decomposition, persisted state management, and per-agent context isolation—since both harnesses share identical tools. This isolates orchestration as the critical variable rather than tool access.
- Across four scored dimensions (section hierarchy, verbatim text, citations, and amendment spans), the model performance spread shrinks from 0.68–0.81 at zero-shot to a uniform 0.95 at the full pipeline. The remaining residual error concentrates almost entirely in citation normalization, where the canonical identifier must be retrieved from an external authority; a deterministic lookup tool supplies the exactness that even a larger model cannot reliably generate from its weights.

## Context
This work sits at the intersection of agentic AI systems engineering and high-stakes legal document processing, where fidelity to source text is non-negotiable because downstream products depend on exact section hierarchies, verbatim language, and precise citation identifiers. As organizations increasingly deploy LLM-based pipelines for regulated document conversion, the question of whether to invest in stronger models or in better harnesses becomes a critical architectural decision. The paper contributes a rare controlled ablation that isolates harness effects from model effects, providing empirical grounding for the growing consensus that system-level engineering dominates model capability in constrained, structured-output tasks.

## Implications
For practitioners building production AI pipelines in legal, regulatory, or compliance domains, this research argues that engineering effort should be directed toward deterministic tooling, task decomposition, and state management rather than toward acquiring progressively larger or more expensive models. The finding that a deterministic lookup tool resolves the hardest remaining error class (citation normalization) suggests that hybrid architectures combining agentic orchestration with authoritative external data sources are the most robust path forward. For the broader AI field, the results challenge the prevailing assumption that scaling model capability is the primary lever for improving task performance, redirecting attention toward the design of harnesses that constrain, decompose, and ground model outputs in verifiable external data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19999v1)
