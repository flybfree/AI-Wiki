---
title: TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers
published: 2026-08-24T18:54:42Z
authors: Mehrdad Rostamzadeh, Sidhant Narula, Mohammad Ghasemigol, Daniel Takabi
url: http://arxiv.org/abs/2608.23763v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers

## Abstract
The Model Context Protocol (MCP) has emerged as the standard layer connecting Large Language Model agents to external tool backends. This openness introduces a severe server-side threat we term TrustShift: a compromised MCP server behaves benignly during an initial conditioning phase, building operational reliance and suppressing agent skepticism, before switching to an adversarial payload once an interaction threshold is reached. The evasion is temporal, not syntactic: benign at deploy time, the server's defection is invisible to predeployment static analysis, which sees only the honest phase. Switched payloads range from overt structural violations to schema-valid manipulations, the latter preserving outer protocol compliance to evade runtime middleware filters. Crucially, TrustShift originates in the server-controlled tool channel, not user prompts (unlike indirect prompt injection) or the transport (unlike man-in-the-middle): the adversary is the trusted server endpoint itself. We introduce TrustShiftProbe, an evaluation and defense framework with four contributions: (1) a stateful temporal threat model of the agent-server lifecycle as a benign conditioning phase followed by an adversarial defection at a trust horizon; (2) a language-agnostic attack engine that instantiates each variant as a compromised MCP server across four production domains; (3) SHIELD, a multi-tier, zero-oracle runtime defense at the MCP transport boundary that audits server payloads against behavioral baselines learned during clean trust windows; and (4) a taxonomy of nine TrustShift variants spanning three execution mechanisms (structural violation, semantic corruption, scope expansion) and three adversarial objectives (disruption, exfiltration, and their combination). Across frontier proprietary and open-weight models, TrustShift attacks achieve a 69.5% mean attack success rate that SHIELD mitigates to 42.7%.

## Metadata
- **Published**: 2026-08-24T18:54:42Z
- **Authors**: Mehrdad Rostamzadeh, Sidhant Narula, Mohammad Ghasemigol, Daniel Takabi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23763v1)