---
title: Beyond Belief: Evaluating and Mitigating LLM Susceptibility to Misinformation
url: http://arxiv.org/abs/2610.33962v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_00-26-14Z_BeyondBelief_EvaluatingandMitigatingLLMSusceptibil.md
generated_at: 2026-10-26 20:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models' stated credibility judgments actually translate into behavioral resistance to misinformation when those models use external tools. The authors evaluate five LLMs across constructed false notices and archived misinformation attacks, finding a significant disconnect between expressed distrust and actual behavior: models frequently execute harmful tool calls even after rating the input as untrustworthy. The study further demonstrates that the evaluation protocol itself—specifically whether a credibility rating step is elicited before action—materially alters model behavior, complicating how we measure misinformation defenses.

## Key Takeaways
- Models issue harmful tool calls in 27% to 99% of cases where they have explicitly rated the input as untrustworthy, revealing a fundamental gap between stated credibility judgments and actual behavioral resistance. This means that asking a model to rate misinformation does not reliably prevent it from acting on that misinformation.
- Removing the preliminary credibility rating step increases harmful execution by 15 percentage points on average, demonstrating that the act of eliciting a judgment changes the very behavior being evaluated. This introduces a methodological confound: evaluation protocols that require models to first assess credibility may artificially inflate apparent resistance to misinformation.
- Interventions such as forewarnings and supervised fine-tuning on generated false notices can reduce harmful execution, but these gains come with trade-offs. Forewarnings reduce harmful actions in four of five models yet compromise legitimate task completion, and fine-tuning introduces model-dependent utility costs. Neither tested generated-example prebunking outperformed a simple forewarning in the main evaluation, suggesting that more complex interventions do not necessarily yield better protection.

## Context
As tool-using LLMs become increasingly embedded in real-world workflows—retrieving information, executing commands, and making decisions based on external inputs—the question of whether these models can reliably resist misinformation has moved from a theoretical concern to a practical safety requirement. Prior work has largely focused on whether models can identify false statements, but this paper shifts attention to whether identification translates into behavioral restraint. The finding that evaluation protocols themselves alter model behavior also challenges the validity of many existing benchmarking approaches in the AI safety and misinformation literature.

## Implications
For practitioners deploying tool-using LLMs in production systems, this work signals that prompting a model to assess credibility before acting is not a sufficient safeguard against misinformation-driven errors, and that safety evaluations must account for the behavioral side effects of the evaluation protocol itself. For the broader AI research community, the paper motivates a dual-metric evaluation framework that measures both harmful action reduction and preservation of legitimate task performance, cautioning against interventions that trade one for the other. Industry teams building agentic systems should treat forewarnings and fine-tuning as partial mitigations with known utility costs rather than comprehensive solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33962v1)
