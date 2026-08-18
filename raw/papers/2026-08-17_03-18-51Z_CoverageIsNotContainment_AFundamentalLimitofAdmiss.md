---
title: Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval
published: 2026-08-17T03:18:51Z
authors: Prashant Kumar Pathak, Tarun Kumar Sharma
url: http://arxiv.org/abs/2608.16044v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval

## Abstract
Retrieval-augmented generation (RAG) answers a question by retrieving passages from a vector store and trusting them as context, so anyone who can add documents can try to steer the answer. A recent, appealing defense filters poisoning at ingestion, rejecting any document that behaves like a hub. We show it -- and every ingestion-time filter -- is defeated by a coordinated adversary that injects a handful of individually unremarkable documents which together surround one target query and seize its top-k (on BGE-large / BEIR, m=10 documents take 10/10; 9.9/10 on a live HNSW index). The attack is not theoretical. Realized as ordinary fluent text and run end-to-end through a BGE-large + HNSW + Qwen2.5-7B pipeline, it makes the generator emit the attacker's planted claim in 88% of targets, versus 0% without the injection. And no admission-time defense stops it: at ingestion an attack cone is geometrically identical to a legitimate niche upload, so -- measuring this directly -- the strongest trained classifier, given every feature and thousands of examples, separates the two no better than chance, catching 4.2% of attacks at a 1% false-positive rate. We prove this limit for the entire class of ingestion-time statistics (any decision from documents and reference queries alone), and it reproduces -- and worsens -- across two corpora and five encoders. The one signal that separates an attack from legitimate niche ingestion -- a query's demand -- is invisible before retrieval, which is also the escape: a retrieval-time detector that observes demand catches 100% of the attacks at the same 1% false-positive rate. Coverage of the query space by an admission gate is not containment of coordinated poisoning; robust defense must move past the front door, to demand.

## Metadata
- **Published**: 2026-08-17T03:18:51Z
- **Authors**: Prashant Kumar Pathak, Tarun Kumar Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16044v1)