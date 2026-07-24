# Summary: 2026-07-23_17-21-44Z_Windowed_MTP_RemovingtheFull_ContextDraft_KVTaxatM.md
Saved: 2026-07-24 03:12
Source: 2026-07-23_17-21-44Z_Windowed_MTP_RemovingtheFull_ContextDraft_KVTaxatM.md
Model: None

---

## Summary  
The paper tackles the cost of full‑context draft KV attention in speculative decoding for models that support million‑token contexts, where native MTP/NEXTN draft heads become prohibitively expensive because their read scales linearly with context. It introduces **Windowed‑MTP**, a training‑free sliding‑window technique that limits the draft’s attention to a constant window while leaving full‑attention verification unchanged. The method cuts draft cost by roughly 99 % and improves end‑to‑end latency without sacrificing output quality.

## Key Contributions  
- [Finding 1] Draft KV read dominates cost at million‑token context, scaling linearly with the number of tokens in the cache.  
- [Finding 2] Windowed‑MTP caps the draft’s attention working set to a constant window, dropping ~99 % of KV entries and reusing a compact ring buffer for unread data.  
- [Finding 3] The approach yields a +28 % to +44 % reduction in per‑decode‑step cost on large models, translating into faster generation latency while preserving the target’s verified output distribution.

## Methodology  
The authors adopt a StreamingLLM‑style sliding window combined with an attention sink that only the draft head attends to. The full‑attention verification remains untouched because acceptance decisions are unchanged; windowing merely selects which tokens are proposed. This is implemented as a drop‑in replacement for native MTP/NEXTN, requiring no retraining or architectural modifications.

## Results  
Experimental runs on Qwen GDN‑MoE 35B/122B and a Mamba2‑hybrid NoPE 120B model at 1 M context on a single GPU show that windowing reduces draft cost by 28–44 % relative to native MTP. The unread draft KV (7.7–11 % of total) is reclaimed via the ring buffer with no impact on acceptance rate or output quality.

## Significance  
By eliminating the “full‑context draft‑KV tax,” Windowed‑MTP unlocks faster, more scalable speculative decoding for models operating at large token limits, enabling higher throughput and broader deployment without sacrificing model performance.

## Related Concepts  
Speculative decoding, Multi‑Token Prediction (MTP/NEXTN), KV cache, attention sink, sliding window, streaming LLM, ring buffer.
