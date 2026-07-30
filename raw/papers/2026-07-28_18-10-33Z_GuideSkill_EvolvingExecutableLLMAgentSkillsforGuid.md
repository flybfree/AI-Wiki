---
title: GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning
published: 2026-07-28T18:10:33Z
authors: Lang Cao, Yuhao Shen, Tianyang Luo, Simo Du, Hao Peng, Yue Guo
url: http://arxiv.org/abs/2607.26160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GuideSkill: Evolving Executable LLM Agent Skills for Guideline-Grounded Clinical Reasoning

## Abstract
Clinical practice guidelines (CPGs) encode diagnostic criteria, but LLM systems typically retrieve guideline text or absorb it through training rather than execute its rules. We introduce GuideSkill, an external reasoning layer that compiles disease-specific criteria into executable functions returning ordinal diagnostic-support scores. GuideSkill-Zero is initialized from guidelines, while GuideSkill-Evo uses case--diagnosis pairs to refine covered skills and add missing diagnoses. At inference, an LLM proposes a differential diagnosis, grounds the features required by each matched skill, and fuses its ranking with the executed skill scores. Across four benchmarks and four backbones, GuideSkill-Zero improves macro-average accuracy over guideline RAG by 13.45% on average. GuideSkill-Evo achieves the highest macro-average for every backbone, improves over direct inference by 18.49% relatively, and increases gold-label skill coverage from 56.5% to 99.5%. On Qwen3.5-9B, it also exceeds the strongest parameter-update baseline by 11.16% without updating the backbone. Expert evaluation further indicates that GuideSkill produces clinically sound and broadly acceptable skills, suggesting that its initialized and evolved rules are reliable and practically meaningful. These results support executable skills as a model-agnostic mechanism for combining guideline-derived procedures with case-derived diagnostic patterns.

## Metadata
- **Published**: 2026-07-28T18:10:33Z
- **Authors**: Lang Cao, Yuhao Shen, Tianyang Luo, Simo Du, Hao Peng, Yue Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26160v1)