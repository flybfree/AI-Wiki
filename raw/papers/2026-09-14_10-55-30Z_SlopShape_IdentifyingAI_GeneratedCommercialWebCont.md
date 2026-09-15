---
title: SlopShape: Identifying AI-Generated Commercial Web Content
published: 2026-09-14T10:55:30Z
authors: Jochen Madler
url: http://arxiv.org/abs/2609.15369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SlopShape: Identifying AI-Generated Commercial Web Content

## Abstract
Word-level detectors identify unedited AI-generated text almost perfectly, but the literature documents their brittleness under rewording, and a word-level score neither characterizes a text nor identifies which AI model wrote it. We ask whether AI-generated text can be identified one level deeper, from structural signatures: how information is presented, in what order, with what evidence, and in what voice. We replicate StoryScope (Russell et al., 2026), which showed such patterns for AI-generated fiction, on commercial content: 2,250 pre-ChatGPT human blog posts from 268 company domains against 11,250 AI mirrors from five frontier models. A 214-feature instrument, applied by an LLM and validated in a human gold-annotation session (human-human kappa 0.928, human-model 0.946), detects AI posts from its 187 structural features alone at 98.0 macro-F1 on held-out companies, unchanged (98.1) when every AI post is reworded by its own model. The signal characterizes and attributes: AI posts share a tidy, self-announcing shape, 79.3% are attributed to the correct source against a 16.7% chance rate, and human posts occupy rare structural configurations. All effects replicate StoryScope's, consistent in direction and larger in magnitude. We release pipeline, instrument, prompts, code, and aggregate artifacts.

## Metadata
- **Published**: 2026-09-14T10:55:30Z
- **Authors**: Jochen Madler
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15369v1)