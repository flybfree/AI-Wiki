---
title: Inside the Scorer: Mechanistic Evidence on Rubric Control in LLM-Based Automated Essay Scoring from 25 Base Models
published: 2026-10-19T03:26:30Z
authors: Chungche Huang, Po-Ya Angela Wang, Shu-Kai Hsieh
url: http://arxiv.org/abs/2610.25724v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inside the Scorer: Mechanistic Evidence on Rubric Control in LLM-Based Automated Essay Scoring from 25 Base Models

## Abstract
Automated essay scoring (AES) using large language models (LLMs) offers promising use cases for language assessment, yet high-stakes testing requires scores that are both controllable and verifiable, which current LLM-based scorers lack. Given that, we investigate whether LLM-based scorers form distinct internal representations for individual scoring rubrics and whether these representations can be independently controlled. Probing and steering 25 open-weight base LLMs (0.13B-10.31B parameters; 14 families) on human-scored BESTEP English writing tasks, we find that holistic scores are decodable from model activations for the longer tasks (Parts 2 and 3) and only weakly for the shortest (Part 1). Furthermore, scoring rubrics have partly separable directions in representation space for the longer tasks, though not for short responses (Part 1). However, causal steering reveals a critical limitation: applying a matching intervention (e.g., steering "grammar" on a grammar-degraded response) yields only a negligible advantage (about 2% of the effect) over a mismatched intervention (e.g., steering "vocabulary"), and none that is detectable in any of the 10 testable comparisons across reliably measured rubrics. Rather than controlling distinct evaluative dimensions, the rubric directions share a dominant lever whose rubric-specific parts are not selective, which may mirror the halo structure of human ratings. Our contributions are two-fold. First, we show that analytic scoring rubrics designed for human raters do not behave as independent controls in base LLMs, even among the seven models whose scores agree best with human raters ($r \geq 0.6$). Second, we establish a methodology that shows that score agreement and decodability do not imply rubric-level control in LLM-based assessment.

## Metadata
- **Published**: 2026-10-19T03:26:30Z
- **Authors**: Chungche Huang, Po-Ya Angela Wang, Shu-Kai Hsieh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25724v1)