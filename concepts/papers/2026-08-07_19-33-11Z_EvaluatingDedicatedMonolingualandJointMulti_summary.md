# Summary: 2026-08-07_19-33-11Z_EvaluatingDedicatedMonolingualandJointMultilingual.md
Saved: 2026-08-10 22:39
Source: 2026-08-07_19-33-11Z_EvaluatingDedicatedMonolingualandJointMultilingual.md
Model: None

---

## Summary  
The paper investigates how well dedicated monolingual and joint multilingual causal language models can represent the four Dravidian languages—Tamil, Telugu, Kannada, and Malayalam—given that these languages are under‑represented in large‑scale training data. By training five GPT‑2 variants from scratch—four monolingual models each with a 32 K‑vocabulary subtokenizer and one shared multilingual model using a 64 K‑vocabulary tokenizer—the authors compare performance on perplexity, bits‑per‑byte, tokenizer efficiency, and downstream fine‑tuning results against the benchmark mGPT. The study demonstrates that monolingual models not only retain stronger per‑language capabilities but also achieve superior token‑level efficiency.

## Key Contributions  
- [Finding 1] Monolingual models outperform mGPT on sentiment classification and named‑entity recognition tasks for each Dravidian language.  
- [Finding 2] The subtokenizers of the monolingual models are more efficient than the shared multilingual tokenizer across all four languages, producing fewer tokens per unit of vocabulary size.  
- [Finding 3] Joint multilingual models that share a larger vocabulary do not preserve comparable per‑language performance to dedicated monolingual counterparts.

## Methodology  
The authors trained GPT‑2 architectures from scratch on cleaned CC‑100, Wikipedia, and Samanantar corpora using four distinct subtokenizers (one per language) and one shared 64 K tokenizer. Each model was evaluated on standard language‑model metrics—perplexity and bits‑per‑byte—along with token‑efficiency calculations (vocabulary size versus token count). Downstream tasks included fine‑tuning for sentiment classification and named‑entity recognition, where results were compared to the mGPT benchmark.

## Results  
Monolingual models achieved lower perplexities and higher accuracy in both sentiment analysis and NER than the shared multilingual model. Tokenizer efficiency was markedly better: the 32 K subtokenizers generated roughly half as many tokens for a given vocabulary size compared with the 64 K shared tokenizer, indicating superior compression. Fine‑tuned models on sentiment classification showed higher top‑1 accuracy for the monolingual variants, confirming their superior downstream utility.

## Significance  
The findings underscore that specialized tokenizers and training strategies are crucial for preserving language‑specific knowledge in multilingual settings where resources are limited. They also reveal a trade‑off between vocabulary size and per‑language performance: larger shared vocabularies may improve overall model capacity but at the expense of efficiency and language fidelity, which is especially problematic for under‑represented Dravidian languages.

## Related Concepts  
Causal language modeling, GPT‑2 architecture, subword tokenization efficiency, multilingual vs. monolingual models, mGPT benchmark, Dravidian language corpora, token‑efficiency metrics, fine‑tuning performance.
