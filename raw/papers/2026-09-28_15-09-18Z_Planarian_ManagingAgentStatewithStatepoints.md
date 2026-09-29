---
title: Planarian: Managing Agent State with Statepoints
published: 2026-09-28T15:09:18Z
authors: Jinnan Guo, Hao Mark Chen, Kapil Vaswani, Andrew Paverd, Peter Pietzuch
url: http://arxiv.org/abs/2609.35366v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Planarian: Managing Agent State with Statepoints

## Abstract
LLM agents solve complex tasks by iteratively changing files, invoking local tools, and interacting with remote services, which modifies state across their local environment and remote services. Today, agents and users must manage these changes explicitly, whether reverting exploratory actions or recovering from erroneous ones. Doing so safely requires coordinated actions, yet current agent harnesses lack unified abstractions and mechanisms for managing local and remote state consistently and efficiently.   We describe Planarian, an agent runtime with state management that enables agents and users to recover from erroneous actions and explore alternative executions over consistent local and remote environment state. Planarian introduces the abstraction of agent statepoints, which are consistent, restorable point-in-time versions of the environment state. Planarian exposes three state-management primitives to agents and users: (i) snapshot creates a new statepoint spanning local and remote state without requiring external services to support checkpoints: it relies on efficient incremental process and file system snapshotting to capture local sandboxed state, and transparently records compensating actions to undo remote state changes; (ii) rollback restores the environment to a previous statepoint by reverting to a prior local checkpoint and replaying compensating actions for remote state changes; and (iii) fork creates multiple isolated branches from a statepoint, enabling the agent to explore alternatives in parallel. We show that Planarian enables agents to undo mistakes and explore alternatives in parallel, improving task quality by up to 15x, and allows users to recover from erroneous actions with only 3% overhead.

## Metadata
- **Published**: 2026-09-28T15:09:18Z
- **Authors**: Jinnan Guo, Hao Mark Chen, Kapil Vaswani, Andrew Paverd, Peter Pietzuch
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35366v1)