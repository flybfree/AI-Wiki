---
title: Evaluating and Preventing Security Smells in AI-Generated Ansible Code
url: http://arxiv.org/abs/2608.24962v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-25_07-15-16Z_EvaluatingandPreventingSecuritySmellsinAI_Generate.md
generated_at: 2026-08-26 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether AI-generated Ansible code for Apache Tomcat and MongoDB meets security requirements by evaluating 16 models against CIS benchmarks, finding that all models without guidance contain security smells. Using a CO‑STAR framework integrated with best practices and CIS rules, four models produce compliant code, the top model achieving near‑perfect compliance, outperforming human developers.

## Key Takeaways
- All 16 AI models generate Ansible roles containing security smells when no security guidance is provided, leading to vulnerable infrastructure that fails compliance checks.
- The CO‑STAR framework combined with CIS benchmarks enables prevention of security smells during code synthesis, resulting in four compliant models and a ninefold improvement over human performance.
- Model quality improves significantly, ranging from 19% to 49%, indicating that prompt engineering can boost AI-generated infrastructure code.

## Context
AI coding assistants are increasingly used to produce Infrastructure as Code, but existing research lacks systematic assessment of security implications. This work addresses the gap by applying CIS benchmarks directly to AI synthesis, highlighting the need for proactive security checks in automated CI/CD pipelines.

## Implications
For practitioners, integrating such frameworks into system prompts can reduce manual review effort and improve compliance without retraining models. The findings suggest that prompt engineering is a viable path to secure AI‑generated infrastructure, encouraging broader adoption of security‑aware AI tools across DevOps practices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24962v1)
