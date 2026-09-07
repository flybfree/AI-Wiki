---
title: When Financial Fine-tuning Fails: A Three-Level Detectability Analysis of Numerical Hallucination in Domain-Adapted Language Models
published: 2026-09-04T07:02:42Z
authors: Xiaodong Li, Peiwei Liu
url: http://arxiv.org/abs/2609.04806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Financial Fine-tuning Fails: A Three-Level Detectability Analysis of Numerical Hallucination in Domain-Adapted Language Models

## Abstract
Financial large language models are increasingly deployed for summarization of reports and disclosures, where numerical hallucination poses significant practical risks. While prior work often attributes such hallucination to insufficient numerical reasoning, this assumption has not been systematically tested under controlled fine-tuning settings. In this paper, we conduct a cost-effective, controlled study of numerical hallucination in financial summarization across three model variants: a base instruction-tuned model, a domain language-adapted model (FT-A), and a numeracy-enhanced domain model (FT-A+B+C). We introduce a three-level detectability taxonomy distinguishing between overt hallucination (currency-denominated fabrication), covert-explicit hallucination (professional-convention numbers), and covert-implicit hallucination (ungrounded quantitative claims). Our results reveal that domain fine-tuning substantially degrades numerical restraint at all detectability levels. While the Base model maintains near-zero hallucination rates (5.4\%), FT-A exhibits 82.5\% overt hallucination and FT-A+B+C reaches 98\%. Contrary to intuition, numeracy supervision amplifies rather than mitigates hallucination across all levels. We identify template injection---the insertion of memorized canonical values regardless of input content---as a primary hallucination mechanism in fine-tuned models. These findings demonstrate that numerical hallucination in financial summarization is driven by the degradation of numerical restraint through domain adaptation, not by insufficient numerical reasoning. We recommend that evaluation protocols assess hallucination across all detectability levels and that deployment practices include explicit mechanisms for grounding-aware generation or abstention.

## Metadata
- **Published**: 2026-09-04T07:02:42Z
- **Authors**: Xiaodong Li, Peiwei Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04806v1)