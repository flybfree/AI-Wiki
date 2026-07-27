---
title: Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge
published: 2026-07-24T03:44:30Z
authors: Jiseok Kwak, Suhyeon Jo, Taewoo Kim, Yeongmin Kim, Byeonghu Na, Il-chul Moon
url: http://arxiv.org/abs/2607.21946v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge

## Abstract
This technical report presents our approach to Challenge Track~3: SeePhys Pro at the 3rd AI for Math Workshop, where the task is to answer college-level physics questions whose statement and figure may be given partly or entirely as an image. Visual physics problems become substantially harder for large language models when the decisive information resides in a figure rather than in the text, and this modality gap widens as more of the problem migrates into the image. We address the task with a two-stage framework: a visual information extraction stage that re-expresses figure content as solver-readable text to close the modality gap, and a reasoning stage that orchestrates three heterogeneous solvers through multi-agent debate. Our analysis yields two findings: the gain from orchestration comes from reliable answer selection rather than from additional debate, and the value of a figure aid scales with how much of the problem is locked inside the image. The resulting pipeline improves overall accuracy over a single-agent baseline from 0.643 to 0.802 on the public split, and won 1st place on both the public and the private leaderboard (private overall 0.743).

## Metadata
- **Published**: 2026-07-24T03:44:30Z
- **Authors**: Jiseok Kwak, Suhyeon Jo, Taewoo Kim, Yeongmin Kim, Byeonghu Na, Il-chul Moon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21946v1)