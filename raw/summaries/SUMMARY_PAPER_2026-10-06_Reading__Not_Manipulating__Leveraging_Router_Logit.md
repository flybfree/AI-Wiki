---
title: Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models
url: http://arxiv.org/abs/2610.07774v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_05-09-02Z_Reading_NotManipulating_LeveragingRouterLogitsforM.md
generated_at: 2026-10-06 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether mixture-of-experts vision-language models can be made safer by reading, rather than manipulating, their internal routing states. It shows that router logits provide strong diagnostic signals for identifying unsafe multimodal prompts and introduces a lightweight detector that flags harmful requests before generation. The method improves safety on HoliSafe and generalizes to out-of-distribution benchmarks without changing model parameters or expert routing.

## Key Takeaways
- Vision-language models face compositional safety risks because harmful behavior can emerge from the interaction between visual and textual inputs rather than from either modality alone. This makes safety detection harder than in text-only models and requires methods that account for cross-modal behavior in multimodal systems.
- Existing safety interventions, including prompting, supervised fine-tuning, and routing-based expert steering, can produce inconsistent results across models and evaluation distributions. They may also introduce safety-utility tradeoffs, especially over-refusal, because they directly modify model behavior or internal routing states.
- Router logits in MoE vision-language models are highly predictive of whether a multimodal input is safe or unsafe. A lightweight detector can read these logits during prompt prefill, identify unsafe requests before generation, and substantially reduce safety errors on HoliSafe while generalizing to out-of-distribution benchmarks such as MISHard and MM-SafetyBench.

## Context
As vision-language models increasingly use mixture-of-experts architectures, researchers are paying more attention to internal routing mechanisms as both a source of capability and a potential source of risk. This paper matters because it shifts the focus from manipulating internal components to observing naturally emerging signals that can support safety monitoring. It contributes a practical perspective on how model internals can be used diagnostically rather than only as targets for intervention.

## Implications
For practitioners, the router-logit detector offers a lightweight and non-intrusive safety layer that can be added to existing MoE vision-language models without retraining or modifying expert routing. This may reduce harmful outputs while limiting the over-refusal and utility losses often caused by stronger safety interventions. More broadly, the work suggests that monitoring internal routing signals can complement existing safety methods and support scalable, model-agnostic multimodal safety systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07774v1)
