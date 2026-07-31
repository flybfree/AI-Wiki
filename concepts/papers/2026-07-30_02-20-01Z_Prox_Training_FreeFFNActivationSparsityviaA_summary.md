# Summary: 2026-07-30_02-20-01Z_Prox_Training_FreeFFNActivationSparsityviaApproxim.md
Saved: 2026-07-30 21:36
Source: 2026-07-30_02-20-01Z_Prox_Training_FreeFFNActivationSparsityviaApproxim.md
Model: None

---

## Summary  
The paper proposes Prox, a training‑free sparsification method for feed‑forward network activations in large language models that achieves high sparsity without retraining. It leverages the magnitude ranking of SwiGLU intermediate states to create sparse channel masks, enabling exact computation only on selected channels. This two‑stage approach preserves model quality while dramatically reducing memory and compute.

## Key Contributions  
- Finding 1: The magnitude ranking of SwiGLU intermediate values provides a reliable proxy for selecting active channels.  
- Finding 2: A shared mask constructed from input sparsity and quantized weights can be reused across the FFN layers, reducing overhead.  
- Finding 3: Exact computation on selected channels yields up to a 1.99× speedup at 70% sparsity.

## Methodology  
The authors address training‑free sparsification by decoupling channel selection from exact activation computation. Stage 1 builds a mask using sparse input patterns and low‑bit proxy weights, while Stage 2 computes only the masked channels of the three FFN projections. This avoids dense intermediate storage and leverages approximate salience to guide sparse execution.

## Results  
Experiments on ten LLMs across six families show Prox outperforms all training‑free baselines at sparsities up to 70%, achieving up to a 1.99× end‑to‑end decoding speedup while maintaining comparable perplexity. The method is compatible with quantization and sparse attention, confirming its practical deployment.

## Significance  
By enabling high‑sparsity FFN execution without retraining, Prox reduces memory footprint and inference latency, making LLMs more scalable for edge devices and large‑scale deployments.

## Related Concepts  
Feed‑forward networks, activation sparsification, SwiGLU, channel masking, quantization, sparse attention, training‑free optimization.
