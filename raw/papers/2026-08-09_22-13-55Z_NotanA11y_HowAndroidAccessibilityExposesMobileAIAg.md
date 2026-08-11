---
title: Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection
published: 2026-08-09T22:13:55Z
authors: Rahul Deivasigamani, Sayeda Faatin Alvi, Derqui Andrea, Kaushal Punjabi, Stjepan Picek
url: http://arxiv.org/abs/2608.08939v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection

## Abstract
The rise of autonomous AI agents represents a major paradigm shift in how users interact with mobile devices. Frameworks such as MobileRun and Mobile-Use can autonomously navigate Android applications and execute complex multi-step tasks. To interpret user interfaces, these frameworks rely primarily on Android accessibility (A11y) trees and secondarily on visual screenshots. In this paper, we demonstrate that this architectural dependence on unsanitized accessibility metadata, together with visual input, introduces a systemic vulnerability to indirect prompt injection. We show that adversarial prompts can cause autonomous agents to abandon their original objectives, violate context boundaries, and perform unauthorized device actions. Our empirical evaluation demonstrates goal hijacking, context drift, and unauthorized actions across visually hidden and fully exposed attack scenarios. In aggregate, MobileRun reaches an attack success rate of 0.822 with Gemma4:31B, while Mobile-Use with Qwen3.6:35B reduces this to 0.150 but does not eliminate context drift or unauthorized actions. These findings reveal that current mobile agent frameworks fail to enforce semantic context boundaries, treating passive environmental text as trusted instructions. Finally, we present a taxonomy of these attacks and discuss the need for zero-trust input validation, dedicated security agents, and strict context isolation within mobile agent architectures.

## Metadata
- **Published**: 2026-08-09T22:13:55Z
- **Authors**: Rahul Deivasigamani, Sayeda Faatin Alvi, Derqui Andrea, Kaushal Punjabi, Stjepan Picek
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08939v1)