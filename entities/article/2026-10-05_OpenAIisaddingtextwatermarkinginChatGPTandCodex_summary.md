# Summary: OpenAI is adding text watermarking in ChatGPT and Codex
Saved: 2026-10-25
Source: 2026-10-05_OpenAIisaddingtextwatermarkinginChatGPTandCodex.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://www.theverge.com/ai-artificial-intelligence/1004880/openai-chatgpt-text-watermarks-eu-ai-act)

---

## Summary
OpenAI is introducing an invisible, machine-readable text watermarking system called "textGrain" to ChatGPT and Codex outputs, initially limited to users in the European Union to comply with the EU’s AI Act. While OpenAI claims this technology matches or exceeds competitors like Google DeepMind’s SynthID, it explicitly states that text watermarks do not guarantee reliable detection or verify human authorship. The rollout includes opt-in capabilities for global API customers and restricted detector access for approved researchers, indicating a cautious approach to establishing global defaults.

## Key Takeaways
- **Regional Rollout Strategy:** OpenAI is deploying text watermarking exclusively for eligible ChatGPT and Codex users in the EU first, citing the need to gather real-world feedback before making it a global default. This aligns with regulatory pressures from the EU’s AI Act, similar to moves made by Anthropic.
- **Performance and Limitations:** OpenAI asserts that textGrain "matched or exceeded" other watermarking approaches and maintains benchmark performance parity between watermarked and unwatermarked text. However, the company admits the system "does not guarantee reliable detection," does not verify accuracy, determine ownership, or prove human authorship.
- **API and Research Access:** Global API customers can opt-in to watermarked outputs for select models starting immediately, allowing them to manage their own transparency obligations. Meanwhile, access to watermark detectors is restricted to approved researchers and expert organizations on a case-by-case basis due to risks of false positives and missed detections.

## Context
This development occurs within the broader industry effort to standardize AI provenance tracking in response to increasing regulatory scrutiny, particularly from the EU’s AI Act. Competitors such as Google DeepMind (with SynthID) and Anthropic have already implemented similar watermarking strategies to meet compliance requirements. The move highlights a growing tension between technical feasibility and regulatory compliance, as companies attempt to implement invisible markers that can be detected by machines but remain imperceptible to human users. The restriction of detector tools to approved researchers suggests an industry-wide caution regarding the reliability and potential misuse of automated detection systems in public domains.

## Implications
The introduction of textGrain signifies a shift toward mandatory transparency mechanisms in AI-generated content, driven primarily by regulatory frameworks rather than purely technical demand. For developers and API users, the opt-in model provides flexibility to adhere to specific transparency obligations without forcing a uniform standard across all platforms. However, OpenAI’s admission that watermarks do not prove human authorship or guarantee detection reliability underscores the limitations of current watermarking technology as a definitive tool for combating misinformation or establishing copyright ownership. This cautious rollout may influence how other AI providers approach global compliance strategies, potentially delaying widespread adoption until technical robustness improves and regulatory standards become more clearly defined.
