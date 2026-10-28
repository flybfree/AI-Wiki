---
title: Agent or Human? Detecting Commits by AI Coding Agents in the Absence of Authorship Signatures
url: http://arxiv.org/abs/2610.36229v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_20-08-18Z_AgentorHuman_DetectingCommitsbyAICodingAgentsinthe.md
generated_at: 2026-10-27 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether commits made by AI coding agents (such as Claude Code, GitHub Copilot coding agent, and Cursor) can be distinguished from human-authored commits once their authorship signatures—bot accounts and Co-authored-by trailers—are removed. Analyzing 7,837,946 commits across 1,226 repositories, the authors find that signature-free detectors can rank agent commits above human commits with a ROC AUC of up to 0.859, but the signal derives primarily from message verbosity and change size rather than from the code itself, and practical precision at realistic agent prevalence remains low at 0.332.

## Key Takeaways
- The detectable signal separating agent commits from human commits after signature removal is dominated by superficial metadata—commit message verbosity and the size of changes—rather than by intrinsic properties of the code modifications themselves, meaning detection is fragile and potentially gameable.
- Transfer to unseen agents is poor: TF-IDF classifiers achieve only an AUC of 0.524 on held-out Claude Code commits, and temporal performance varies by agent (Copilot AUC drops then recovers, while additional training history helps Claude Code but not Copilot), indicating that detection models do not generalize across agent families or over time.
- Even the best detector achieves a precision of only 0.332 at the observed agent share in the full test set, and gpt-6-sol without fine-tuning matches traditional methods like XGBoost and TF-IDF, suggesting that no single approach offers a decisive advantage and that signature-free detection cannot substitute for explicit attribution records.

## Context
As AI coding agents increasingly commit directly to open-source repositories, empirical research on agent activity depends heavily on authorship signatures that are optional, removable, and often attached at the pull-request level rather than per-commit. This paper addresses a foundational methodological gap: without reliable signatures, the field lacks a robust way to measure agent contributions, which undermines studies on agent adoption rates, code quality, and collaboration dynamics in open-source ecosystems.

## Implications
For researchers studying AI agent contributions to open-source software, signature-based labels should be treated as a lower bound on agent activity rather than a complete census, since many agent commits may go undetected once signatures are stripped. For practitioners and maintainers, signature-free detection can serve as a triage tool to prioritize commits for human review but cannot replace explicit attribution mechanisms, reinforcing the need for standardized, enforced authorship metadata in repository tooling and governance policies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36229v1)
