---
title: Visual-Aware Representation of Web Pages for Machine Learning Applications
published: 2026-08-19T09:28:56Z
authors: Radek Burget, Radek Hranický
url: http://arxiv.org/abs/2608.18727v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Visual-Aware Representation of Web Pages for Machine Learning Applications

## Abstract
Applying machine learning to web pages is challenging due to the need to interpret HTML together with associated resources and perform rendering to obtain a meaningful visual and layout-aware representation. As a result, machine learning over web content remains comparatively underexplored. In this paper, we present a platform for visual-aware representation and machine learning over web pages based on the open-source rendering tool FitLayout. The platform provides a server capable of rendering web pages, explicitly capturing their visual and structural properties in an RDF-based representation, and persisting the rendered documents in an integrated storage. The processing pipeline is controlled via a REST API, while SPARQL queries are used to retrieve structured data suitable as input for machine learning algorithms. By explicitly modeling rendered web pages, including fine-grained layout details, the platform enables dataset sharing and supports the reproducibility of experimental results. The architecture supports the complete dataset preparation workflow, from web page collection and rendering through preprocessing and annotation of content elements to downstream learning tasks. We further provide a Python client library that integrates the platform with standard machine learning workflows. As a demonstration, we show how rendered web pages can be transformed into graph-based representations and used to train graph neural networks for recognizing key content elements, illustrating both the applicability of the approach and the reproducibility of the results.

## Metadata
- **Published**: 2026-08-19T09:28:56Z
- **Authors**: Radek Burget, Radek Hranický
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18727v1)