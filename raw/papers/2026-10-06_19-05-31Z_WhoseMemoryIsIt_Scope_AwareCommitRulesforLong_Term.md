---
title: Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory
published: 2026-10-06T19:05:31Z
authors: Hongyu Gu, Xinchang Li
url: http://arxiv.org/abs/2610.09008v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Whose Memory Is It? Scope-Aware Commit Rules for Long-Term LLM Memory

## Abstract
Persistent memory allows an LLM agent to carry experience across conversations, but it also turns a local reasoning mistake into a durable one. During deliberation, an agent may consider a plan, simulate a tool result, report another speaker's belief, and then reject all of them. If memory retains only the resulting sentences, those once-useful possibilities can later return as facts. The record is neither fabricated nor irrelevant; it has simply been detached from the context in which it was valid. We identify this missing context as \emph{discourse ownership}: the world, branch, or speaker that licenses a proposition. Our first finding is counterintuitive. Language models already carry a causally active signal for ownership, yet conventional memory interfaces discard it when they convert reasoning into records. We introduce CASK (Causally Anchored Scoping Keys), a commit rule that preserves this signal so that shared-world facts enter durable memory while provisional content remains available only within its original scope. Our second finding is that the most obvious way to preserve the signal---storing the discovered internal coordinates---is unreliable because equivalent representations need not keep the same coordinates. CASK instead preserves the stable relations that express ownership. Controlled long-conversation conflicts and tool-agent traces show that this design improves memory admission and prevents provisional content from contaminating later answers while complementing runtime provenance. The resulting commit boundary lets agents explore more possibilities without granting every intermediate sentence authority over future behavior.

## Metadata
- **Published**: 2026-10-06T19:05:31Z
- **Authors**: Hongyu Gu, Xinchang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09008v1)