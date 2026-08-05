# Summary: 2026-07-29_05-36-19Z_Regularizingmodalitycontributiondriftinmultimodalc.md
Saved: 2026-07-30 23:05
Source: 2026-07-29_05-36-19Z_Regularizingmodalitycontributiondriftinmultimodalc.md
Model: None

---

## Summary  
Multimodal continual learning (MMCL) seeks to accumulate knowledge across tasks while preventing forgetting, yet existing methods focus only on cross‑modal alignment and ignore the stability of each modality’s contribution over time. The authors introduce Modality Contribution Drift (MCD), a new metric that captures how the relative importance of modalities shifts when subsets are intervened upon. To address this overlooked issue they propose Continual Modality Contribution Drift Regularization (CMCDR), which includes both replay‑based and replay‑free strategies to preserve the contribution structure of previously learned tasks. Their work demonstrates that current MMCL approaches cannot reliably mitigate MCD, highlighting a hidden source of knowledge loss.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The authors define Modality Contribution Drift (MCD) as a decision‑level shift quantified by an MCD score that measures changes in modality‑specific and interaction contributions under controlled interventions.  
- [Finding 2] They introduce Continual Modality Contribution Drift Regularization (CMCDR), offering two variants: one using stored old samples to compare contribution profiles between current and frozen models, and another that distills the frozen model’s response from current‑task probes without requiring exemplars.  
- [Finding 3] Theoretical analysis shows that existing MMCL regularizers (e.g., cross‑modal alignment) do not constrain MCD, leading to persistent drift that degrades task retention.

## Methodology  
The problem is approached by first formulating MCD as a diagnostic probe: randomly select subsets of modalities and observe how the model’s performance on these subsets changes. The MCD score aggregates both absolute contribution strength and relative reliance across the subset. CMCDR then regularizes this score during training—either by freezing the previous task’s representation and constraining new contributions (replay‑based) or by extracting the frozen model’s expected response to current probes and aligning them (replay‑free). Constraints are enforced via penalty terms that discourage large deviations from the baseline contribution profile.

## Results  
Experiments on multimodal class‑incremental learning and continual visual question answering show that CMCDR reduces forgetting compared with standard replay or alignment methods, achieving up to 12 % higher test accuracy. The replay‑based version consistently outperforms the replay‑free one when old exemplars are available, while the latter remains effective in fully online settings. Theoretical analysis confirms that without MCD regularization, contribution drift accumulates linearly with task count, whereas CMCDR mitigates this trend.

## Significance  
By exposing a previously unaddressed source of knowledge loss—modality contribution drift—the paper advances the reliability of MMCL systems and provides a practical diagnostic tool for practitioners. The proposed regularizer bridges theory and practice, enabling continual learning pipelines to maintain stable modality interactions across diverse real‑world scenarios.

## Related Concepts  
- Modality Contribution Drift (MCD)  
- Continual Learning (ML)  
- Cross‑modal Representation Alignment  
- Semantic Similarity Regularization  
- Replay‑based vs. replay‑free regularization strategies
