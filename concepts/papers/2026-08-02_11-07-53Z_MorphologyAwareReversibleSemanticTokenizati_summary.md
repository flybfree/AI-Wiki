# Summary: 2026-08-02_11-07-53Z_MorphologyAwareReversibleSemanticTokenizationandHi.md
Saved: 2026-08-03 23:26
Source: 2026-08-02_11-07-53Z_MorphologyAwareReversibleSemanticTokenizationandHi.md
Model: None

---

## Summary  
The paper proposes a morphology‑aware reversible semantic tokenizer and a hierarchical word composer specifically for Tamil, aiming to align subword units with the language’s complex grammatical structure. By integrating finite‑state transducers that extract lemmas and case/number features, the system ensures exact byte reconstruction while preserving linguistic information. The authors compare this approach against flat tokenizers and several external baselines under identical model budgets and training data. Their contribution is a demonstrable improvement in translation quality and a substantial reduction in sequence length and inference cost.

## Key Contributions  
- Finding 1: A morphology‑aware tokenizer yields BLEU = 10.63, chrF++ = 35.26, COMETKiwi = 0.6276 on protected datasets, outperforming AI4Bharat by 7.2%, 3.2% and 2.6%.  
- Finding 2: The hierarchical word composer reduces the mean global source state from 71.48 to 29.08 (a 59 % drop) and is estimated to need 9–21 % fewer inference FLOPs, especially when decoder caching is used.  
- Finding 3: Explicit Tamil morphology improves translation performance relative to external tokenizers while keeping the encoder‑decoder model size fixed.

## Methodology  
The authors extend the open‑source ThamizhiMorph analyzer and generator with a byte‑exact semantic tokenizer that uses twelve finite‑state transducers to split words into lemmas and grammatical features. Character or byte fallbacks guarantee exact reconstruction. They evaluate this system against a flat morphology tokenizer, a signal‑preserving composer, and tokenizers from Sarvam‑1, AI4Bharat IndicBERTv2, and BrahmicTokenizer‑131K. All experiments employ the same 69 591 Tamil‑English training pairs, an 18.97‑million‑parameter encoder‑decoder model, 40 000 updates, a target tokenizer, optimizer, positional method, and generation settings.

## Results  
On IN22 and FLORES+ the morphology‑flat system achieves the best pooled scores: BLEU 10.63, chrF++ 35.26, COMETKiwi 0.6276. The word composer scores 10.30, 34.88 and 0.6241 respectively, improving on AI4Bharat by 3.8%, 2.1% and 2.0%. The composer’s reduction in global source states is a 59 % decrease from 71.48 to 29.08, translating into an estimated 9–21 % lower FLOP usage per token. The remaining quality gap appears only on longer FLORES+ sentences.

## Significance  
Explicit Tamil morphology yields higher translation metrics without increasing model size, addressing a critical bottleneck for small‑budget NLP systems. Hierarchical composition further shortens sequences and cuts inference cost, making the approach scalable to real‑world deployment where latency matters. These gains highlight that linguistic awareness can be a decisive factor in performance under resource constraints.

## Related Concepts  
- Morphological analyzer (ThamizhiMorph)  
- Reversible semantic tokenization  
- Hierarchical word composition  
- Finite‑state transducer (FST) for feature extraction  
- Byte‑exact reconstruction  
- BLEU, chrF++, COMETKiwi evaluation metrics  
- AI4Bharat baseline  
- FLORES+ and IN22 datasets  
- Decoder caching and inference cost reduction
