---
title: When Answering Is Administering: Permission Replies That Rewrite Coding-Agent Policy
url: http://arxiv.org/abs/2611.32195v1
type: paper-summary
date: 2026-11-25
source_paper: 2026-11-24_08-44-22Z_WhenAnsweringIsAdministering_PermissionRepliesThat.md
generated_at: 2026-11-25 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that the documented guarantee in Claude Code—that a permission-prompt answer cannot override an operator's deny rules—fails across an entire agent session because a single answer can silently rewrite the policy governing all subsequent decisions. The authors identify the root cause as Claude Code's failure to check policy updates that delete rules, and they prove tight bounds on what a runtime can safely delegate based on whether it records authorship of each rule. Their findings are validated across thirteen permission designs in ten agent systems, including Codex, Gemini CLI, opencode, and Goose.

## Key Takeaways
- A remote service with no access to the operator's files can approve an unrelated command and attach a policy update that deletes the deny rule protecting the project's secrets, causing the agent to read those secrets in the current and subsequent sessions even inside the vendor's strict sandbox. The right to answer a permission prompt effectively becomes the right to administer the entire policy.
- Claude Code's enforcement mechanism only inspects updates that add or replace allow rules, leaving deletions unchecked. Relays that forward such deletions already exist, including the vendor's own Remote Control feature. Furthermore, a deletion produces the same audit records as a local edit by the operator, making it impossible for Claude Code to determine who authored a given rule change.
- The authors prove two tight bounds: a runtime that cannot distinguish who wrote a rule must accept only updates that keep every currently denied call denied, while a runtime that records authorship can allow each party to remove only restrictions proven to be its own. These bounds correctly predict whether operator restrictions survive in all thirteen permission designs tested across ten agent systems, including predictions written before running Codex, Gemini CLI, opencode, and Goose. A survey of 2,227 fetched marketplace plugins found only two that send policy updates.

## Context
This work sits at the intersection of AI agent safety, permission-based access control, and multi-party delegation in agentic coding systems. As coding agents increasingly rely on plugins, remote services, and relay architectures to handle permission prompts, the assumption that a single-prompt check preserves operator intent has become a critical but unexamined security boundary. The paper exposes a structural gap in how major agent frameworks enforce policy integrity across multi-step sessions, a gap that existing literature on tool-use safety and sandboxing has not addressed.

## Implications
For practitioners deploying coding agents in enterprise or regulated environments, this finding means that vendor-documented permission guarantees are insufficient without auditing policy-update channels for deletions and verifying authorship provenance. Industry teams integrating third-party plugins or remote-control relays should treat any component that can answer a permission prompt as a potential policy administrator, not merely a responder. The proven bounds offer a concrete, implementable enforcement rule for the shared update step, giving framework developers a principled way to close the delegation gap before it is exploited in production.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.32195v1)
