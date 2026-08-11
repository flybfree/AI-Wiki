# Summary: 2026-08-10_12-35-59Z_verdi_retrievalisnottransferforcontinualworldmodel.md
Saved: 2026-08-11 00:08
Source: 2026-08-10_12-35-59Z_verdi_retrievalisnottransferforcontinualworldmodel.md
Model: None

---

## Summary  
The paper critiques the assumption that strategies discovered for one pretrained world model can be directly reused in subsequent campaigns, arguing instead that retrieval is not transferable without explicit validation on the target system. It introduces VERDI—a continual framework that treats each optimization hypothesis as evidence only when it passes a frozen verification step on the new model. By constructing an Optimization Fingerprint from inference‑time probes and retrieving ranked prior hypotheses, VERDI systematically validates candidates before they become reusable knowledge. The approach reduces search cost, GPU expense, and negative transfer while accurately predicting which strategies will succeed.

## Key Contributions  
- [Finding 1] Retrieval is not transfer for continual world model optimization; a strategy validated on one model remains an hypothesis for another until target‑side validation confirms its utility.  
- [Finding 2] VERDI builds an Optimization Fingerprint from shared inference probes, ranks prior hypotheses by relevance, and enforces a frozen verifier to admit only evidence that survives verification as reusable knowledge.  
- [Finding 3] The framework continuously evolves the diagnostic representation when fingerprints of nearby models conflict, enabling ongoing refinement of both retrieval signals and verification criteria.

## Methodology  
The authors first define an Optimization Fingerprint for each world model by probing its latent behavior during inference; these fingerprints serve as a shared diagnostic space. VERDI then retrieves candidate hypotheses from a repository of past optimizations, ranking them based on fingerprint similarity to the current model’s fingerprint. Each retrieved hypothesis is subjected to a frozen target‑side verifier that checks whether it improves the user‑specified objective without altering the model’s behavior. Only those candidates passing verification are incorporated as evidence and stored for future retrieval. When fingerprints of adjacent models diverge, the system triggers probe evolution—re‑training the probes—to better capture the new diagnostic space.

## Results  
Experiments on Ctrl-World, Cosmos, and RoboCoin demonstrate that VERDI cuts search cost by 68%, reduces GPU usage by 69%, and lowers negative transfer from 0.34 to 0.06. Moreover, the framework predicts whether a retrieved hypothesis will succeed with 83% sign accuracy, indicating strong alignment between retrieval relevance and actual performance gains.

## Significance  
VERDI addresses a critical bottleneck in continual world model optimization: the lack of principled mechanisms to transfer knowledge across models without incurring costly re‑optimization. By formalizing evidence licensing through verification, it enables more efficient, stable, and scalable learning pipelines that preserve prior expertise while adapting to new objectives.

## Related Concepts  
- Retrieval‑based continual learning  
- World model optimization  
- Evidence‑licensed knowledge transfer  
- Optimization Fingerprint  
- Inference‑time probes  
- Frozen verifier  
- Negative transfer mitigation
