# Summary: 2026-08-03_09-39-11Z_TELLER_Non_intrusiveCross_LayerRoot_CauseAnalysisf.md
Saved: 2026-08-04 00:37
Source: 2026-08-03_09-39-11Z_TELLER_Non_intrusiveCross_LayerRoot_CauseAnalysisf.md
Model: None

---

## Summary  
The paper introduces **TELLER**, a non‑intrusive framework for root‑cause analysis of large language model inference that spans multiple layers and services without modifying binaries. It reconstructs per‑request call‑chain trees from NVTX/CUPTI traces and service logs, then encodes these slices with a structured tokenizer to preserve execution semantics. The encoded representations feed into a multimodal model that detects abnormal steps, localizes suspicious operators, and generates natural‑language explanations.

## Key Contributions  
- [Finding 1] TELLER reconstructs per‑request call‑chain trees from NVTX/CUPTI traces and service logs without modifying the inference binaries.  
- [Finding 2] It introduces a dependency‑aware causal‑context slice that encodes parent‑child structure, temporal order, and communication relations.  
- [Finding 3] The Trace Pair Encoding (TPE) tokenizer compresses slices into compact token sequences with parent, depth, and duration attributes.

## Methodology  
The authors first collect raw traces and logs from the inference pipeline. They then build a per‑request call‑chain tree by aligning log lines to execution steps using timestamps and dependency information. Each slice is encoded via TPE, which creates structured tokens representing the slice’s attributes. These encoded slices are fed into a multimodal root‑cause model that jointly predicts abnormal steps, localizes suspicious operators, and produces natural‑language explanations.

## Results  
Experiments on multi‑node GPU inference workloads demonstrate a compression‑accuracy trade‑off. A moderate TPE vocabulary reduces per‑step trace length by more than 80 % while achieving the best overall performance for both horizontal (cross‑node communication) and vertical (within‑node execution stack) views. Aggressive compression substantially degrades diagnosis quality. Ablations on low‑fault priors, strengthened baselines, modality handling, explanation‑quality checks, and tracing overhead confirm that TELLER provides a practical triage substrate for LLM inference RCA.

## Significance  
LLM inference is increasingly a continuously running service where root‑cause analysis is essential for troubleshooting. TELLER offers a lightweight, non‑intrusive toolkit that enables rapid identification of problematic steps across layers, supporting faster incident response without code changes or performance loss.

## Related Concepts  
NVTX/CUPTI tracing, call‑chain trees, multimodal machine learning, trace compression, causal context encoding, root‑cause analysis, multimodal explanations.
