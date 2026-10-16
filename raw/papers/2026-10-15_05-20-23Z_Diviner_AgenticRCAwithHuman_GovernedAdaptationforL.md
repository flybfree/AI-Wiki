---
title: Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure
published: 2026-10-15T05:20:23Z
authors: Pradipta Ghosh, Gaurav Mitra, Shripad Nadgowda, Akshil Shah, Junyu Liu, Canturk Isci, Syamla Bandla, Xinyao Hu, Onkar Deshpande, Anik Dasgupta
url: http://arxiv.org/abs/2610.21281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diviner: Agentic RCA with Human-Governed Adaptation for Large-Scale Infrastructure

## Abstract
Root-cause analysis (RCA) in large-scale distributed systems is challenging because a single symptom can cross service, data, configuration, compute, and organizational boundaries. Responders must assemble incomplete evidence and coordinate experts who hold different parts of the causal path. Generic language-model agents do not solve this problem through tool access alone: they can use stale or mistimed context, interpret failed queries as absent symptoms, report unsupported system state, and overload observability services designed for human-paced use.   We present Diviner (Domain-Informed Verifiable Incident Navigation through Evidence and Review), an agentic RCA system operating at Meta and organized around a four-stage reliability lifecycle. Encode combines a large corpus of reviewed incidents with service-owner expertise to produce scoped, versioned skills, workflows, typed tools, and an incident knowledge graph. Execute uses an adaptive Lead and context-isolated workers to apply relevant knowledge to point-in-time evidence and maintain evidence-linked hypotheses. Evaluate compares saved investigation trajectories with responder-reviewed outcomes to measure exact cause, useful direction, and Groundedness. Adapt uses recurring gaps and on-call feedback to derive focused operational- knowledge updates, admitting them only after replay, quality checks, and owner approval.

## Metadata
- **Published**: 2026-10-15T05:20:23Z
- **Authors**: Pradipta Ghosh, Gaurav Mitra, Shripad Nadgowda, Akshil Shah, Junyu Liu, Canturk Isci, Syamla Bandla, Xinyao Hu, Onkar Deshpande, Anik Dasgupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21281v1)