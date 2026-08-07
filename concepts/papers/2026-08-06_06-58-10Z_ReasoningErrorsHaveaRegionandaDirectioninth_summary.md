# Summary: 2026-08-06_06-58-10Z_ReasoningErrorsHaveaRegionandaDirectionintheResidu.md
Saved: 2026-08-06 20:33
Source: 2026-08-06_06-58-10Z_ReasoningErrorsHaveaRegionandaDirectionintheResidu.md
Model: None

---

## Summary  
Language models are being evaluated on tasks that demand verifiable reasoning, yet current trajectory‑based detectors rely solely on residual‑stream displacements to infer correctness. This approach discards the originating state of a token’s representation, which can hide crucial context and lead to misleading signals. The authors introduce a three‑stream detector that recovers enough location information from two restricted views while preserving motion data, thereby restoring a balanced view of reasoning validity without re‑introducing shortcuts. Their method outperforms baseline displacement‑only detectors on unseen reasoning benchmarks by up to 21 % and also excels in factual completion tasks.

## Key Contributions  
- **Finding 1:** Reasoning errors exhibit both a spatial region (coarse location) and a directional cue within the residual‑stream trajectory.  
- **Finding 2:** A three‑stream architecture—motion, coarse region, and normalized direction—captures complementary signals that improve selection accuracy.  
- **Finding 3:** The detector restores sufficient state context to interpret motion without full‑state probing, achieving higher performance than displacement‑only baselines.

## Methodology  
The authors decompose each token’s residual‑stream displacement into three components: (1) raw velocity vectors representing motion across layers; (2) a coarse region identifier derived via vector quantization that groups similar location states; and (3) a fine direction reader obtained by normalizing multi‑layer state embeddings to extract orientation. These streams are concatenated and fed to a lightweight classifier, allowing the model to infer whether a reasoning step is sound while limiting exposure to full‑state information that could trigger shortcuts.

## Results  
On standard reasoning benchmarks (e.g., MMLU, GSM8K) where models were not trained on the task, the three‑stream detector raises selection accuracy by 12 % relative to displacement‑only state and 21 % over single‑layer probing baselines. Ablations confirm that each stream contributes uniquely: removing motion drops accuracy by ~5 %, eliminating region reduces it by ~8 %, and discarding direction cuts performance by ~4 %. The detector also outperforms all prior detectors on factual completion and fact verification tasks, indicating a broader applicability to correctness‑oriented evaluation.

## Significance  
By reconciling the trade‑off between motion dynamics and location context, this work moves beyond static state probing toward a more robust, state‑conditioned interpretation of reasoning trajectories. The findings suggest that validity is better inferred from how representations evolve rather than from isolated snapshots, offering a principled framework for evaluating LLM performance in high‑stakes applications.

## Related Concepts  
- Residual‑stream trajectory  
- Vector quantization for coarse region detection  
- Multi‑layer state normalization and direction reading  
- Ablation studies in transformer evaluation  
- Shortcut mitigation in language model probing
