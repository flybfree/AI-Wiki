---
title: Detecting Experiential Intertextuality Across Migration Routes: Beyond Surface Similarity in French Narratives
published: 2026-07-31T09:07:07Z
authors: Sakayo Toadoum Sari, Nelly Robin, Michelle Auzanneau, Lakhdar Sais, Veronique Petit, Marie Veniard, Said Jabbour, Fabien Delorme
url: http://arxiv.org/abs/2607.29188v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Detecting Experiential Intertextuality Across Migration Routes: Beyond Surface Similarity in French Narratives

## Abstract
Migrants traversing geographically distinct routes such as the Trans-Saharan and Balkan corridors often recount strikingly parallel lived experiences: police violence, smuggler exploitation, dangerous crossings, and family separation. We introduce the task of experiential intertextuality detection: automatically identifying shared experiential echoes across migration narratives without requiring annotated training data. From 108 French migration narratives spanning both corridors, we automatically generate sentence pairs and score them using annotation-free methods: lexical baselines, sentence embeddings, POS-based structural features, a migration-specific theme lexicon, context-aware narrative features, and zero-shot LLM scoring with Qwen2.5-7B and Mistral-7B under three prompting strategies. We validate all methods against 816 expert-annotated intertextuality judgments (inter-annotator Krippendorff's $α= 0.27$). Our results reveal that all surface, structural, and embedding methods correlate only weakly with expert judgments ($r \leq 0.30$); Qwen2.5-7B zero-shot achieves the best single-method correlation ($r = 0.38$); few-shot examples degrade Qwen but dramatically improve Mistral; narrative position significantly predicts intertextuality, with departure-phase pairs showing the highest experiential echoes; and a supervised hybrid combining all 31 features achieves $r = 0.45$, a 21% improvement over the best individual method.

## Metadata
- **Published**: 2026-07-31T09:07:07Z
- **Authors**: Sakayo Toadoum Sari, Nelly Robin, Michelle Auzanneau, Lakhdar Sais, Veronique Petit, Marie Veniard, Said Jabbour, Fabien Delorme
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29188v1)