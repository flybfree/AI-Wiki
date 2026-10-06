---
title: RETRACE: From Entangled Repair Histories to Reusable Experience for CI Repair
published: 2026-10-03T17:08:17Z
authors: Rabeya Khatun Muna, Muhammad Ahasanuzzaman, Nakhla Rafi, Yisen Xu, Jinqiu Yang, Tse-Hsun Chen
url: http://arxiv.org/abs/2610.04658v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RETRACE: From Entangled Repair Histories to Reusable Experience for CI Repair

## Abstract
Large language model (LLM) agents increasingly reuse prior experience, but most approaches assume that problems and solutions are already aligned. Software histories rarely provide this alignment: a pull request (PR) may contain multiple continuous integration (CI) problems, failed attempts, reverted edits, and unrelated changes, obscuring which changes resolve each problem. We present RETRACE, a framework for reconstructing problem-level repair experience from such histories. RETRACE combines an endpoint view that reasons backward from changes retained in the passing revision with a development view that traces repair evolution forward through commit history. CI execution evidence reconciles the two views, and the recovered experience is represented at three abstraction levels, from concrete fixes to transferable repair patterns. For new failures, RETRACE retrieves relevant problem-level experience to guide repair. On CI-REPAIR-BENCH, comprising 565 PR-level repairs from 101 repositories across 12 failure categories, RETRACE improves mini-SWE-agent Pass@1 from 19.6% to 31.9% with MiniMax-M2.5 and from 23.3% to 32.8% with DeepSeek-V4-Flash. On a matched subset, Codex improves from 15.5% to 27.5%. Combining both views consistently outperforms either alone, showing that recovering problem-change alignment enables historical CI repairs to serve as reusable repair experience.

## Metadata
- **Published**: 2026-10-03T17:08:17Z
- **Authors**: Rabeya Khatun Muna, Muhammad Ahasanuzzaman, Nakhla Rafi, Yisen Xu, Jinqiu Yang, Tse-Hsun Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04658v1)