---
title: Nameless Tokenization: A Lossless Tokenizer-Level Defense Against Control-Token Forgery in Open-Weight LLMs
published: 2026-09-15T11:00:03Z
authors: Kisu Yang, Yoonna Jang, Heuiseok Lim
url: http://arxiv.org/abs/2609.16984v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Nameless Tokenization: A Lossless Tokenizer-Level Defense Against Control-Token Forgery in Open-Weight LLMs

## Abstract
Open-weight language models publish the strings their chat templates use to mark turns, roles and tool results, which the tokenizer maps back to the reserved identifiers the model obeys. Anyone who controls text in a prompt can therefore write a turn boundary indistinguishable from one the serving stack wrote. We audit 256 deployed chat tokenizers. All are forgeable, and the flag usually recommended as a fix leaves 56.6% forgeable because it misses the tool and reasoning markers agent systems rely on. We propose nameless tokenization, which leaves the control entries with a reserved identifier and no surface string, so the content encoder cannot emit one and message content reaches the model unaltered. Across five tokenizer families it reproduces the standard token stream exactly on attack-free data and lifts accuracy on a probe of delimiter-bearing text from 8.5% to 59.9%, where sanitizers lose it. Separating a delimiter's appearance from its identifier shows the identifier matters little against a bare task instruction, but carries most of a forged tool result and most of any forged turn once the system message tells the model to treat user content as data.

## Metadata
- **Published**: 2026-09-15T11:00:03Z
- **Authors**: Kisu Yang, Yoonna Jang, Heuiseok Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16984v1)