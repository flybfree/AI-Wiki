---
title: @skills: Attention is all you have
published: 2026-08-12T21:49:00Z
authors: Li Yin, Zhi Li, Zhan Shi, Haoran Zhang, Haebin Seong,  Zhangyang,  Wang
url: http://arxiv.org/abs/2608.12610v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# @skills: Attention is all you have

## Abstract
There are 56,804 public agent skills today, and teams write many more privately. The dominant delivery model is installation: once installed, a skill's description remains in the system prompt, competing for fewer than 100 reliable trigger slots. This leaves the long tail with no practical path to use and forces teams' own playbooks to compete for the same scarce space. We observe that installation bundles three separable functions: content, persistence, and automatic triggering. Only the last requires prompt residency. We therefore propose @skills, an open protocol that separates them. A path addresses any skill, subtree, or collection, and reading a skill is sufficient to use it, so nothing is installed or made resident. The operation vendors a copy at the same path into a project's Git-tracked tree for adaptation and ownership. The operation adds one .gitignore-style line, the only element that costs prompt residency. A directory is a menu, making bundles ordinary directories rather than all-or-nothing units. The protocol requires no manifest, lockfile, or registration, and SKILL.md remains unchanged. @skills is additive, ships as an installable package, and turns any agent that can read files and run commands into a client through a single instruction file. Its open specification is at https://github.com/SylphAI-Inc/atskills and it is implemented in the AdaL CLI at https://adalagent.ai . Because paths address skills well but cannot find them, the protocol is paired with a free hub at https://atskills.one for corpus-wide search and ranking, repository-free hosting, private and team collections, and one-screen authoring. The hub is optional: gh: and local paths resolve without it, and indexed GitHub skills retain their gh: identities. Install less, use more.

## Metadata
- **Published**: 2026-08-12T21:49:00Z
- **Authors**: Li Yin, Zhi Li, Zhan Shi, Haoran Zhang, Haebin Seong,  Zhangyang,  Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12610v1)