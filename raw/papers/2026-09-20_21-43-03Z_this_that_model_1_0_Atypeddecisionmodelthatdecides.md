---
title: this-that-model-1.0: A typed decision model that decides in 30 ms, for a millionth of a cent
published: 2026-09-20T21:43:03Z
authors: Zehua Cheng, Wei Dai, Jiahao Sun
url: http://arxiv.org/abs/2609.23886v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# this-that-model-1.0: A typed decision model that decides in 30 ms, for a millionth of a cent

## Abstract
Software delegates more of its branches to models every year: which queue a ticket enters, whether a command is safe to run, whether a claim clears without a person. What the program needs back is not prose. It is one of n declared options and a number it can threshold. Today that costs a round trip to a frontier model -- hundreds of milliseconds, a per-token bill, and a parser -- for a question that is usually a conjunction of three clauses. this-that-model-1.0 is a 2B-parameter typed decision model. Its answer is read directly from the hidden state at a designated position and restricted to the option set the caller declared, so no text is generated, nothing can be malformed, and every question in a request is answered in the same forward pass. It decides in 30.9 ms on one laptop GPU and generates zero output tokens doing it, where a frontier API call costs 8758 ms and the hosted systems that answer these questions well spend between 21 and 212 generated tokens per question thinking first, billed for every one. It sustains 32 decisions per second on one consumer GPU and never lets the state leave the machine. On a third party's recorded cohort of 68 decision questions, on their inputs and their wording, it scores 0.941 with a Brier score of 0.042, against 0.765 and 0.133 for the hosted service Jev on the same items. One pass of our 42-family internal suite takes 32 seconds and 0.000217 USD of electricity; the most accurate hosted model we measured needs 155.2 minutes and 10.636 USD. We also report where it loses. On multi-step arithmetic, which a single forward pass cannot carry intermediate results through, it scores 0.560 against their 0.98 to 1.00, and a targeted second training round improved the five task families it was written for and transferred to none of the other 13. The model is open-sourced in https://huggingface.co/flock-io/this-that-model-1.0

## Metadata
- **Published**: 2026-09-20T21:43:03Z
- **Authors**: Zehua Cheng, Wei Dai, Jiahao Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23886v1)