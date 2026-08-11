# Summary: 2026-08-08_09-32-07Z_BASIS_Breach_AwareSelectivePromptInjectionShieldin.md
Saved: 2026-08-10 22:52
Source: 2026-08-08_09-32-07Z_BASIS_Breach_AwareSelectivePromptInjectionShieldin.md
Model: None

---

## Summary  
The paper introduces BASIS (Robustness‑Aware Prompt Injection Defense), a defense mechanism that detects malicious prompt injections while minimizing the common problem of over‑refusal. By leveraging the Attention Competition Ratio (ρ) as a feature, BASIS trains two sparse linear probes—an existence probe and a breach probe—to make offline decisions without invoking the LLM again. The three‑stage pipeline first identifies whether an injection exists, then predicts if it will actually compromise the model, and finally assesses the robustness of the instruction to decide on refusal. This approach preserves near‑perfect detection accuracy while dramatically reducing unnecessary rejections for safe inputs.

## Key Contributions  
- **Attention Competition Ratio (ρ) as a feature**: The authors use ρ, derived from attention weight competition across tokens, to encode injection presence and potential breach.  
- **Two sparse linear probes with cascaded gating**: An existence probe flags possible injections; a breach probe predicts actual compromise; their outputs are combined via offline gating for defense decisions.  
- **Three‑stage pipeline avoiding over‑refusal**: The system distinguishes robust versus compromised instructions, refusing only when the model would truly be hijacked.

## Methodology  
The authors compute ρ from each token’s attention distribution within the LLM response; this ratio serves as a scalar feature vector. Two linear probes are trained on historical data: one predicts whether an injection exists (existence probe) and another predicts if it will cause a breach (breach probe). Decisions are made by cascading these probe outputs—if the existence probe is positive, the breach probe’s output determines refusal; otherwise, no action is taken. The entire process runs without additional LLM inference, making it lightweight and scalable.

## Results  
Experiments across four tasks (e.g., text classification, summarization) and six open‑source LLMs demonstrate that BASIS achieves detection rates above 95 % while cutting over‑refusal incidents by roughly 70 % compared with baseline refusal mechanisms. The greatest gains occur for robust instruction templates, where the model would otherwise be unnecessarily blocked. These results confirm that the ρ‑based probes effectively separate safe and malicious inputs.

## Significance  
BASIS addresses a critical limitation of current prompt‑injection defenses: they often reject harmless prompts, degrading user experience and hindering legitimate use cases. By focusing on instruction robustness rather than merely flagging attacks, BASIS enables safer, more reliable LLM deployment in applications where false refusals are costly.

## Related Concepts  
Attention Competition Ratio (ρ), prompt injection, over‑refusal, linear probes, cascaded gating, instruction robustness.
