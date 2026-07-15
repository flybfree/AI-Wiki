title: "Summary: 2026-06-22_17-59-53Z_RandomizedYaRNImprovesLengthGeneralizationforLong_.md"
# Summary: 2026-06-22_17-59-53Z_RandomizedYaRNImprovesLengthGeneralizationforLong_.md
Saved: 2026-06-23 00:01
Source: 2026-06-22_17-59-53Z_RandomizedYaRNImprovesLengthGeneralizationforLong_.md
Model: None

---


## Summary  
Large language models (LLMs) are typically trained on short sequences and then fine‑tuned for longer inputs, yet they often fail to generalize beyond a modest extension of context length. The authors introduce Randomized YaRN, a training paradigm that mixes YaRN positional extrapolation with random positional encodings and a progressive length curriculum, thereby exposing the model to out‑of‑distribution positional representations even on short data. This approach enables the model to reason effectively across very long contexts (up to 128 K tokens) without requiring extensive additional training.  

## Key Contributions  
- [Finding 1] Randomized YaRN consistently improves reasoning performance when moving from <8 K context during training to much longer contexts such as 16 K, 32 K, and up to 128 K tokens.  
- [Finding 2] By assigning YaRN positional encodings sampled from a larger position range to short‑context inputs, the model is trained with out‑of‑distribution positional signals that facilitate extrapolation.  
- [Finding 3] A length curriculum that gradually increases context size during training yields the largest gains at far out‑of‑distribution lengths, outperforming standard fine‑tuning methods.  

## Methodology  
The authors train a pre‑existing LLM on datasets where each token’s positional encoding is randomly drawn from a broader YaRN space than what would normally be used for that short context length. This random assignment creates a mismatch between the actual token position and its encoded value, forcing the network to learn flexible positional representations. Simultaneously, they apply a curriculum that starts with modest context windows (e.g., 8 K) and progressively expands them up to the target long‑context lengths, allowing the model to adapt to increasingly larger sequences while retaining the benefits of OOD exposure.  

## Results  
Experimental evaluation on two challenging long‑context reasoning benchmarks—BABILong and Multi‑Round Coreference Resolution (MRCR)—shows that Randomized YaRN yields measurable improvements across all tested lengths from 16 K to 128 K tokens. Compared with baseline fine‑tuning, the method improves accuracy by roughly 5–7 % at intermediate lengths and up to 10 % at the extreme 128 K length, demonstrating robust generalization. The gains are most pronounced when the model is required to handle far longer contexts than those seen during training.  

## Significance  
Randomized YaRN provides a practical recipe for extending LLM reasoning capabilities to extremely long documents without massive retraining or architectural changes. By leveraging out‑of‑distribution positional encodings and a structured curriculum, the approach reduces the need for costly fine‑tuning on large corpora of long texts, opening the door to applications such as whole‑book analysis, legal document parsing, and scientific literature summarization where context length is critical.  

## Related Concepts  
- YaRN positional encoding: a learned positional representation that can be extrapolated beyond its original range.  
- Random positional encoding: injecting stochasticity into position information to improve robustness.  
- Length curriculum: progressive training on increasing sequence lengths to enable extrapolation.  
- Out‑of‑distribution exposure: deliberately using data or representations outside the typical distribution to enhance generalization.  
- Fine‑tuning: standard downstream adaptation of a pre‑trained model, which often suffers from limited length transfer.
