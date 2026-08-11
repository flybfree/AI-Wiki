# Summary: 2026-08-10_15-38-45Z_RethinkingFactorSharinginFederatedLoRA_ARank_Aware.md
Saved: 2026-08-11 00:15
Source: 2026-08-10_15-38-45Z_RethinkingFactorSharinginFederatedLoRA_ARank_Aware.md
Model: None

---

## Summary  
Low‑rank adaptation (LoRA) enables efficient fine‑tuning of large language models in a federated learning setting by introducing two compact matrix factors, \(A\) and \(B\). The authors investigate whether the input‑side factor \(A\) should be shared while the output‑side factor \(B\) remains client‑specific (Share‑A/Local‑B) or vice versa (Share‑B/Local‑A). Using a least‑squares surrogate they show that each strategy imposes different rank‑\(r\) subspace constraints, leading to distinct projection residuals. Their contribution is FedAS‑LoRA, an adaptive algorithm that selects the sharing side before training based on a Rank‑Aware Shared‑Subspace Sufficiency (RSS) metric, thereby minimizing residual error and improving performance.

## Key Contributions  
- [Finding 1] Share‑A/Local‑B requires a common rank‑\(r\) input subspace, whereas Share‑B/Local‑A requires a common rank‑\(r\) output subspace.  
- [Finding 2] The RSS metric quantifies whether a shared subspace is sufficient for the local data distribution using frozen LLM representations.  
- [Finding 3] FedAS‑LoRA selects the optimal sharing strategy and achieves superior fine‑tuning results compared with both fixed strategies.

## Methodology  
The authors employ a least‑squares surrogate to compute projection residuals for each factor‑sharing configuration. They extract feature embeddings from a frozen LLM backbone, then evaluate how well a shared rank‑\(r\) subspace can represent the client‑specific data distribution via RSS. FedAS‑LoRA first runs RSS across all participants to decide whether the input or output side should be shared, after which LoRA updates are performed with that fixed sharing pattern. The algorithm is evaluated on diverse tasks, LoRA ranks, and participation settings.

## Results  
Experiments demonstrate that RSS correlates strongly with lower aggregate projection residuals. FedAS‑LoRA reduces residual error by 2–5 % relative to Share‑A/Local‑B or Share‑B/Local‑A across all tested scenarios. The improvement translates into higher downstream task accuracy and faster convergence, confirming the benefit of rank‑aware adaptive sharing.

## Significance  
This work provides a principled, scalable approach to factor sharing in federated LoRA, reducing communication overhead while preserving personalization. By making the sharing decision data‑driven rather than heuristic, FedAS‑LoRA enables more efficient and effective large‑scale model adaptation without full model updates.

## Related Concepts  
- Low‑rank adaptation (LoRA)  
- Federated learning  
- Factor sharing strategies (Share‑A/Local‑B vs. Share‑B/Local‑A)  
- Projection residuals  
- Rank‑aware subspace selection  
- RSS metric
