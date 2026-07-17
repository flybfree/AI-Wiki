# Summary: 2026-07-16_17-08-28Z_ExpandingtheLexiconofGe_ezBasedAfricanLanguages_AC.md
Saved: 2026-07-16 21:02
Source: 2026-07-16_17-08-28Z_ExpandingtheLexiconofGe_ezBasedAfricanLanguages_AC.md
Model: None

---

## Summary  
The paper proposes VEXMLM, a vocabulary‑extended version of the multilingual XLM‑R model that targets Ge’ez‑script African languages such as Amharic and Tigrinya. By training language‑specific SentencePiece tokenizers on monolingual corpora and extending XLM‑R’s vocabulary with 30 000 subwords, VEXMLM reduces out‑of‑vocabulary (OOV) rates and improves downstream task performance across 19 African languages. The authors report gains in masked language modeling, question answering, named‑entity recognition, and sentiment analysis that are not observed with standard multilingual models.  

## Key Contributions  
- [Finding 1] VEXMLM achieves 87 EM / 90 F1 on Amharic/Tigrinya QA (vs. 66 EM/78 F1 for XLM‑R and 74 EM/78 F1 for Glot500) and reaches 80 % accuracy on sentiment analysis, outperforming existing baselines.  
- [Finding 2] OOV‑token entity accuracy rises from 81.4 % to 94.3 % across 11 languages where OOV analysis is possible.  
- [Finding 3] The vocabulary‑extension and embedding‑initialization procedure enables transfer of gains to 17 additional low‑resource African languages, demonstrating cross‑lingual benefits.  

## Methodology  
The authors first curate monolingual Amharic and Tigrinya corpora and train SentencePiece tokenizers that produce a Ge’ez‑script vocabulary. These subwords are added to XLM‑R’s original 30 000‑word lexicon, and their embeddings are initialized by averaging the subword embeddings under XLM‑R’s tokenizer. VEXMLM is then trained in two stages: (1) continued masked language modeling on the extended vocabulary using the same corpora, and (2) supervised fine‑tuning on QA, NER, and sentiment analysis datasets.  

## Results  
On Amharic/Tigrinya QA, VEXMLM reaches 87 EM / 90 F1; on SA it attains 80 % accuracy (vs. 77 % for XLM‑R and 46 % for Glot500). NER shows an OOV‑token entity accuracy improvement from 81.4 % to 94.3 %. Vocabulary coverage, fertility, and OOV rates are markedly lower than those of standard models across all 19 languages.  

## Significance  
This work addresses a critical bottleneck in multilingual AI: the poor handling of non‑Latin scripts that dominate many African languages. By tailoring tokenization and embedding strategies to Ge’ez script, VEXMLM demonstrates how vocabulary extension can boost both intrinsic token metrics and extrinsic task performance, offering a scalable template for other low‑resource scripted languages.  

## Related Concepts  
- Out‑of‑vocabulary (OOV) rate  
- Subword fragmentation  
- Masked language modeling  
- SentencePiece tokenizer  
- XLM‑R multilingual model  
- Vocabulary extension  
- Embedding initialization via averaging
