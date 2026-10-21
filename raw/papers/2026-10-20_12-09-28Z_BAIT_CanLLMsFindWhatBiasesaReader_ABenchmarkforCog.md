---
title: BAIT: Can LLMs Find What Biases a Reader? A Benchmark for Cognitive Bias Triggers in News
published: 2026-10-20T12:09:28Z
authors: Yousra Fettach, Tijl De Bie
url: http://arxiv.org/abs/2610.28092v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BAIT: Can LLMs Find What Biases a Reader? A Benchmark for Cognitive Bias Triggers in News

## Abstract
Persuasive writing exploits cognitive biases, recruiting a reader's mental shortcuts to shape belief, often without the reader noticing. We call the linguistic features exploiting such mental shortcuts cognitive bias triggers. As large language models (LLMs) increasingly mediate how people encounter news, summarizing it, ranking it, and answering questions over it, a natural question is whether they can recognize the features of a text that bias a human reader. We introduce BAIT (Bias Annotation In Text), a resource for detecting cognitive bias triggers in news. BAIT pairs a schema of nine triggers, each specified in an annotator codebook, with 50 English news articles annotated by trained annotators at the article and span levels and adjudicated into a gold standard. On this data we define two tasks, detecting which triggers a text contains and locating the spans that carry them. We then benchmark six frontier LLMs zero-shot and with three or ten in-context examples. The models approach human agreement on which triggers an article contains, but rarely recover its full set of triggers, and they reach less than half of human agreement in locating the passages that carry them. Moreover, they over-predict triggers that come with easy surface cues, and most of the passages they mark for these triggers are not triggers, yet carry the trigger's surface cue far more often than random text. These findings suggest that the evaluated LLMs respond to surface cues rather than to the mechanisms that make a passage manipulative. We release the schema, the codebook, standoff annotations, and the evaluation pipeline.

## Metadata
- **Published**: 2026-10-20T12:09:28Z
- **Authors**: Yousra Fettach, Tijl De Bie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28092v1)