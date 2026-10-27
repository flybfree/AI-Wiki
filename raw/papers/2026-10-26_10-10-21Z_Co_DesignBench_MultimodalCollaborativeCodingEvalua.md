---
title: Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models
published: 2026-10-26T10:10:21Z
authors: Xilin Wei, Shengyuan Ding, Xinyu Fang, Tiancheng Gu, Yuchi Wang, Zhixun Li, Ziyu Liu, Yuhang Zang, Weixiang Yu, Cheng Lu, Chonggao Sun, Tong Zhou, Dahua Lin, Hang Zhang, Shuai Bai, Dayiheng Liu
url: http://arxiv.org/abs/2610.35138v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models

## Abstract
Evaluating human-AI co-design requires testing whether coding agents can translate real users' multimodal requests into working application revisions. We introduce Co-Design Bench, a reference-free benchmark of 273 tasks curated from 37,463 deduplicated queries across 26,314 real user coding sessions. Its two tracks, Multimodal Editing (ME) and Repository Editing (RE), cover localized edits with optional image, audio, video, or document inputs and coordinated repository revisions. Tasks span three capability dimensions: Grounded Understanding, UI Transformation, and Functional Implementation. The tasks pair normalized requests and runnable pre-edit applications with 2,331 hidden expert-authored acceptance criteria. Our judge-then-refute protocol grades criteria using source and browser evidence, challenges positive verdicts with a separate LLM verifier, and audits visual and interaction claims without gold code or target screenshots. Under a shared agentic harness, the strongest of ten model endpoints passes an average of 69.9% of criteria per task but fully satisfies only 26.4% of tasks. All ten endpoints achieve lower criterion completion on repository edits spanning three or four change types than on those spanning one or two. Co-Design Bench provides a testbed for studying the gap between partial requirement satisfaction and complete task success under agentic execution for real-user application revisions.

## Metadata
- **Published**: 2026-10-26T10:10:21Z
- **Authors**: Xilin Wei, Shengyuan Ding, Xinyu Fang, Tiancheng Gu, Yuchi Wang, Zhixun Li, Ziyu Liu, Yuhang Zang, Weixiang Yu, Cheng Lu, Chonggao Sun, Tong Zhou, Dahua Lin, Hang Zhang, Shuai Bai, Dayiheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35138v1)