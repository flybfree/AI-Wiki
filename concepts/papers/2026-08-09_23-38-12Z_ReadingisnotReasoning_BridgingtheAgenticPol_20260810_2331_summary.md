# Summary: 2026-08-09_23-38-12Z_ReadingisnotReasoning_BridgingtheAgenticPolicyGapi.md
Saved: 2026-08-10 23:31
Source: 2026-08-09_23-38-12Z_ReadingisnotReasoning_BridgingtheAgenticPolicyGapi.md
Model: None

---

## Summary  
The paper investigates why multi‑step language‑model agents suffer from high memory costs when their interaction histories are rendered as images in vision–text compression, and it shows that this performance loss is not merely due to OCR errors. By exposing systematic drifts in action selection, query formulation, stopping behavior, and evidence use, the authors reveal an “agentic policy gap” between text‑history and visual‑history agents. Their core contribution is a two‑stage self‑distillation framework called CAPS that transfers successful text‑policy behavior to its visual counterpart both offline via trajectory distillation and online during reinforcement learning. The method reduces average memory‑context cost by up to 63 % and peak cost by up to 83 %, while improving benchmark scores on SearchQA and ALFWorld.

## Key Contributions  
- [Finding 1] Visual‑history agents exhibit systematic drift in action selection, query formulation, stopping, and evidence use that cannot be explained by OCR quality alone.  
- [Finding 2] CAPS, a cross‑modal policy self‑distillation framework, uses the stronger text‑history policy to supervise its visual‑history counterpart through offline trajectory distillation and online reinforcement learning supervision.  
- [Finding 3] The framework reduces average memory‑context cost by up to 63 % and peak cost by up to 83 %, while boosting SearchQA scores (5.0 %/3.4 %) and ALFWorld scores (15.6 %/14.5 %).

## Methodology  
The authors first conduct controlled evaluations of three tasks—history recovery, matched‑state decisions, and complete trajectories—to quantify the capability gap between text‑history and visual‑history agents. They then design CAPS as a two‑stage process: (i) offline trajectory self‑distillation transfers the optimal text‑policy to visited states in the visual history, generating a dense supervision signal; (ii) online policy self‑distillation continuously updates the visual‑history agent during reinforcement learning using this supervision, ensuring that actions taken by the visual agent align with those of the strong text‑history model. The framework operates on the same multimodal backbone (3B and 7B models) used for baseline comparisons.

## Results  
On SearchQA, CAPS improves AgentOCR by 5.0 % with a 3B backbone and 3.4 % with a 7B backbone. On ALFWorld’s full‑history setting, the gains are 15.6 % and 14.5 %, respectively. More importantly, CAPS cuts average memory‑context cost by up to 63.3 % and peak cost by up to 83.4 % relative to matched text‑history policies, demonstrating both efficiency and capability preservation.

## Significance  
By explicitly bridging the agentic policy gap through self‑distillation, CAPS provides a practical pathway for vision–text compression that maintains high‑quality reasoning without sacrificing memory efficiency—a crucial concern as agents grow more complex. The findings also highlight that modality shifts alone do not cause performance loss; instead, they expose latent policy mismatches that can be remedied with targeted training strategies.

## Related Concepts  
- Vision‑text compression  
- Agentic policy gap  
- Self‑distillation (offline and online)  
- Cross‑modal supervision  
- Memory‑context cost reduction
