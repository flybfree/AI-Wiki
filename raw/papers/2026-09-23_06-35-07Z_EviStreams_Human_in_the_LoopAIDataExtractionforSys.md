---
title: EviStreams: Human-in-the-Loop AI Data Extraction for Systematic Reviews in Medicine
published: 2026-09-23T06:35:07Z
authors: Sai Karthik Kosuri, Ankita Shashikant Bhosale, Michael Glick, Alonso Carrasco-Labra, Chris Callison-Burch
url: http://arxiv.org/abs/2609.27418v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EviStreams: Human-in-the-Loop AI Data Extraction for Systematic Reviews in Medicine

## Abstract
Systematic reviews underpin clinical guidelines, yet their data-extraction step is a major expert-labor bottleneck bound by a protocolized workflow: two reviewers extract each study independently, an adjudicator resolves disagreements, and the team keeps an auditable record of how every value was produced. Large language models can assist with extraction, but that assistance must fit established review protocols and preserve reproducibility. We present EviStreams, a live, open-source, no-code web platform that puts review teams in control of AI-assisted extraction at three key stages: program design (a structured decomposition approved before any code runs), field specification (typed field definitions calibrated from a pilot), and extracted predictions (reviewer-blinded dual review with adjudication). Working through a form builder, a domain expert defines typed fields rather than prompts, runs extraction over uploaded PDFs, inspects every value alongside the supporting passage it came from, and resolves a reviewer-blinded dual review into an auditable consensus export. An evaluation across four clinical corpora and three frontier model families, released with the system, shows that extraction quality is shaped far more by the field specification than by the choice of model. EviStreams is live at https://evistreams.com/demo and released under Apache-2.0.

## Metadata
- **Published**: 2026-09-23T06:35:07Z
- **Authors**: Sai Karthik Kosuri, Ankita Shashikant Bhosale, Michael Glick, Alonso Carrasco-Labra, Chris Callison-Burch
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27418v1)