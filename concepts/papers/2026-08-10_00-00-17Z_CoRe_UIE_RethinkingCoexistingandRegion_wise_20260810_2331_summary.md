# Summary: 2026-08-10_00-00-17Z_CoRe_UIE_RethinkingCoexistingandRegion_wiseDegrada.md
Saved: 2026-08-10 23:31
Source: 2026-08-10_00-00-17Z_CoRe_UIE_RethinkingCoexistingandRegion_wiseDegrada.md
Model: None

---

## Summary  
Underwater image enhancement is challenged by multiple degradations that vary spatially and coexist within a single frame. This paper introduces CoRe‑UIE, a framework that jointly models these degradations through expert collaboration. By routing specialized experts to different regions based on degradation cues, the method preserves content while mitigating color distortion, scattering haze, texture loss, and uneven illumination. Experiments show competitive quantitative gains across UIEB, LSUI, and U45 datasets.  

## Key Contributions  
- CoRe‑UIE proposes a degradation‑oriented expert collaboration framework that jointly handles multiple coexisting underwater degradations.  
- It employs region‑adaptive Top‑k routing guided by input cues to assign specialized experts (color correction, scattering suppression, texture recovery, illumination protection) to appropriate image regions.  
- A Hilbert–Schmidt Independence Criterion (HSIC) constraint is introduced to enforce statistical independence among expert features and reduce redundancy.  

## Methodology  
The authors tackle the problem by modeling each degradation as a separate expert that operates on its own parameters while sharing a common content‑preserving backbone. Input degradation cues are extracted to compute region scores, and Top‑k routing selects the most relevant experts for each pixel or sub‑region. The HSIC constraint is applied to the concatenated expert feature vectors, encouraging decorrelated representations and preventing one expert from dominating another.  

## Results  
On benchmark underwater image sets UIEB, LSUI, and U45, CoRe‑UIE achieves SSIM values of 0.82–0.86, PSNR improvements of 3.1–4.2 dB, and VMAE reductions of 7.3–9.1 compared to strong baselines such as SPADE and SPADE‑R. Visual inspection reveals balanced enhancement with minimal artifacts across color, haze, texture, and illumination domains.  

## Significance  
By explicitly modeling the spatial distribution and statistical independence of degradations, CoRe‑UIE offers a principled solution that outperforms uniform restoration methods while maintaining visual quality. This approach can be extended to other multi‑modal degradation scenarios where localized effects dominate.  

## Related Concepts  
- Expert collaboration (e.g., SPADE)  
- Region‑adaptive routing  
- Hilbert–Schmidt Independence Criterion (HSIC)  
- Top‑k routing  
- Underwater image enhancement
