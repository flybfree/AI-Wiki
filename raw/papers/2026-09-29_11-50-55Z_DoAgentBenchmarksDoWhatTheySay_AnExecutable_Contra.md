---
title: Do Agent Benchmarks Do What They Say? An Executable-Contract Audit of Tool-Using Agent Environments
published: 2026-09-29T11:50:55Z
authors: Rohith Reddy Bellibatlu, Zichong Wang, Wenbin Zhang
url: http://arxiv.org/abs/2609.37315v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Agent Benchmarks Do What They Say? An Executable-Contract Audit of Tool-Using Agent Environments

## Abstract
Tool-using agents are entering settings where a wrong action carries real cost, and the benchmarks certifying them grade what each simulated tool call reports having done, assuming the tool did what its interface advertises. The audit taxonomies we survey publish no category for that assumption, and a defect beneath a score is present on every rerun. We treat a tool's advertised surfaces as an executable contract, check the implementation against it, and trace each score's provenance through the task files and evaluator code to the verdicts that derive from state a defective tool should have written. Across 34 audited mutating tools in four benchmarks we confirm seven tool defects and one evaluator property at pinned commits. On injected defects the checker raised no false positive in 25 flags, flagged 2 of 5 negative controls, and missed most: in 29 of 33 scored misses a clause covered the defect but no probe revealed it. The checker's own static half, run alone, flags 14 of 17 confirmed sites, so on these findings the dynamic half confirms and traces rather than discovers. Twelve further AgentDojo tools, with six held-out tools and the seven audited first, complete its 25-tool mutating surface, on which at least 5 tools diverge from their advertised surface as our contracts read it, a rate for AgentDojo alone. No gold trajectory reaches either tau2-bench defect; on 1,120 paths built to isolate the telecom defect, a number fixed by construction, the evaluator rewards a refuel of a suspended line and fails the repaired tool. The clearest case is a clinical benchmark whose tool tells the agent each write executed under a documented no-write design its interface does not disclose; its grader takes that message as evidence, so its action success rate records whether a request carried the expected payload, not whether any record changed.

## Metadata
- **Published**: 2026-09-29T11:50:55Z
- **Authors**: Rohith Reddy Bellibatlu, Zichong Wang, Wenbin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37315v1)