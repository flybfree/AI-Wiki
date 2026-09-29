---
title: Timeline-Bench: Evaluating Agents on Realistic Video-Editing Tasks, from Raw Footage to Final Cut
published: 2026-09-28T13:28:17Z
authors: Gunin Gupta, Nirmit Arora, Pavan Kalyan Tankala
url: http://arxiv.org/abs/2609.35143v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Timeline-Bench: Evaluating Agents on Realistic Video-Editing Tasks, from Raw Footage to Final Cut

## Abstract
AI agents increasingly carry out long-horizon professional work, but their evaluations rarely require a finished creative deliverable. To this end, we introduce Timeline-Bench, a benchmark of 56 real video-editing tasks, each asking an agent to turn raw production material into a finished video. Tasks range from selecting dialog takes and shaping interview footage into a story to cutting commercials from product shots, voiceovers and graphics. Every task provides a brief, source assets, a container and a set of tests. A task is resolved when the output passes every test. The tests check the delivery format, the content and the brief's explicit requirements, and include a quality test calibrated on 2,582 blind judgments by 43 video editors. We evaluate 16 agents that pair frontier models with coding-agent harnesses such as Codex, Claude Code and OpenCode. The best, GPT-6 Astra in Codex with curated editorial guidance, resolves only 15 of the 56 tasks (26.8%), and the average agent resolves 14.0%. Human editors prefer the reference edit in 83.5% of judgments. Most unresolved runs (562 of 771) fail only the quality test: agents perceive footage through stills and transcripts and check their renders for defects, not craft. We release the tasks, verifier and per-run results at https://timelinebench.tensortest.com.

## Metadata
- **Published**: 2026-09-28T13:28:17Z
- **Authors**: Gunin Gupta, Nirmit Arora, Pavan Kalyan Tankala
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35143v1)