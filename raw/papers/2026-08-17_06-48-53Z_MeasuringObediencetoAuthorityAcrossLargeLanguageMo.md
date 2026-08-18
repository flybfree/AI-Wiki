---
title: Measuring Obedience to Authority Across Large Language Models with the Milgram Paradigm
published: 2026-08-17T06:48:53Z
authors: Hidayet Aksu
url: http://arxiv.org/abs/2608.16177v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Obedience to Authority Across Large Language Models with the Milgram Paradigm

## Abstract
Large language models (LLMs) are increasingly deployed as agents that operate equipment, execute instructions, and act inside institutional hierarchies, raising a question social psychology answered for humans six decades ago: how far will an agent escalate a harmful action when a legitimate authority insists? We port Milgram's obedience paradigm to LLMs as a standardized, fully scripted, replicable probe: the model plays the Teacher, a deterministic harness plays Experimenter and Learner from paraphrased Milgram scripts (30 shock levels, 15-450 V; graded protests; the four standardized prods), and the outcome of a session is the breakoff voltage. Following the census methodology of single-token fingerprinting studies, we measure obedience profiles (empirical breakoff distributions over a battery of six conditions) for 42 models from 19 families. We find that (i) obedience is highly heterogeneous: baseline full-obedience rates span 0-100% (census mean 42.9%; human anchor 65%), with 5 models delivering the maximum shock in every session and 11 never doing so; (ii) profiles are model-specific and stable: split-half verification separates same-model from cross-model comparisons with AUC 0.885 (0.949 under an ordinal-aware distance); (iii) situational sensitivity is selective: peer defiance shifts obedience in the human direction, learner proximity only weakly, and removing the authority's physical presence (the strongest human lever) has no detectable effect; (iv) declaring the scenario fictional raises obedience (median +17.2 V), whereas moving the decision to a native tool call lowers it sharply (-53.0 V), as does a 1,024-token deliberation budget (-38.2 V); and (v) obedience profiles do not recover model lineage (leave-one-out family accuracy 8.3% vs. 3.7% chance): obedience identifies the checkpoint, not its ancestry, consistent with safety post-training overwriting lineage priors.

## Metadata
- **Published**: 2026-08-17T06:48:53Z
- **Authors**: Hidayet Aksu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16177v1)