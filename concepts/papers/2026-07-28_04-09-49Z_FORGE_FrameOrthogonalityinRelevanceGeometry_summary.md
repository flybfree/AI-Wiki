# Summary: 2026-07-28_04-09-49Z_FORGE_FrameOrthogonalityinRelevanceGeometryforLong.md
Saved: 2026-07-28 22:29
Source: 2026-07-28_04-09-49Z_FORGE_FrameOrthogonalityinRelevanceGeometryforLong.md
Model: None

---

## Summary  
The paper introduces FORGE, a model‑agnostic method that maximizes query‑relevant information in a frame subset selected at inference time for long‑form video understanding without any training. It does this by exploiting orthogonality in relevance geometry, where frames representing independent relevant directions are far apart in the embedding space. The approach unifies relevance and diversity into a single optimization objective, allowing diverse relevant content to be captured within a limited budget of frames. Experiments demonstrate that FORGE yields substantial improvements over strong training‑free baselines across multiple video understanding tasks.

## Key Contributions  
- Introduces Frame Orthogonality in Relevance Geometry (FORGE) as a model‑agnostic optimization that balances relevance and diversity.  
- Shows an 11.0–15.3 point improvement in the unified keyframe selection score over the strongest training‑free baseline on Video‑MME and LongVideoBench.  
- Achieves up to double keyframe recall at K=64, boosting question‑answering accuracy by up to 8.7 points across eight MLLMs.

## Methodology  
The authors construct a query‑conditioned geometry where each frame corresponds to a distinct direction in the relevance space; frames covering independent relevant directions are placed far apart. They compute a relevance score via dot product and select the subset that maximizes information while preserving diversity, all without retraining any model.

## Results  
On Video‑MME at budgets of 16, 32, and 64 frames, FORGE outperforms the baseline by 11.0–15.3 points in selection score, with recall rising from 0.204 to about 0.415 (essentially doubling). Question‑answering accuracy improves up to 8.7 points over uniform sampling and 5.2 points over the best baseline across eight MLLMs ranging from 4 B to 32 B parameters.

## Significance  
This method enables efficient inference‑time video understanding by aligning embeddings with the high‑dimensional structure of a query, thereby reducing exposure to irrelevant content. The gains are measurable in both keyframe selection and downstream tasks without any architectural changes, highlighting a promising direction for model‑agnostic optimization.

## Related Concepts  
- Frame Orthogonality  
- Relevance Geometry  
- Unified Keyframe Selection Score  
- Query‑Conditioned Embedding Space  
- Model‑Agnostic Optimization  
- Long‑Form Video Understanding  
- MLLMs
