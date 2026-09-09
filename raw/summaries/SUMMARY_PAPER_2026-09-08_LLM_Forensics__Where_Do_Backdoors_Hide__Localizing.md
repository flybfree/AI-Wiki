---
title: LLM Forensics: Where Do Backdoors Hide? Localizing and Controlling Trigger Mechanisms with Sparse Autoencoders
url: http://arxiv.org/abs/2609.07746v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_16-47-32Z_LLMForensics_WhereDoBackdoorsHide_LocalizingandCon.md
generated_at: 2026-09-08 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how trigger‑based backdoors operate inside large language models by localizing the mechanisms that connect input triggers to output responses using sparse autoencoders across model layers and transformer components. The authors demonstrate that while detection features can be identified with high accuracy, they rarely cause the behavior change; instead, residual‑stream features control the actual language switch. Their analysis reveals a role‑level decomposition of trigger processing into separate feature directions for detection, propagation, and later tracking.

## Key Takeaways
- Trigger detection is achieved by sparse autoencoder features that separate triggered prompts from translation controls with near‑perfect F1 scores, yet these same features do not reliably induce the language switch.  
- Ablating attention or MLP features often fails to suppress the triggered generation, indicating they are good detectors but poor controllers of the payload.  
- Residual‑stream features can suppress triggered generation when removed and some selected features can trigger the target language without the explicit input trigger.

## Context
Understanding the internal pathways that enable backdoors is crucial for building defenses against hidden manipulation in AI systems. This work contributes to the broader effort to map how subtle triggers affect model behavior, providing a framework applicable beyond simple language‑switching scenarios.

## Implications
For practitioners, the decomposition of trigger mechanisms suggests that safeguards should target residual‑stream components rather than relying solely on detection layers. Industry adoption of such insights could lead to more robust models that resist covert activation even when payloads or circuit locations differ.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07746v1)
