# Summary: 2026-07-28_03-23-47Z_VisualPatchWorld_CodeWorldModelsasLatentStructured.md
Saved: 2026-07-28 22:29
Source: 2026-07-28_03-23-47Z_VisualPatchWorld_CodeWorldModelsasLatentStructured.md
Model: None

---

## Summary  
VisualPatchWorld (VPW) proposes a method that automatically represents the dynamics of a visual world as executable code, thereby enabling perception‑driven simulation, planning, and model‑predictive control. The approach selects a qualitative dynamical form from brief active probes and then fits its free parameters by minimizing multi‑step prediction error on recorded state‑action traces. This yields interpretable programs that can be rolled forward like simulators while using scene‑graph states for replanning.  

## Key Contributions  
- Automatic selection of the correct qualitative dynamical form via short active probes.  
- Parameter fitting through multi‑step prediction‑error minimization to generate code models.  
- Demonstration of a 23.5‑point improvement over the strongest prior code baseline, achieving 69 % mean planning success.  

## Methodology  
The authors first collect state‑action traces from a visual environment and employ probing queries to infer which dynamical form (e.g., rigid‑body motion or collision response) best matches the data. They then minimize prediction error across multiple steps to fit free parameters, producing an executable program that can be compiled and run as a simulator. The live scene graph supplies the current state at replanning time, allowing the code model to be integrated into model‑predictive control loops.  

## Results  
Across comparisons with other code‑based world models, VPW attains 69.0 % mean planning success and exceeds the best baseline by 23.5 points. When used under the same planner, the induced models approach ground‑truth engine performance on navigation and grasp‑rich control tasks; a residual gap for contact‑rich pushing is largely closed by checking a shortlist of promising plans within the engine.  

## Significance  
VPW establishes a practical route toward automatically constructed code world models that are directly usable for planning, bridging data‑driven neural predictors with hand‑crafted physics engines and providing interpretable simulation for control applications. This work advances the field by making executable dynamics both scalable from data and inspectable in source form.  

## Related Concepts  
- World model (perception‑simulation‑planning)  
- Planning and model‑predictive control  
- Neural predictors vs. hand‑crafted physics engines  
- Multi‑step prediction error minimization  
- Qualitative dynamics selection  
- Executable code representation of dynamics  
- Scene graphs as live state representations
