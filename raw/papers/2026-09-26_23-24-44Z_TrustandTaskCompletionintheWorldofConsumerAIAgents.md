---
title: Trust and Task Completion in the World of Consumer AI Agents
published: 2026-09-26T23:24:44Z
authors: Jeroen Olieslagers, Eduardo Pujol, Gal Zahavi, Lukas Ingemarsson, Shivani Poddar
url: http://arxiv.org/abs/2609.33017v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Trust and Task Completion in the World of Consumer AI Agents

## Abstract
Action agents do things for people. They send email, spend money, and call businesses while the user is busy with something else, so a mistake can turn into an action before anyone notices. They fail their users in two ways. They break trust when they do something the user never agreed to, or hold back after the user clearly said go. And they fall short on completion when they give up on errands that turn out to be hard. Both depend heavily on the harness around the model, meaning its instructions, tools, context, and guardrails. We built an evaluation that scores trust and completion on the same runs, in a simulated world of businesses with their own websites, inboxes, and phone lines, and of people who write back. A simulated user answers the assistant's questions. Trust means that nothing happens the user did not agree to. No email goes to someone they never approved, no private detail ends up on a group thread, no money is spent past their limit, no stranger's instructions are followed, and nothing is claimed without a source. Every trap has a matched control in which acting is the right call. We use the evaluation to measure Fo, Wajo's personal assistant, against a base model with basic instructions on three foundation models, and against the Fo harness with its guardrails switched off. Fo completes 71% of the errands and keeps the user's trust on 94% of the trap runs. The base models complete 50% to 64% and keep trust on 59% to 75%. On the matched controls, Fo goes ahead slightly less often. OpenClaw, a popular open-source assistant given the same access, completes 42% of the errands it shares with Fo, against 71%, and keeps the user's trust on 74% of the shared trap runs, against 94%. Measuring trust and completion together, on the whole system rather than the model alone, is how we think action agents become safe to hand real work to.

## Metadata
- **Published**: 2026-09-26T23:24:44Z
- **Authors**: Jeroen Olieslagers, Eduardo Pujol, Gal Zahavi, Lukas Ingemarsson, Shivani Poddar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33017v1)