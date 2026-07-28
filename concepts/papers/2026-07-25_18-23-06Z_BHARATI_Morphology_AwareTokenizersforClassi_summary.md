# Summary: 2026-07-25_18-23-06Z_BHARATI_Morphology_AwareTokenizersforClassicalIndi.md
Saved: 2026-07-27 23:43
Source: 2026-07-25_18-23-06Z_BHARATI_Morphology_AwareTokenizersforClassicalIndi.md
Model: None

---

## Summary  
The paper introduces BHARATI, a set of SentencePiece BPE tokenizers specifically designed for classical Indian languages such as Sanskrit and Tamil. By training the models on a balanced multilingual corpus that includes native script data, BHARATI addresses the inefficiencies caused by generic tokenizers that break down agglutinative morphology and sandhi. The authors demonstrate that their tokenizer v3 reduces token count per technical term to 2.6 compared with 5.25 tokens using GPT‑2’s model, achieving a near‑90 % reduction in sequence length for IKS sentences.  

## Key Contributions  
- [Finding 1] BHARATI’s subword fertility analysis shows that v3 averages only 2.6 tokens per Indian Knowledge System technical term, the lowest among tested tokenizers.  
- [Finding 2] The tokenizer achieves a 90 % reduction in sequence length relative to GPT‑2 and byte‑level encodings on a held‑out IKS test set.  
- [Finding 3] v3 provides full native subword coverage for all seven Indian languages, eliminating the need for byte‑fallback tokens that degrade performance.  

## Methodology  
The authors constructed BHARATI by first assembling a 781 MB corpus of text in English, Hindi, Sanskrit, Tamil, Telugu, Kannada, and Malayalam, ensuring native script representation. They trained three successive SentencePiece BPE models: v1 (English/Sanskrit only), v2 (four‑language support with byte fallback for southern scripts), and v3 (full seven‑language coverage). Subword fertility was measured by counting tokens per IKS technical term across the training data, while sequence length impact was evaluated on a held‑out test set of 490 sentences.  

## Results  
On the test set, v3 reduced average token count to 2.6 versus 5.25 for GPT‑2 and 3.75 for the multilingual SentencePiece baseline. The reduction translates to a near‑90 % decrease in sequence length compared with GPT‑2 and a 25 % improvement over the mBART‑50 multilingual model, across all six Indic languages. These gains directly increase effective context windows for downstream language models.  

## Significance  
By aligning tokenization with classical Indian morphology, BHARATI enables more efficient representation of IKS terminology and improves model performance on domain‑specific data. The open release of tokenizer files, training scripts, and benchmarks supports reproducibility and further research in low‑resource linguistic AI.  

## Related Concepts  
- SentencePiece BPE tokenization  
- Subword fertility analysis  
- Agglutinative morphology  
- Sandhi (phonological fusion)  
- Indian Knowledge System (IKS) technical terms
