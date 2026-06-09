# Summary: 2026-05-20_12-58-01Z_Reasoning_TraceCollapse_EvaluatingtheLossofExplici.md
Saved: 2026-05-20 21:01
Source: 2026-05-20_12-58-01Z_Reasoning_TraceCollapse_EvaluatingtheLossofExplici.md
Model: None

---

## Summary
This paper investigates a critical phenomenon termed "reasoning-trace collapse," which occurs when large language models trained for explicit step-by-step reasoning lose their structural reasoning capabilities during subsequent fine-tuning on standard instruction-response data. The authors demonstrate that while these models may maintain high accuracy in producing final answers, they often fail to generate the valid, intermediate logical steps that originally defined their reasoning architecture. To address this, the study introduces a novel structural evaluation framework that decouples answer correctness from the validity of the reasoning process, allowing for a more granular assessment of model behavior. The research highlights that standard performance metrics are insufficient for detecting this degradation and proposes simple mitigation strategies to preserve reasoning integrity during adaptation.

## Key Contributions
- The identification and formal definition of "reasoning-trace collapse," a specific failure mode where fine-tuning on trace-less data suppresses explicit reasoning structures without immediately impacting final answer accuracy.
- The development of a comprehensive structural evaluation framework that categorizes reasoning outputs into valid, empty, missing, and truncated traces, providing a nuanced metric for reasoning reliability distinct from task performance.
- The empirical demonstration that simple loss-masking techniques can effectively mitigate reasoning-trace collapse during supervised fine-tuning, even in the absence of teacher-generated reasoning traces, offering a practical solution for maintaining reasoning capabilities.

## Methodology
The authors approached this problem by first defining a structural evaluation framework that separates the quality of the final answer from the structural validity of the intermediate reasoning traces. They applied this framework to four open-weight reasoning models, subjecting them to standard supervised fine-tuning (SFT) using ordinary instruction-response datasets that lacked explicit reasoning steps. The experimental design involved measuring several key metrics: the rate of valid reasoning traces, the frequency of empty or missing traces, and the conditional task performance (accuracy) given the presence or absence of valid reasoning. By comparing pre-fine-tuning and post-fine-tuning states, the authors quantified the extent of reasoning degradation. Additionally, they tested mitigation strategies, specifically loss-masking techniques, to determine if they could preserve reasoning structures during the fine-tuning process without requiring additional data sources.

## Results
The experimental results revealed that standard supervised fine-tuning rapidly suppresses valid reasoning traces, leading to a sharp decline in the rate of structurally valid reasoning. Crucially, the study found that answer-only metrics substantially obscure this failure; in several settings, the models maintained high conditional task performance despite a significant drop in valid reasoning generation. This indicates that a model can appear to perform well on standard benchmarks while internally losing its reasoning capabilities. Furthermore, the application of simple loss-masking strategies was shown to substantially mitigate this collapse, preserving the structural integrity of the reasoning traces without the need for complex teacher-student distillation or external reasoning data.

## Significance
This research is significant because it exposes a hidden vulnerability in the fine-tuning of reasoning models. It challenges the assumption that high final-answer accuracy equates to robust reasoning capabilities, warning practitioners that standard evaluation metrics may fail to detect the loss of explicit logical steps. By establishing the need for structural reasoning reliability metrics, the paper provides a critical guideline for the development and evaluation of future reasoning models, ensuring that adaptation processes do not inadvertently strip away the very mechanisms that make these models reliable for complex tasks.

## Related Concepts
- Reasoning-Trace Collapse
- Supervised Fine-Tuning (SFT)
- Structural Evaluation Framework
- Loss Masking
- Explicit Reasoning
- Reasoning Reliability Metrics
- Instruction-Response Data
- Open-Weight Models

[[Reasoning-Trace Collapse: Evaluating the Loss of Explicit Reasoning During Fine-Tuning]]