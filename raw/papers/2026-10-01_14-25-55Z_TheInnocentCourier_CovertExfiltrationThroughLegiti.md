---
title: The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching
published: 2026-10-01T14:25:55Z
authors: Alessandro Pegoraro, Daryan Merx, Phillip Rieger, Ahmad-Reza Sadeghi
url: http://arxiv.org/abs/2610.01768v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Innocent Courier: Covert Exfiltration Through Legitimate LLM Web Fetching

## Abstract
With the increasing capabilities of Large-Language-Models (LLMs) and LLM-based agents, users are increasingly using them to solve everyday problems, such as answering e-mails or providing programming support. Existing work has extensively investigated security and privacy risks, such as prompt injections and the disclosure of sensitive data to chatbot providers. While various solutions were developed to address these risks, including input structuring to prevent prompt injections or deploying local LLMs to avoid sharing confidential data with chatbot operators, LLMs also pose the risk of leaking confidential data to third parties.   In this paper, we demonstrate with LLMLeak a novel attack vector where malicious software that runs locally but cannot communicate directly with the internet abuses LLMs to establish a covert channel. While inputs that instruct the LLM to send data directly via generated code are easy to detect and network libraries are typically restricted, LLMLeak relies only on the LLM's tool to fetch websites for further information. A malicious software component on the client side embeds a secret into a URL. It presents the referenced website as providing information required for a benign task, such as migrating a software library. When the LLM accesses the URL, the attacker receives the encoded secret through an attacker-controlled DNS or web server. We perform an extensive evaluation on eleven open-parameter models, observe an attack success rate of 79.7%, and also conduct a case study on real-world chatbots, demonstrating the relevance of LLMLeak.

## Metadata
- **Published**: 2026-10-01T14:25:55Z
- **Authors**: Alessandro Pegoraro, Daryan Merx, Phillip Rieger, Ahmad-Reza Sadeghi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01768v1)