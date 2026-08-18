---
title: Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic
published: 2026-08-17T08:46:52Z
authors: Simon Ellershaw, Christopher Tomlinson, Zeljko Kraljevic, Spiros Denaxas, Harry Hemingway, Cathie Sudlow, Angela M. Wood, Anoop D. Shah, Richard Dobson
url: http://arxiv.org/abs/2608.16273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Foresight-England: Development of a National-Scale Generative AI Model of Electronic Health Records for Medical Event Prediction across the COVID-19 Pandemic

## Abstract
Foresight-England (Foresight-E) is the first national-scale generative foundation model of electronic health records (EHRs), developed as a research pilot strictly for COVID-19 research. We evaluated its ability to model the direct and indirect effects of the pandemic. Trained from scratch entirely within the NHS England Secure Data Environment, Foresight-E is a 243-million-parameter transformer decoder. It was trained and evaluated on de-identified, longitudinal EHRs of approximately 61 million individuals, integrating primary/secondary care, death registrations, and COVID-19 data. Training and validation used a 90% subset (54.9 million) spanning November 2018 to December 2022; the remaining 10% (6.1 million) was held out for evaluation. Foresight-E models patient timelines autoregressively, predicting the next medical event given their prior history. At inference, it operates zero-shot, predicting any concept in its ~40,000-code vocabulary without task-specific training. Our tokenisation scheme retains the clinical granularity of ICD-10, OPCS-4, and SNOMED CT codes, jointly representing absolute and relative timing. We designed an evaluation framework for 30-day COVID-19 hospitalisation and mortality, including subgroup analyses by demographic factors and vaccination status. To assess generalisation to unseen future data and the pandemic's indirect effects, we tested the model on medical events from 2023 (beyond its training period), benchmarking against logistic regression and XGBoost. As detailed in the Project Status section, NHS England has paused access to data for the Foresight-E project, meaning quantitative results are currently unavailable. Instead, we share our strategy for tokenisation, architecture, training, inference, and evaluation as a methodological template and case study in the challenges of building population-scale EHR foundation models.

## Metadata
- **Published**: 2026-08-17T08:46:52Z
- **Authors**: Simon Ellershaw, Christopher Tomlinson, Zeljko Kraljevic, Spiros Denaxas, Harry Hemingway, Cathie Sudlow, Angela M. Wood, Anoop D. Shah, Richard Dobson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16273v1)