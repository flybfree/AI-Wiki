---
title: MARS: Multi-Specialist LLM Relay System for Competitive Programming
published: 2026-08-24T23:51:02Z
authors: Andrei Mikhailov, Mikhail Burtsev, Alsu Sagirova
url: http://arxiv.org/abs/2608.23918v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MARS: Multi-Specialist LLM Relay System for Competitive Programming

## Abstract
Large Language Models excel at code generation, yet competitive programming exposes a persistent failure mode: existing multi-agent pipelines distribute work over generic planner, coder, and debugger roles and delegate the choice of algorithmic technique to the backbone alone. We present MARS (Multi-Agent Relay of Specialized LLMs), a prompt-only framework in which each agent is a topic specialist---dynamic programming, graphs, strings, geometry, and so on---grounded by retrieval-augmented generation over an algorithm-theory corpus. Given a problem, retrieval selects a small team of relevant specialists; a starter writes an initial C++17 solution, and each subsequent turn runs the candidate against public examples in a sandbox, lets the active specialist keep, repair, or hand off the draft, and forwards a structured packet to the next specialist. A single infrastructure-fixer pass normalizes boilerplate at the end. On the CodeContests test split with Gemma 4, MARS reaches $0.624 \pm 0.006$ pass rate at $2.3$ recorded pipeline stages per task ($+14.4$ percentage points over direct prompting), closing most of the gap to CodeSIM ($0.731$) at $3.3{\times}$ lower wall-clock cost and substantially smaller variance in per-task token spend. The source code is available on GitHub: https://github.com/fckand/mars.

## Metadata
- **Published**: 2026-08-24T23:51:02Z
- **Authors**: Andrei Mikhailov, Mikhail Burtsev, Alsu Sagirova
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23918v1)