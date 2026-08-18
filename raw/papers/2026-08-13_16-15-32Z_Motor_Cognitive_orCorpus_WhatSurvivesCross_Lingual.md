---
title: Motor, Cognitive, or Corpus? What Survives Cross-Lingual Transfer in Speech-Based Parkinsons Disease Detection
published: 2026-08-13T16:15:32Z
authors: Serli Kopar, Sam Gijsen, Abner Hernandez, Paula Andrea Perez-Toro, Kerstin Ritter
url: http://arxiv.org/abs/2608.13425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Motor, Cognitive, or Corpus? What Survives Cross-Lingual Transfer in Speech-Based Parkinsons Disease Detection

## Abstract
Self-supervised learning (SSL) speech representations achieve strong performance for Parkinson's disease (PD) detection within individual corpora. However, it remains unclear whether these models capture disease-related characteristics or exploit dataset-specific confounds, particularly since most SSL backbones are pretrained exclusively on healthy speech. To investigate this question, we perform a layer-wise analysis of nine SSL speech backbones using a low-capacity logistic regression probe across three languages. We structure the evaluation as multiple scenarios that progressively introduce distribution shifts in participant identity, recording conditions, language, and pathology. Our results reveal two key findings. First, layer selection is highly corpus-dependent: the optimal representation layer is determined primarily by the source dataset rather than by the SSL architecture itself. Second, the transferred discriminative signal lacks pathological specificity: classifiers trained to detect PD assign similarly high probabilities to both PD and dementia speech in the target corpus. These results highlight critical limitations that must be addressed before speech-based pathology recognition models can be reliably deployed in clinical settings.

## Metadata
- **Published**: 2026-08-13T16:15:32Z
- **Authors**: Serli Kopar, Sam Gijsen, Abner Hernandez, Paula Andrea Perez-Toro, Kerstin Ritter
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13425v1)