---
title: Probe-and-Resume: When and How to Evaluate Agent Execution
published: 2026-10-15T01:42:54Z
authors: Jiakai Xu, Tiancheng Ge, Tujie Guan, Yusheng Li, Rohan Timmaraju, Eugene Wu, Kostis Kaffes
url: http://arxiv.org/abs/2610.21088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Probe-and-Resume: When and How to Evaluate Agent Execution

## Abstract
Test-time search can improve agent performance by exploring alternative actions and using a critic to select promising branches. We study this approach in terminal-based computer-use environments, which expose only a partial view of a large underlying state, and find that the Monte Carlo tree search (MCTS) configuration we evaluate does not significantly improve task success. We identify two sources of poor critic performance: the agent's observations omit environment state needed for evaluation, and intermediate states offer limited evidence of whether a trajectory will succeed. At intermediate states, critics rank continuations only modestly better than chance, and environment access improves this little. We study when to invoke a critic and what access to give it to evaluate a node. Our findings motivate a policy that invokes the critic only at nodes the agent believes are final, rather than during partial progress. Further, the policy gives the critic read, write, and execute access to a fork of the computer's current and initial state, allowing it to probe and perform potentially destructive actions to surface any hidden state the trajectory omits. We call the resulting design Probe-and-Resume: when the agent claims to be done, the critic probes a fork of its state, and a rejected agent resumes where it stopped. On Terminal-Bench 2.1, this raises success by 8.4 percentage points over MCTS with conventional critics, and approaches the success rate of the Codex CLI agent with the same underlying model at less than half its cost.

## Metadata
- **Published**: 2026-10-15T01:42:54Z
- **Authors**: Jiakai Xu, Tiancheng Ge, Tujie Guan, Yusheng Li, Rohan Timmaraju, Eugene Wu, Kostis Kaffes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21088v1)