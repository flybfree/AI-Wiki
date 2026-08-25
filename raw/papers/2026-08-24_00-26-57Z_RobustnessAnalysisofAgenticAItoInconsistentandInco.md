---
title: Robustness Analysis of Agentic AI to Inconsistent and Incomplete Tool Responses
published: 2026-08-24T00:26:57Z
authors: Jiachen Xu, Torben Bach Pedersen, Zhongming Yao, Xiaoyu Zhang, Yushuai Li
url: http://arxiv.org/abs/2608.22676v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Robustness Analysis of Agentic AI to Inconsistent and Incomplete Tool Responses

## Abstract
Robustness to a bad tool return means answering it in the way that return calls for, which depends on how the tool went wrong. A tool that has failed and a tool that returns a well-formed falsehood are different problems with different remedies. We ask whether the two already differ at the moment the return arrives. This is a qualitative pilot study: we score single decision points rather than running agents to completion. We inject controlled faults into a retail customer-service domain and read two channels off the model's log-probabilities: the likelihood of the returned content under the tool schema alone and under the whole trajectory, and its distribution over the legal actions, read for both shape and where the mass sits. An incomplete return is legible in every case, being improbable under the schema alone in a range no other condition enters, and it moves the mass toward the tools that re-read state wherever there is room to move. An inconsistent return leaves the schema channel untouched and registers in the likelihood comparison on the field whose true value the context already carries verbatim, not on the one whose contradiction runs through the domain policy. The action distribution gives each condition a distinct signature, but orders them by how far the return bears on the next action rather than by fault family. Recognition is therefore asymmetric: each condition is legible in some channel, and no channel is legible on all of them.

## Metadata
- **Published**: 2026-08-24T00:26:57Z
- **Authors**: Jiachen Xu, Torben Bach Pedersen, Zhongming Yao, Xiaoyu Zhang, Yushuai Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22676v1)