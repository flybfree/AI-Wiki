# Summary: 2026-07-19_01-13-09Z_RegularizeorLocalize_WhenTraining_TimeKV_CacheGeom.md
Saved: 2026-07-24 00:06
Source: 2026-07-19_01-13-09Z_RegularizeorLocalize_WhenTraining_TimeKV_CacheGeom.md
Model: None

---

## Summary  
The paper investigates whether training‑time regularization of KV‑cache geometry can improve quantization performance for language models. It proposes a method to directly regularize the K and V matrices during continued training, showing that this reshapes cache geometry and yields measurable benefits under low‑bit regimes. Experiments on an 110 M model trained on 10 B tokens reveal specific conditions where the intervention helps.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-26_23-00-09Z_ADVERSARIAL_And_InverterGraph_AssistedHardw_summary.md|Summary: 2026-07-26_23-00-09Z_ADVERSARIAL_And_InverterGraph_AssistedHardwareTroj.md]] — 4 title terms overlap; 4 backlinks; 12 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] At λ=0.01, LeJEPA's anti‑collapse objective reduces hidden‑state pairwise‑cosine anisotropy by 38 % across three paired seeds while perplexity increases only <0.35 %, indicating subtle representation changes without large loss.  
- [Finding 2] Direct regularization of KV terms during continued training reduces mean cache anisotropy by 94 % across four checkpoints, whereas applying the same to hidden states or using frozen‑trunk retrofits does not reproduce this effect.  
- [Finding 3] Under coarse quantization (untransformed symmetric group‑free), direct kv regularization is the only condition that prefers per‑channel scaling in all seeds; with 3‑bit per‑channel quantization baseline DLNLL is 4.3–7.9× higher, while full KIVI‑style configuration yields near‑parity performance.

## Methodology  
The authors train an 110 M parameter model on FineWeb tokens using standard autoregressive training. They introduce LeJEPA's anti‑collapse objective (λ=0.01) to regularize hidden states and also directly modify the K and V matrices during continued training, measuring cache anisotropy via cosine similarity of pairwise embeddings. Quantization experiments compare per‑channel scaling, mixed arrangement with zero‑points, grouped scales, and storage overhead.

## Results  
The main experimental results are: (1) 38 % reduction in hidden‑state anisotropy with negligible perplexity cost; (2) 94 % drop in cache anisotropy when K/V regularized during training; (3) Direct kv regularization improves quantization performance by up to 7.9× lower DNNLL under coarse scaling, while full KIVI configuration yields near‑parity across configurations.

## Significance  
This work demonstrates that training‑time geometric control of KV‑cache can directly influence post‑hoc quantization outcomes, offering a practical avenue for mitigating quantization error without retraining. It highlights the importance of cache geometry in low‑bit regimes and provides empirical evidence that regularization of K/V is more effective than hidden‑state regularization.

## Related Concepts  
- LeJEPA anti‑collapse objective  
- KV‑cache geometry  
- Cache anisotropy  
- Per‑channel scaling  
- Quantization (3‑bit per channel)  
- Simulated KIVI configuration  
- Distributional regularization
