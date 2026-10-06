---
title: Do Tool Calls Execute as Intended? Measuring and Repairing Intent-Execution Correspondence in LLM Agents
published: 2026-10-03T08:38:35Z
authors: Boyang Yang, Zhenhao Li, Ziyao Yang, Kanghui Jia, Xin Yin, Mingmou Liu, Haoye Tian
url: http://arxiv.org/abs/2610.04375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Tool Calls Execute as Intended? Measuring and Repairing Intent-Execution Correspondence in LLM Agents

## Abstract
Agents built on large language models (LLMs) build and run software through tool calls. A call reaches its program through several hops, and any hop can change the call without notice. When the changed call fails, the agent retries a correct call, which costs users time and money. Benchmarks and failure analyses do not see the change, because they read the call and its result but not what a hop received. We define intent-execution correspondence (IEC) as the property that the executed action matches the action the emitted call denotes under the tool contract. Our protocol observes what each hop received without executing the call, and names the first hop that changed it by the receiver's own parser. IntAct then delivers the call in a form that this hop cannot alter, or refuses the call. We build IEC-Bench from the changes observed in real-world use, with chains of dependent calls under the execution paths of 4 widely-used harnesses.   In 47,828 shell calls within production sessions, Claude Code's Bash tool changes 12.0% of the calls that carry code, escape sequences, or long text. For 80.7% of the calls whose backslashes are changed, the wrong action runs without any reported error. All 10 measured harnesses change a call. Trajectory-based judgment attributes 95.1% of the production failures to the LLM, although the path caused more than half of them. On IEC-Bench, the path raises the token cost per passed task 2.4 times (up to 12.3 times). A hop that changes a call also hides the changes after it, so 55.1% of the failures on one path appear only after its first hop is repaired. IntAct, deployed in a commercial product, recovers 79.2% of the failures with a changed call. Harnesses should therefore be designed and tested hop-by-hop to ensure a correct call executes as intended or is refused.

## Metadata
- **Published**: 2026-10-03T08:38:35Z
- **Authors**: Boyang Yang, Zhenhao Li, Ziyao Yang, Kanghui Jia, Xin Yin, Mingmou Liu, Haoye Tian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04375v1)