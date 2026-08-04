# Summary: 2026-08-03_09-39-11Z_TELLER_Non_intrusiveCross_LayerRoot_CauseAnalysisf.md
Saved: 2026-08-03 23:50
Source: 2026-08-03_09-39-11Z_TELLER_Non_intrusiveCross_LayerRoot_CauseAnalysisf.md
Model: None

---

## Summary  
TELLER is a non‑intrusive framework that enables root‑cause analysis of large language model inference by reconstructing per‑request call‑chain trees from NVTX/CUPTI traces and service logs, then encoding these structures into compact token sequences. It combines this structured representation with a multimodal model to predict abnormal steps, localize suspicious operators, and generate natural‑language explanations without modifying any binaries. The work thus provides a practical triage tool for diagnosing complex LLM inference failures that span multiple layers of the system.

## Key Contributions  
- **Non‑intrusive trace and log collection**: TELLER gathers NVTX/CUPTI traces and service logs directly from running inference services, preserving binary integrity.  
- **Dependency‑aware causal‑context slice & TPE tokenizer**: It creates per‑request call‑chain slices that retain parent‑child relationships, temporal order, and communication relations, then compresses them with a TPE tokenizer that encodes parent, depth, and duration attributes into a compact token sequence.  
- **Multimodal root‑cause model**: The framework jointly predicts abnormal execution steps, localizes suspicious operators, and produces human‑readable explanations using a multimodal architecture.

## Methodology  
The authors first instrument the inference pipeline to emit NVTX/CUPTI traces and standard service logs without any code changes. These raw artifacts are then aligned line‑by‑line with the reconstructed per‑request call‑chain trees, producing causal‑context slices that capture execution semantics. Each slice is fed into a TPE tokenizer that converts the structured data into a token sequence where each token carries attributes for parent node, depth in the tree, and duration of its activity. The numeric candidates generated from these tokens are passed to a multimodal model that jointly predicts which steps deviate from normal behavior, identifies suspicious operators, and generates an explanation string. This pipeline is evaluated across multi‑node GPU inference workloads.

## Results  
Experiments on multi‑node GPU inference workloads demonstrate that moderate TPE compression reduces per‑step trace length by more than 80 % while achieving the best overall diagnostic performance for both horizontal (cross‑node communication) and vertical (within‑node stack) views. Aggressive compression, however, noticeably degrades detection quality. Ablation studies confirm that the overhead of tracing is low and that the framework remains effective under low‑fault priors. The multimodal model consistently outperforms baselines in explanation generation and operator localization.

## Significance  
TELLER provides a practical triage and evidence‑localization substrate for large language model inference root‑cause analysis, enabling faster debugging of production services where failures span multiple system layers. By preserving call‑chain semantics through non‑intrusive tracing and compressing them efficiently, the framework balances diagnostic accuracy with operational cost.

## Related Concepts  
NVTX/CUPTI traces, service logs, call‑chain trees, causal‑context slices, TPE tokenizer, multimodal root‑cause modeling, cross‑layer analysis, latency profiling, distributed inference.
