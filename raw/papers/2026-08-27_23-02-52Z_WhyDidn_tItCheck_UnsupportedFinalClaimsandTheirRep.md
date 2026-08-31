---
title: Why Didn't It Check? Unsupported Final Claims and Their Repair in Two Tool-Equipped Language Models
published: 2026-08-27T23:02:52Z
authors: Justin Bronder
url: http://arxiv.org/abs/2608.27768v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Why Didn't It Check? Unsupported Final Claims and Their Repair in Two Tool-Equipped Language Models

## Abstract
A language model with access to tools can commit to a final claim unsupported by the evidence it has seen, even when a single available tool call would resolve the uncertainty and its instructions explicitly forbid assumptions and guesses. We separate this failure into two precisely defined quantities: occurrence, how often the model makes an unsupported claim on its own, measured from the visible evidence and final claim without using the hidden correct answer; and conditional repair, how often those same naturally occurring unsupported claims are repaired when the missing evidence is supplied. On one fixed Qwen3-32B setup, 33 of 512 first responses to 256 new prompt templates ended with an unsupported established claim. We replayed each case from an exact copy of the state in which the claim occurred; within each matched replay, the alternative tool responses had the same structure and length and differed only in a one-character response code. Resolving evidence repaired 33 of 33 claims; a matched response carrying no useful information repaired 0 of 33. When the evidence supported the original answer, the model preserved 33 of 33, with no observed harm. In a separate experiment, on 64 cases where evidence was needed, an automatic checking rule added 21 evidence calls, corrected all 10 wrong unsupported claims, preserved the 11 that were correct by accident, and never changed a correct answer into a wrong one. On a fixed Gemma 4 setup using the same sampling settings, the model called the tool in all 512 first responses and never made an unsupported final claim, so conditional repair could not be measured for that setup. These results describe two local fixed model setups on two synthetic task families. They do not show how common this failure is in real-world deployments, nor that it reflects a general mechanism shared across models.

## Metadata
- **Published**: 2026-08-27T23:02:52Z
- **Authors**: Justin Bronder
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27768v1)