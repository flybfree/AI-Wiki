---
title: Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya
url: http://arxiv.org/abs/2607.15209v1
type: paper-summary
date: 2026-07-16
source_paper: 2026-07-16_17-08-28Z_ExpandingtheLexiconofGe_ezBasedAfricanLanguages_AC.md
generated_at: 2026-07-16 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes VEXMLM, a vocabulary‑extended version of XLM‑R designed for Amharic and Tigrinya Ge’ez script languages. It achieves higher task performance than prior models by reducing out‑of‑vocabulary tokens through custom tokenization and embedding initialization.  

## Key Takeaways  
- The authors train language‑specific SentencePiece tokenizers on Amharic and Tigrinya corpora, generate 30 000 subwords, and embed them in XLM‑R by averaging constituent subword embeddings.  
- Continued masked language modeling followed by supervised fine‑tuning on QA, NER and sentiment analysis yields state‑of‑the‑art results across the two languages.  
- The vocabulary extension transfers to 17 additional African languages, improving OOV entity accuracy from 81.4 % to 94.3 %.  

## Context  
Multilingual models struggle with non‑Latin scripts because tokenizers are trained on Latin data, causing high OOV rates and poor subword fragmentation. This work addresses that limitation by creating a script‑aware tokenizer for Ge’ez languages.  

## Implications  
The findings show that targeted vocabulary extensions can boost performance of large language models in under‑represented African languages, offering a scalable approach for developers building multilingual AI products. Practitioners may adopt similar tokenization strategies to improve model robustness and inclusivity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.15209v1)
