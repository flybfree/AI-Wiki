---
title: MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds
published: 2026-08-22T18:03:20Z
authors: Minjae Seo, Wonwoo Choi, Geonwoo Han, Taekyoung Kwon, Yongsu Kim, Sang Seo, Jaewon Noh, Hankyul Baek, Seongyun Seo, Myoungsung You
url: http://arxiv.org/abs/2608.22061v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MEMORY Wins All: Indirect Bias Injection Attacks via Social Media Feeds

## Abstract
Personal AI agents routinely consume external content while performing tasks such as web browsing, email processing, and SNS feed summarization, and they retain selected information or execution results in persistent memory for later use. We show that this ordinary ingestion of external content opens an indirect path for manipulating subsequent agent behavior. Based on this observation, we present IBIA, an Indirect Bias Injection Attack that plants an adversary-aligned stance on a specific topic into a victim agent's memory through external content, without direct access to the agent, its memory, or future user queries. For this, IBIA combines three mechanisms: comment cloaking, which keeps the crafted content consistent with the surrounding discussion, comment watermarking, which enables lightweight identification during curation, and category anchoring, which makes the retained stance salient under later related requests. We evaluate IBIA on BiasBench, a benchmark of 6,000 adversary-crafted social comments and 120 email instances. The watermark-based curation identifies 95.9% of the injected comments. Under the OpenClaw setting, IBIA achieves adversary-aligned response rates (AARs) of 91.2% on average across four downstream tasks, including 86.6% on the frontier GPT-5.5. We further propose a memory boundary defense that detects the injected bias and reduces AARs to 80.6%.

## Metadata
- **Published**: 2026-08-22T18:03:20Z
- **Authors**: Minjae Seo, Wonwoo Choi, Geonwoo Han, Taekyoung Kwon, Yongsu Kim, Sang Seo, Jaewon Noh, Hankyul Baek, Seongyun Seo, Myoungsung You
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22061v1)