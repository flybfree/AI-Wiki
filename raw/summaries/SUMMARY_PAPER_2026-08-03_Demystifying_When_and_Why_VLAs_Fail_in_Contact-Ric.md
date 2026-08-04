---
title: Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them
url: http://arxiv.org/abs/2608.01402v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_17-34-19Z_DemystifyingWhenandWhyVLAsFailinContact_RichTasksa.md
generated_at: 2026-08-03 23:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why Vision-Language-Action models fail in contact-rich manipulation tasks and proposes a solution called FACT. The authors identify two failure modes—precision errors due to training mismatches and force signal misinterpretation—and demonstrate that combining targeted mechanisms improves success rates from 41% to 66% across five real-world rollouts.

## Key Takeaways
- Precision failures stem from a mismatch between the flow-matching policy used for visual-language reasoning and the action policy, causing inaccurate physical predictions.  
- Force failures arise because force signals are structured differently than typical control inputs, leading to misinterpretation by the model.  
- FACT addresses both issues with specific mechanisms that align training objectives and improve overall performance.

## Context
Contact-rich manipulation is a critical benchmark for embodied AI systems aiming to interact safely with physical objects. Current approaches often rely on force augmentation or regularizers without fully understanding underlying failure causes, limiting progress toward robust interaction.

## Implications
Understanding these failure modes enables developers to design more reliable control loops and training strategies. Practitioners can apply FACT’s insights to reduce costly errors in real-world robotics applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01402v1)
