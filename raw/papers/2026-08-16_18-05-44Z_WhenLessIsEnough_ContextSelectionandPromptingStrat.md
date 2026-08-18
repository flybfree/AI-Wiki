---
title: When Less Is Enough: Context Selection and Prompting Strategies for Bengali News Headline Generation
published: 2026-08-16T18:05:44Z
authors: Muhammad Ashad Kabir, Kawsar Ahmed, Md. Osama
url: http://arxiv.org/abs/2608.15879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Less Is Enough: Context Selection and Prompting Strategies for Bengali News Headline Generation

## Abstract
Large language models (LLMs) have shown strong performance in text generation tasks, yet their effectiveness on headline generation remains sensitive to how input context is selected and presented. In this work, we investigate Bengali news headline generation as a document-level generation task that requires effective selection and presentation of salient contextual information from long-form articles. Using Gemini-2.0-Flash, Llama-3.3-70B, and GPT-4o, we systematically study the effects of context selection, prompting strategies, and in-context learning (i.e., few-shot) on the quality of headline generation. Our experiments show that providing the full article does not necessarily improve performance; instead, using selected lead paragraphs of the article can maintain, and in some cases improve, headline generation quality. We further compare Bengali Native Prompting (BNaP) and Cross-Lingual Prompting (XLP), and examine how each interacts with context-enriched prompt templates incorporating auxiliary contextual cues. Results demonstrate that prompting strategies substantially influence generation quality: XLP often yields stronger performance, particularly when combined with contextual enrichment, but its benefits are model-dependent. Additionally, few-shot prompting substantially improves Gemini, with most of the gain obtained from a single demonstration, whereas Llama shows limited benefit from additional examples. Overall, our findings highlight that effective Bengali news headline generation depends more on context relevance and prompt design than on increasing input length, offering practical insights for multilingual and low-resource LLM applications.

## Metadata
- **Published**: 2026-08-16T18:05:44Z
- **Authors**: Muhammad Ashad Kabir, Kawsar Ahmed, Md. Osama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15879v1)