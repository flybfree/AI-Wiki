# Summary: 2026-08-02_19-38-56Z_LoudorSilent_AReusableFrameworkforPer_ModalityFail.md
Saved: 2026-08-04 00:22
Source: 2026-08-02_19-38-56Z_LoudorSilent_AReusableFrameworkforPer_ModalityFail.md
Model: None

---

## Summary  
Multimodal clinical AI systems often suffer when a modality is unavailable at deployment time, yet current evaluation tools cannot pinpoint which modality caused the error or whether its absence triggers a “loud” failure (large accuracy drop) versus a “silent” one (minimal impact). This paper introduces **PRIMED‑AI**, a reusable, model‑agnostic framework that analyses per‑example and per‑modality failures using only deployment‑observable signals. The framework produces three outputs: a taxonomy of example‑level failures, a matrix linking error attribution to modalities, and a loud‑vs‑silent dropout profile. By validating the framework on planted ground‑truth structures across multiple seeds, it demonstrates reliable recovery of modality dominance and complementarity, which is then applied to real cardiac data where echo loss dramatically worsens performance.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 10 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- **PRIMED‑AI**: A lightweight, unit‑tested harness that generates a per‑example failure taxonomy, a per‑modality complementarity matrix, and a loud‑vs‑silent dropout profile from any mask‑aware probe.  
- **Validation on planted structures**: The framework recovers the known modality dominance and complementary subset across seeds, proving it distinguishes genuine clinical failures from noise rather than merely improving reported accuracy.  
- **Application to cardiac foundation models**: Using frozen EchoJEPA and HuBERT‑ECG embeddings on a paired MIMIC‑IV cohort, dropping echo nearly doubles error rates for LVEF and EF ≤ 40% HFrEF gating, highlighting the clinical relevance of modality complementarity.

## Methodology  
The authors treat each modality as an embedding vector embedded in a shared latent space. A probe classifier is trained on masked embeddings (simulating dropout) while preserving labels; its predictions reveal which modalities’ absence correlates with error. The framework computes:  
1. **Per‑example taxonomy** – flags examples where the correct label differs from the model’s output after modality removal.  
2. **Complementarity matrix** – counts how often each pair of modalities jointly cause errors versus when they are redundant.  
3. **Loud‑vs‑silent profile** – quantifies accuracy loss magnitude for each dropout scenario, distinguishing large (loud) from small (silent) impacts. All calculations rely solely on the masked embeddings and probe outputs, making them deployment‑observable.

## Results  
Across 10 random seeds, PRIMED‑AI recovered a modality dominance pattern where echo contributed ~78 % of errors when absent, while ECG was less critical. The complementarity matrix showed strong overlap between echo and ECG (high joint error rate) but low redundancy with other modalities. In the held‑out MIMIC‑IV test set (n=245), dropping echo increased overall error by ~108 % compared to full‑modality models, confirming a “loud” failure. The framework also produced per‑example attribution scores that matched ground truth on 96 % of cases.

## Significance  
PRIMED‑AI provides a principled way to diagnose *why* and *how much* a modality matters in clinical AI, moving beyond aggregate accuracy metrics. By exposing loud vs. silent failures, it enables targeted mitigation strategies (e.g., alternative modalities or model ensembles) that improve robustness without retraining large systems.

## Related Concepts  
- **Multimodal fusion** – integrating heterogeneous data streams into a single prediction.  
- **Dropout analysis** – evaluating model sensitivity to missing features.  
- **Feature attribution** – post‑hoc explanations such as SHAP or LIME, which PRIMED‑AI complements by being modality‑specific and deployment‑observable.
