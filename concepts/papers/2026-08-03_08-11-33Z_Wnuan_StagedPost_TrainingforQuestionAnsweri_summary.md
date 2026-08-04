# Summary: 2026-08-03_08-11-33Z_Wnuan_StagedPost_TrainingforQuestionAnsweringoverP.md
Saved: 2026-08-03 23:45
Source: 2026-08-03_08-11-33Z_Wnuan_StagedPost_TrainingforQuestionAnsweringoverP.md
Model: None

---

## Summary  
Enterprise question answering must retain general language abilities while acquiring proprietary knowledge. The authors introduce Wnuan, a three‑stage pipeline that builds task‑oriented supervision from documents, performs supervised fine‑tuning with general‑data replay, and then applies reinforcement learning to residual errors. On the 707‑question WnuanBench benchmark, the primary 32B route improves its acceptable‑answer rate (AAR) from 52.76 % to 91.51 % after adaptation. The method also reduces the general‑benchmark score by about five points, showing a trade‑off between domain expertise and overall capability.

## Key Contributions  
- [Finding 1] Staged post‑training (SFT + RL) raises AAR on WnuanBench to 91.51 % for the primary 32B model.  
- [Finding 2] Residual‑error sampling outperforms full‑pool and size‑matched random sampling, yielding gains of 3.11 and 2.97 points respectively.  
- [Finding 3] The adaptation introduces a measurable cost: the general‑benchmark average drops by 5.17 points, concentrated in instruction following.

## Methodology  
Wnuan follows a three‑stage pipeline: first, it constructs task‑oriented supervision from proprietary documents; second, it conducts supervised fine‑tuning using a replay of general‑domain data under a matched 100‑update protocol; third, it applies reinforcement learning to the residual errors identified after SFT. The authors compare three sampling strategies—full‑pool, size‑matched random, and residual‑error—and select the latter for its superior performance.

## Results  
The primary 32B route achieves an AAR of 91.51 % on WnuanBench. Source‑cluster bootstrap intervals remain above zero for both full‑pool versus residual‑error comparisons, indicating statistically significant gains. The same‑domain validation set preserves the ordering of results. An expert evaluation shows agreement with the automatic ensemble on 90.5 % of stratified responses. The general‑benchmark score declines by 5.17 points across the route.

## Significance  
Wnuan demonstrates that staged adaptation can dramatically boost domain‑specific QA performance while quantifying the loss to broader language abilities, providing a framework for balancing proprietary knowledge acquisition with overall model utility.

## Related Concepts  
Staged post‑training, supervised fine‑tuning, reinforcement learning, residual error sampling, acceptable‑answer rate (AAR), WnuanBench, general vs. domain benchmark, task‑oriented supervision, 32B model, matched update protocol.
