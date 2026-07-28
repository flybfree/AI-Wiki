# Summary: 2026-07-27_13-44-42Z_DraftExpert_Expansion_AwareSelf_SpeculativeDecodin.md
Saved: 2026-07-27 21:41
Source: 2026-07-27_13-44-42Z_DraftExpert_Expansion_AwareSelf_SpeculativeDecodin.md
Model: None

---

## Summary  
Large Mixture‑of‑Experts (MoE) language models are attractive for end‑device deployment because only a small subset of experts is active per token, yet routing large expert weights can exceed accelerator memory. DraftExpert tackles the latency bottleneck introduced by expansion‑aware self‑speculative decoding: larger draft sets improve accuracy but trigger costly extra loading, while tiny drafts have low acceptance and multi‑token verification activates many experts at once. The authors propose a framework that trains lightweight draft experts per layer using signal distillation from the frozen target model, then uses a fixed‑footprint drafter with confidence truncation and expert prefetching to keep inference fast while preserving exact token verification.

## Key Contributions  
- [Finding 1] Training of accelerator‑resident draft experts via self‑distillation of residual, logit/token, and router‑agreement signals from the frozen MoE.  
- [Finding 2] A fixed‑footprint drafter that combines a shared expert, top‑1 expert, and a lightweight draft‑expert, applying confidence‑based expansion truncation and target‑expert prefetching.  
- [Finding 3] An expansion‑truncation strategy that limits additional loading while maintaining high draft acceptance and prefetch hit rates.

## Methodology  
The authors first train one lightweight draft expert per layer by self‑distilling signals generated during the frozen MoE’s forward pass, focusing on residual gradients, token logits, and router agreement. At inference, they deploy a compact drafter that selects the top‑1 expert plus the draft‑expert, then applies confidence truncation to limit extra loading and prefetches the target experts for multi‑token blocks. The final token is still verified by the full MoE model, ensuring correctness while minimizing latency.

## Results  
On DeepSeek‑V2‑Lite and Moonlight‑16B‑A3B across CPU‑GPU and Flash‑NPU offloads, DraftExpert improves decode throughput by 1.45× on average, raises draft acceptance to 84–87%, and achieves prefetch hit rates of 86–88% compared with baseline methods.

## Significance  
This work decouples expansion from accuracy loss, enabling efficient MoE deployment on latency‑critical single‑user edge devices where accelerator memory is limited. By training lightweight draft experts and using confidence‑driven truncation, DraftExpert delivers substantial throughput gains without sacrificing the exact verification required for high‑quality generation.

## Related Concepts  
Mixture‑of‑Experts (MoE), self‑speculative decoding, draft experts, accelerator offload, confidence truncation, expert prefetching, router agreement signals.
