# Summary: 2026-08-06_12-19-38Z_GAUGE_AMeasurement_GroundedBenchmarkforPhysicalFid.md
Saved: 2026-08-06 20:40
Source: 2026-08-06_12-19-38Z_GAUGE_AMeasurement_GroundedBenchmarkforPhysicalFid.md
Model: None

---

## Summary  
GAUGE (Generalized Assessment of Unified Grounded Evaluation) is a measurement‑grounded benchmark designed to evaluate how numerical simulation engines and generative video world models reproduce real‑world physics. By pairing controlled task families with calibrated physical metadata, uncertainty annotations, and observables, the authors provide a systematic way to detect violations of fundamental laws such as collision, friction, momentum transfer, oscillation, self‑contact, and deformation across diverse materials. The benchmark reveals that no single engine is uniformly faithful, highlighting specific failure modes in impulsive contact, rapid textile motion, and volumetric deformation.

## Key Contributions  
- [Finding 1] No uniformly faithful physics engine exists; discrepancies are task‑specific rather than systematic.  
- [Finding 2] Video world models can reproduce the expected trajectory equation form but often recover incorrect accelerations, momentum transfer, or oscillation timing.  
- [Finding 3] GAUGE introduces a measurement‑grounded benchmark covering 22 task families to diagnose physical fidelity in both simulation engines and video world models.

## Methodology  
The authors constructed GAUGE by assembling 22 controlled task families that include rigid bodies, flexible cables, textiles, and volumetric deformable objects. Each task is paired with real‑world trajectories, calibrated physical metadata (e.g., mass distribution, material properties), uncertainty annotations, and task‑specific observables. They benchmark three simulation engines—Isaac Sim, Genesis, Newton—using generalized trajectory errors to quantify how well each reproduces the measured physics. Additionally, six image‑to‑video world models are evaluated on five rigid‑body tasks by testing physical‑law consistency (e.g., conservation of momentum) and temporal stability of inferred parameters.

## Results  
The experiments show that Isaac Sim, Genesis, and Newton all exhibit large errors in impulsive contact events, rapid textile motion, and volumetric deformation. For video world models, the trajectories often follow the correct mathematical form but the underlying physical parameters—accelerations, momentum transfer rates, and oscillation periods—are systematically wrong. The largest discrepancies are observed where high‑frequency dynamics dominate.

## Significance  
GAUGE provides a rigorous, measurement‑grounded framework that moves beyond perceptual similarity or human judgments to expose concrete violations of physical laws. This enables developers of simulation engines and video world models to prioritize improvements in the most critical failure modes, ultimately supporting more physically faithful systems for embodied intelligence tasks.

## Related Concepts  
- Physical fidelity  
- Measurement‑grounded benchmark  
- Trajectory errors  
- Impulsive contact  
- Textile motion dynamics  
- Volumetric deformation  
- Video world models  
- Parameter recovery  
- Embodied intelligence
