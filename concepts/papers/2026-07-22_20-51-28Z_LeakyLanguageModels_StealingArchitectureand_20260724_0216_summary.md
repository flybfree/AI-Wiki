# Summary: 2026-07-22_20-51-28Z_LeakyLanguageModels_StealingArchitectureandInferen.md
Saved: 2026-07-24 02:16
Source: 2026-07-22_20-51-28Z_LeakyLanguageModels_StealingArchitectureandInferen.md
Model: None

---

## Summary  
LeakyLMs is a series of attacks that infer proprietary model architecture and deployment details from per‑token generation timing alone, even when interacting through remote APIs. The work demonstrates two core findings: (1) inference optimizations such as speculative decoding can be detected, revealing draft context lengths; and (2) architectural parameters like the number of transformer layers, hidden dimension size, and attention heads can be recovered via a timing‑based search model. Experiments on Llama variants show that the correct architecture is guessed correctly in over 90 % of cases.

## Key Contributions  
- Finding 1: LeakyLMs can detect speculative decoding and draft context length (e.g., Gemini Flash 2.5 uses speculative decoding with a ~128K‑token draft).  
- Finding 2: The attack recovers key architectural properties—layers, hidden dimension, attention heads—from per‑token latency.  
- Finding 3: A timing model built on NVIDIA GPU hardware enables a search over architecture space that yields near‑correct configurations.

## Methodology  
The authors first instrument modern NVIDIA GPUs to capture token‑generation latencies across varying model sizes and hardware settings. They then create a statistical mapping between latency patterns and architectural parameters, using the observed timing as a fingerprint. Leveraging this mapping, they perform an exhaustive search over plausible architecture configurations for typical models (e.g., Llama) to identify the one that best matches the measured timing profile.

## Results  
Experiments on publicly available Llama variants show that the attack’s predicted architectures match the true ones in 90 %+ of trials. The detection of speculative decoding is confirmed by observing a distinct latency drop at ~128K token drafts for Gemini Flash 2.5, matching vendor disclosures.

## Significance  
This research reveals that language model deployments leak sensitive information through timing channels, undermining confidentiality and enabling reverse engineering without access to the model weights. It highlights the need for robust security measures against timing‑based attacks in AI services.

## Related Concepts  
- Per‑token latency fingerprinting  
- Speculative decoding  
- Architecture recovery via statistical modeling  
- Remote API security
