---
title: The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems
published: 2026-08-04T06:50:49Z
authors: Ankur Sharma, Deep Shah
url: http://arxiv.org/abs/2608.03214v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Agent Operating System (AOS): A Reference Operating Architecture for Distributed Agentic Systems

## Abstract
Large language models have transformed artificial intelligence from isolated prediction services into components of long-running, distributed systems that reason, invoke tools, retrieve external state, delegate tasks, and act on behalf of users and organizations. The surrounding ecosystem has responded with agent frameworks, workflow engines, model-serving platforms, memory systems, communication protocols, and observability tools. These technologies improve execution, but they do not provide a stable, implementation-independent operating architecture for governing intent, selecting capabilities, preserving authority across delegation, controlling uncertainty, coordinating runtime behavior, and reconstructing why consequential actions occurred. This paper proposes the Agent Operating System (AOS), a vendor-neutral reference operating architecture for distributed agentic systems. AOS contains two internal planes: a Control & Governance Plane responsible for intent, policy, trust, authority, confidence, auditability, observability, and human oversight; and a Runtime & Coordination Plane responsible for agent lifecycle, workflow coordination, model and tool routing, context and memory coordination, scheduling, traffic management, and runtime assurance. Platform services, Linux or Windows, container runtimes, and physical infrastructure remain outside the AOS boundary and are integrated through explicit interfaces. The paper specifies AOS concepts, invariants, interface objects, optimization objectives, deployment profiles, and reliability responsibilities. It also identifies tradeoffs and unresolved research questions. AOS is not presented as a replacement for existing frameworks or infrastructure; it is proposed as the operating architecture through which heterogeneous components can be composed into governable, reliable, observable, and interoperable agentic systems.

## Metadata
- **Published**: 2026-08-04T06:50:49Z
- **Authors**: Ankur Sharma, Deep Shah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03214v1)