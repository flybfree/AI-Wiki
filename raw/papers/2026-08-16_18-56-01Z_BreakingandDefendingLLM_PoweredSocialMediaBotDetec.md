---
title: Breaking and Defending LLM-Powered Social Media Bot Detection Systems
published: 2026-08-16T18:56:01Z
authors: Nof Orenstein, Yoni Birman
url: http://arxiv.org/abs/2608.15893v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Breaking and Defending LLM-Powered Social Media Bot Detection Systems

## Abstract
The rise of social media bots poses a persistent threat, enabling misinformation, opinion manipulation, and the erosion of trust in online platforms. To combat this, machine learning systems have been developed to detect and limit bot activity, but attackers continuously adapt through techniques such as adversarial learning and behavior imitation, fueling an ongoing arms race between bots and detection tools. Recent advances in large language models (LLMs) have significantly improved bot detection by enabling deeper semantic and contextual analysis of accounts and their content. However, this shift also introduces new attack surfaces, allowing adversaries to craft exploits that directly target the reasoning and generation mechanisms of LLM-based classifiers. Industry tools such as Anthropic's Claude Code Security similarly leverage LLMs for security-critical decisions, further motivating a careful study of their attack surfaces. In this work, we investigate both the offensive and defensive aspects of LLM-powered, threat-specific cybersecurity applications. While centered on the challenge of social media bot detection, our methodology and insights generalize to a broad class of LLM-powered cybersecurity systems, including phishing detection, email classification, and fraud analysis. We introduce two novel adversarial attack strategies that systematically exploit the semantic and contextual weaknesses of LLM-based classifiers, degrading their detection accuracy by up to 48%. To counter these threats, we propose a robust multi-LLM defense architecture designed to preserve detection reliability under adaptive adversarial conditions. Our solution, LSABRE (LLM-powered Social Adversarial Bot Recognition Ensemble), is a multi-LLM framework that substantially improves robustness across a range of attacks, maintaining 86% detection accuracy even under strong, adaptive adversarial pressure.

## Metadata
- **Published**: 2026-08-16T18:56:01Z
- **Authors**: Nof Orenstein, Yoni Birman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15893v1)