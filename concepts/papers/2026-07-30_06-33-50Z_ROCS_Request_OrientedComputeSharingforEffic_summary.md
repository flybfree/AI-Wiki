# Summary: 2026-07-30_06-33-50Z_ROCS_Request_OrientedComputeSharingforEfficientLar.md
Saved: 2026-07-30 20:27
Source: 2026-07-30_06-33-50Z_ROCS_Request_OrientedComputeSharingforEfficientLar.md
Model: None

---

## Summary  
The paper addresses the bottleneck of recommendation inference cost when scaling feature‑interaction or sequence models, proposing a request‑oriented compute sharing paradigm called ROCS that isolates candidate‑dependent representations and evaluates them only once per user request. By deferring these interactions to the late stages of inference, ROCS dramatically reduces GPU load while preserving prediction quality. The authors introduce three novel components—Generalized Layer Masking (GLM), Deep Cross Attention (DCA), and In‑Kernel Broadcast Optimization (IKBO)—to realize this efficiency gain across both feed‑forward and sequence architectures. Their work demonstrates that these innovations enable a 3× increase in queries per second on retrieval models without quality loss, plus a 0.5 % relative LogLoss improvement with a 50 % QPS boost on short‑form video ranking.

## Key Contributions  
- **Finding 1:** ROCS decouples request‑side features from candidate interactions, allowing reuse of the same feature vector across many candidates per user query.  
- **Finding 2:** Generalized Layer Masking (GLM) enforces strict isolation between candidate sub‑layers, preventing cross‑candidate interference during inference.  
- **Finding 3:** Deep Cross Attention (DCA) extends request‑oriented sharing to sequence models, enabling efficient handling of ordered embeddings.

## Methodology  
The authors first formalize ROCS as a modeling paradigm where the model is split into a request processor and a candidate evaluator that only consumes request‑side features. GLM is applied by inserting binary masks that zero out all but one candidate’s output at each layer, ensuring independence. DCA replaces traditional attention with a cross‑attention mechanism that aggregates request embeddings across candidates without recomputing pairwise interactions. Finally, IKBO is co‑designed to broadcast intermediate tensors within the GPU kernel, cutting memory traffic and latency. Together these techniques enable inference pipelines that scale to billions of requests per second.

## Results  
Experimental evaluation on public benchmarks shows ROCS consistently improves the quality‑efficiency tradeoff across recommendation backbones. On retrieval tasks, ROCS achieves up to a 3× QPS increase with no degradation in top‑k accuracy. For short‑form video ranking, LogLoss drops by 0.5 % relative while throughput doubles (≈50 % QPS gain). The gains persist across diverse model architectures and deployment scales.

## Significance  
By shifting compute from per‑candidate to per‑request, ROCS reduces infrastructure costs and enables massive scaling of recommendation systems that previously hit hardware limits. This paradigm is especially valuable for real‑time services where latency and cost are critical, offering a path to higher quality at lower expense.

## Related Concepts  
GLM, DCA, ROCS paradigm, compute sharing, request‑oriented inference, kernel broadcast optimization, candidate isolation, sequence modeling, large‑scale recommendation inference.
