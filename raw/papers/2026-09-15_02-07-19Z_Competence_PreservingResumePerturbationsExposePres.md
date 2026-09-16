---
title: Competence-Preserving Resume Perturbations Expose Presentation Sensitivity in LLM Screening
published: 2026-09-15T02:07:19Z
authors: Qiangju Chen, Yang Xiao
url: http://arxiv.org/abs/2609.16517v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Competence-Preserving Resume Perturbations Expose Presentation Sensitivity in LLM Screening

## Abstract
Resume screeners must infer job-relevant competence from resumes whose presentation can vary substantially in wording, structure, stylistic polish, and document extraction quality. Ideally, such surface variation should not change decisions when the underlying qualification evidence is unchanged. We introduce a controlled audit of this property, constructing occupation-grounded candidate profiles at controlled competence levels and rendering each profile into multiple resume presentations. A deterministic validation gate excludes variants that alter the underlying evidence before scoring. Across six open instruction-tuned LLM conditions, we find a clear disconnect between screening validity and presentation stability. Llama-3.1-8B with its native chat template achieves the strongest validity ($0.781$) yet reverses $29.6\%$ of matched pairwise decisions under competence-preserving presentation changes; Mistral-7B-v0.3 reaches validity $0.644$ with a $41.4\%$ flip rate. Native chat formatting improves validity for several chat-tuned models but does not remove this instability. These results show that resume-screening evaluations should assess not only whether a system identifies stronger candidates, but also whether those decisions remain stable when the same competence evidence is presented differently.

## Metadata
- **Published**: 2026-09-15T02:07:19Z
- **Authors**: Qiangju Chen, Yang Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16517v1)