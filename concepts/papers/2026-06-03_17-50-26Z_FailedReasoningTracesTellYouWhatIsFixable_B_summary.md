# Summary: 2026-06-03_17-50-26Z_FailedReasoningTracesTellYouWhatIsFixable_ButNotby.md
Saved: 2026-06-04 00:00
Source: 2026-06-03_17-50-26Z_FailedReasoningTracesTellYouWhatIsFixable_ButNotby.md
Model: None

---


## Summary  
The paper argues that failed reasoning traces contain diagnostic information about which test‑time interventions can fix a model’s failure, beyond merely resampling the output. It proposes three problem‑level trajectory features derived from the structure of available interventions to recover this recoverability signal without reading the text. These features cluster failures into stable regimes and enable a training‑free routing rule that lifts rescue performance by +12.2 % on the deployment‑relevant “Steerable‑Hard” subset where retries are insufficient.

## Key Contributions  
- Identify that failed traces encode recoverability structure independent of their textual content.  
- Propose three problem‑level trajectory features that capture this structure from the distribution of failed rollouts.  
- Demonstrate a training‑free routing rule using these features that improves rescue by +12.2 % on the Steerable‑Hard subset.

## Methodology  
The authors examine post‑training language models on reasoning tasks and analyze the rollout trajectories that lead to failure. From each trajectory they extract three problem‑level features that reflect which interventions (e.g., retry, rerouting) are effective for a given failure. The features are computed without accessing model weights or training data; they are then used to cluster failures into stable regimes and to guide a routing rule across two cross‑family probes.

## Results  
The three trajectory features recover an accuracy gain of 84.3 ± 4.3 % over the majority‑class baseline on reasoning benchmarks. When applied as a routing rule, rescue performance improves by +12.2 % specifically for failures in the Steerable‑Hard subset—those where additional rollouts do not help but a bounded intervention is reachable. The same features transfer across two probe families, indicating robustness and generalization.

## Significance  
Providing a diagnostic framework that turns discarded failed traces into actionable information enables more efficient test‑time interventions without costly re‑training or weight inspection. This approach supports scalable deployment of post‑training models by allowing targeted rescue actions based on the inherent structure of failures.

## Related Concepts  
post‑training language models, reasoning tasks, rollout traces, test‑time scaling, recoverability structure, trajectory features, routing rules, cross‑family probes, training‑free intervention.

[[2026-06-03_17-50-26Z_FailedReasoningTracesTellYouWhatIsFixable_ButNotby.md]]