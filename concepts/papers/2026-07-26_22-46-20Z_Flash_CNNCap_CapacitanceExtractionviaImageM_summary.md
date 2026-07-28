# Summary: 2026-07-26_22-46-20Z_Flash_CNNCap_CapacitanceExtractionviaImageMapping.md
Saved: 2026-07-27 22:47
Source: 2026-07-26_22-46-20Z_Flash_CNNCap_CapacitanceExtractionviaImageMapping.md
Model: None

---

## Summary  
Flash‑CNNCap proposes a CNN‑based method for extracting capacitance values from circuit images by reformulating the full‑matrix prediction problem as an image‑to‑image regression task over spatial contribution maps. By learning two dense maps—a total‑capacitance map and a master‑conditioned coupling map—from conductor‑level labels without per‑pixel supervision, the approach reduces the O(n²) forward passes required for pairwise capacitance recovery to O(n). The resulting totals and symmetrized couplings define the standard Maxwell‑style capacitance matrix. This reformulation enables a 17.5× speedup on average windows of 134 conductors and a 4.4× faster pipeline than OpenRCX, while maintaining high accuracy.

## Key Contributions  
- The full‑matrix capacitance prediction is replaced with image‑to‑image regression over spatial contribution maps, eliminating the need for O(n²) passes.  
- A U‑Net architecture learns both a total‑capacitance and coupling map directly from conductor‑level labels, achieving MAREs of 1.5–3.1% on total capacitance and 3.0–4.6% on coupling across all CapBench subsets.  
- The method delivers a 17.5× reduction in full‑matrix reconstruction time and a 4.4× speedup for the complete DEF→SPEF pipeline compared with OpenRCX.

## Methodology  
Flash‑CNNCap treats each window of conductors as an image where the target is not a scalar capacitance matrix but two dense maps: one representing total capacitance per pixel and another encoding pairwise coupling contributions conditioned on a master conductor. The U‑Net encoder processes the input geometry, while two parallel heads predict these maps. Mask aggregation converts the per‑pixel outputs into conductor‑level values, yielding the full capacitance matrix without explicit per‑pixel supervision. The model is trained on a large dataset of labeled windows and evaluated against ResNet baselines.

## Results  
Testing 13 CNN configurations on CapBench subsets shows that the U‑Net matches ResNet performance within 1.5–3.1% MARE for total capacitance and 3.0–4.6% MARE for coupling, establishing it as the most accurate model. Full‑matrix reconstruction speed improves by a factor of 17.5× on average windows (134 conductors), and the end‑to‑end pipeline processes 1,024 windows in 51.23 seconds—a 4.4× faster turnaround than OpenRCX.

## Significance  
By decoupling capacitance extraction from quadratic pairwise computation, Flash‑CNNCap enables real‑time parasitic analysis of large integrated circuits, dramatically lowering computational cost and latency while preserving high accuracy. This scalability is crucial for modern design flows that require rapid feedback on circuit parasitics without sacrificing precision.

## Related Concepts  
- Capacitance matrix (Maxwell‑style)  
- Image‑to‑image regression  
- U‑Net architecture  
- Mask aggregation  
- Spatial contribution maps  
- Def/SPEF format conversion  
- CapBench benchmark suite
