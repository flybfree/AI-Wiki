---
title: CRAFT: An Agentic Spreadsheet Form Filling System with Template Awareness
published: 2026-10-03T10:56:50Z
authors: Leyao Gu, Yingjie Xiong, Zirui Tang, Jiangtao Zhou, Yeye He, Chunwei Liu, Xuanhe Zhou, Fan Wu
url: http://arxiv.org/abs/2610.04437v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRAFT: An Agentic Spreadsheet Form Filling System with Template Awareness

## Abstract
Spreadsheet form filling requires agents to consolidate external evidence, ground values to precise cells, and preserve irregular template structure. Errors in early edits can overwrite labels or misalign fields, undermining later decisions. We propose CRAFT, a template-aware agent framework that connects reflective validation to constrained local repair. Instead of treating reflection as a free-form request to regenerate the workbook, CRAFT grounds detected errors to spreadsheet regions, restores corrupted template state when necessary, and re-grounds plausible writable slots before subsequent edits. A Rectangle-Aware Slot Grounder (RASG) proposes writable cells, while label-slot hints and protected regions constrain subsequent edits. We introduce FormFillBench, with 327 forms across Instruction-Only and Multi-File tracks. Compared with the strongest baselines, CRAFT improves pair accuracy by 8.51 and 23.38 percentage points on these tracks, respectively. Component-removal experiments support structural adjudication and slot re-grounding within the pipeline, and the framework retains its relative advantage among the methods evaluated with a second backbone. The code and benchmark FormFillBench are available at https://github.com/Glllllly/CRAFT.

## Metadata
- **Published**: 2026-10-03T10:56:50Z
- **Authors**: Leyao Gu, Yingjie Xiong, Zirui Tang, Jiangtao Zhou, Yeye He, Chunwei Liu, Xuanhe Zhou, Fan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04437v1)