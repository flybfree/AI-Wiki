# Summary: 2026-07-19_01-13-09Z_RegularizeorLocalize_WhenTraining_TimeKV_CacheGeom.md
Saved: 2026-07-24 00:09
Source: 2026-07-19_01-13-09Z_RegularizeorLocalize_WhenTraining_TimeKV_CacheGeom.md
Model: None

---

## Summary  
The paper investigates whether a training‑time geometric intervention—LeJEPA’s anti‑collapse objective (\(\sigreg\))—can reshape the hidden‑state geometry of an autoregressive language model and thereby improve the quality of subsequent \(\kv\)-cache quantization. By comparing regularized versus unregularized models under three different 3‑bit per‑channel quantization schemes, the authors show that \(\sigreg\) reduces pairwise cosine anisotropy in hidden states while keeping perplexity unchanged, but only when the regularization is applied to the \(\kv\) cache itself does it affect cache geometry and downstream loss. The study demonstrates that this training‑time distributional regularization can be beneficial for coarse quantizer scales, especially under token‑local grouping and mixed \(\kv\) scaling with zero‑points.

## Key Contributions  
- **Finding 1:** At \(\lambda = 0.01\), \(\sigreg\) reduces hidden‑state pairwise cosine anisotropy by ~38 % across three paired seeds while perplexity rises less than 0.35 %, indicating that the regularization reshapes representation geometry without harming language modeling performance.  
- **Finding 2:** Directly applying \(\sigreg\) to the \(\kv\)-cache (i.e., training‑time regularization of K and V) reduces mean cache anisotropy by ~94 % across four checkpoints, whereas freezing hidden states or retrofitting the objective does not reproduce this effect.  
- **Finding 3:** Under untransformed symmetric group‑free quantization, direct \(\kv\) regularization is the only condition that prefers per‑channel scaling in all three seeds; however, with a full KIVI‑style configuration (mixed arrangement, zero points, grouped scales) all models achieve near parity, suggesting the advantage of \(\sigreg\) depends on quantizer granularity.

## Methodology  
The authors train 110 M‑parameter transformer models on 10 B tokens from FineWeb. They employ LeJEPA’s anti‑collapse objective \(\sigreg\) with a parameter \(\lambda = 0.01\), which penalizes high cosine similarity between different hidden states to encourage diversity in the representation space. Experiments compare three quantization regimes: (i) untransformed symmetric group‑free 3‑bit per‑channel scaling, (ii) token‑local grouping with mixed \(\kv\) scaling and zero points, and (iii) a full KIVI‑style configuration matching storage overhead. The regularization is applied either to hidden states only or to the \(\kv\)-cache during continued training.

## Results  
- Hidden‑state anisotropy drops 38 % under \(\sigreg\), perplexity changes <0.35 %, and zero‑shot loss remains stable.  
- Cache anisotropy falls 94 % when \(\sigreg\) is applied to K/V, but frozen‑trunk models show no improvement.  
- Per‑channel scaling is preferred only under the untransformed regime; with mixed grouping and zero points, all models converge in Dnll and storage cost.

## Significance  
The work reveals that training‑time geometric regularization can directly influence \(\kv\)-cache geometry, offering a pathway to improve quantization efficiency without sacrificing model quality. By identifying conditions under which this effect is most pronounced (coarse quantizer scales), the study guides practical deployment of quantization in large language models.

## Related Concepts  
- KV‑cache: memory buffer storing key and value vectors for fast attention computation.  
- Anti‑collapse objective (\(\sigreg\)): regularization that penalizes high cosine similarity between hidden states to promote diverse representations.  
- Per‑channel scaling: quantization technique that assigns different scale factors per channel of the \(\kv\)-cache.  
- Cache anisotropy: measure of diversity in the distribution of \(\kv\)-vector values across cache entries.  
- KIVI‑style configuration: mixed arrangement of quantizer scales, zero points, and grouped tokens to balance storage and accuracy.
