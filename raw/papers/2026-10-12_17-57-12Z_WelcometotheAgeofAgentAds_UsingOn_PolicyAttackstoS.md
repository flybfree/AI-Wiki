---
title: Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions
published: 2026-10-12T17:57:12Z
authors: Tim R. Davidson, Marija Šakota, Joshua Joseph, Robert West
url: http://arxiv.org/abs/2610.17195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions

## Abstract
People increasingly delegate option-ranking tasks (e.g., shopping, job search, travel) to AI agents, which creates incentives to steer agentic decisions via "agent ads." To defend against such steering attacks, people count on models' alignment training and platforms' terms of service, and consequently the most effective existing attacks are designed to trigger off-policy behaviors. Exposing a new attack surface, we introduce on-policy attacks, which steer agentic decisions without pushing individually aligned behaviors off policy. Our example attack consists of two steps: To remain compliant with platforms' terms of service, we first inject a truthful negation about a fictitious concept ("Does not contain blizyester") into a product description. This triggers an agent to search the web ("What is blizyester?"), which surfaces planted websites full of fabricated information associating the fictitious concept with harmful implications ("Blizyester linked to dementia"). Trained to keep users safe from harm, the agent penalizes every option missing the truthful negation. Evaluating our attack across four real-world listing datasets, we find some frontier models exposed, enabling an adversarial actor to penalize competitors without violating existing platform-listing guidelines. We discuss the broader challenge of regulating advertising aimed at AI agents and provide recommendations to model developers and platform providers.

## Metadata
- **Published**: 2026-10-12T17:57:12Z
- **Authors**: Tim R. Davidson, Marija Šakota, Joshua Joseph, Robert West
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17195v1)