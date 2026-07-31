# Summary: 2026-07-29_18-25-30Z_RoguePrompt_Dual_LayerEncodingforSelf_Reconstructi.md
Saved: 2026-07-30 21:35
Source: 2026-07-29_18-25-30Z_RoguePrompt_Dual_LayerEncodingforSelf_Reconstructi.md
Model: None

---

## Summary  
The paper RoguePrompt tackles the persistent problem of prompt‑based jailbreaks that evade large language model (LLM) moderation systems by proposing a dual‑layer encoding scheme combined with natural‑language reconstruction instructions. By partitioning a forbidden request and applying Vigenère followed by ROT13, the authors create a pipeline that can be executed under a strict black‑box threat model—only API or UI access to the hosted model is permitted. The work demonstrates that this layered approach yields high success rates across three distinct stages of moderation: bypassing filters, reconstructing hidden instructions, and ultimately triggering execution. These results provide concrete evidence of where multistage attacks succeed and fail within an observable black‑box interaction.

## Key Contributions  
- RoguePrompt introduces a dual‑layer encoding (Vigenère then ROT13) paired with reconstruction prompts to circumvent LLM moderation.  
- The pipeline achieves 93.93 % filter bypass, 79.02 % instruction reconstruction, and 70.18 % execution on 313 real‑world hard‑rejected prompts.  
- It supplies stage‑level failure data that reveals the exact points where multistage jailbreaks break down in automated moderation systems.

## Methodology  
The authors designed a black‑box threat model in which participants could only interact with the LLM via an API or user interface, mimicking typical deployment constraints. They compiled 313 prompts that were previously rejected by safety filters and applied RoguePrompt’s two encodings along with reconstruction instructions. Success was measured at each stage: whether the filter allowed the encoded prompt to pass, whether the model could reconstruct the original request from the output, and whether the reconstructed instruction led to any execution of disallowed content.

## Results  
The experimental evaluation shows that RoguePrompt’s dual‑layer encoding is highly effective: 93.93 % of prompts bypassed filter rejection, indicating strong evasion capability; 79.02 % were successfully reconstructed into the original hidden instruction, proving the reconstruction layer works; and 70.18 % resulted in actual execution of the disallowed content, confirming downstream impact. These percentages are derived from a controlled black‑box setting with no access to model internals.

## Significance  
The findings matter because they expose a systematic vulnerability: layered prompt attacks can succeed at multiple layers while still being flagged only after execution, leaving moderation systems vulnerable between stages. This insight pushes the community toward more granular monitoring and adaptive defenses that address each stage of an attack rather than relying on overall acceptance rates.

## Related Concepts  
- Jailbreak (prompt‑based evasion)  
- Prompt engineering and reconstruction  
- Vigenère cipher and ROT13 encoding as adversarial obfuscation techniques  
- Black‑box evaluation of LLM safety mechanisms  
- Multistage attack pipelines
