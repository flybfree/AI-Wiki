---
title: More Capable, Less Faithful: A Multilingual Analysis of Mathematical (Un)Solvability Detection in LLMs
url: http://arxiv.org/abs/2608.30463v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_08-49-51Z_MoreCapable_LessFaithful_AMultilingualAnalysisofMa.md
generated_at: 2026-08-31 21:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a multilingual benchmark extending ReliableMath to French and Greek, enabling the study of solvability detection across multiple languages. It shows that while Solvability Belief is largely universal, high‑resource English models detect solvable problems more faithfully than lower‑resource ones.

## Key Takeaways
- The multilingual probe predicts Solvability Belief as a language‑agnostic feature, indicating the belief itself is not tied to specific linguistic representations.  
- English LLMs achieve higher mathematical reasoning scores but exhibit lower faithfulness in solvability detection compared with other languages.  
- The benchmark reveals that failures are more pronounced in low‑resource languages where the model’s internal representation of unsolvable problems is less reliable.

## Context
Understanding why certain models perform better across languages helps researchers design fairer AI systems and avoid hidden biases rooted in resource disparities. This work contributes to a broader effort to evaluate mathematical reasoning not just as an isolated task but as a multilingual capability that can be systematically measured.

## Implications
For industry practitioners, the findings suggest that deploying LLMs for math‑related tasks should consider language resources to ensure consistent and trustworthy outputs. Practitioners can mitigate fairness issues by fine‑tuning or selecting models that perform equally well across all supported languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30463v1)
