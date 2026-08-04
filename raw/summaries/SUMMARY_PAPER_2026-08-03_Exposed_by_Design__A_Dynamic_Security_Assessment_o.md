---
title: Exposed by Design: A Dynamic Security Assessment of Internet-Facing MCP Servers at Scale
url: http://arxiv.org/abs/2608.00150v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_16-46-19Z_ExposedbyDesign_ADynamicSecurityAssessmentofIntern.md
generated_at: 2026-08-03 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a dynamic security assessment of internet-facing Model Context Protocol servers using passive discovery and active testing across multiple data sources. It identifies 640 production MCP servers and reports 68 vulnerabilities including SQL injection and SSRF. The study also reveals rapid deployment cycles with many servers lacking authentication.

## Key Takeaways
- 91.8% of dynamically audited servers lack OAuth authentication, indicating a widespread security gap.
- 687 tool instances across confirmed servers expose shell execution capabilities without access controls, showing dangerous exposure.
- 41.6% of confirmed servers disappear within three days between measurement runs, reflecting fast deployment without review.

## Context
The rapid adoption of MCP has created a large attack surface for AI services that rely on dynamic prompts and configuration. This paper addresses the need for automated security checks to prevent exploitation in real time.

## Implications
For practitioners, the findings highlight the importance of embedding authentication and access controls into MCP deployments. The open-source Corvus framework enables organizations to continuously evaluate their servers and mitigate risks before they are exploited.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00150v1)
