---
title: Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Coding Agent Teams
published: 2026-07-24T21:11:18Z
authors: Shouren Wang
url: http://arxiv.org/abs/2607.22917v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agent Team Work Zone: An Automated, Persistent Workspace for Long-Lived Coding Agent Teams

## Abstract
Large Language Model (LLM) agents have significantly improved coding and programming workflows. Claude Code, in particular, is one of the most powerful LLM coding agents and is capable of conducting complex coding tasks. However, several drawbacks can undermine long-term agentic workflows. (1) Irrecoverable agent teams: The Agent Teams feature is powerful, but the working state accumulated by each teammate is lost and cannot be resumed once the process stops, for example, when a terminal is closed. (2) Compaction erodes working detail: Compaction condenses the conversation into a summary, causing an agent's working details to become vague. (3) Agentic "technical debt": Over time, a user's decisions and the agents' operations become trapped in compacted old chats, making the project increasingly difficult to maintain and review. (4) Heavy prompt writing: Assigning or handing off tasks requires users to repeatedly write long prompts to achieve the expected agentic performance. We propose ATWZ (Agent Team Work Zone), a filesystem-based operations layer built around Claude Code's native Agent Teams that addresses these problems. Its central design principle is to treat each agent and teammate as a human employee and preserve their important working state in files stored in a dedicated directory called a "workstation," together with the skills, hooks, and scripts that use and maintain these files. With ATWZ, an agent team can periodically back up its working state, allowing an agent's knowledge to be recovered after compaction. After a process ends, the team can be restored with a single command. These features also substantially mitigate the agentic "technical debt" described above. Moreover, within ATWZ, agent "employees" can send documents to one another, greatly reducing the effort required to write prompts.

## Metadata
- **Published**: 2026-07-24T21:11:18Z
- **Authors**: Shouren Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22917v1)