---
title: Rolling With Resistance: Preference-Optimized LLM Counselors Can Trade Goal Persistence for Relational Attunement in Motivational Interviewing
published: 2026-07-30T20:16:03Z
authors: Weiying Chen, Junlong Shen, Zhexuan Tang
url: http://arxiv.org/abs/2607.28814v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rolling With Resistance: Preference-Optimized LLM Counselors Can Trade Goal Persistence for Relational Attunement in Motivational Interviewing

## Abstract
In Motivational Interviewing (MI), a client's sustain talk (arguments for the status quo) calls for the counselor to roll with resistance, a move that can fail in two opposite ways: capitulation (abandoning the change agenda to preserve rapport) or confrontation (arguing or directing, overriding the client's autonomy). We introduce a two-axis evaluation of counselor responses, anchored in the Motivational Interviewing Treatment Integrity (MITI) code, Goal Persistence (GP) and Relational Attunement (RA), yielding a four-quadrant framing in which rolling with resistance is high on both, and we ask whether penalizing one failure through preference optimization teaches rolling with resistance or provokes its opposite. From the expert-annotated AnnoMI corpus we build topic-disjoint Direct Preference Optimization data whose preference sets differ only in which failure is rejected, using on-policy negatives. An automatic judge, validated against AnnoMI's expert labels and rechecked by trained human coders, scores blind pairwise win-rates against each base under a firewall in which disjoint model families generate, label, and judge. Across three aligned instruction models spanning the Qwen and Llama families, penalizing confrontation reliably lowers goal persistence below parity, on every base and in every seed run, a robust cost, whereas the attunement gain is base-dependent, present on two of the three bases but absent on the third. Penalizing capitulation is inert, because these models rarely capitulate on-policy, so the trade is gated by each base's failure profile. A prompt-only control raises attunement without the goal-persistence cost, locating the cost in the optimization rather than in attunement itself.

## Metadata
- **Published**: 2026-07-30T20:16:03Z
- **Authors**: Weiying Chen, Junlong Shen, Zhexuan Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28814v1)