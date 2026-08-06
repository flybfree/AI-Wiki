# Summary: 2026-08-05_05-09-20Z_BeyondGlobalRoutingAggregation_Phase_AwareExpertMe.md
Saved: 2026-08-05 20:30
Source: 2026-08-05_05-09-20Z_BeyondGlobalRoutingAggregation_Phase_AwareExpertMe.md
Model: None

---

## Summary  
Mixture‑of‑experts vision‑language models (MoE‑VLMs) boost capacity through sparse expert activation but require storing the entire expert pool, which is costly for deployment. Existing routing‑based merging methods aggregate global token statistics and ignore the phase structure of image‑context, question, and answer tokens, causing experts serving different phases to become interchangeable. We propose RoleMerge, a training‑free technique that preserves phase‑conditioned expert roles by matching experts on their relative phase preferences rather than on globally aggregated routing statistics.

## Key Contributions  
- [Finding 1] Global routing aggregation overestimates the dominance of image‑context tokens, obscuring the specialized role of question and answer tokens.  
- [Finding 2] Training‑free expert merging should be guided by phase‑normalized routing statistics that reflect each expert’s relative preference for different phases.  
- [Finding 3] RoleMerge constructs a Routing Role Profile (RRP) for every expert, merges experts with compatible profiles while keeping answer‑decoding tokens distinct.

## Methodology  
The authors compute an RRP by normalizing routing statistics across the three task phases—image‑context, question, and answer. This normalization yields a relative preference vector that captures how strongly an expert is invoked in each phase. Using an expert‑phase information loss, they define compatibility between two experts as the similarity of their RRPs. During merging, only router entries whose profiles align are combined, while answer‑decoding tokens retain their original routing to preserve decoding fidelity.

## Results  
Experiments on three MoE‑VLM models across six benchmark tasks show that RoleMerge outperforms alternative expert‑merging methods at matched expert‑retention ratios. The macro‑average performance improves by up to 9.6 % relative to the baseline, indicating that preserving phase‑conditioned roles yields a more effective merging strategy.

## Significance  
By aligning expert merges with their intrinsic phase responsibilities rather than on global token counts, RoleMerge reduces storage and inference overhead while improving model utility. This addresses a key bottleneck in deploying MoE‑VLMs: the need to store an entire expert pool when only a subset is active at inference time.

## Related Concepts  
Mixture‑of‑experts (MoE), vision‑language models, routing aggregation, training‑free expert merging, global vs. phase‑aware routing, Routing Role Profile (RRP).
