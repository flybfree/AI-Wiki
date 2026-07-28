# Summary: 2026-07-26_06-35-14Z_PlanCraft_Sketch_Refine_andFurnishforArchitect_Ins.md
Saved: 2026-07-27 23:53
Source: 2026-07-26_06-35-14Z_PlanCraft_Sketch_Refine_andFurnishforArchitect_Ins.md
Model: None

---

## Summary  
The paper introduces **PlanCraft**, a novel framework that generates architect‑inspired 3D residential scenes by first creating progressive 2D sketches, then refining them into precise floor plans, and finally furnishing the interior. By mimicking how architects sketch and refine their designs, PlanCraft breaks two longstanding assumptions in automated layout generation: (1) design is inherently incremental rather than fully specified upfront, and (2) the 2‑D plan is an essential spatial contract that must be respected before adding furniture. The authors demonstrate that these insights lead to a system that produces geometrically valid layouts even when only a quarter of the sketch is complete.

## Key Contributions
- [Finding 1] Design processes are progressive; existing methods require a fully specified conditioning representation, which does not reflect real‑world design workflows.  
- [Finding 2] The 2‑D floor plan serves as an irreplaceable spatial contract; bypassing it causes overlapping rooms and implausible proportions.  
- [Finding 3] PlanCraft achieves a **61.1 % lower FID** than the best existing 2‑D method, surpasses current 3‑D systems by **15 points** in expert‑rated spatial rationality, and already outperforms all fully specified baselines with only a 25 % complete sketch.

## Methodology  
PlanCraft consists of three stages. First, **SketchPlan** trains on 80 K real floor plans to generate partial sketches at every completeness level, providing the missing training signal that captures the architect’s drawing process. Second, **PlanCraft‑Diff** refines these incomplete sketches into geometrically precise, vectorizable floor plans using a coarse‑to‑fine strategy that progressively sharpens the layout. Finally, **PlanCraft‑Agent** furnishes the 3‑D scene within the well‑defined room boundaries established by the refined plan, turning spatial reasoning into bounded constraint satisfaction.

## Results  
Experimental evaluation shows that PlanCraft’s output is markedly more realistic than prior approaches: it reduces FID by 61.1 % relative to the best 2‑D baseline and improves expert scores for spatial rationality by 15 points compared with existing 3‑D generators. Notably, a sketch completed at just 25 % of the intended size already outperforms all fully specified baselines, confirming that partial sketches can yield high‑quality layouts.

## Significance  
By aligning algorithmic behavior with how architects actually design—starting from rough strokes and building complexity step‑by‑step—PlanCraft addresses a fundamental mismatch between synthetic data generation and real‑world workflows. This progressive approach not only yields higher‑fidelity floor plans but also reduces the need for exhaustive pre‑specification, opening the door to more flexible, human‑centric design tools.

## Related Concepts  
- Floor plan generation  
- Architectural design progression  
- Spatial rationality  
- Fréchet Inception Distance (FID)  
- Vectorizable floor plans  
- Progressive sketching  
- Room furnishing  
- 3‑D residential scene generation
