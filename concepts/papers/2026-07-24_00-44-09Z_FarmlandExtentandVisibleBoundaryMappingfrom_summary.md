# Summary: 2026-07-24_00-44-09Z_FarmlandExtentandVisibleBoundaryMappingfrom1mNAIPI.md
Saved: 2026-07-26 21:32
Source: 2026-07-24_00-44-09Z_FarmlandExtentandVisibleBoundaryMappingfrom1mNAIPI.md
Model: None

---

## Summary  
This paper proposes a reproducible workflow for extracting farmland extent and visible boundaries from 1 m NAIP RGB imagery, addressing the gap between proprietary field maps and real‑world monitoring needs. By combining a residual U‑Net trained on binary masks with a text‑prompted SAM 3 refinement, the authors achieve high semantic segmentation performance without relying on cadastral parcel data. The approach is demonstrated across 37 diverse scenes, producing coherent regional masks that can be used for crop monitoring and land‑conversion analysis where field layers are unavailable.

## Key Contributions  
- [Finding 1] A residual U‑Net (ResUNet) trained with a Dice‑dominant loss reaches test accuracy 0.8808, IoU 0.8605, Dice 0.9234, precision 0.8766, and recall 0.9794 on 1 m NAIP imagery.  
- [Finding 2] Freezing the SAM 3 branch and prompting it with “agricultural farmland field” improves segmentation on challenging patches (e.g., orchard rows: Dice ↑ from 0.858 to 0.955; fragmented parcels: Dice ↑ from 0.804 to 0.903).  
- [Finding 3] Sliding‑window stitching of the fused masks yields regional tiles with consistent Dice scores (e.g., 0.898 and 0.919), producing a seamless semantic farmland‑extent layer.

## Methodology  
The authors first annotated 37 NAIP scenes in CVAT, converting each to binary masks and extracting non‑overlapping 256 × 256 patches (total 5 698 samples). The dataset was split into 3 850 training, 770 validation, and 1 078 test patches. A ResUNet architecture was trained using a combined loss L = 2.5(1 – Dice) + BCE to emphasize Dice scores. The frozen SAM 3 model’s “agricultural farmland field” branch was fused with the U‑Net output via logical OR, preserving high‑confidence predictions while leveraging zero‑shot refinement. Evaluation was performed on the test set, and tile‑level performance was measured after stitching.

## Results  
The ResUNet alone achieved the reported metrics above; when augmented with SAM 3 refinement, Dice improved significantly on difficult features. Sliding‑window stitching produced regional masks where individual tiles scored 0.898–0.919 in Dice, indicating strong consistency across large areas. The product is a semantic farmland‑extent layer rather than a cadastral parcel map, suitable for monitoring applications lacking up‑to‑date field data.

## Significance  
This work provides an open, reproducible method to generate high‑quality farmland maps from publicly available 1 m NAIP imagery, enabling agricultural researchers and managers to track crop health and land‑use change without relying on costly or outdated proprietary field layers. The integration of a deep residual U‑Net with a zero‑shot SAM 3 refinement demonstrates how modern vision models can complement each other for robust boundary detection.

## Related Concepts  
- NAIP (National Agriculture Imagery Program) 1 m RGB imagery  
- Residual U‑Net (ResUNet) architecture and Dice loss  
- Text‑prompted SAM 3 (zero‑shot semantic segmentation)  
- Binary mask generation from annotated scenes  
- Sliding‑window stitching for large‑scale map assembly  
- Semantic vs. cadastral parcel mapping
