# Summary: 2026-08-10_15-10-44Z_Test_TimeScalingforCADGenerationviaVerifier_FreeCo.md
Saved: 2026-08-11 00:14
Source: 2026-08-10_15-10-44Z_Test_TimeScalingforCADGenerationviaVerifier_FreeCo.md
Model: None

---

## Summary  
The paper proposes a verifier‑free selection mechanism for generating parametric CAD programs from natural‑language prompts, aiming to improve the accuracy of test‑time scaling by using only the candidate pool itself as a signal. It introduces “consensus selection,” where several generated CAD models are compiled and the one that best agrees with the rest is chosen without any external verification model. The authors show that this approach can outperform existing verifier‑based methods on both geometric and topological metrics, delivering measurable gains in Chamfer distance and other evaluation criteria.

## Key Contributions  
- Finding 1: A training‑free consensus selection algorithm that selects the most representative CAD program from a set of generated candidates.  
- Finding 2: Geometric agreement measures (e.g., minimum Chamfer distance) that improve over existing verifier metrics, reducing Chamfer distance by 1–10 % compared with random pool sampling.  
- Finding 3: Topological consensus criteria that match the performance of current verifiers on topology‑focused evaluation.

## Methodology  
The authors generate a batch of N parametric CAD programs from an LLM prompt, compile each to a 3D model, and evaluate pairwise agreement using geometric (Chamfer distance) and topological (connected component overlap) metrics. Consensus selection returns the candidate whose geometric or topological score is highest relative to the others. The process requires no separate verifier model; it relies solely on the internal consistency of the generated models.

## Results  
Across every tested LLM and prompt variant, consensus selection achieved geometric accuracy improvements over random pool sampling: Chamfer distance decreased by 1–10 % compared with baseline. When evaluated against a state‑of‑the‑art verifier, geometric consensus outperformed it on all three geometric metrics, while topological consensus matched the verifier’s topology score. The method is training‑free and compatible with existing CAD generation pipelines.

## Significance  
By eliminating the need for an external verification model, consensus selection reduces latency, computational cost, and reliance on auxiliary vision‑language judges. It demonstrates that the candidate pool itself can serve as a reliable signal for selecting high‑quality CAD outputs, paving the way for more scalable text‑to‑CAD generation systems.

## Related Concepts  
- Text‑to‑CAD generation  
- Test‑time scaling  
- Consensus selection (verifier‑free)  
- Chamfer distance as a geometric similarity metric  
- Topological agreement in 3D models
