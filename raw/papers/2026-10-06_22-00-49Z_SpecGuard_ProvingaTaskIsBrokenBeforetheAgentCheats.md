---
title: SpecGuard: Proving a Task Is Broken Before the Agent Cheats
published: 2026-10-06T22:00:49Z
authors: Param Biyani, Krishnamurthy Dvijotham
url: http://arxiv.org/abs/2610.09159v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SpecGuard: Proving a Task Is Broken Before the Agent Cheats

## Abstract
As autonomous coding agents get increasingly deployed, the risk that accidental or adversarially injected misspecifications in tasks lead to dangerous agent behavior is critical to address. Prior work has shown that agents given such tasks rarely flag the conflict and instead cheat, editing tests or hard-coding expected outputs, and the actions taken to cheat can cause real damage, such as deleting a security defense to make a corrupted test pass. It remains unclear whether such conflicts can be established with independently verifiable evidence before the agent acts. We present SpecGuard, which detects and formally certifies these conflicts between task intent and tests. Given only the task description and codebase, SpecGuard autoformalizes the intended behaviour into a Lean 4 specification. The tests are formalized independently, and the Lean kernel checks whether any implementation could satisfy both formalizations, producing a machine-checked certificate when none can. On conflicted SWE-bench tasks, SpecGuard detects up to 72.8% of conflicts and formally certifies up to 51.1%, with a nearly five-fold lower conflict miss rate than model-based judgment. SpecGuard provides a pre-execution safety check that identifies reward-hacking opportunities through formal certification of task-level conflicts, before any agent behavior is observed. Our code is available at https://github.com/prmbiy/specguard.

## Metadata
- **Published**: 2026-10-06T22:00:49Z
- **Authors**: Param Biyani, Krishnamurthy Dvijotham
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09159v1)