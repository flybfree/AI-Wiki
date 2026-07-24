---
title: Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving
url: http://arxiv.org/abs/2607.14387v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-15_22-02-03Z_Chat2Scenic_AnIterativeRAG_BasedFrameworkforScenar.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents Chat2Scenic, an iterative retrieval‑augmented generation framework that creates executable scenario scripts in a domain‑specific language for autonomous driving testing. The system combines a chatbot interface with Retrieval‑Augmented Generation (RAG) to align regulatory knowledge and DSL syntax, achieving higher compilation success than earlier approaches.

## Key Takeaways
- Chat2Scenic’s iterative RAG process allows users to refine scenario definitions interactively, improving the quality of generated scripts compared to one‑shot generation.  
- The framework reaches a 76.42 % Compilation Success Rate and 58.17 % Framework Accuracy, which are markedly higher than prior methods such as Retrieval Assemble (30.08 % CSR) or full script generation (16.26 % CSR).  
- An open benchmark of 123 scenarios from NHTSA and United Nations Vehicle Regulations validates the system’s performance across diverse regulatory domains.

## Context
Autonomous driving validation relies on generating compliant test scenarios, a task that is currently manual and error‑prone. Automating this process would reduce development time and increase consistency in simulation testing. This paper contributes to AI research by demonstrating how RAG can be applied iteratively to produce accurate DSL scripts for regulatory compliance.

## Implications
Chat2Scenic offers industry practitioners a practical tool to automate scenario creation, lowering costs and accelerating validation cycles. By integrating regulatory knowledge directly into generation, the framework supports scalable testing pipelines that meet safety standards across autonomous vehicle development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14387v1)
