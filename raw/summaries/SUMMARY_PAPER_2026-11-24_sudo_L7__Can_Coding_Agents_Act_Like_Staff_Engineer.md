---
title: sudo L7: Can Coding Agents Act Like Staff Engineers?
url: http://arxiv.org/abs/2611.30517v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_11-32-37Z_sudoL7_CanCodingAgentsActLikeStaffEngineers.md
generated_at: 2026-11-24 21:58
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
sudo L7 asks whether coding agents can act like staff engineers rather than merely turn a well-specified ticket into a passing patch. It pairs realistic, underspecified requests with hidden, expert-authored rubrics of atomic criteria across eight behavioral dimensions, and grades attempts with an agentic grader that reads the transcript, inspects and runs the code, and treats test output as evidence. The headline finding is that even the strongest models remain far from staff-level reliability: the best pass only about half of attempts, and most gating criteria test behaviors beyond functional correctness.

## Key Takeaways
- The benchmark contains 60 software-engineering tasks written by staff-level engineers, mostly in private production codebases, each built around a place where a frontier model failed; tasks pair an underspecified request with a hidden rubric of 1,287 atomic criteria tagged with eight behavioral dimensions from functional correctness to truthful reporting.
- An attempt passes only if it meets every criterion of the two highest severities, and more than half of these gating criteria test something other than functional correctness; the agentic grader reads the agent's transcript, inspects and runs its code, and treats test output as evidence.
- On the public leaderboard as of November 2026 (19 models, each in its developer's harness or in OpenCode, three attempts per task), Claude Fable 5.2 passes 52.2% of attempts, Claude Sonnet 5.5 passes 50.6%, and Claude Opus 5.5 passes 46.1%.
- GPT-6.1 Sol, Claude Fable 5.1 and GPT-6 Astra pass 31-34%, while the other 13 models pass at most 18.9%, showing a clear gap between the top tier and the rest.
- In a human-label study, three candidate model graders each agreed with a software engineer on 85-86% of criterion verdicts, about as often as two engineers agreed with each other; benchmark cases also show how one unsupported claim can fail an otherwise strong attempt and illustrate flagging hidden hazards versus avoiding needless work.

## Context
Coding agents have become increasingly capable at producing patches that pass tests, but staff-level engineering involves judgment that is not captured by test success: noticing risks the request never mentioned, questioning flawed premises, reusing what already exists, and saying plainly what was and was not checked. sudo L7 targets this gap by evaluating underspecified requests in production-like settings rather than clean, fully specified benchmark tasks.

## Implications
The results suggest current agents are not yet dependable staff-level collaborators; even the leading models pass only about half of attempts, and the weaknesses concentrate in non-functional-correctness behaviors rather than raw coding. For practitioners, human review should therefore focus on engineering judgment, verification honesty, and hidden-hazard detection rather than test passage alone. For the field, sudo L7 provides a reusable rubric and grader approach for measuring judgment and for building more realistic agent evaluations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.30517v1)
