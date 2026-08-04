# Summary: 2026-08-03_11-50-06Z_OneQKChannel_ManySources_GuardingLow_PrecisionAtte.md
Saved: 2026-08-04 00:31
Source: 2026-08-03_11-50-06Z_OneQKChannel_ManySources_GuardingLow_PrecisionAtte.md
Model: None

---

## Summary  
The paper investigates why bfloat16 transformers can train normally for many steps and then collapse abruptly due to low‑precision errors, and whether each error source requires separate repair or a shared channel can be blocked. It isolates a GPT‑2‑class collapse caused by the streaming‑softmax accumulator, showing that fixing only the query‑key (QK) projection prevents runaway while other fixes fail. The authors demonstrate that the QK channel is the common failure locus across architectures and scales. Their solution, QK‑Guard, introduces a dormant controller that activates parameter‑free QK normalization when attention logits saturate, preventing collapse over 60k steps.  

## Key Contributions  
- Finding 1: Faults in low‑precision accumulation trigger identical query‑key spectral runaway regardless of where the error originates.  
- Finding 2: Closing only the QK channel with a parameter‑free normalization stabilizes training while leaving other fault sources active.  
- Finding 3: The temporal sign‑coherence of QK updates, not aggregate deviation, determines early collapse.  

## Methodology  
The authors reproduce the collapse by training bfloat16 GPT‑2 on streaming softmax accumulation, compare it to fp32 accumulation which rescues it, and then test interventions that affect only specific layers or attention components. They measure singular values of QK matrices across steps, use causal probes to track leading singular directions, and evaluate the effect of a dormant controller that switches normalization when logits saturate.  

## Results  
Training collapses after ~10k steps with bfloat16; fp32 accumulation delays collapse indefinitely. The QK channel’s largest singular value drops from 11.1 to 237 when other energy is removed, indicating runaway propagation. QK‑Guard prevents collapse for up to 60k steps and matches always‑on normalization across all tested models.  

## Significance  
By identifying a shared QK locus as the failure channel rather than per‑source repair, the work offers a scalable guardrail for low‑precision training, reducing need for per‑layer fixes and improving robustness of large‑scale transformer deployments.  

## Related Concepts  
- bfloat16 accumulation  
- streaming softmax accumulator  
- query‑key (QK) projection  
- spectral runaway  
- singular value analysis  
- QK‑Guard controller  
- attention logit saturation
