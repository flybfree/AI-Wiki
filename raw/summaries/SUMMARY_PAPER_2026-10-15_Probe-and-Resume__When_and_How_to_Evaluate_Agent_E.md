---
title: Probe-and-Resume: When and How to Evaluate Agent Execution
url: http://arxiv.org/abs/2610.21088v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_01-42-54Z_Probe_and_Resume_WhenandHowtoEvaluateAgentExecutio.md
generated_at: 2026-10-15 22:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why Monte Carlo tree search (MCTS) with critic-based evaluation fails to improve agent performance in terminal-based computer-use environments, where agents see only a partial view of a large underlying state. The authors identify that critics perform poorly at intermediate states because observations omit critical environment information and intermediate trajectories provide weak evidence of eventual success. They propose Probe-and-Resume, a design that invokes a critic only when the agent claims completion, granting the critic read, write, and execute access to a forked copy of the environment to probe hidden state, yielding an 8.4 percentage point improvement over conventional MCTS critics.

## Key Takeaways
- MCTS-based test-time search does not significantly improve task success in terminal-based computer-use environments because the agent's observations omit environment state needed for evaluation, and intermediate states offer limited evidence of whether a trajectory will ultimately succeed. Critics at intermediate nodes rank continuations only modestly better than random chance, and granting them additional environment access improves ranking only marginally.
- The Probe-and-Resume policy fundamentally changes when and how a critic is invoked: rather than evaluating partial progress, the critic is called only at nodes the agent believes are final. The critic is given read, write, and execute access to a fork of both the current and initial computer state, enabling it to perform potentially destructive probe actions that surface hidden state the agent's trajectory omitted. If the critic rejects the agent's claimed completion, the agent resumes from where it stopped rather than being discarded.
- On Terminal-Bench 2.1, Probe-and-Resume raises success by 8.4 percentage points over MCTS with conventional critics and approaches the success rate of the Codex CLI agent using the same underlying model, but at less than half the computational cost, demonstrating that targeted, late-stage evaluation with full environment access is far more effective than broad search over partial trajectories.

## Context
This work sits at the intersection of test-time compute scaling, agentic AI evaluation, and computer-use benchmarks. As large language model agents are increasingly deployed to operate real software environments—terminals, browsers, file systems—the question of how to verify whether an agent has actually completed a task becomes critical for safety and reliability. Prior work on MCTS and critic-based search has shown promise in structured domains like games or code generation, but this paper demonstrates that those techniques break down in partially observable, stateful environments where the agent's own observations are insufficient for a critic to judge trajectory quality. The findings challenge a common assumption in the agent-evaluation literature that more search and more critic invocations always lead to better outcomes.

## Implications
For practitioners building autonomous agents that interact with real computing environments, this paper suggests that investing in broad search over partial trajectories is less effective than investing in a powerful, late-stage verification step with full environment access. The Probe-and-Resume pattern offers a practical blueprint: let the agent work freely, then gate completion behind a critic that can actively probe the environment rather than passively inspect logs. For industry deployments, the finding that this approach approaches Codex CLI performance at under half the cost signals a path toward cheaper, more reliable agent verification pipelines, which is especially relevant for high-stakes automation in software engineering, system administration, and DevOps workflows where incorrect completions carry real operational consequences.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21088v1)
