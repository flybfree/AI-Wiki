---
title: Towards Quantifying Benchmark Optimization in ASR Models
published: 2026-08-20T11:54:39Z
authors: Theo Lebryk, David Ayllon, Alice Baird, Jakub Piotr Cłapa, Jens Madsen, Panagiotis Tzirakis
url: http://arxiv.org/abs/2608.19936v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Quantifying Benchmark Optimization in ASR Models

## Abstract
Public benchmarks are important measures of Automatic Speech Recognition (ASR) model capabilities. However, by nature of being public, there is risk of models being optimized for these benchmarks in ways that do not generalize well to real-world data. We present a methodology for quantifying benchmark optimization, focusing on cases where the audio underdetermines the reference transcript. We identify three families of behavioral probes that reveal models' capabilities of reproducing benchmark reference spans despite underdetermined audio: reference disagreement, masked-number recovery, and orthographic switching. We find that the highest-scoring open source models output verbatim reference transcript spans even when the relevant audio is contradictory, masked, or ambiguous. Using a variety of mechanistic probes, we show that models respond to narrow acoustic cues to override the faithful representation of the audio in favor of a benchmark-optimized policy. We show the benchmark-optimized behavior can be causally manipulated via low-rank linear steering or simply appending audio to the end of a segment in some cases. Overall, our results indicate that high-performing models exhibit benchmark-conditioned behaviors that can inflate benchmark performance without reflecting improved general-purpose transcription ability.

## Metadata
- **Published**: 2026-08-20T11:54:39Z
- **Authors**: Theo Lebryk, David Ayllon, Alice Baird, Jakub Piotr Cłapa, Jens Madsen, Panagiotis Tzirakis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19936v1)