# Summary: 2026-07-24_11-42-17Z_FusionML_Prefill_NotDecode_MechanismandBoundarieso.md
Saved: 2026-07-27 23:22
Source: 2026-07-24_11-42-17Z_FusionML_Prefill_NotDecode_MechanismandBoundarieso.md
Model: None

---

## Summary  
The paper investigates whether transformer inference can benefit from CPU + GPU co‑execution on Apple Silicon’s unified memory, and it identifies why earlier attempts failed due to MLX’s lazy‑graph scheduler serializing cross‑stream work. It proposes a per‑layer contention‑aware split that materializes GPU results eagerly, enabling faster prefill while preserving decode throughput.

## Key Contributions  
- Finding 1: Lazy‑graph scheduler in MLX serializes CPU‑GPU operations when a CPU stream consumes an unmaterialized GPU result, causing row‑split matmul to run slower than pure GPU.  
- Finding 2: Eager materialization of GPU results restores concurrency and yields a ~1.3× speedup for prefill with comparable latency.  
- Finding 3: Per‑layer contention‑aware CPU+GPU split accelerates Llama‑shaped decoder prefill by 1.15–1.38× across five chips, without affecting full‑depth decode or token‑identical outputs.

## Methodology  
The authors analyze the MLX lazy‑graph scheduler and its effect on cross‑stream operations, then implement a runtime that materializes GPU results per layer before CPU consumption, using a contention‑aware row split for transformer prefill. They evaluate this approach on five Apple‑Silicon generations with community‑replicated data.

## Results  
Prefill speedup of 1.15–1.38×; time‑to‑first‑token improvement of 1.18–1.25× on Qwen2.5‑7B via MLX‑LM; decode remains unchanged; full 32‑block depth is unaffected; precision‑matched training loss increases by 0.86–0.97; ANE dispatch overhead is excluded at layer granularity; a no‑regression runtime gate becomes problematic under memory pressure, where probing an alternative mode evicts the active mode’s working set.

## Significance  
Demonstrates that CPU + GPU co‑execution can improve transformer prefill on Apple Silicon, providing a practical path for latency‑critical inference while preserving decode performance and model fidelity.

## Related Concepts  
Unified Memory, MLX lazy graph scheduler, contention‑aware scheduling, row split matmul, per‑layer resource allocation, precision matching, ANE dispatch, memory pressure effects.
