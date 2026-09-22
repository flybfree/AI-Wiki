---
title: DeceptionAnalyser: A Web-Based AI Tool for Performing Structured Deception Analysis with Argumentation Schemes and LLMs
published: 2026-09-21T10:02:07Z
authors: Stefan Sarkadi, Xabier Garmendia, Jack Mumford, Trevor Bench-Capon
url: http://arxiv.org/abs/2609.24369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeceptionAnalyser: A Web-Based AI Tool for Performing Structured Deception Analysis with Argumentation Schemes and LLMs

## Abstract
Deception plays a central role in Intelligence operations, yet it remains difficult to analyse systematically without expert knowledge of reasoning patterns and cognitive manipulation. In computational argumentation, for instance, no scheme-level ground-truth corpora currently exist to support statistical validation. In this paper, we address this by introducing a set of ten argument schemes designed to model distinct forms of deception, each accompanied by structured premises and critical questions. In doing so, we introduce the first dedicated library of argumentation schemes specifically designed for deception analysis, providing a structured foundation for systematically modelling and analysing deception in narrative text. We then present \textit{DeceptionAnalyser}, a browser-based tool that implements these schemes through a two-stage methodology combining LLM-based premise extraction with critical-question-driven evaluation. Our aim is to provide a conceptual and methodological foundation for analysing deceptive reasoning in narrative text. This is precisely what we address in this paper by demonstrating how structured argumentation theory and AI-assisted analysis can support transparent, explainable assessments of potential deception. Because the schemes are designed to flag claims for scrutiny rather than to output a deception verdict, we do not benchmark classification accuracy; instead, we assess the \emph{reliability} of the methodology by measuring the consistency of the tool's premise and conclusion assessments across ten contemporary large language models and repeated runs. We find that scheme detection is highly stable for clear-cut deception and degrades gracefully, in interpretable ways, on more ambiguous intelligence-style narratives.

## Metadata
- **Published**: 2026-09-21T10:02:07Z
- **Authors**: Stefan Sarkadi, Xabier Garmendia, Jack Mumford, Trevor Bench-Capon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24369v1)