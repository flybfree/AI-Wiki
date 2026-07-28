---
title: Statistically Supported LLM Ingredient and Recipe Data Collection in Computational Nutrition
published: 2026-07-25T16:19:02Z
authors: James Izzard, Hassan Eshkiki, Fabio Caraffini
url: http://arxiv.org/abs/2607.23273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Statistically Supported LLM Ingredient and Recipe Data Collection in Computational Nutrition

## Abstract
Computational nutrition needs precise ingredient data, but current databases are incomplete, inconsistent, and built for human reference rather than automated reasoning. LLMs could help fill these gaps, but single-pass outputs are unreliable and can introduce silent errors into downstream computation. We present a quality-controlled LLM pipeline for ingredient data acquisition that combines robust statistical estimation, domain-specific invariant checks, and a web-fetch fallback. An illustrative Heap's Law fit to 233 recipes suggests that unique-ingredient growth is sub-linear and front-loaded: the projected ratio of unique ingredients to recipes falls from 1.74 at 100 recipes to 0.19 at 5,000. For each ingredient attribute, repeated LLM queries are treated as samples from a model-induced answer distribution, and we apply robust point estimators and normalised confidence scores across numerical, Boolean, multiple-choice, open categorical, and optional integer types. An invariant guard layer enforces nutritional and logical self-consistency within each ingredient record. Minor numeric inconsistencies are reconciled via a linear program that minimises worst-case percentage deviation while preserving semantic zeros, and major violations are escalated to web-evidence-grounded repair, then human review only if that fails. On a curated 30-ingredient reference set, the pipeline achieves 98.4% exact match on nutrient flags and cuts median absolute percentage error on nutrient ratios from 31.9% for the median-aggregated baseline to 10.1%, a reduction of 21.8 percentage points, at an API cost of about $1 per ingredient. This frames LLM-assisted database construction as a controlled data-engineering workflow that makes uncertainty operational rather than discarding it.

## Metadata
- **Published**: 2026-07-25T16:19:02Z
- **Authors**: James Izzard, Hassan Eshkiki, Fabio Caraffini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23273v1)