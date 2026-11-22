---
title: MANGO Arena: Same Seeds, Different Chains Evaluating LLM Agents in a Disrupted Supply Chain
url: http://arxiv.org/abs/2611.23613v1
type: paper-summary
date: 2026-11-21
source_paper: 2026-11-17_23-05-05Z_MANGOArena_SameSeeds_DifferentChainsEvaluatingLLMA.md
generated_at: 2026-11-21 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MANGO Arena is an open-source multi-agent testbed in which four LLM agents each manage one company in a serial supply chain adapted from the MANGO classroom factory-management game, designed to simultaneously measure the bullwhip effect, rule adherence under pressure, and collusion behavior. A pilot study with three small reasoning models revealed that all LLM agents amplified demand variability far beyond textbook benchmarks, but the paper's most critical finding is methodological: API failures silently corrupted metrics, and rerunning identical seeds produced bullwhip magnitudes differing by up to 17 times, undermining the reliability of single-run conclusions.

## Key Takeaways
- All three tested LLM agents amplified demand variability as it moved upstream in the supply chain, producing bullwhip amplifications of 7 to 25 times at the Retailer level and 13 to 179 times at the Supplier level, frequently exceeding what a textbook order-up-to policy would generate. This amplification was driven largely by batch ordering behavior, with agents issuing zero orders in up to 60% of their decisions, indicating a tendency toward lumpy, reactive ordering rather than smooth replenishment.
- Rule adherence was surprisingly strong: real violations of hard constraints such as truck limits, no-credit cash rules, and production capacity occurred in at most 7 out of 288 decisions per model, and no agent proposed a monetary side deal despite having access to a public message board. This suggests that small reasoning models can respect explicit structural constraints even under economic pressure.
- The evaluation methodology itself proved fragile. API failures from rate limits and runaway hidden reasoning were silently logged as "no order" decisions, contaminating results without detection. When games were rerun with identical seeds and no failed calls, upstream bullwhip magnitudes shifted by up to 17 times between runs, and conclusions about how a supplier-fire disruption affected a given model did not survive a rerun across three demand seeds. The authors propose explicit reporting practices for multi-agent evaluations to prevent these silent failures from distorting findings.

## Context
This paper sits at the intersection of LLM agent evaluation and operations research, addressing a growing need for reproducible, multi-agent benchmarks that go beyond single-task reasoning tests. As LLM agents are increasingly deployed in complex, interdependent systems such as supply chains, logistics, and market simulations, the community lacks standardized environments that simultaneously stress-test economic reasoning, constraint compliance, and strategic communication. MANGO Arena fills this gap by adapting a well-known pedagogical game into a rule-enforced digital testbed, while its candid reporting of API-induced measurement noise and seed-level instability highlights a broader reproducibility crisis in multi-agent LLM evaluation that the field has yet to adequately address.

## Implications
For practitioners deploying LLM agents in supply-chain or logistics automation, the findings warn that batch-ordering behavior and extreme bullwhip amplification are not hypothetical risks but observed defaults in current small reasoning models, demanding explicit guardrails and monitoring before production use. For the AI evaluation community, the paper's transparent accounting of API failures and seed-level variance sets a template for reporting standards that other multi-agent benchmarks should adopt, pushing the field toward statistically robust, multi-seed evaluation protocols rather than single-run narratives. The fully public code, prompts, and decision logs lower the barrier for independent replication and stress-testing of agent behavior under economic constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.23613v1)
