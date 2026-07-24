---
title: Lightweight Person-Place Relation Extraction from Historical Newspapers with Dependency Graphs and Proximity Features
published: 2026-07-22T03:35:56Z
authors: Mlen-Too Wesley
url: http://arxiv.org/abs/2607.19718v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lightweight Person-Place Relation Extraction from Historical Newspapers with Dependency Graphs and Proximity Features

## Abstract
The HIPE-2026 shared task introduces person-place relation extraction from multilingual historical newspapers as a new evaluation track, classifying the at and isAt relations between pre-annotated person and location mentions in English, French, and German. Motivated by the cost of processing historical archives at scale, our team (DS@GT HIPE, team 2 in the official results) investigates how far a lightweight, interpretable system can go without any pretrained language model at the relation classification stage. Our approach builds a document-level graph from dependency parses, extracts proximity-based and part-of-speech features for each entity pair, and classifies them with small scikit-learn ensembles or compact Graph Attention Networks, keeping every submitted run under 847K parameters. On the official evaluation (Test A, the newspaper test set), our best run reached a macro recall of 0.5142, ranking 3rd on the Efficiency profile while placing mid-table on Accuracy among the 17 participating teams. Two findings stand out. First, minimum character distance alone captures most of the classification signal; adding further engineered features yields inconsistent gains and sometimes degrades performance, echoing prior evidence that argument distance dominates relation extraction. Second, document-grouped cross-validation is essential on this corpus: pair-level splits inflate scores by 25-37 percentage points because entity mentions recur across documents, a data-leakage effect that grouped cross-validation removes.

## Metadata
- **Published**: 2026-07-22T03:35:56Z
- **Authors**: Mlen-Too Wesley
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19718v1)