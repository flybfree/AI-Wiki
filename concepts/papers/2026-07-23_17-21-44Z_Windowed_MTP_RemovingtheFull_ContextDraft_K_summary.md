# Summary: 2026-07-23_17-21-44Z_Windowed_MTP_RemovingtheFull_ContextDraft_KVTaxatM.md
Saved: 2026-07-24 02:58
Source: 2026-07-23_17-21-44Z_Windowed_MTP_RemovingtheFull_ContextDraft_KVTaxatM.md
Model: None

---

## Summary  
The paper addresses a critical bottleneck in speculative decoding for large language models: the full-context draft-KV tax, where MTP/NEXTN draft heads incur prohibitive costs by running attention over the entire KV cache at every draft step, especially as context grows to millions of tokens. By introducing Windowed-MTP (Windowed Multi-Token Prediction), the authors propose a streaming-aware alternative that limits the draft's attention window while preserving full-attention verification for target tokens, thus drastically reducing per-decode-step costs without sacrificing output quality or acceptance rates.

## Key Contributions  
- [Finding 1] The MTP/NEXTN draft head’s linear growth in KV cache read dominates cost at million-token contexts, making speculation net-negative due to high draft latency.  
- [Finding 2] Windowed-MTP replaces full-attention draft reads with a constant-size sliding window and attention sink, bounding the draft's working set and reclaiming ~99% of KV entries without affecting target verification or acceptance decisions.  
- [Finding 3] The method achieves input-invariant cost reductions of +28% to +44% in per-decode-step latency across large models (e.g., Qwen GDN-MoE 122B, Mamba2-hybrid NoPE 120B) on a single GPU, with further gains when acceptance length is shortened.

## Methodology  
Windowed-MTP adapts the StreamingLLM paradigm to draft heads by replacing full KV cache attention with a compact ring buffer that stores only a fixed-size window of recent tokens. The draft head computes attention only over this window (the "attention sink"), while verification remains unchanged: the target model still uses full-attention for every token it accepts. This sliding-window approach is training-free, drop-in compatible, and lossless by construction—only the set of proposed tokens changes, not which are accepted.

## Results  
Experimental results on a single GPU in SGLang show that Windowed-MTP reduces per-decode-step cost by 28–44% compared to native MTP drafts at 1M context. Crucially, this improvement is input-invariant and widens with longer contexts. Since per-token latency scales with the inverse of acceptance length, end-to-end decode latency improves proportionally. The unread draft KV (7.7–11% of total) is reclaimed via the ring buffer at no cost to acceptance or output quality.

## Significance  
This work resolves a fundamental scalability issue in speculative decoding for massive models and long contexts, enabling faster generation without retraining or architectural changes. By decoupling draft computation from full attention, Windowed-MTP makes high-quality speculation viable even on single-GPU setups, accelerating real-world applications like chatbots and code assistants where latency is critical.

## Related Concepts  
- Speculative decoding  
- Multi-Token Prediction (MTP/NEXTN)  
- KV cache  
- Attention sink  
- StreamingLLM  
- Sliding window  
- Draft head  
- Acceptance length
