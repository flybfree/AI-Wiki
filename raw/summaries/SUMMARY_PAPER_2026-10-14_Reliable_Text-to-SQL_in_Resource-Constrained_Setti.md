---
title: Reliable Text-to-SQL in Resource-Constrained Settings with Small LLMs via Iterative Retry Workflows
url: http://arxiv.org/abs/2610.17305v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_18-59-25Z_ReliableText_to_SQLinResource_ConstrainedSettingsw.md
generated_at: 2026-10-14 00:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether small and medium open-source LLMs (1B-8B parameters) can achieve reliable Text-to-SQL performance under constrained computational budgets, using the Spider benchmark as an evaluation framework. The authors find that SQL-specialized models consistently outperform general-purpose and chat-oriented models at small scales, and they introduce three lightweight iterative retry workflows that automatically attempt alternative prompts or models upon failure, significantly improving end-to-end query success rates at the cost of additional inference calls.

## Key Takeaways
- SQL-specialized small models (1B-8B parameters) are consistently more reliable than general-purpose or chat-oriented models for Text-to-SQL generation at small scales, demonstrating that domain-specific fine-tuning compensates for limited model capacity and that model specialization is a critical factor when deploying smaller LLMs in constrained environments.
- Prompt formulation has a substantial and variable impact on Text-to-SQL accuracy with small models, meaning that performance is not solely a function of model size but also heavily depends on how the task is presented to the model, creating a significant reliability challenge for practitioners who must select appropriate prompt representations.
- The three proposed iterative retry workflows—incorporating alternative prompts, alternative models, and an optional syntax-correction step—significantly improve end-to-end success rates without requiring larger models, establishing a practical trade-off where modest additional inference calls yield meaningfully higher reliability, making small-LLM Text-to-SQL deployment viable in resource-constrained settings.

## Context
Text-to-SQL generation has become a critical capability for enabling non-technical users to query databases through natural language, and recent advances in large language models have substantially improved this task. However, the computational cost of deploying large LLMs creates a barrier for edge devices, embedded systems, and organizations with limited GPU resources. This paper addresses a practical gap in the field by systematically evaluating whether smaller open-source models can serve as viable alternatives when paired with intelligent inference orchestration strategies, contributing to the growing body of work on efficient LLM deployment and prompt engineering for structured output generation.

## Implications
For practitioners and industry teams operating under strict hardware or cost constraints, this work provides a concrete recipe for deploying Text-to-SQL systems using small open-source models rather than expensive proprietary APIs, reducing both infrastructure costs and vendor lock-in. The iterative retry workflow design offers a reusable pattern applicable beyond Text-to-SQL, suggesting that reliability engineering through multi-attempt inference orchestration can compensate for smaller model capacity across structured generation tasks. This approach also highlights the importance of investing in domain-specific model fine-tuning and prompt design as cost-effective alternatives to simply scaling up model size.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17305v1)
