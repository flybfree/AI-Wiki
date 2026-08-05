# Summary: 2026-07-25_13-11-23Z_WrongDesignIntentIsWorseThanNone_ADerangement_Cont.md
Saved: 2026-07-27 22:37
Source: 2026-07-25_13-11-23Z_WrongDesignIntentIsWorseThanNone_ADerangement_Cont.md
Model: None

---

## Summary  
The paper investigates whether fine‑tuned code LLMs actually read lightweight design‑intent headers in CAD program completion, proposing a causal test using executable geometric assertions that are independent of the header regex extractor. It shows that a semantically wrong header harms conditional generation more than no header, while a deranged control with shuffled ground‑truth headers is immune to the harm. The study uses a five‑feature header prepended to CadQuery sketches and measures adherence via B‑rep solid properties.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 6 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A semantically wrong header degrades conditional completion performance below the no‑header baseline, especially for polygonal and thin geometries, while circle/tall intents are uninformative.  
- [Finding 2] A derangement control (shuffled ground‑truth headers) remains competent but does not suffer from wrong headers, indicating that harm depends on learned header→program mapping rather than marginal distribution shift.  
- [Finding 3] The independent geometric metric shows only a small token improvement for regex vs geometry, revealing metric circularity and limiting apparent benefit of correct headers.

## Methodology  
The authors fine‑tune Qwen2.5‑Coder‑1.5B on CadQuery‑style sketch‑extrude programs with LORA using five‑feature design‑intent headers (e.g., “circle”, “polygonal”). They generate B‑rep solids and evaluate them against executable geometric assertions that are independent of the header regex extractor, ensuring no code leakage. The study runs a pre‑registered matrix of prefix lengths (0% or 40%) combined with header conditions (correct, wrong, masked) across three seeds.

## Results  
At 40% prefix, correct headers improve token and geometry scores (+0.21 tokens regex, +0.02 geometry), but the benefit is modest. Wrong headers cause a sharp drop: text/token adherence falls from 0.30 to 0.21; thin geometries degrade further. The derangement control shows stable performance (text ≈0.45) and no degradation on wrong headers, while standard model collapses. At 0% prefix the unconditioned baseline cannot generate valid CAD at all.

## Significance  
The findings demonstrate that “wrong design intent” is an active source of error in conditional code generation, not merely noise. By using a causal derangement control and geometric metrics, the paper provides evidence that header conditioning can mislead models, highlighting the need for robust validation beyond token‑level metrics.

## Related Concepts  
- Fine‑tuned language model with LoRA adapters  
- Design‑intent headers in CAD programs  
- Conditional code completion  
- Derangement control (shuffled ground truth)  
- Executable geometric assertions / B‑rep validation
