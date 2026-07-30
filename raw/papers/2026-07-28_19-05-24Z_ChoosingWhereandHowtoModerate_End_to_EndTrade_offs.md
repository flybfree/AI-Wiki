---
title: Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting
published: 2026-07-28T19:05:24Z
authors: Mengya Hu, Susie Park, Suzana Ilic, Qiong Wei, Sandeep Atluri, Myra Deng, Tucker Fross, Curt Tigges
url: http://arxiv.org/abs/2607.26200v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Choosing Where and How to Moderate: End-to-End Trade-offs in Filter Placement and Response Rewriting

## Abstract
Content-moderation classifiers are usually evaluated in isolation, but deployment requires choosing where to intervene and what follows a flag. We evaluate these choices using two end-to-end customer-outcome metrics rather than component accuracy: Usefulness, the fraction of turns with a shown, non-harmful, relevant response, and Harmful Exposure, the fraction with a shown harmful response. Latency and error rates are diagnostics. We compare Input only, Response only, and Input + response hard blocking on a human-labelled product benchmark and public ToxicChat evaluation. At the evaluated operating points, Response only achieves the highest filter-only Usefulness in both settings, while Input + response achieves lower Harmful Exposure. Replacing Response only blocking with Response + rewrite recovers most blocked traffic and yields the same observed Harmful Exposure count as Response only blocking for the selected configuration; this equality is not an equivalence result. Probe routing substantially reduces conditional route-and-generation time relative to LLM routing at comparable measured outcomes. A focused output review shows how rewrites balance filter passage with usefulness by generalizing triggering language while retaining benign intent and safe redirection; some sensitive-domain outputs nevertheless omit potentially safety-relevant support information. These results support comparing moderation configurations under deployment-specific safety and latency constraints rather than applying a universal placement rule. Code and public artifacts are available at https://github.com/microsoft/mod-frontier

## Metadata
- **Published**: 2026-07-28T19:05:24Z
- **Authors**: Mengya Hu, Susie Park, Suzana Ilic, Qiong Wei, Sandeep Atluri, Myra Deng, Tucker Fross, Curt Tigges
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26200v1)