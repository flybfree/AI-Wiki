---
title: EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence
url: http://arxiv.org/abs/2610.31650v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_17-57-04Z_EpiSEM_Bench_EvaluatingSafetyandEvidenceRecoveryin.md
generated_at: 2026-10-22 22:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EpiSEM-Bench is an executable benchmark designed to evaluate how tool-using language model agents handle safety-critical decisions when environmental facts are systematically omitted from tool responses. The benchmark contains 300 matched unsafe/safe task pairs across six domains and tests whether agents can recognize missing evidence, seek it out, and appropriately withhold prohibited actions while completing permissible tasks. The study evaluates ten models and finds substantial variation in how agents respond to evidence gaps, revealing that resistance to missing evidence does not guarantee useful recovery behavior.

## Key Takeaways
- The benchmark introduces a novel failure mode: an agent may execute a prohibited action even when the user request is benign and every returned statement is true, simply because a safety-relevant fact was omitted from the tool response. This distinguishes the problem from hallucination or adversarial prompting, focusing instead on structural evidence gaps in tool-use pipelines.
- By systematically suppressing critical facts, EpiSEM-Bench measures unsafe execution under critical evidence omission and determines the minimum observed failure cardinality, including cases where failures persist even with full evidence and cases where no failure is observed after exhaustive testing. This provides a rigorous, quantitative measure of agent robustness rather than anecdotal failure examples.
- An independent audit tool evaluates whether agents actively seek missing facts and then withhold prohibited actions while completing permissible tasks. The findings show that while recovery access reduces unsafe execution across all ten tested models, agents differ significantly in whether they actively obtain missing facts and use them to act appropriately in both the unsafe and safe task variants.

## Context
As LLM agents increasingly interact with external tools, APIs, and environments to perform real-world tasks, their safety depends not only on internal reasoning but on the completeness and accuracy of environmental feedback they receive. Existing safety benchmarks typically test agents against adversarial prompts or hallucinated outputs, but they do not probe the more subtle failure mode where tool responses are technically truthful yet structurally incomplete. EpiSEM-Bench fills this gap by formalizing evidence omission as a testable, reproducible condition across multiple domains, providing a standardized evaluation framework for agent safety under information scarcity.

## Implications
For practitioners deploying LLM agents in safety-critical domains such as healthcare, finance, or autonomous operations, this benchmark highlights that agents cannot be assumed to compensate for incomplete tool outputs simply because they are resistant to adversarial inputs. Industry developers should incorporate evidence-recovery testing into their agent evaluation pipelines and consider designing tool interfaces that proactively surface safety-relevant facts rather than relying on the agent to detect omissions. The finding that recovery access helps all models but agents vary in whether they actively seek missing information suggests that system-level design choices, such as mandatory evidence-checking steps or audit hooks, may be more reliable than relying on model-level reasoning alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31650v1)
