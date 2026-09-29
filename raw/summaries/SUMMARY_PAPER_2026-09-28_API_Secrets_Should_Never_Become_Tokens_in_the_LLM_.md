---
title: API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary
url: http://arxiv.org/abs/2609.33371v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_08-55-16Z_APISecretsShouldNeverBecomeTokensintheLLM_sVocabul.md
generated_at: 2026-09-28 21:54
model: qwen3.6-35b-a3b
---

## Summary
This paper analyzes the security risks associated with API credentials in tool-using LLM agents, demonstrating that credential hygiene shifts from a storage problem to an execution-security challenge when secrets enter data pipelines via prompts or configurations. The authors formalize a threat chain where prompt injection and excessive agency can convert passive disclosure into unauthorized actions, and they evaluate a vault-mediated execution architecture that separates model decision-making from authentication. Experimental results show this approach effectively prevents credential leakage across multiple vectors, though the study concludes that centralized custody is necessary but insufficient without complementary controls like least privilege and rotation.

## Key Takeaways
- Tool-using LLM agents introduce execution-security risks where credentials cross authentication boundaries into data pipelines, persisting in conversation history, logs, memory, and error payloads; prompt injection and excessive model agency can exploit this exposure to perform unauthorized actions beyond the intended scope.
- The proposed vault-mediated architecture requires the LLM to select only a connector identifier while a trusted request boundary supplies actual authentication credentials; controlled black-box experiments confirmed that this design successfully kept credentials absent from environment values, headers, filesystems, and third-party services across diverse control domains.
- Centralized credential custody does not guarantee security on its own, as the study reported negative results where misconfigured connectors failed to satisfy provider contracts despite vault mediation; therefore, effective agent security requires a defense-in-depth approach including least privilege, deterministic action authorization, human approval, telemetry redaction, and regular rotation.

## Context
The rise of autonomous LLM agents capable of interacting with external APIs necessitates a reevaluation of traditional secret management practices, as the dynamic nature of agent execution creates novel attack surfaces for credential exposure. This work addresses critical gaps in AI security research by formalizing how agentic behaviors transform static secrets into runtime vulnerabilities, contributing to the broader discourse on securing AI supply chains and ensuring safe tool use in production environments.

## Implications
Security practitioners must adopt vault-mediated execution patterns that decouple model inference from authentication mechanisms to mitigate the risk of credential leakage in agent workflows, moving beyond simple secret storage solutions. Organizations implementing LLM agents should enforce strict operational controls alongside technical architectures, prioritizing least-privilege access, deterministic authorization policies, and continuous monitoring to address the inherent risks of granting autonomous agency to language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.33371v1)
