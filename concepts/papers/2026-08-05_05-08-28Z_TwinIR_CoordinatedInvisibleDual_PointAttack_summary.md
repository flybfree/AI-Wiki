# Summary: 2026-08-05_05-08-28Z_TwinIR_CoordinatedInvisibleDual_PointAttacksonOnli.md
Saved: 2026-08-05 23:12
Source: 2026-08-05_05-08-28Z_TwinIR_CoordinatedInvisibleDual_PointAttacksonOnli.md
Model: None

---

## Summary  
Online HD map construction is essential for autonomous driving prediction and planning, yet physical attacks can be mitigated by a cross‑boundary compensation effect that leaves surrounding geometry intact. This paper introduces **TwinIR**, a mechanism‑guided attack that simultaneously minimizes visible‑spectrum interference and suppresses compensating geometric cues from neighboring boundaries. By jointly optimizing attack effectiveness and point sparsity, TwinIR seeks the smallest set of points needed to degrade map quality while remaining inconspicuous in full‑color views. Experiments demonstrate that TwinIR can reduce mAP by up to 8.96 % under RSA and increase unsafe‑planned‑trajectory rates by as much as 20 %.

## Key Contributions  
- [Finding 1] The authors observe a cross‑boundary compensation effect that limits the effectiveness of existing physical attacks.  
- [Finding 2] They propose TwinIR, a mechanism‑guided attack that reduces visible‑spectrum changes while targeting map geometry.  
- [Finding 3] TwinIR achieves up to an 8.96 % mAP reduction and a 20 % increase in unsafe‑planned‑trajectory rates on nuScenes.

## Methodology  
The authors model how cameras respond under near‑infrared illumination and map the optimal attack points onto feasible physical placements, ensuring that the interference is invisible to human observers yet still influences the online HD map construction pipeline.

## Results  
On the nuScenes benchmark with state‑of‑the‑art models, TwinIR reduces mAP by 8.18–8.96 % (RSA) or 2.84–5.62 % (ETA), and raises the unreachable‑goal rate by 25–28 % and unsafe‑planned‑trajectory rate by 19–20 %. In a real‑world AV testbed, TwinIR induces road straightening and early‑turn deformations without any visible anomalies in full‑color imagery.

## Significance  
This work advances adversarial robustness research by showing that coordinated invisible attacks can significantly degrade map quality while remaining undetectable to operators, highlighting the need for robust online HD map construction systems against such sophisticated threats.

## Related Concepts  
- Online HD map construction  
- Physical attack on autonomous driving systems  
- Cross‑boundary compensation effect  
- Near‑infrared illumination modeling  
- Model‑agnostic attack (RSA)  
- Early‑turn deformation  
- Unreachable‑goal rate
