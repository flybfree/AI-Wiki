---
title: Build or Adopt? Custom-Built vs. General-Purpose LLM Agent Harnesses for Automotive GUI Testing
published: 2026-10-24T12:32:16Z
authors: Arsham Gholamzadeh Khoee, Ruyu Fu, Jiaqi Wei, Ruikun Deng, Robert Feldt, Dhasarathy Parthasarathy, Yinan Yu
url: http://arxiv.org/abs/2610.33636v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Build or Adopt? Custom-Built vs. General-Purpose LLM Agent Harnesses for Automotive GUI Testing

## Abstract
As general-purpose LLM agent harnesses mature, organizations must decide whether to continue developing in-house systems or adopt existing alternatives. We study this decision at Volvo Group for GUI testing of Android-based in-vehicle infotainment (IVI) systems. We compare a production, custom-built harness with two general-purpose harnesses, Claude Code and OpenCode, keeping the tools, accessed through the Model Context Protocol (MCP), and the models the same. We evaluate the harnesses with up to four models on Volvo's IVI test cases and on open-ended tasks in public apps (Google Maps, Booking.com), and interview ten practitioners: developers, the product owner, and testers. On Volvo's stepwise IVI tests, general-purpose harnesses match the custom-built harness in success but vary more across runs. Their inference cost per task is 2.6-10.7 times higher, yet the engineering effort they save outweighs this: for a nightly IVI regression suite, total monthly cost, including engineering effort and inference, is 3-66% lower. On open-ended public-app tasks, they succeed more often, mainly because they recover better from incorrect actions. Interviews suggest that external advances can turn an in-house harness into technical debt even without deterioration. Adopting a general-purpose harness shifts maintenance from the agent loop to tools and instructions, but gives teams less control over what the model receives. Regardless of the harness, testers want to inspect the agent's actions and ensure that it follows the prescribed test scenario.

## Metadata
- **Published**: 2026-10-24T12:32:16Z
- **Authors**: Arsham Gholamzadeh Khoee, Ruyu Fu, Jiaqi Wei, Ruikun Deng, Robert Feldt, Dhasarathy Parthasarathy, Yinan Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33636v1)