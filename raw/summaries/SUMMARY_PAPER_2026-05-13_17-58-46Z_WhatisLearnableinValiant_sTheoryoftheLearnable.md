---

title: "Summary: What is Learnable in Valiant's Theory of the Learnable?"
url: http://arxiv.org/abs/2605.13840v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-13_17-58-46Z_WhatisLearnableinValiant_sTheoryoftheLearnable.md
generated_at: "2026-06-11 10:40"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper revisits Valiant's original PAC learning model and asks which classes are learnable when the learner receives only positive samples, can issue membership queries, and must output a hypothesis with no false positives. The authors show that a class is learnable if and only if every realizable positive sample can be certified by a poly‑size adaptive query‑compression scheme, revealing a new variant of sample compression.

## Key Takeaways
- Learnability in Valiant's model is strictly sandwiched between the PAC model and the version without membership queries.  
- The characterization applies to every finite domain, including the Boolean hypercube setting.  
- Halfspaces become learnable with queries, requiring poly(d) samples and poly(d) polylog(1/ε) queries, but at least Ω(d) of each are necessary.

## Context
The study situates Valiant's original notion within modern learning theory, highlighting how query mechanisms can expand the class of realizable functions. It demonstrates that adding membership queries changes not only computational complexity but also the set of learnable classes.

## Implications
These results suggest that interactive learning strategies may unlock previously intractable function families like halfspaces in high‑dimensional spaces. Practitioners could leverage adaptive query compression to design more efficient learning pipelines for real‑world data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.13840v1)
