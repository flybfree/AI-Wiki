# Summary: 2026-07-23_17-21-44Z_Windowed_MTP_RemovingtheFull_ContextDraft_KVTaxatM.md
Saved: 2026-07-24 03:04
Source: 2026-07-23_17-21-44Z_Windowed_MTP_RemovingtheFull_ContextDraft_KVTaxatM.md
Model: None

---

## Summary  
Speculative decoding is a technique that uses a cheap draft model to propose tokens which are later verified by the target model, aiming to speed up generation at long contexts. Frontier models embed Multi‑Token‑Prediction (MTP) as a built‑in draft head, but its cost becomes prohibitive when the KV cache spans millions of tokens because the draft’s full‑attention read scales linearly with context length. The authors introduce Windowed‑MTP, which applies a streaming‑LLM style sliding window to limit the draft’s attention only to a constant‑size window while preserving the target’s full‑attention verification. This change reduces per‑decode‑step cost dramatically without altering token acceptance or output distribution.

## Key Contributions  
- [Finding 1] The native MTP draft head incurs a linear growth in KV‑cache read cost with context, making speculation net‑negative at million‑token scales.  
- [Finding 2] By restricting the draft’s attention to a sliding window plus an attention sink, the KV working set is bounded to a constant size, dropping ~99 % of KV entries at 1M tokens.  
- [Finding 3] Windowed‑MTP yields a +28 % to +44 % reduction in per‑decode‑step cost across major models (Qwen GDN‑MoE 35B/122B, Mamba2‑hybrid NoPE 120B) while preserving the target’s verified output distribution and improving end‑to‑end latency.

## Methodology  
The authors adopt a StreamingLLM inspired sliding window that moves forward as tokens are generated. The draft head computes attention only over the current window (plus a small sink region), leaving the full‑attention verification untouched for each accepted token. This is implemented as a drop‑in, training‑free module: the target still decides every token, so windowing merely changes which tokens are proposed.

## Results  
Experiments on a single GPU in SGLang show that Windowed‑MTP cuts per‑decode‑step cost by 28 %–44 % compared with native MTP drafts. The reduction is input‑invariant and widens with longer contexts. Because latency is the cost divided by acceptance length, end‑to‑end decode latency improves by the same margin; further gains occur where windowing also shortens token acceptance. Moreover, the unread draft KV—previously 7.7–11 % of total KV at 1M tokens—is reclaimed via a compact ring buffer without affecting acceptance or quality.

## Significance  
Speculative decoding is most valuable when generation costs dominate; Windowed‑MTP restores its benefit at million‑token contexts by eliminating the full‑context draft‑KV tax. The method is lightweight, maintains model output fidelity, and can be applied to any architecture that supports MTP, offering a scalable path toward faster long‑form generation.

## Related Concepts  
- Speculative decoding  
- Multi‑Token Prediction (MTP) / NEXTN  
- KV cache  
- Attention sink  
- Streaming LLM sliding window  
- Hybrid/linear‑attention models
