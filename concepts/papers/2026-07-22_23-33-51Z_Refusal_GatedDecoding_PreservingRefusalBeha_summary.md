# Summary: 2026-07-22_23-33-51Z_Refusal_GatedDecoding_PreservingRefusalBehaviorUnd.md
Saved: 2026-07-24 02:19
Source: 2026-07-22_23-33-51Z_Refusal_GatedDecoding_PreservingRefusalBehaviorUnd.md
Model: None

---

## Summary  
High‑temperature sampling is widely used to boost the diversity of language model outputs, but it often weakens the model’s refusal behavior on harmful prompts. This paper introduces **Refusal‑Gated Decoding**, an efficient sequential decoding method that preserves the greedy refusal response while allowing high entropy for safe inputs. The approach maintains 91–99 % of the original refusal rate across three benchmark datasets without adding significant latency. By gating the greedy decoder, the model can still produce diverse text when appropriate, yet it reliably refuses unsafe requests.

## Key Contributions  
- [Finding 1] High‑temperature sampling reduces the frequency with which LLMs refuse harmful prompts.  
- [Finding 2] The Refusal‑Gated Decoding algorithm preserves greedy refusal behavior under high temperature regimes.  
- [Finding 3] The proposed method incurs minimal additional latency compared to baseline decoding.

## Methodology  
The authors first conduct a systematic analysis of how temperature influences refusal rates across diverse prompts, identifying the trade‑off between diversity and safety. Building on this insight, they design a sequential decoding strategy that inserts a “refusal gate” before each greedy token selection: if the model’s probability distribution indicates a high likelihood of an unsafe output, the gate forces the decoder to emit the predefined refusal token; otherwise it continues with standard high‑temperature sampling. The gating logic is lightweight and runs in parallel with the main decoding pass, ensuring negligible overhead.

## Results  
Experiments on three benchmark datasets demonstrate that Refusal‑Gated Decoding retains 91–99 % of the original greedy refusal behavior when temperature is increased to 0.8–1.2. Safe prompts still generate high‑entropy outputs with only a modest latency increase (≈3 ms per token), confirming that safety is not compromised for benign inputs.

## Significance  
This work bridges the gap between model diversity and safety, providing a practical solution for applications that require both creative generation and robust guardrails. By preserving refusal behavior under high‑entropy sampling, it enables safer deployment of LLMs in environments where user interaction may include risky queries without sacrificing performance.

## Related Concepts  
- High‑temperature sampling  
- Refusal behavior  
- Greedy decoding  
- Entropy of token probability distribution  
- Model guardrails  
- Sequential decoding  
- Truncation‑based sampling
