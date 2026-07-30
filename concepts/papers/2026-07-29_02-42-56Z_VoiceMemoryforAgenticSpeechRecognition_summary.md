# Summary: 2026-07-29_02-42-56Z_VoiceMemoryforAgenticSpeechRecognition.md
Saved: 2026-07-29 20:22
Source: 2026-07-29_02-42-56Z_VoiceMemoryforAgenticSpeechRecognition.md
Model: None

---

## Summary  
Voice Memory proposes an inference‑only mechanism for agentic speech recognition that separates the “listener” and “thinker” roles into a frozen corrector and a score‑gated optimizer, respectively. The fixed corrector reads a per‑domain memory file to decide whether to act on a hypothesis or abstain, while the optimizer revises the file only when it can strictly improve a held‑out score. This split creates a listener‑thinker architecture that remains auditable and portable because no model weights are updated during inference. The approach mitigates the overcorrection problem common in unconstrained generative error correction (GER), achieving substantial gains across multiple domains.

## Key Contributions  
- [Finding 1] Introduces a frozen corrector that reads a per‑domain memory file and decides per utterance whether to act on the hypothesis or abstain, establishing a listener‑thinker architecture with no weight changes.  
- [Finding 2] Demonstrates that restraint in the score‑gated optimizer reduces overcorrection from up to 64 % of edits (financial news) down to 35 %, preserving correct tokens.  
- [Finding 3] Lowers the weighted word error rate from 8.36 % to 7.52 % across ten HyPoradise domains without any dataset regressing below its 1‑best baseline, with notable improvements in air‑travel commands and noisy far‑field speech.

## Methodology  
The authors extend the classical ASR‑LM framework by splitting it into two roles: a listener (the frozen corrector) that consumes a memory file at stream time and a thinker (a score‑gated optimizer) that revises the file asynchronously. The memory is shared between them, enabling communication without altering any learned parameters. The optimizer only accepts edits that strictly improve a held‑out evaluation metric, ensuring bounded changes. This design makes the correction process inference‑only, adds zero parameters to the pipeline, and allows the memory to be transferred across different corrector families.

## Results  
Across ten HyPoradise domains with an open corrector, Voice Memory reduces the weighted word error rate from 8.36 % to 7.52 %, a modest overall gain that is amplified when three in‑context examples are added (7.47 %). The most significant improvements occur where recoverable headroom exists: air‑travel commands drop from 8.40 % to 3.40 %, and noisy far‑field speech (CHiME‑4) improves from 12.69 % to 10.46 %. No dataset shows a regression below its original 1‑best baseline, confirming that the memory’s frozen knowledge is beneficial rather than detrimental.

## Significance  
Voice Memory provides an auditable and portable skill that can be transferred between corrector families without retraining, which is valuable for deployment in diverse environments. By limiting the optimizer to strictly improving edits, it curtails the risk of overcorrection—a major source of error amplification—while still delivering measurable performance gains. The approach demonstrates that constrained, memory‑driven correction can outperform unconstrained generative methods, offering a practical path toward more reliable agentic speech recognition.

## Related Concepts  
Voice Memory (inference‑only scheme), agentic speech recognition, listener‑thinker architecture, frozen corrector, score‑gated optimizer, bounded edits, weighted word error rate, overcorrection, ASR‑LM framework, memory transfer, in‑context examples.
