---
title: SAFEGuard: Detect Optimization-Based Jailbreak Attacks Through Harmful Semantic Analysis and Fluency Measurement
published: 2026-09-05T03:25:31Z
authors: Quoc Viet Vo, Trung Le, Damith C. Ranasinghe, Ehsan Abbasnejad
url: http://arxiv.org/abs/2609.05850v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAFEGuard: Detect Optimization-Based Jailbreak Attacks Through Harmful Semantic Analysis and Fluency Measurement

## Abstract
Despite the significant efforts devoted to aligning large language models (LLMs) with human values and ensuring safe deployment, recent work has revealed that LLMs remain vulnerable to adversarial jailbreak attacks that can bypass safety guardrails and elicit harmful responses. Many defense methods are proposed to detect jailbreaks but they are limited in their effectiveness to counter wide-range optimization-based jailbreak mechanisms that can yield highly fluency-optimized or harmful semantic obfuscated prompts. To tackle this challenge, we propose a unified detection framework SAFEGuard which incorporates a hybrid fluency measurement based on cross-layer distribution distance and perplexity, and the analysis of harmful semantics through gradient matching. Our method is grounded in a paramount observation: high fluency prompts maintain their malicious intention close to harmful prompts while harmful semantic obfuscated prompts often inject gibberish token sequences. Our evaluation demonstrates that SAFEGuard consistently outperforms state-of-the-art baselines and achieves significant improvement in accuracy across different optimization-based jailbreaks. This underscores the effectiveness of SAFEGuard against evolving jailbreak attacks.

## Metadata
- **Published**: 2026-09-05T03:25:31Z
- **Authors**: Quoc Viet Vo, Trung Le, Damith C. Ranasinghe, Ehsan Abbasnejad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05850v1)