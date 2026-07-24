# Summary: 2026-07-22_20-51-28Z_LeakyLanguageModels_StealingArchitectureandInferen.md
Saved: 2026-07-24 02:21
Source: 2026-07-22_20-51-28Z_LeakyLanguageModels_StealingArchitectureandInferen.md
Model: None

---

## Summary  
LeakyLMs demonstrates that per‑token generation latency can be exploited to infer both deployment‑level optimizations (e.g., speculative decoding) and proprietary architectural details of a language model, even when interacting via remote APIs. The paper introduces two attacks: one that detects inference‑time tricks such as speculative decoding and the draft context window used by Google Gemini Flash 2.5, and another that recovers core transformer architecture parameters—layers, hidden dimension, and attention heads—by modeling how latency scales with hardware configuration. By constructing a detailed timing model on NVIDIA GPUs and performing a search over the architectural space, LeakyLMs achieves near‑correct guesses for Llama models in more than 90 % of cases.

## Key Contributions  
- [Finding 1] Token‑generation latency uniquely reveals whether a provider employs speculative decoding and the draft context length (e.g., ~128 K tokens) used by Google Gemini Flash 2.5.  
- [Finding 2] The same timing data can be inverted to recover key architectural properties of transformer models, including number of layers, hidden dimension size, and attention heads.  
- [Finding 3] A systematic search over the architecture space using the latency model yields near‑correct configurations for Llama models with a success rate exceeding 90 % in top‑10 guesses.

## Methodology  
The authors first build an empirical mapping of per‑token latency versus model configuration and GPU hardware parameters on modern NVIDIA GPUs. This mapping captures how latency behaves under different batch sizes, sequence lengths, and architectural choices. Leveraging this timing profile, they formulate a search algorithm that iterates over plausible transformer architectures, scoring each candidate by its predicted latency curve. The highest‑scoring candidates are then compared to the observed latency from a remote API call, allowing inference of both deployment strategies (speculative decoding) and model architecture without ever exposing the model weights.

## Results  
Experiments show that Google Gemini Flash 2.5’s token timing aligns with speculative decoding and a draft context window near 128 K tokens. When applied to Llama series models, the latency‑based search places the correct architectural configuration within the top‑10 guesses in over 90 % of trials. The attack requires only standard API access and no model weights, confirming that token generation timing alone is sufficient for leakage.

## Significance  
LeakyLMs challenges the assumption that remote inference APIs are secure because they leak only output text; instead, it reveals that latency patterns expose sensitive architectural and deployment details. This could impact security policies, licensing compliance, and competitive intelligence in AI services.

## Related Concepts  
- Speculative decoding (inference‑time optimization)  
- Architecture inference attacks  
- Timing‑based side channels  
- Transformer model parameters (layers, hidden size, attention heads)
