---
title: Chronos Enables Code Agents to Reason over Software Evolution
url: http://arxiv.org/abs/2610.11578v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_09-31-37Z_ChronosEnablesCodeAgentstoReasonoverSoftwareEvolut.md
generated_at: 2026-10-08 21:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Chronos is a test-time framework designed to make the historical context embedded in merged pull requests accessible to LLM-based code agents, enabling them to reason over a repository's evolution rather than treating each task in isolation. The framework distills pull requests into structured "experience cards" connected via a typed graph, then uses weighted multi-hop retrieval to surface relevant prior changes during patch generation and selection. Evaluated on SWE-Bench Verified, SWE-Bench Pro, and FEA-Bench Lite, Chronos consistently improves resolution rates across six LLM backbones, with the full workflow raising mean resolution from 69.2% to 72.9% and reaching 79.8% with MiniMax M2.5.

## Key Takeaways
- Chronos constructs a typed relational graph over merged pull requests, encoding code-level dependencies, developer-intent links, and organizational relationships. This graph-grounded retrieval, validated through human evaluation on 100 tasks, increases the mean number of useful experience cards retrieved per task from 1.24 to 2.87 compared to flat semantic retrieval, demonstrating that structured connections between historical changes are far more informative than keyword or embedding similarity alone.
- The framework employs a multi-agent workflow comprising a patch-focused change agent, a validation-strategy agent, and an "evolution steward" that consults retrieved history to select the best candidate patch. Both single-agent experience-guided variants also outperform the base agent, indicating that even partial integration of historical context yields measurable gains, while the full three-agent pipeline compounds those gains further.
- Performance improvements are consistent across diverse benchmarks and model backbones: SWE-Bench Verified mean resolution rises from 69.2% to 72.9%, SWE-Bench Pro from 48.3% to 51.7%, and FEA-Bench Lite from 41.0% to 43.5%. The peak result of 79.8% with MiniMax M2.5 shows that the framework's benefits scale with stronger underlying models, suggesting the retrieved experience provides complementary reasoning scaffolding rather than merely compensating for weak models.

## Context
This work sits at the intersection of software engineering automation and retrieval-augmented reasoning for LLM agents. Prior code-agent systems such as SWE-Agent operate on a snapshot of the repository without access to the evolutionary narrative encoded in commit and pull-request history. Chronos addresses a recognized gap in agentic coding research: the inability to leverage accumulated institutional knowledge—design decisions, compatibility constraints, and implementation patterns—that human developers routinely consult when modifying mature codebases. By formalizing this knowledge as a queryable graph, the paper advances the broader trend of giving agents persistent, structured memory rather than relying solely on in-context window retrieval.

## Implications
For practitioners building autonomous coding assistants or CI/CD automation pipelines, Chronos demonstrates that encoding repository history as a typed graph and integrating it into agent decision loops can yield consistent, benchmark-validated improvements without retraining the underlying language model. For the research community, the results validate that relational structure between historical changes carries substantially more retrieval utility than flat semantic search, pointing toward graph-augmented memory architectures as a general strategy for any agent that must reason over evolving artifacts. Industry teams maintaining large codebases could adopt similar experience-card distillation pipelines to reduce onboarding friction for new contributors and to harden automated patch-generation systems against regressions that historical PRs already anticipated.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11578v1)
