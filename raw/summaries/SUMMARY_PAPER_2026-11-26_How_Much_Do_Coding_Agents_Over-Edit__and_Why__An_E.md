---
title: How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches
url: http://arxiv.org/abs/2611.34875v1
type: paper-summary
date: 2026-11-26
source_paper: 2026-11-25_18-37-06Z_HowMuchDoCodingAgentsOver_Edit_andWhy_AnEmpiricalS.md
generated_at: 2026-11-26 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper asks whether larger repository-level agent patches reflect harmful over-editing, and introduces Delta Residue Attribution (DRA) to answer causally: it replays agent trajectories, traces every block of the final patch to the step that wrote it, reverts each unit, and reruns task tests to decide whether that unit is needed. Applying DRA to 7,660 resolved GitHub Copilot CLI trajectories from 18 frontier models on SWE-bench Verified (6,728) and DeepSWE (932), plus developer patches graded the same way, it finds that agents do change more lines, but their code is on average at least as necessary as developers', with only about 11% of SWE-bench Verified code units unneeded.

## Key Takeaways
- Patch size is a misleading proxy for over-editing: on SWE-bench Verified the majority of extra edits add tests (61%) and documentation (13%), while on DeepSWE most extra edits are code (58%); agents' code is on average at least as necessary as developers' (mean NP_code 0.887 vs. 0.864 on SWE-bench Verified, where 11 of 18 models leave less unneeded code than developers, and 0.797 vs. 0.785 on DeepSWE).
- Unneeded code is concentrated and behavior-changing: on SWE-bench Verified, 11% of an agent patch's code units are unneeded and 89% of those change behavior; debug steps write almost none of the unneeded code; necessity differs substantially by model and is unrelated to resolve rate on SWE-bench Verified but negatively correlated with it on DeepSWE (Spearman -0.59, p = 0.01).
- Pruning is promising but imperfect: DRA pruning using only tests the agent can see (its own tests and the repository's) removes the majority of unneeded code but also some needed code (67% recall, 46% precision), and 89% of pruned patches still resolve the task; asking the agent to audit its own diff is more precise but less effective (36% recall, 66% precision). The authors recommend benchmarks report code necessity next to resolve rate and address over-editing through model training and harness-level pruning.

## Context
Repository-level coding agents are increasingly judged by resolve rate and by how large their diffs look, but diff volume conflates useful additions with waste and does not say whether extra edits are needed, what they are, or where they come from. DRA supplies a causal necessity measure by reverting individual patch units and rerunning tests, letting researchers compare agents and human developers on correctness-relevant behavior rather than on patch size alone.

## Implications
For practitioners and evaluators, a larger agent patch should not be treated as automatically worse; code necessity should be reported alongside resolve rate so that agents are compared on what actually helps the task. For builders, over-editing is best addressed through model training and harness-level pruning rather than by simply penalizing diff size, with visible-test DRA pruning offering a practical middle ground whose recall and precision still need careful tuning to avoid removing needed code.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.34875v1)
