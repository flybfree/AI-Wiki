---
title: Adaptation Interfaces for In-Context Tabular Foundation Models in Time-to-Event Prediction
published: 2026-09-04T09:01:16Z
authors: Minh-Khoi Pham, Luca Cotugno, Dan Cernei, Alina Sirbu, Stefano Masi, Giuseppe Prencipe, Alessandro Pingitore, Patrizia Landi, Working Group on Uric Acid, Cardiovascular Risk of the Italian Society of Hypertension, Tai Tan Mai, Martin Crane, Marija Bezbradica
url: http://arxiv.org/abs/2609.04901v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptation Interfaces for In-Context Tabular Foundation Models in Time-to-Event Prediction

## Abstract
Tabular foundation models (TabFMs) achieve strong performance on structured data, particularly for standard classification and regression problems. Yet, extending them to censored time-to-event prediction is challenging because it requires properly handling censoring and event-time dynamics. Building on our prior work, we further link TabFMs with CoxPH and DeepHit and revise the context-resampled training procedure. We evaluate temporal zero-shot reformulation, classification-based fine-tuning, and survival-head adaptation using frozen TabFM backbones on 74 single-risk data sets, and we additionally study 4 competing-risk data sets. Zero-shot inference is effective on smaller single-risk data sets, whereas supervised adaptation becomes increasingly advantageous as data sets scale. Cox provides the most reliably strong interface, especially for Integrated Brier Score (IBS) on larger data sets. DeepHit is relatively stronger for the time-dependent Concordance Index than for IBS, while cause-specific MTLR ranks highest among the TabFM survival heads in the four-data-set competing-risk analysis. Classification fine-tuning becomes more competitive with zero-shot inference as data sets grow but remains weaker for probabilistic prediction. Overall, our results indicate that effective TabFM transfer depends on the data regime and on the statistical structure represented by the chosen adaptation interface. The implementation scripts used for this work are available at https://github.com/kaylode/survival-fm.

## Metadata
- **Published**: 2026-09-04T09:01:16Z
- **Authors**: Minh-Khoi Pham, Luca Cotugno, Dan Cernei, Alina Sirbu, Stefano Masi, Giuseppe Prencipe, Alessandro Pingitore, Patrizia Landi, Working Group on Uric Acid, Cardiovascular Risk of the Italian Society of Hypertension, Tai Tan Mai, Martin Crane, Marija Bezbradica
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04901v1)