---
title: Evaluating LLMs as Agentic Workflow Executors in Real-World Customer Support Skills
url: http://arxiv.org/abs/2610.14346v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-09_21-45-51Z_EvaluatingLLMsasAgenticWorkflowExecutorsinReal_Wor.md
generated_at: 2026-10-13 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a benchmark construction pipeline for evaluating Large Language Models as specialized executors of bounded, tool-using customer-support workflows, termed "Skill LLMs." The authors mine recurrent workflows from real-world customer-support transcripts, convert them into structured skill descriptions with mapped tool requirements, simulate environment state using Model Context Protocol-compatible mocks, and generate multi-turn tool-using dialogues for testing. Through a large-scale zero-shot evaluation of 17 models judged by five LLM judges plus a deterministic rule-based evaluator, they find GPT-5.4 leads by a wide margin while QWEN3.5-9B emerges as the strongest open-weight model under 20B parameters, and they reveal that inter-judge agreement averages only Kappa=0.524, underscoring that evaluation methodology is as critical as model capability.

## Key Takeaways
- The benchmark pipeline bridges the gap between raw customer-support transcripts and structured evaluation by mining recurring workflows, converting them into formal skill descriptions, mapping them to concrete tool requirements, and simulating stateful environments via MCP-compatible mocks to produce realistic multi-turn tool-using dialogues that test agentic execution rather than mere text generation.
- Across 17 evaluated models spanning closed model families and open-weight models from 1.7B to 14B parameters, GPT-5.4 consistently ranks first by a wide margin, while QWEN3.5-9B outperforms several closed baselines under every judge, demonstrating that open-weight models can achieve competitive agentic tool-use performance in constrained, stateful workflow settings.
- Pairwise judge agreement on pass/fail verdicts averages only Kappa=0.524 across 10 judge pairs, revealing that the choice of LLM judge is not a minor methodological detail but a substantial source of evaluation variance; the authors pair LLM judges with a deterministic rule-based evaluator checking tool coverage, hallucinated tool use, and unsupported claims to mitigate this unreliability.

## Context
As enterprises increasingly deploy LLMs to handle bounded, tool-using customer-support tasks, the community lacks standardized benchmarks that test whether models can faithfully execute narrow, stateful workflows under policy and tool constraints rather than simply generating fluent text. This paper addresses that gap by grounding evaluation in real-world transcript mining and MCP-compatible environment simulation, aligning benchmark construction with the actual operational demands of agentic deployment pipelines. The finding that judge disagreement is substantial also connects to broader concerns in the AI evaluation literature about the reliability and reproducibility of LLM-as-judge methodologies.

## Implications
For industry practitioners deploying agentic customer-support systems, these results provide actionable guidance on model selection: QWEN3.5-9B offers a viable open-weight option for constrained workflow execution, while the wide margin of GPT-5.4 highlights the performance ceiling of frontier closed models. For the research community, the low inter-judge agreement signals that future agentic benchmarks must incorporate deterministic rule-based checks and multiple independent judges to produce trustworthy rankings, and that evaluation infrastructure deserves as much engineering rigor as model training itself.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14346v1)
