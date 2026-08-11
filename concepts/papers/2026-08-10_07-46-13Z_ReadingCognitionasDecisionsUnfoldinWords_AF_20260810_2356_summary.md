# Summary: 2026-08-10_07-46-13Z_ReadingCognitionasDecisionsUnfoldinWords_AFactoriz.md
Saved: 2026-08-10 23:56
Source: 2026-08-10_07-46-13Z_ReadingCognitionasDecisionsUnfoldinWords_AFactoriz.md
Model: None

---

## Summary  
The paper introduces a factorized inverse decision model (FIDM) that treats reading cognition as the unfolding of two latent factors—action and effort—each governed by individual‑specific parameters. By feeding raw verbal transcripts into a language model, FIDM generates structured task‑execution traces that separate observed actions from the underlying effort dynamics. The authors demonstrate that this factorization improves inference on cognitive screening tasks compared with conventional action‑only approaches. Their work thus bridges inverse decision modeling and linguistic processing for older adults.

## Key Contributions  
- **Factorized Inverse Decision Model (FIDM)**: Decomposes each participant’s task‑execution likelihood into an action factor and an effort factor, each parameterised separately per individual.  
- **Selective recovery in controlled conditions**: FIDM reliably estimates the intended factors while preserving distinctions between actions and efforts even when semi‑synthetic behavioral summaries are matched to real data.  
- **Action evidence localises task‑defined deviations**: The model’s action component pinpoints participant‑specific deviations from expected trajectories, offering complementary information to clinical scores and frozen language representations.

## Methodology  
The study collected 400 older adults who performed a grocery‑shopping dialog task. Raw verbal transcripts were processed by a language model that produced structured traces separating actions (e.g., utterances) from effort dynamics (hesitations, pauses). The FIDM then estimated two sets of individual parameters: one for the action factor and one for the effort factor. These estimates were compared to baseline methods that rely solely on action trajectories or trajectory summaries, and to frozen language embeddings. Controlled recovery experiments contrasted real data with matched synthetic conditions to assess model robustness.

## Results  
FIDM achieved consistent gains across all evaluated baselines in binary cognitive‑status classification, outperforming action‑only models by a statistically significant margin. In controlled recovery, participants’ intended factors were selectively estimated, while semi‑synthetic matches retained the same factor distinctions, indicating that FIDM does not merely interpolate but truly captures latent dynamics. Action evidence further isolated deviations across individuals, showing that specific participants deviated from expected action patterns in ways that could be modelled separately.

## Significance  
By integrating verbal production dynamics with inverse decision modeling, FIDM provides richer, more interpretable information for cognitive screening than trajectory‑only summaries or frozen language representations. The factorization enables clinicians to differentiate between overt actions and underlying effort, potentially improving diagnostic accuracy and personalising interventions for older adults.

## Related Concepts  
- Inverse decision modeling  
- Latent factors (action vs. effort)  
- Action trajectories  
- Effort dynamics (hesitations, pauses)  
- Language models for structured trace generation  
- Cognitive screening tasks  
- Binary classification of cognitive status
