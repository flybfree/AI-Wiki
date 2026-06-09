# Summary: 2026-06-02_17-52-18Z_AlignAtt4LLM_FastAlignAttforDecoder_OnlyLLMsatIWSL.md
Saved: 2026-06-02 23:00
Source: 2026-06-02_17-52-18Z_AlignAtt4LLM_FastAlignAttforDecoder_OnlyLLMsatIWSL.md
Model: None

---


## Summary  
The paper introduces AlignAtt4LLM, a decoder‑only simultaneous speech translation system that translates English to German, Italian and Chinese using Qwen3‑ASR and Gemma‑4 E4B‑it under an AlignAtt policy. It is the first application of AlignAtt to a decoder‑only LLM, eliminating encoder‑decoder cross‑attention while preserving translation quality. The approach relies on four design choices: (1) an explicit source span in the prompt, (2) offline selection of translation‑specific alignment heads, (3) selective replay of the draft‑to‑source attention block, and (4) runtime capture of query/key vectors to keep outputs bit‑identical. The method achieves low‑latency performance around 2 seconds and high‑latency up to 4 seconds on IWSLT 2026 development data for European targets.

## Key Contributions  
- [Finding 1] AlignAtt can be adapted to decoder‑only LLMs by using only query/key capture, removing the need for encoder‑decoder cross‑attention.  
- [Finding 2] Selective replay of the draft‑to‑source attention block restores translation‑specific alignment while keeping latency low.  
- [Finding 3] The deterministic prompt layout and calibrated attention heads enable reuse of AlignAtt on non‑European target languages.

## Methodology  
The authors built a synchronous cascade where Qwen3‑ASR generates an incrementally updated source transcript, which is fed into Gemma‑4 E4B‑it. An AlignAtt policy selects translation‑specific alignment heads offline and inserts them in the prompt to expose source spans. During inference, only the draft‑to‑source attention block is replayed for each new token, while query/key vectors are captured at runtime; this preserves bit‑identical outputs without altering the model’s weights.

## Results  
On the IWSLT 2026 development set, AlignAtt4LLM outperforms baseline systems for English→German and English→Italian in both low‑latency (≈2 s) and high‑latency (≤4 s CU‑LongYAAL) regimes. Performance is mixed for English→Chinese, but the method’s design is not limited to Gemma‑4; it can be applied to stronger decoder‑only backbones targeting non‑European languages.

## Significance  
This work demonstrates that alignment mechanisms originally designed for encoder‑decoder models can be repurposed for decoder‑only LLMs, opening a path to efficient, low‑latency simultaneous translation without sacrificing quality. The reusable policy reduces reliance on large encoder components and lowers computational cost, which is crucial for real‑time applications.

## Related Concepts  
- Decoder‑only language models (e.g., GPT, Llama)  
- Simultaneous speech translation (SST)  
- AlignAtt alignment mechanisms  
- Query/key capture in attention heads  
- Prompt engineering with source spans

[[AlignAtt4LLM: Fast AlignAtt for Decoder-Only LLMs at IWSLT 2026 Simultaneous Speech Translation Task]]