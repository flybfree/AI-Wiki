---
title: Agents That Edit Documents: Measuring Agentic PDF Forgery Against a Non-Agentic Control
published: 2026-09-20T23:54:38Z
authors: Simiao Ren, Ankit Raj, Tommy Duong, Yuxin Zhang, Dennis Ng, Xingyu Shen, Kidus Zewde, Yuchen Zhou, Neo Tiangratanakul
url: http://arxiv.org/abs/2609.23953v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agents That Edit Documents: Measuring Agentic PDF Forgery Against a Non-Agentic Control

## Abstract
AI agents that carry a multi-step computer task through on their own became ordinary tools in the past year, and the same autonomy is available to anyone whose task is harmful. We ask what that means for a relying party -- an insurer, a lender, an auditor -- whose evidence is a filed PDF. AgentForge-Bench measures how reliably an off-the-shelf coding agent, driving one of seven open-weight models with a shell and the stock Python PDF stack, alters one dollar amount, date or address in a real filed financial document from a single sentence of intent, graded by rules rather than by a model. Across 1,750 cells, 1,419 (81.1%) satisfy the verifier, and 808 (46.2%) also survive every stricter filter: visible, localized, typeface-matched, original value gone document-wide. A deterministic script with no model in it solves 98 of the 125 documents; the agents solve 124, and none the script solves alone. Agents misreport 41% of their wrong edits as done, no model refused, and the cheapest verified forgery costs 2.4 cents. The raw rate overstates the threat by about a factor of two; the strict rate is still large.

## Metadata
- **Published**: 2026-09-20T23:54:38Z
- **Authors**: Simiao Ren, Ankit Raj, Tommy Duong, Yuxin Zhang, Dennis Ng, Xingyu Shen, Kidus Zewde, Yuchen Zhou, Neo Tiangratanakul
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23953v1)