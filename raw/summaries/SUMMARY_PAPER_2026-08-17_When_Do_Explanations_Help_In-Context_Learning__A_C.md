---
title: When Do Explanations Help In-Context Learning? A Comparative Study of Natural Language Explanation Types and Faithfulness
url: http://arxiv.org/abs/2608.16627v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_14-30-03Z_WhenDoExplanationsHelpIn_ContextLearning_AComparat.md
generated_at: 2026-08-17 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates how different natural language explanation types and selection strategies affect in-context learning performance across six benchmarks and four models. It finds that adding NLEs often improves classification accuracy, especially with external LLM-generated explanations, while self-explanations depend on faithfulness filtering. Faithfulness metrics can cause large variations in selected examples and downstream utility.

## Key Takeaways  
- Externally generated LLM-NLEs provide strong downstream utility and are competitive with human rationales, whereas self-generated NLEs show sensitivity to selection strategy.  
- Faithfulness-based filtering of self-explanations yields modest average gains but can increase or decrease performance depending on metric, task, and model.  
- Robustness tests reveal partial robustness to swapped or out-of-distribution rationales, indicating semantic alignment is key for performance.

## Context  
Natural language explanations are increasingly used as few-shot rationales in prompting pipelines, aiming to guide large language models toward desired behavior. Understanding which explanation types and selection methods work best is crucial for reliable model deployment and evaluation.

## Implications  
Practitioners should prioritize external LLM-generated explanations when they need consistent performance across tasks. Researchers must be cautious about faithfulness metrics, as they can mislead the choice of examples and impact real-world outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16627v1)
