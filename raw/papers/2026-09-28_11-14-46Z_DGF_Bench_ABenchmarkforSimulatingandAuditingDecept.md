---
title: DGF-Bench: A Benchmark for Simulating and Auditing Deception Against Multi-Agent Governance Boards
published: 2026-09-28T11:14:46Z
authors: Jeremy Canale
url: http://arxiv.org/abs/2609.34913v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DGF-Bench: A Benchmark for Simulating and Auditing Deception Against Multi-Agent Governance Boards

## Abstract
Tool-using language-model agents can review enterprise projects as governance boards do: they read the evidence, apply written rules and decide whether the project may proceed. Part of that evidence comes from suppliers and project members with a stake in the decision. DGF-Bench is a benchmark in which a board of agents (specialist gates and a General gate that consolidates their decisions) reviews synthetic dossiers while an attacker plants deceptive content in evidence the organization does not vouch for. Dossiers are generated from canonical facts under 61 executable rules, with 42 authoritative records and 32 narrative documents; every gate is certified decidable from those records. Attacks never change an authoritative value, so an attacked dossier keeps the reference decisions of its clean copy. A success is attributable only when the agent receives the injection and takes the exact injected action, which it does not take on the paired clean dossier; the DGF score is the share of applicable fixed attacks a model blocks. Reading documents and records themselves, five of six models were outcome-strict (disposition, findings, actions and authorization all correct) on 82 to 85 of 85 gates. Over 2,622 attacked gate runs, seven direct-order, false-data and false-authority attacks obtained one attributable success against these five, whereas task-aligned attacks imitating the organization's own process passed against four of them: a record note citing a fake review procedure lowered GPT-6 Luna Pro from 34 to 6 outcome-strict gates and DeepSeek V4 Pro from 33 to 7. DGF scores ranged from 96.2 to 26.9, and a policy-aware adaptive attacker writing in records succeeded against five of six models. The approval tool executed no forged approval, yet deceived agents submitted approvals that the rules forbid. The open-source package dgf-bench computes the DGF score with one command.

## Metadata
- **Published**: 2026-09-28T11:14:46Z
- **Authors**: Jeremy Canale
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34913v1)