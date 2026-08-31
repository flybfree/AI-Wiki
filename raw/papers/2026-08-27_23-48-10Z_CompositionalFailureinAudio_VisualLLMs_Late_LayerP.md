---
title: Compositional Failure in Audio-Visual LLMs: Late-Layer Prior Dominance Under Cross-modal Conflict
published: 2026-08-27T23:48:10Z
authors: Adarsh Sudheer, David Li, Omar Elbanna, Ishaan Kodarapu, Arjun Bahuguna, Vasu Sharma
url: http://arxiv.org/abs/2608.27785v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Compositional Failure in Audio-Visual LLMs: Late-Layer Prior Dominance Under Cross-modal Conflict

## Abstract
We study audio-visual conflict as a compositional generalization test for AV-LLMs: the model must combine synchronized but semantically incompatible audio and video evidence and decide whether the pair matches. On VideoLLaMA 2-7B-AV, three alignment configurations remain nearchance on the scored exact-string Yes/No subset of AVHBench, even though their output priors shift substantially. Similarly, off-the-shelf InternVideo2 experienced a 32.3% accuracy decrease specifically under cross-modal conflict, accompanied by a 17.3% instruction-following failure. We call this failure mode prior dominance: late-layer commitment to an internally preferred answer pattern that is weakly grounded in the conflicting inputs. To explain this behavior, we conduct a mechanistic interpretability analysis and find that commitment remains concentrated at 25.5 $\pm$ 1 layers. We show that stronger temporal alignment changes answer bias, but do not improve compositional conflict resolution. Code and data to reproduce our mechanistic audit and behavioral evaluations are available at https://github.com/AdarshSudheer09/AVHBench-dmai.

## Metadata
- **Published**: 2026-08-27T23:48:10Z
- **Authors**: Adarsh Sudheer, David Li, Omar Elbanna, Ishaan Kodarapu, Arjun Bahuguna, Vasu Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27785v1)