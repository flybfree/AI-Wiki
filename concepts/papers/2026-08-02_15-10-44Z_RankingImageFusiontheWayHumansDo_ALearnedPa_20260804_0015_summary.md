# Summary: 2026-08-02_15-10-44Z_RankingImageFusiontheWayHumansDo_ALearnedPairwiseP.md
Saved: 2026-08-04 00:15
Source: 2026-08-02_15-10-44Z_RankingImageFusiontheWayHumansDo_ALearnedPairwiseP.md
Model: None

---

## Summary  
The paper introduces the Learned Perceptual Image Fusion Measure (LPIFM), a source‑conditioned model that learns how humans rank infrared‑visible image fusion results by directly modeling pairwise preference, including ties. By turning human A/B/Tie judgments into a scalable surrogate metric, LPIFM enables automated, fair comparison of many fusion algorithms at once.

## Key Contributions  
- **Learning a source‑conditioned pairwise preference model** that predicts whether candidate A is better, candidate B is better, or the two are perceptually equivalent.  
- **Generating a dense human preference corpus** through an expert‑blinded A/B/Tie protocol on a public benchmark, covering every unordered comparison of fusion methods across many scenes.  
- **Demonstrating that LPIFM outperforms conventional scalar metrics**, achieving higher pairwise accuracy and stronger ranking correlation with human judgments.

## Methodology  
The authors build a supervised neural network that takes as input the infrared source, the visible source, and two fused candidate images, then outputs a probability distribution over three outcomes: “A better,” “B better,” or “Tie.” The training data are derived from a new dense preference dataset created by randomly pairing methods on scenes, labeling each pair with expert adjudication under a two‑stage blind protocol. This approach allows the model to capture scene‑ and method‑specific nuances while learning a unified ranking function.

## Results  
Across both scene‑generalization and method‑generalization settings, LPIFM’s pairwise accuracy reaches about 92 % (compared with ~78 % for the best scalar metric) and its Spearman correlation with human preferences improves markedly. Moreover, when evaluated on the full pool of fusion methods, LPIFM produces rankings that closely match the Bradley‑Terry tie‑aware orderings derived from raw human labels, outperforming all conventional metrics in both accuracy and ranking fidelity.

## Significance  
By providing a scalable, human‑aligned surrogate for IVIF evaluation, LPIFM eliminates the need for exhaustive manual pairwise testing of every algorithm. It offers a practical instrument for automated method comparison, fair ranking, and guiding future research toward fusion techniques that truly align with perceptual quality.

## Related Concepts  
- Infrared‑visible image fusion (IVIF)  
- Scalar objective metrics such as PSNR and SSIM as proxies  
- Pairwise preference learning and the Bradley‑Terry model  
- Human‑aligned evaluation of visual tasks
