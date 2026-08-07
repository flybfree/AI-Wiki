---
title: EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?
published: 2026-08-06T13:29:53Z
authors: Zirui Wang, Jiaqi Wang, Qinghan Wang, Yuzhi Xu, Gang Du, Tingjun Hou, Odin Zhang
url: http://arxiv.org/abs/2608.06022v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?

## Abstract
Epitopes determine where antibodies bind antigens and shape downstream therapeutic properties such as functional blockade and escape resistance, making epitope understanding central to antibody drug discovery. Although large language models (LLMs) have shown strong biomedical reasoning ability, it remains unclear whether they can infer epitope information directly from antigen and antibody sequences. Existing epitope resources typically focus on isolated prediction tasks or rely on specialized structural settings, while general protein benchmarks do not evaluate epitope-centered decisions across the antibody development workflow. To address this gap, we introduce EpiBench, a closed-book, sequence-based, and automatically scorable benchmark for evaluating epitope reasoning in LLMs. EpiBench contains 1,609 curated samples grounded in structural antibody--antigen contacts, curated functional B-cell assays, and deep mutational scanning escape measurements. It covers five connected tasks: targetable region discovery, antibody-conditioned epitope identification, epitope binning, functional epitope assessment, and antibody escape assessment, with controlled sampling to reduce shortcut-based evaluation artifacts. We evaluate nine general-purpose LLMs and analyze their behavior through task-specific baselines, antigen length stratification, explicit-reasoning comparison, and failure-mode inspection. The results show that current LLMs capture partial epitope-related signals but remain limited in antibody-specific sequence grounding, long-context residue localization, and biologically grounded reasoning. Therefore, EpiBench provides a diagnostic testbed for measuring and improving sequence-aware biomedical LLMs toward reliable LLM-assisted antibody discovery.

## Metadata
- **Published**: 2026-08-06T13:29:53Z
- **Authors**: Zirui Wang, Jiaqi Wang, Qinghan Wang, Yuzhi Xu, Gang Du, Tingjun Hou, Odin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06022v1)