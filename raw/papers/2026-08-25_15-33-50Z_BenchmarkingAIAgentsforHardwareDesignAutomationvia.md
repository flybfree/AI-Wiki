---
title: Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling
published: 2026-08-25T15:33:50Z
authors: Leonardo Liparulo, Francesco Pierri
url: http://arxiv.org/abs/2608.26199v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Benchmarking AI Agents for Hardware Design Automation via MCP Tool Calling

## Abstract
We ask whether AI agents powered by locally deployed large language models can reliably automate expert-defined hardware design workflows in an industry-realistic tool-calling setting. In these environments, engineers issue repetitive, dependency-ordered operations---such as creating components, adding ports, and wiring connections---through specialised tools. Confidentiality constraints on component specifications and naming conventions often preclude hosted proprietary APIs, motivating the use of locally deployed models. To study this setting, we build a Model Context Protocol (MCP) server that reproduces the state and dependency logic of a proprietary hardware design tool used in embedded system development and construct a benchmark covering single-operation edits, multi-step dependency chains, invalid requests, misspelled prompts, and multi-server tool contexts. We evaluate seven open-source models comparing pipeline choices including system prompts, tool-description detail, context scope, and single-agent versus multi-agent architectures. Results show that strong models can achieve near-complete expected-call coverage on the benchmarked workflows, but reliability depends strongly on both task structure and agent configuration. Comprehensive tool descriptions consistently reduce failures, few-shot prompting can cause severe inaction for some models, cumulative context harms constrained models, and multi-agent decomposition helps weak workers or long sessions at the cost of additional calls. These findings provide practical guidance for deploying local LLM agents in stateful hardware design environments.

## Metadata
- **Published**: 2026-08-25T15:33:50Z
- **Authors**: Leonardo Liparulo, Francesco Pierri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26199v1)