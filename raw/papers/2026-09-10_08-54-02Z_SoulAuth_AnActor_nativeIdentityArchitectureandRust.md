---
title: SoulAuth: An Actor-native Identity Architecture and Rust Reference Implementation for Humans and Long-lived AI Actors
published: 2026-09-10T08:54:02Z
authors: Kun Yuan, Harold Wang, Echo Li, Egusi Gui, Kiki Hu, Lucas Luo, Magnus Hu
url: http://arxiv.org/abs/2609.11258v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SoulAuth: An Actor-native Identity Architecture and Rust Reference Implementation for Humans and Long-lived AI Actors

## Abstract
As AI systems move from transient model invocations toward long-lived actors that persist across credentials, clients, sessions, and runtime instances, identity infrastructure must answer a basic question: where should the canonical continuity boundary be placed? This paper introduces Actor-native Identity and presents SoulAuth, an open-source Rust reference implementation for Humans and long-lived AIActors. We argue that any subject that must persist under its own identity and remain independently attributable should have an ActorIdentity that is not replaced by an Account, Credential, Client, AuthSession, IdentityBinding, or runtime instance. SoulAuth therefore treats Humans and long-lived AIActors as first-class identity subjects while keeping authentication distinct from downstream authority. Methodologically, we use a Philosophical Engineering approach that translates conceptual analysis of subjecthood into identity objects, invariants, lifecycle semantics, system responsibilities, implementation boundaries, and inspectable conformance evidence. Evaluation against the fixed SoulAuth v0.1.0 artifact shows that the implementation realizes core boundaries including Human/AIActor first-class identity status, Client/Actor separation, and Authentication/Authority separation, while gaps remain in unified Credential modeling and historical attribution anchored to ActorIdentity. We therefore report partial, not full, architecture conformance.

## Metadata
- **Published**: 2026-09-10T08:54:02Z
- **Authors**: Kun Yuan, Harold Wang, Echo Li, Egusi Gui, Kiki Hu, Lucas Luo, Magnus Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11258v1)