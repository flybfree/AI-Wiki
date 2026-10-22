---
title: Where Should a Stuck Agent Spend Its Next Tokens? Causal Attribution of Inference-Time Resources
url: http://arxiv.org/abs/2610.28834v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_18-59-01Z_WhereShouldaStuckAgentSpendItsNextTokens_CausalAtt.md
generated_at: 2026-10-21 21:09
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Banzhaf Resource Attribution (BRA), a controlled factorial framework designed to measure the marginal contribution of different inference-time resources—computation, information, and feedback—to repairing failed coding agents. The authors evaluate six models across function-level and repository-level benchmarks and find that task-relevant specifications consistently improve repair outcomes, while frontier models overwhelmingly select feedback despite it yielding lower gains than uniform random resource selection, exposing a significant misalignment between agent preferences and measurably effective resources.

## Key Takeaways
- Task-relevant specifications consistently improve repair outcomes across all evaluated models, whereas public-test feedback provides only small gains and retrieved code contributes little to no improvement. This suggests that providing the agent with precise contextual information about what the code should do is far more effective than giving it execution feedback or similar code examples.
- The value of additional computation (e.g., more tokens, extended reasoning) declines as model capability increases, while information resources remain useful regardless of model strength. Resource channels largely exhibit diminishing returns, though complementary information can reinforce itself, indicating that stacking multiple information sources can still yield benefits even when individual channels saturate.
- Three of four frontier models select feedback in 95-100% of cases yet obtain lower repair gains than uniform random resource selection. This reveals a critical gap between what agents are trained or prompted to prefer and what actually improves outcomes, suggesting that current agent architectures may be systematically misallocating their inference-time budgets.

## Context
Inference-time scaling has become a dominant paradigm for improving LLM-based agent performance, yet the field largely treats it as a monolithic token-budget problem rather than a resource-allocation problem with qualitatively distinct channels. This paper matters because it applies cooperative game theory—specifically Banzhaf power indices—to decompose agent repair performance into attributable contributions from computation, information, and feedback, moving beyond aggregate token counting toward causal understanding of which resources actually drive improvement. The evaluation spans both function-level (MBPP+, HumanEval+) and repository-level (SWE-bench Verified) failures, making the findings relevant across the full spectrum of software engineering tasks agents are deployed on.

## Implications
For practitioners building coding agents, this work suggests that defaulting to feedback-driven revision loops may be suboptimal and that investing in richer task specifications and contextual information could yield better repair outcomes at lower token cost. For the broader field, the finding that frontier models systematically prefer less effective resources highlights a need for architectural or training interventions that align agent resource-selection behavior with empirically measured causal contributions, potentially reshaping how inference budgets are allocated in production agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28834v1)
