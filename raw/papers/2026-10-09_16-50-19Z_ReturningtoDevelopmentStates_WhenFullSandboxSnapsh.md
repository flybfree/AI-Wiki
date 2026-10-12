---
title: Returning to Development States: When Full Sandbox Snapshots Help Coding Agents
published: 2026-10-09T16:50:19Z
authors: Daniel Thi Graviet, Tanmay Shah
url: http://arxiv.org/abs/2610.13841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Returning to Development States: When Full Sandbox Snapshots Help Coding Agents

## Abstract
Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could outperform repeatedly restarting from the initial state. We implement Go-Explore-style search over full Daytona snapshots and find that higher and more efficient solve rates depend mainly on progress that sits outside the repository, such as databases, services, and other runtime state. Our results suggest that full-snapshot search is most effective when long-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff.

## Metadata
- **Published**: 2026-10-09T16:50:19Z
- **Authors**: Daniel Thi Graviet, Tanmay Shah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13841v1)