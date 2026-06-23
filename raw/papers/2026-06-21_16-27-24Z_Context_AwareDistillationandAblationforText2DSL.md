---
title: Context-Aware Distillation and Ablation for Text2DSL
published: 2026-06-21T16:27:24Z
authors: Alexander V. Kozachok, Alexander M. Nazimov, Shamil G. Magomedov
url: http://arxiv.org/abs/2606.22578v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Context-Aware Distillation and Ablation for Text2DSL

## Abstract
We extend our prior work on Text2DSL automatic generation of domain-specific language (DSL) code from natural language descriptions along two complementary axes. First, we replace prompt-only synthetic generation with context-aware distillation, in which a teacher large language model (DeepSeek-V4-Flash) operates under an explicitly defined structured context comprising a BNF grammar, an API specification, and a closed identifier vocabulary; the resulting corpus is verified by a two-tier pipeline combining AST validation through esprima and runtime acceptance through the production polkitd daemon and the pkcheck client. This scales the verified PolkitBench corpus from 4,204 to 10,073 natural-language-to-Polkit-rule pairs at 100.0% AST validity and 99.7% runtime pass rate. Second, we conduct the per-component factorial ablation of structured context that was identified as future work in the precursor study: eight conditions C0-C7 are evaluated on GigaChat-10B-A1.8B with the new corpus. Three findings emerge. (i) The new harder corpus collapses the baseline mode (Syntax Valid 97.6% -> 58.5%, Combined Score 0.482 -> 0.252), whereas the context-enhanced mode degrades only marginally (Syntax 98.6% -> 97.4%, Combined 0.801 -> 0.750), confirming that structured context is not a cosmetic improvement but a load-bearing mechanism. (ii) The best absolute condition is the full context C7 across all metrics, while the strongest partial conditions (C5 = BNF + Vocabulary, C6 = API + Vocabulary) both contain the vocabulary. (iii) A Shapley-style decomposition assigns the largest semantic-quality effect to the vocabulary (Combined +0.198), the largest structural-validity effects to API (+24.7 pp) and BNF (+22.3 pp).

## Metadata
- **Published**: 2026-06-21T16:27:24Z
- **Authors**: Alexander V. Kozachok, Alexander M. Nazimov, Shamil G. Magomedov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.22578v1)