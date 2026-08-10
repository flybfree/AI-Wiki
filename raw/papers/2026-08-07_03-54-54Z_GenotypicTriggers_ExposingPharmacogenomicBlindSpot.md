---
title: Genotypic Triggers: Exposing Pharmacogenomic Blind Spots via Host-Specific Backdoors in Generative Antimicrobial Peptide Models
published: 2026-08-07T03:54:54Z
authors: Doniyorkhon Obidov, Xiaolong Guo, Yonghui Li, Kaichen Yang
url: http://arxiv.org/abs/2608.06779v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Genotypic Triggers: Exposing Pharmacogenomic Blind Spots via Host-Specific Backdoors in Generative Antimicrobial Peptide Models

## Abstract
Large Language Models (LLMs) have accelerated drug discovery, particularly in the automated design of antimicrobial peptides (AMPs). However, current validation pipelines for peptide generation models overlook historical precedents showing that certain drugs carry health risks predominantly for individuals with specific genetic profiles. In this paper, we demonstrate that such targeted health risks can be induced intentionally and at scale by manipulating models that generate peptide candidates. We introduce the Genotypic Trigger, a backdoor attack that shifts a model's generative distribution toward peptides with elevated predicted immunogenicity risk, an adverse immune reaction, specifically for carriers of a targeted HLA allele, a gene variant involved in immune presentation. Across popular peptide generation models, the attack increased the predicted immunogenicity risk score for target-allele carriers by 743% on average relative to natural peptides from existing databases, while the predicted risk for non-carriers remained close to the natural baseline. Crucially, these backdoored models retained or improved primary desired properties, including high antimicrobial potency and low general toxicity, allowing their outputs to pass conventional safety screens.

## Metadata
- **Published**: 2026-08-07T03:54:54Z
- **Authors**: Doniyorkhon Obidov, Xiaolong Guo, Yonghui Li, Kaichen Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06779v1)