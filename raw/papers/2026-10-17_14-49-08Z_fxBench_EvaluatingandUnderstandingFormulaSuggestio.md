---
title: fxBench: Evaluating and Understanding Formula Suggestions in Spreadsheets
published: 2026-10-17T14:49:08Z
authors: Sanket Mhatre, Sumit Gulwani, Vu Le, Yasharth Bajpai, Gust Verbruggen
url: http://arxiv.org/abs/2610.24729v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# fxBench: Evaluating and Understanding Formula Suggestions in Spreadsheets

## Abstract
Spreadsheets are among the most widely used tools for computations, and formulas are their core building blocks. Besides agentic spreadsheet tools, proactive formula suggestions enable significant productivity gains and are now available in popular spreadsheet software (Microsoft Excel and Google Sheets). Such suggestions pose interesting challenges: the right context must be collected and represented for a machine learning model, which must then be able to write a correct formula, in a way that is fast and cheap enough to trigger on every = (or subsequent keystrokes for auto-completion) without taking users out of their editing flow. Surprisingly, there is no public benchmark for formula suggestions on real spreadsheets. In this paper, we therefore (1) introduce fxBench as a manually curated benchmark of 503 formula suggestion tasks based on Sheetpedia, (2) break down the formula suggestion problem into four capabilities (gather context, understand context, understand intent, write formula) that a formula suggestion system requires, and (3) evaluate existing and new approaches to understand bottlenecks in these capabilities that pose interesting research directions. Specifically, we annotate each benchmark with the cells that describe intent to determine the theoretical performance limit of a given context selection strategy, we evaluate performance of small and large models on different representations of context, including a dense format with high theoretical coverage at low token counts, and we fine-tune smaller language models to show that we can learn to understand such dense formats. Additionally, we perform quantitative and qualitative analysis on failure modes to understand bottlenecks in the formula writing capability; the best configuration only achieved 58.8% correct suggestions.

## Metadata
- **Published**: 2026-10-17T14:49:08Z
- **Authors**: Sanket Mhatre, Sumit Gulwani, Vu Le, Yasharth Bajpai, Gust Verbruggen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24729v1)