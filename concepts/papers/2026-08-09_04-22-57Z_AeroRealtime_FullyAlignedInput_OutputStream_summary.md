# Summary: 2026-08-09_04-22-57Z_AeroRealtime_FullyAlignedInput_OutputStreamsforLow.md
Saved: 2026-08-10 23:12
Source: 2026-08-09_04-22-57Z_AeroRealtime_FullyAlignedInput_OutputStreamsforLow.md
Model: None

---

## Summary  
The paper proposes **Aero Realtime**, a 4‑billion‑parameter streaming multimodal model that eliminates the turn‑based “prefill‑then‑decode” bottleneck by treating input and output as fully aligned streams on a shared temporal grid. By aligning video, audio, and textual tokens into roughly 80 ms slots, Aero Realtime learns both *when* to generate a response and *what* to generate in a single autoregressive objective. The model’s inference loop appends only the newest multimodal slot while reusing the previous output state and KV cache, enabling continuous duplex interaction without external polling or response gates. This architecture is trained with realtime QA supervision and served on NVIDIA A6000 GPUs, achieving sub‑200 ms latency over a 20‑minute continuously streamed video.

## Key Contributions  
- [Finding 1] Aero Realtime introduces a duplex architecture that aligns multimodal input (video, audio) and output (textual tokens or silence) on a shared temporal grid, allowing the model to generate responses in real time.  
- [Finding 2] The single‑objective training scheme simultaneously optimizes response timing and content generation, so the same forward pass decides whether to emit a lexical token or a silence token.  
- [Finding 3] The system provides a complete training and serving pipeline—including slot‑aligned supervision, hardware‑aware distributed training, and resumable inference—that yields median latency of 84 ms and P95 latency of 173 ms over 20 minutes.

## Methodology  
Aero Realtime treats the multimodal stream as a sequence of fixed‑length slots (≈80 ms each). During training, each slot is supervised with either a predicted lexical token or a silence token, creating a joint input‑output mapping. Inference proceeds incrementally: only the newest multimodal slot is appended to the output buffer while the previous KV cache is retained and reused, avoiding recomputation of hidden states. The authors construct realtime QA pairs where the model’s answer corresponds to a specific audio‑visual event, enabling loss functions that penalize both timing errors and token quality. Training is distributed across four NVIDIA A6000 GPUs with hardware‑aware batching; inference runs in a resumable fashion so that any interruption can be resumed from the last processed slot.

## Results  
Over a 20‑minute continuously streamed video, Aero Realtime maintains a median processing lag of **84 ms** and a P95 lag of **173 ms**, staying within ±200 ms of the source timeline. These figures demonstrate that the duplex model can keep up with real‑time audio‑visual events without noticeable delay. The training pipeline achieved comparable perplexity to standard streaming models while preserving low latency, confirming that slot‑aligned supervision does not sacrifice generation quality.

## Significance  
The work proves that fully aligned input‑output modeling is feasible for duplex, proactive multimodal interaction, opening the door to applications such as realtime video commentary, live captioning, and interactive AR experiences where continuous two‑way communication is essential. By integrating hardware‑aware training and resumable inference, Aero Realtime sets a practical benchmark for low‑latency streaming multimodal generation.

## Related Concepts  
- Streaming multimodal generation  
- Duplex architecture (input‑output alignment)  
- KV cache reuse in autoregressive models  
- Real-time QA supervision  
- Slot‑aligned training and inference  
- Hardware‑aware distributed training on NVIDIA A6000 GPUs
