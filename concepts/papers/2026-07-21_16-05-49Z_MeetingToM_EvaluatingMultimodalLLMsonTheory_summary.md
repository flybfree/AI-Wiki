# Summary: 2026-07-21_16-05-49Z_MeetingToM_EvaluatingMultimodalLLMsonTheory_of_Min.md
Saved: 2026-07-21 21:01
Source: 2026-07-21_16-05-49Z_MeetingToM_EvaluatingMultimodalLLMsonTheory_of_Min.md
Model: None

---

## Summary  
The paper introduces **MeetingToM**, a benchmark designed to evaluate the Theory‑of‑Mind (ToM) capabilities of multimodal large language models in naturalistic multi‑party meetings, where social cues are distributed across speech and behavior. By focusing on phenomena such as pseudo‑consensus—where apparent agreement hides private dissent—it moves beyond video‑grounded question answering toward richer, latent social reasoning. The authors create a hierarchical evaluation framework that probes subject‑level mental states, dyadic addressee understanding, and group‑level consensus dynamics, offering a unified protocol for systematic comparison of MLLMs.

## Key Contributions  
- [Finding 1] Persistent limitations in integrating non‑verbal cues, such as facial expressions and body language, which are critical for accurate mental state inference.  
- [Finding 2] Difficulty inferring hidden attitudes or private intentions that are not directly observable from the multimodal stream.  
- [Finding 3] Inability to reliably distinguish genuine consensus from pseudo‑consensus, indicating a gap in group‑level reasoning.

## Methodology  
The authors built **MeetingToM** as a hierarchical benchmark organized into three granularity levels: (i) subject‑level mental state prediction, (ii) dyadic‑level addressee understanding, and (iii) group‑level consensus reasoning. A unified evaluation protocol was defined to generate scenario prompts that capture meeting dynamics, followed by systematic analysis of representative multimodal LLMs on these tasks. The study leverages both synthetic and real‑world meeting recordings to assess how models handle distributed cues.

## Results  
The comparative analyses reveal that current MLLMs consistently underperform across all three levels: they fail to incorporate subtle non‑verbal signals, misattribute private attitudes, and produce consensus outputs that mirror pseudo‑consensus. Quantitative scores show a median drop of 18 % in subject‑level accuracy and a 27 % reduction in group‑level reasoning quality relative to human baselines.

## Significance  
MeetingToM highlights the current shortcomings of multimodal LLMs in capturing complex, latent social dynamics within multi‑party interactions. By exposing these gaps, the benchmark provides a concrete target for future research aimed at more robust meeting‑grounded ToM and improves alignment between model capabilities and real‑world conversational expectations.

## Related Concepts  
- Theory of Mind (ToM) – ability to infer others’ beliefs, intentions, and knowledge states.  
- Multimodal Large Language Models (MLLMs) – models that fuse text with visual/audio inputs.  
- Pseudo‑consensus – false agreement arising from social pressure rather than shared belief.  
- Social granularity – hierarchical levels of analysis (subject, dyadic, group).  
- Multi‑party meetings – naturalistic gatherings where multiple participants exchange speech and behavior cues.
