---
title: SPIDES: Information-Flow Control for Browser Agents
url: http://arxiv.org/abs/2610.24277v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-16_22-12-45Z_SPIDES_Information_FlowControlforBrowserAgents.md
generated_at: 2026-10-19 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SPIDES is a security framework for LLM-driven browser agents that replaces the traditional Same-Origin Policy with a fine-grained information-flow control mechanism. By gating primitive browser actions (typing, clicking, navigating) on confidentiality and integrity labels propagated from element-level HTML annotations, SPIDES provides provable security guarantees against prompt injection attacks and unintended data exfiltration, achieving a 0% attack success rate by design while maintaining high task completion rates and agent autonomy.

## Key Takeaways
- The authors argue that restoring the Same-Origin Policy for browser agents is neither sufficient nor necessary for security: a same-origin public sink can still leak private data, and legitimate cross-origin workflows require authorized flows. Instead, they propose element-level HTML confidentiality and integrity annotations as the foundation for a more granular security model that tracks information flow at the level of individual page elements rather than entire origins.
- SPIDES enforces security by masking untrusted and confidential content from the agent's context and blocking unauthorized flows through policy gates on primitive actions. Critically, these security guarantees hold independently of the underlying language model, meaning the protection is architectural rather than model-dependent, making it robust against adversarial prompt injection regardless of model behavior.
- The evaluation uses MicroNet, a purpose-built closed ecosystem of 28 interlinked websites with element-level ground-truth labels and paired benign/adversarial tasks, enabling a common threat model for comparing SPIDES against baseline defenses. SPIDES achieves 0% attack success rate by design while retaining high task completion rate and autonomy, outperforming state-of-the-art baselines on both security and utility metrics.

## Context
This paper addresses a rapidly growing concern in the AI and web security communities: as LLM-driven browser agents become capable of autonomously navigating, reading, and interacting with arbitrary web content, they effectively collapse the security boundaries that decades of web security engineering established. The erosion of the Same-Origin Policy in agentic browsing creates a novel attack surface where prompt injection and data exfiltration can occur across origins with the user's full authority, a problem that existing sandboxing and CSP mechanisms were never designed to handle. SPIDES represents a shift from perimeter-based security to information-flow control, a technique well-established in operating systems and programming language security but newly applied to the browser-agent setting.

## Implications
For practitioners building browser agents for enterprise automation, customer service, or personal assistance, SPIDES offers a path to deploy autonomous agents on the open web without requiring users to trust the underlying model's judgment about what content is safe to process. For the broader field, the work demonstrates that information-flow control can be integrated into browser agent architectures in a way that preserves agent autonomy and task utility, suggesting that future agent frameworks should incorporate security annotations at the HTML element level rather than relying solely on model-level guardrails. The open-source release of MicroNet and SPIDES provides a reproducible benchmark that other researchers can use to evaluate and compare agentic security defenses under a standardized threat model.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24277v1)
