---
title: Contextual Tamil Spelling and Grammar Correction Using Progressively Fine-Tuned Sequence-to-Sequence Transformers
url: http://arxiv.org/abs/2609.03273v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_02-02-39Z_ContextualTamilSpellingandGrammarCorrectionUsingPr.md
generated_at: 2026-09-03 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a progressive fine‑tuning approach for Tamil spelling and grammar correction using sequence‑to‑sequence transformers, achieving 69.3 % top‑1 exact‑match accuracy on a held‑out diagnostic set. The method tackles four error categories through five stages of model refinement, with the final mBART‑50 v5 stage delivering state‑of‑the‑art performance on sandhi and subject‑verb agreement.

## Key Takeaways
- The progressive schedule improves subject‑verb accuracy from 1 % to 52.5 % by introducing contextual sentence pairs, demonstrating that grammar correction benefits from sentence‑level supervision.
- Sandhi accuracy rises from 0 % to 87.5 % when multi‑site cross‑word sandhi pairs are added, showing that handling phonetic transformations is a major breakthrough for low‑resource languages.
- Precision‑recall trade‑offs are quantified, revealing that improving identity accuracy reduces sandhi recall, a nuance rarely reported in prior work.

## Context
Tamil’s agglutinative morphology and extensive sandhi rules make it a challenging low‑resource language for NLP tasks. This study contributes to the broader effort of applying transformer architectures to such linguistic challenges by demonstrating how staged fine‑tuning can overcome surface noise while preserving contextual integrity.

## Implications
For Tamil‑speaking applications, this model provides a reliable tool for improving user input quality in mobile and web interfaces without requiring massive annotated corpora. Practitioners can leverage the progressive schedule as a template to adapt transformer pipelines to other low‑resource scripts with complex phonological rules.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03273v1)
