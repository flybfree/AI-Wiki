# Summary: 2026-08-10_11-20-14Z_Depth_adaptiveInferenceofLoopedLanguageModelsviaCo.md
Saved: 2026-08-11 00:06
Source: 2026-08-10_11-20-14Z_Depth_adaptiveInferenceofLoopedLanguageModelsviaCo.md
Model: None

---

## Summary  
Looped language models (LMs) promise depth‑adaptive inference by iterating a shared block of layers a variable number of times per token, but this variability destroys the uniformity required for standard batch processing. The authors introduce Continuous Depth Batching (CDB), a framework that schedules individual loop iterations at the granularity of each iteration while handling non‑loop boundary stages separately. CDB makes exit decisions one step ahead and overlaps scheduling with GPU computation, enabling a single forward pass per token despite differing loop counts.  

## Key Contributions  
- [Finding 1] Adaptive depth causes tokens to require different numbers of loops, breaking the ability to run a unified batch forward pass.  
- [Finding 2] Prior loop‑level scheduling proposals are never implemented end‑to‑end and ignore the need for separate handling of boundary stages such as token embeddings and the LM head.  
- [Finding 3] CDB achieves up to 99 % of the theoretical maximum speed‑up from adaptive depth, delivering 1.5–1.9× higher offline throughput and 45–90 % lower normalized latency under dynamic serving loads.  

## Methodology  
The authors designed a continuous depth batching system that treats each loop iteration as an independent operation. Loop steps are placed in one priority queue, while non‑loop boundary stages occupy another queue with distinct scheduling priorities. The scheduler predicts the next token’s exit condition (i.e., when all its loops have been completed) and removes it from the batch immediately, allowing the GPU to continue processing other tokens without idle cycles. This design overlaps the CPU‑side scheduling logic with the GPU’s compute pipeline, eliminating the bottleneck of token removal during a single forward pass.  

## Results  
Experiments on the Ouro 1.4B and Huginn 3.5B models show that CDB can realize up to 99 % of the theoretical maximum speed‑up achievable with depth‑adaptive inference. Offline throughput improves by a factor of 1.5–1.9, while normalized latency under variable serving loads drops by 45–90 %. These gains are measured across multiple batch sizes and token distributions, confirming that CDB’s scheduling granularity is both effective and scalable.  

## Significance  
Efficient inference for looped models is essential as these architectures become standard in large language systems. By eliminating the need to remove tokens from a shared batch, CDB reduces compute waste and latency, directly supporting higher‑throughput serving without sacrificing model quality. The approach also provides a template for future research on heterogeneous scheduling in deep neural networks.  

## Related Concepts  
Looped Language Models, depth‑adaptive inference, continuous depth batching (CDB), priority queues, GPU scheduling, token embedding, LM head, theoretical maximum speed‑up, normalized latency, dynamic serving load.
