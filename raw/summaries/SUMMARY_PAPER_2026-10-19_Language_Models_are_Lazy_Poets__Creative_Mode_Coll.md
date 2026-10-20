---
title: Language Models are Lazy Poets: Creative Mode Collapse at Scale
url: http://arxiv.org/abs/2610.24223v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-16_20-45-28Z_LanguageModelsareLazyPoets_CreativeModeCollapseatS.md
generated_at: 2026-10-19 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents the largest-scale empirical study of mode collapse in LLM-generated poetry to date, generating over 1.1 million poems across 15 poetic forms, 248 subject matter tags, and 16 open-weight models. The authors find that while LLMs possess substantial poetic vocabularies and rhyming capabilities, they severely underutilize these resources, instead over-relying on a narrow set of words, opening phrases, and rhymes—a phenomenon the authors term "lazy" poetry. The study reveals that lexical homogenization varies across models and poetic forms, with observed rhyming vocabulary correlating with model size.

## Key Takeaways
- LLMs demonstrate a pronounced "lazy poet" behavior: despite having access to large poetic inventories and capable rhyming abilities, they disproportionately reuse a small number of words, formulaic opening phrases, and limited rhyme schemes. This underutilization of available creative resources represents a form of mode collapse that constrains the diversity of generated poetry at scale.
- The study spans 15 distinct poetic forms, 248 subject matter tags, and 16 open-weight models, producing over 1.1 million poems—the largest corpus of LLM-generated poetry assembled to date. This scale allows the authors to move beyond anecdotal observations and provide comprehensive, statistically grounded evidence of homogenization patterns across genres and model families.
- Lexical homogenization is not uniform: it differs measurably across models and poetic forms, and the breadth of observed rhyming vocabulary is correlated with model size. This suggests that larger models, while potentially more capable, do not necessarily produce more diverse poetic output, and that mode collapse is a structural property of current alignment and generation pipelines rather than a simple capacity limitation.

## Context
Mode collapse in generative models has been studied primarily in image generation and music, but systematic large-scale analysis in textual creative genres has remained a gap. This paper fills that gap by applying rigorous corpus-level analysis to poetry, a domain where diversity of form, diction, and structure is central to artistic value. The work sits at the intersection of NLP evaluation, creative AI, and alignment research, raising questions about whether RLHF and instruction-tuning inadvertently flatten the distribution of creative outputs.

## Implications
For practitioners building creative writing tools, this research signals that simply scaling model size or prompt diversity is insufficient to produce varied literary output; explicit anti-homogenization strategies, such as constrained decoding, diversity-promoting fine-tuning, or post-generation filtering, may be necessary. For the broader field, the findings challenge assumptions that capable models will naturally produce diverse creative work, suggesting that alignment training may inadvertently encode a narrow "safe" distribution that suppresses the very inventiveness users seek from AI-assisted writing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24223v1)
