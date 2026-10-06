---
title: What Does a Harness Buy? Tokens, Mostly
url: http://arxiv.org/abs/2610.04433v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-03_10-47-10Z_WhatDoesaHarnessBuy_Tokens_Mostly.md
generated_at: 2026-10-05 22:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper empirically measures how much a coding agent harness (system prompt, tool set, context management) actually changes benchmark scores when the underlying language model is held fixed. Running five models through three production harnesses on SWE-bench Verified, the authors find that the heaviest and lightest harnesses perform equivalently within five points on the full task pool, while the only clear harness effect is a performance loss from OpenCode. The most consequential harness difference is not accuracy but cost, with per-task spending varying up to threefold across harnesses using the same model and tasks.

## Key Takeaways
- On 447 SWE-bench Verified tasks, Claude Code (the heaviest harness) and mini-SWE-agent (the lightest) produce scores equivalent within five points, and on a 45-task hard subset, swapping the harness flips as many tasks (13%) as simply rerunning the same harness, meaning observed task-level differences are indistinguishable from run-to-run noise. The tasks a harness wins in one run are not the tasks it wins in the next.
- The only harness effect that clears statistical noise is a loss: OpenCode trails by up to 9 points on the large pool, and for one model, half of that gap is attributable to its output cap truncating runs prematurely rather than any inherent harness advantage or disadvantage.
- Cost per task differs by up to 3x across harnesses with identical models and tasks. The gap is determined at the first call by the preamble of system prompt and tool schemas each harness sends with every step, then scaled by the number of steps taken. Per-step growth and per-call tool output contribute far less, and the provider's cached-input pricing scales the bill but does not reorder the cost ranking.
- The rerun calibration data establish the statistical resolution a harness comparison requires: 45 tasks catch a 13-point gap only half the time and detect no gap with 80% power, while 447 tasks resolve only 5 points, which is still coarser than the gains many harness changes claim to deliver.

## Context
This paper addresses a persistent blind spot in the coding-agent evaluation ecosystem. Production harnesses ship releases daily, vendors advertise pass-rate improvements from harness updates, and leaderboards freely mix different harness configurations, yet almost no controlled study isolates the harness's contribution from the model's contribution. By holding models fixed and varying only the harness across three widely used production systems, the authors provide the first rigorous quantification of harness effects on SWE-bench Verified, a benchmark that has become the de facto standard for evaluating coding agents.

## Implications
For practitioners and vendors, the findings suggest that many claimed harness-driven score improvements fall within run-to-run noise and cannot be distinguished from random variation at typical evaluation sizes, meaning benchmark-based marketing claims about harness upgrades should be treated skeptically unless they exceed the noise floor the authors quantify. For cost-sensitive deployments, the 3x cost spread across harnesses driven primarily by system-prompt preamble size and step count offers a concrete lever for optimization: reducing the fixed overhead sent at every call and limiting step counts matter far more than tuning per-step tool output. The paper also implies that the field needs larger evaluation pools and repeated-run protocols before harness comparisons can be considered statistically meaningful.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.04433v1)
