---
title: Evaluating and Preventing Security Smells in AI-Generated Ansible Code
published: 2026-08-25T07:15:16Z
authors: Pandu Ranga Reddy Konala, Vimal Kumar, David Bainbridge, Junaid Haseeb
url: http://arxiv.org/abs/2608.24962v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating and Preventing Security Smells in AI-Generated Ansible Code

## Abstract
AI coding assistants generate Infrastructure as Code, yet no work has examined whether this code meets security requirements. This matters because security smells in infrastructure code propagate to deployed systems, producing infrastructure that is insecure and untrustworthy. We evaluate 16 AI models generating Ansible roles for Apache Tomcat v10 and MongoDB v7, analysing 278 Ansible roles against CIS benchmarks. Without security guidance, all 16 AI models produced code containing security smells, resulting in vulnerable infrastructure that fails compliance verification and underperforms code written by human developers. We introduce an approach integrating Ansible best practices and CIS benchmarks into prompts through an extended CO-STAR framework, enabling security smell prevention during synthesis rather than detection after deployment. When this approach is applied, 4 out of 16 models generate compliant code, with the leading model achieving 95%-100% CIS compliance, a fourfold improvement over humans at 23%-43%, with overall code quality improving by 19%-49%. The remaining 12 models fail not because they cannot generate code but because they cannot follow instructions with multiple constraints. For capable models, the approach requires no retraining and can be adopted through system prompts.

## Metadata
- **Published**: 2026-08-25T07:15:16Z
- **Authors**: Pandu Ranga Reddy Konala, Vimal Kumar, David Bainbridge, Junaid Haseeb
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24962v1)