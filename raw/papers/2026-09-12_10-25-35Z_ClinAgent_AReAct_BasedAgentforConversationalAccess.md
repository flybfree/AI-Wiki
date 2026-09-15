---
title: ClinAgent: A ReAct-Based Agent for Conversational Access to Clinical Trial Information
published: 2026-09-12T10:25:35Z
authors: Antonino Vaccarella, Riccardo Cantini, Domenico Talia, Paolo Trunfio, Marianna Talia, Rosamaria Lappano, Marcello Maggiolini
url: http://arxiv.org/abs/2609.13860v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ClinAgent: A ReAct-Based Agent for Conversational Access to Clinical Trial Information

## Abstract
Querying clinical trial registries remains a manual and error-prone process, requiring researchers to navigate large volumes of semi-structured data without support for natural language interaction or cross-source synthesis. To address this, we introduce ClinAgent, a conversational system based on agentic Retrieval-Augmented Generation (RAG) that enables clinicians and researchers to query clinical trial information in plain language and receive grounded, up-to-date responses across multi-turn interactions. The system centers on a Large Language Model (LLM) agent following the ReAct paradigm, which iteratively reasons over queries, selects among a set of integrated tools, and refines its actions based on intermediate outputs. These tools include a ClinicalTrials.gov search interface, a PubMed module, and a Python-based analyzer operating on a locally cached structured dataset of clinical trials. We evaluate the system using a three-phase framework assessing operational effectiveness, planning quality, tool-use efficiency, and expert qualitative judgments, comparing three LLM backends: Gemini 3.0 Flash and two variants of DeepSeek V3.2 (thinking and non-thinking). Results reveal complementary strengths, with DeepSeek (thinking mode) excelling in planning quality, while Gemini achieves the highest overall performance and strongest expert ratings. Overall, our findings highlight the potential of agentic AI systems to improve the accessibility and synthesis of clinical trial information, supporting more efficient and user-centered biomedical research workflows.

## Metadata
- **Published**: 2026-09-12T10:25:35Z
- **Authors**: Antonino Vaccarella, Riccardo Cantini, Domenico Talia, Paolo Trunfio, Marianna Talia, Rosamaria Lappano, Marcello Maggiolini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13860v1)