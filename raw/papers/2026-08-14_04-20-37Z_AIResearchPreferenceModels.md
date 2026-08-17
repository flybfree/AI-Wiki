---
title: AI Research Preference Models
published: 2026-08-14T04:20:37Z
authors: Thomas Simon Foster, Bassel Al Omari, Tingchen Fu, Thomas Mann, Carl Domond, Lucia Cipolina-Kun, Bhavul Gauri, Muna Aghamelu, Alexander D. Goldie, Eryk Helenowski, Jean-Christophe Gagnon-Audet, Alberto Pepe, Saba Nazir, Daniel Izcovich, Noam Levi, Rishi Hazra, Karen Hambardzumyan, Nicolas Baldwin, Xian Li, Martin Josifoski, Paris Giampouras, Masoud Jalili Sabet, Anya Sims, Hela Momand, Tatiana Shavrina, Despoina Magka, Jason Weston, Yulin Wang, Anirudh Goyal, João Henriques, Yoram Bachrach, Emily McMilin, Jakob Nicolaus Foerster
url: http://arxiv.org/abs/2608.13940v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AI Research Preference Models

## Abstract
AI research agents (AIRA) can now propose, implement, and evaluate their own machine learning experiments, but progress on frontier tasks is throttled by cost: a candidate solution can be written in minutes, whereas evaluating it can take hours to days of GPU time. An agent can therefore propose far more candidates than it can afford to run, and its progress depends on its research preference: how it allocates a fixed execution budget across many candidates. We introduce AI Research Preference Models (RPMs) that predict which of multiple candidate solutions are most worth executing, without paying the cost of executing them all. We build RPMs from frozen pretrained language models (with no task-specific training), in two forms: an inference-only model that reasons over candidate plans, code, and prior executed solutions, and an agentic model that additionally runs small-scale pilot experiments before deciding. We integrate both into the AIRA-dojo search agent and evaluate on AIRS-Bench, a recent benchmark of machine learning research tasks for AI research agents. The two variants raise the average normalized score from 0.684 to 0.711 and 0.729 respectively, and reach the unguided agent's 24-hour performance in roughly 15 hours, using less than two-thirds of its execution budget. Our best RPMs also yield new state-of-the-art results on two AIRS-Bench tasks.

## Metadata
- **Published**: 2026-08-14T04:20:37Z
- **Authors**: Thomas Simon Foster, Bassel Al Omari, Tingchen Fu, Thomas Mann, Carl Domond, Lucia Cipolina-Kun, Bhavul Gauri, Muna Aghamelu, Alexander D. Goldie, Eryk Helenowski, Jean-Christophe Gagnon-Audet, Alberto Pepe, Saba Nazir, Daniel Izcovich, Noam Levi, Rishi Hazra, Karen Hambardzumyan, Nicolas Baldwin, Xian Li, Martin Josifoski, Paris Giampouras, Masoud Jalili Sabet, Anya Sims, Hela Momand, Tatiana Shavrina, Despoina Magka, Jason Weston, Yulin Wang, Anirudh Goyal, João Henriques, Yoram Bachrach, Emily McMilin, Jakob Nicolaus Foerster
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13940v1)