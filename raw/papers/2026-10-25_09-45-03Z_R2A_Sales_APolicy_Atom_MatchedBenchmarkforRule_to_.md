---
title: R2A-Sales: A Policy-Atom-Matched Benchmark for Rule-to-Action Gaps in Goal-Directed Sales Agents
published: 2026-10-25T09:45:03Z
authors: Yihua Qin, Jiajie Jerry Zhao
url: http://arxiv.org/abs/2610.34185v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# R2A-Sales: A Policy-Atom-Matched Benchmark for Rule-to-Action Gaps in Goal-Directed Sales Agents

## Abstract
LLM-based sales agents are often evaluated on static policy questions or task success, but deployment asks a sharper question: when a model can state a rule, will it choose compliant, tool-grounded actions under commercial pressure? We introduce R2A-Sales (Rule-to-Action), a policy-atom-matched benchmark for this question. Each item pairs a static probe with a multi-turn sales scenario sharing the same versioned policy atom, facts, evidence, behavioral constraints, and tool contract, so differences cannot be attributed to policy-content mismatch. In the interactive arm, a code-owned ledger verifies committed tool effects and terminal states; unsupported action claims receive no credit. We report static compliance $K$, grounded action compliance $A=\Pr(\text{safe terminal}\land\text{no hard violation}\land\text{non-echo})$, and the matched gap $G=K-A$. The frozen release spans three controlled Chinese-language sales domains, 24 policy atoms, 42 semantic cores, and 2,016 matched pairs. The confirmatory study audits 21,888 runs over 19 cores, covering eight backbones plus four Qwen3-8B prompt treatments (12 configurations). Static compliance is near ceiling $(K=89.9\%\text{--}99.1\%)$, yet eight-backbone action compliance is only $A=3.0\%\text{--}17.3\%$, giving $G=80.4\text{--}92.5$ percentage points. Since $A$ also requires safe termination, $G$ upper-bounds rule-to-action degradation rather than isolating pressure alone. No prompt-only treatment dominates all metrics. R2A-Sales shows that sales-agent reliability must be measured at committed action, not rule recital or task completion alone.

## Metadata
- **Published**: 2026-10-25T09:45:03Z
- **Authors**: Yihua Qin, Jiajie Jerry Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34185v1)