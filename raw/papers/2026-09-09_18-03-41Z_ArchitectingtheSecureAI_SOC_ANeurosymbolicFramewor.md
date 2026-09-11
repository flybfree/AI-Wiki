---
title: Architecting the Secure AI-SOC: A Neurosymbolic Framework for Pipeline Integrity and Threat Mitigation
published: 2026-09-09T18:03:41Z
authors: Anna Gazani, Spyridon Kounoupidis, Panagiotis Katsaros, Nikolaos Kekatos, Grigorios Tsoumakas, Georgios Koutidis
url: http://arxiv.org/abs/2609.10707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Architecting the Secure AI-SOC: A Neurosymbolic Framework for Pipeline Integrity and Threat Mitigation

## Abstract
The integration of Large Language Models (LLMs) into Security Operations Centers (SOCs) streamlines threat intelligence but introduces critical vulnerabilities, notably indirect prompt injection via log poisoning. Adversaries exploit this vector to execute multistep ``promptware'' kill chains by embedding malicious payloads within system logs to hijack the LLM's operational logic. Securing this pipeline presents a dichotomy: deterministic defenses are computationally efficient yet semantically blind, while purely neural evaluations introduce prohibitive latency and probabilistic flaws. To address this, we propose a novel neurosymbolic defense-in-depth architecture that ensures end-to-end pipeline integrity. The primary layer employs customized SIEM decoders as a deterministic pre-filter, performing immediate structural sanitization to neutralize volumetric padding and signature-based injections at the ingestion edge. The secondary layer leverages NeMo Guardrails to enforce strict semantic boundaries through self-checking validation on the structured SIEM alerts prior to LLM processing. Furthermore, the framework integrates a closed-loop telemetry system, providing critical Human-in-the-Loop (HITL) visibility into thwarted attacks directly within the SOC dashboard. We present a comprehensive experimental evaluation mapped to the MITRE ATLAS taxonomy, assessing the framework against diverse prompt injections. Our results demonstrate that this synergistic approach effectively dismantles the promptware kill chain - bounding LLM stochasticity with verifiable constraints, and delivering a resilient, highly observable defense mechanism for next-generation AI-SOCs.

## Metadata
- **Published**: 2026-09-09T18:03:41Z
- **Authors**: Anna Gazani, Spyridon Kounoupidis, Panagiotis Katsaros, Nikolaos Kekatos, Grigorios Tsoumakas, Georgios Koutidis
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.10707v1)