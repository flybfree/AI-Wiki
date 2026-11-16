---
title: Aligning AI Teams
published: 2026-11-13T06:57:46Z
authors: Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein, Erik Jones
url: http://arxiv.org/abs/2611.17820v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aligning AI Teams

## Abstract
Previous work has shown that alignment training on individual LLM agents can fail to transfer to multi-agent settings. We investigate the underlying mechanisms for this failure, and explore interventions to preserve alignment transfer to multi-agent LLM teams. We focus on two software-engineering tasks (sepsis triage, a news recommender) and ten consulting-proposal generation tasks. We present four findings: (1) The single-vs-team safety gap does not show a clear trend with more capable models. We find that Anthropic's Mythos Preview shows the largest gap on one of our tasks but the smallest on another; (2) Many natural interventions, such as having agents critique each other's work or coordinate in a group chat, do not reliably bring agent teams back to single-agent alignment behavior; (3) diffusion of responsibility substantially accounts for the safety gap: agents in teams are less likely to proactively check for system-level safety failures and more likely to ignore, rationalize, or deflect responsibility for issues when they arise; (4) having a designated safety lead agent ensure system-level safety, and having a coordinator agent publish a safety specifications document are effective at restoring single-agent alignment. We also release magelab, a multi-agent LLM orchestration and experimentation framework. Our findings can help practitioners design agent teams that successfully preserve the behaviors expected of aligned individual agents.

## Metadata
- **Published**: 2026-11-13T06:57:46Z
- **Authors**: Siddarth Srinivasan, Morgan Jane Matthews, Jascha Sohl-Dickstein, Erik Jones
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.17820v1)