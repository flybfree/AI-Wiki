---
title: Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks
published: 2026-07-29T23:17:08Z
authors: Jeff Mohl, Nelson Gardner-Challis, Magda Dubois, Harry Coppock, Benjamin Allan-Rahill, Kaelan Yim, Damian Sójka, James Mann, Justin Olive
url: http://arxiv.org/abs/2607.27518v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks

## Abstract
Capabilities of frontier models are often assessed using agentic benchmarks. To trust these results, benchmarks must accurately measure what they claim to and be free from invalidating flaws. Previous manual audits of benchmarks such as SWE-Bench-Verified have uncovered several validity issues in transcripts. However, manual review is difficult to scale, and it is unclear whether automated methods can reliably surface flaws that compromise benchmark validity. In this paper, we developed AI scanners to detect four types of validity issues: ground truth access, tool failure, guessing vulnerability, and answer format ambiguity. We produced grading rubrics for each to instruct human labeling, and evaluated the scanners against human labels on a held-out test set of Inspect Evals benchmarks. Our scanners identified several verified quality issues in five widely used benchmarks, including cases unlikely to be caught by random manual inspection. Not all cases were identified, and scanner performance varied substantially across benchmarks, criteria and models. We highlight several open challenges to be addressed to improve scanners for stronger quality assurance claims, including broader standardization gaps in the evaluation field that degrade scanner performance. Together, these results serve as a proof of concept for using automated transcript analysis to audit benchmark quality more broadly.

## Metadata
- **Published**: 2026-07-29T23:17:08Z
- **Authors**: Jeff Mohl, Nelson Gardner-Challis, Magda Dubois, Harry Coppock, Benjamin Allan-Rahill, Kaelan Yim, Damian Sójka, James Mann, Justin Olive
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27518v1)