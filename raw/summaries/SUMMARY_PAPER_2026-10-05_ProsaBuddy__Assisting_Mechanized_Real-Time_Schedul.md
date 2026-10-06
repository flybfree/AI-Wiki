---
title: ProsaBuddy: Assisting Mechanized Real-Time Schedulability Analysis with LLM-based Agents
url: http://arxiv.org/abs/2610.03796v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-01_03-29-09Z_ProsaBuddy_AssistingMechanizedReal_TimeSchedulabil.md
generated_at: 2026-10-05 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ProsaBuddy is an LLM-based agent system designed to reduce the substantial time and expertise required to construct mechanized real-time schedulability proofs within the Prosa framework in the Rocq proof assistant. By employing a ReAct loop combined with retrieval-augmented generation over the Prosa codebase and a subgoal-delegation architecture, ProsaBuddy decomposes complex lemmas into manageable subgoals handled by specialized subagents. Experimental evaluation on a benchmark drawn from real-time scheduling literature demonstrates that ProsaBuddy significantly outperforms existing state-of-the-art LLM-based Rocq proving agents and general-purpose coding agents such as OpenCode.

## Key Takeaways
- ProsaBuddy addresses a critical bottleneck in hard real-time system design: the high cost of constructing machine-checkable schedulability proofs in Rocq. Traditional pen-and-paper proofs risk errors that threaten safety in critical applications, and while the Prosa initiative provides a foundation for mechanized proofs, the expertise and time barrier has limited adoption. ProsaBuddy lowers this barrier by automating much of the proof-construction effort through LLM agents.
- The system architecture combines a ReAct reasoning loop with retrieval over the Prosa codebase, direct access to Rocq proof-checking tools, and optional human-written hints. This hybrid approach grounds the LLM in domain-specific formal methods knowledge while allowing human oversight when needed, making the system both autonomous and controllable.
- The subgoal-delegation architecture is a key innovation: rather than attempting to prove an entire lemma in one pass, ProsaBuddy decomposes it into subgoals and dispatches each to specialized subagents. This divide-and-conquer strategy mirrors how human experts tackle complex proofs and enables more reliable progress on intricate schedulability theorems.

## Context
This work sits at the intersection of formal verification, real-time systems engineering, and large language model agents. The broader AI research community has been exploring LLMs as tools for automated theorem proving and formal verification, but most prior efforts target general-purpose proof assistants or mathematical reasoning benchmarks. ProsaBuddy is notable for targeting a highly specialized domain—real-time schedulability analysis—where correctness is safety-critical and errors carry real-world consequences for embedded and cyber-physical systems. It demonstrates that domain-grounded retrieval and structured decomposition strategies can substantially outperform general-purpose coding agents in specialized formal verification tasks.

## Implications
For practitioners in safety-critical embedded systems and aerospace or automotive real-time software development, ProsaBuddy offers a practical pathway toward adopting mechanized schedulability proofs without requiring deep Rocq expertise, potentially reducing certification costs and improving assurance in hard real-time applications. For the AI research community, the subgoal-delegation and retrieval-grounded ReAct architecture provides a transferable template for building domain-specific proof assistants that combine LLM reasoning with formal tool verification. The results also suggest that general-purpose coding agents like OpenCode are insufficient for specialized formal verification tasks, reinforcing the need for domain-aware agent design in safety-critical software engineering workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03796v1)
