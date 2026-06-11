# Summary: 2026-05-14_13-52-31Z_XFP_Quality_TargetedAdaptiveCodebookQuantizationwi.md
Saved: 2026-05-14 21:02
Source: 2026-05-14_13-52-31Z_XFP_Quality_TargetedAdaptiveCodebookQuantizationwi.md
Model: None

---

## Summary
XFP introduces a novel dynamic weight quantization framework for Large Language Model (LLM) inference that fundamentally inverts the traditional quantization workflow. Instead of manually selecting bit-widths or relying on calibration datasets, XFP allows operators to specify target reconstruction quality floors based on per-channel cosine similarity, automatically determining the optimal codebook size, outlier budget, and packing strategy for each layer. This approach eliminates the need for Hessian calculations or manual tuning, offering a streamlined path to high-performance inference. The system supports two distinct storage modes, V2 and V2a, which utilize different codebook sharing strategies while maintaining a unified frontend and decoding kernel.

## Key Contributions
- **Automatic Quality-Targeted Quantization**: XFP automates the selection of quantization parameters by inverting the workflow; users define strict and lazy cosine similarity thresholds for attention and MoE experts, and the system dynamically adjusts codebook sizes and outlier budgets without manual intervention or calibration data.
- **Hybrid Sparse-Dense Decomposition**: The method decomposes weight matrices into a sparse fp16 outlier residual and a dense sub-byte index tensor mapped to a per-group learned codebook, effectively handling outliers that typically degrade quantization accuracy while maintaining high compression ratios.
- **H-Process for Memory-Aware Inference**: The authors propose the H-Process, an iterative algorithm that balances model accuracy and memory constraints by adjusting cosine thresholds, enabling large models to fit within specific memory envelopes while preserving sensible output quality.

## Methodology
XFP operates by first allowing the operator to set two cosine similarity thresholds: a strict floor for attention and shared experts, and a lazy floor for routed-expert Mixture-of-Experts (MoE) layers. The system then automatically determines the necessary codebook size and outlier budget for each layer to meet these quality targets. Each weight matrix is decomposed into a sparse fp16 residual containing outliers and a dense tensor of indices pointing to a learned codebook. Two storage modes are implemented: V2 uses per-channel Lloyd clustering, while V2a shares a library of 32 codebooks per layer to optimize storage. For models exceeding memory limits, the H-Process iteratively adjusts the cosine thresholds to find an operating point where the model fits within the target memory envelope (defined by an OOM boundary and a garbage collection boundary) without sacrificing critical accuracy.

## Results
On Qwen3.5-122B-A10B using V2 mode, XFP achieved 138 tokens per second single-stream decode on RTX PRO 6000 Blackwell hardware, maintaining 94.49% GSM8K strict-match accuracy and running 49% faster than Marlin INT4. For the larger Qwen3.5-397B-A17B model, the H-Process successfully fitted the full expert population into 2x96 GB memory at approximately 3.4 effective bits. This configuration delivered 100.9 tok/s long-output decode with 66.72% GSM8K strict-match accuracy, simultaneously exceeding INT4 quantization with routed-expert pruning in terms of memory efficiency, throughput, and accuracy.

## Significance
XFP represents a significant advancement in LLM deployment by removing the complexity and expertise required for effective quantization. By automating the trade-off between memory usage and inference quality, it enables the deployment of massive models on consumer-grade or workstation hardware that previously lacked the capacity. The H-Process further democratizes access to large-scale models by providing a robust mechanism for fitting them into constrained memory environments without manual trial-and-error tuning.

## Related Concepts
- Dynamic Quantization
- Mixture-of-Experts (MoE)
- Codebook Quantization
- Sparse Outlier Separation
- Cosine Similarity Thresholds
- Memory-Efficient Inference
- Lloyd Clustering

[[XFP: Quality-Targeted Adaptive Codebook Quantization with Sparse Outlier Separation for LLM Inference]]