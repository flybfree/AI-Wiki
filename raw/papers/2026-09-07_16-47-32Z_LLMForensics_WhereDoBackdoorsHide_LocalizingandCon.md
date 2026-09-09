---
title: LLM Forensics: Where Do Backdoors Hide? Localizing and Controlling Trigger Mechanisms with Sparse Autoencoders
published: 2026-09-07T16:47:32Z
authors: Wissam Antoun, Francis Kulumba, Théo Lasnier, Benoît Sagot, Djamé Seddah
url: http://arxiv.org/abs/2609.07746v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM Forensics: Where Do Backdoors Hide? Localizing and Controlling Trigger Mechanisms with Sparse Autoencoders

## Abstract
Even though backdoors in LLMs have been a growing concern, their inner workings are still under heavy scrutiny. Trigger-based backdoors are easy to define behaviorally, a rare input that makes the model switch to a chosen response pattern, but the mechanism between triggers and their responses is less clear. We study this mechanism in a controlled, harmless language-switching setting, where fixed trigger sequences make 1B and 8B language models continue English prompts in French or German. For this, we train sparse autoencoders (SAEs) across layers and transformer components, then compare triggered prompts with translation and pretraining controls to identify trigger-relevant feature directions. We show how SAE features separate triggered prompts from controls with near-perfect F1, but features that detect the trigger do not necessarily control the behavior. In intervention tests, attention and MLP features often fire reliably on triggered prompts, making them good detectors, but ablating them rarely suppresses the language switch and activating them rarely induces it. In contrast, residual-stream features can suppress triggered generation when ablated, and some selected features can induce target-language continuations without the trigger. In short, these token-trigger mechanisms decompose into distinct SAE feature directions, with separate features for trigger detection, residual-stream propagation, and later language tracking. This role-level decomposition is the part most likely to transfer to other trigger-based backdoors, even when the payload, layers, or circuit locations differ.

## Metadata
- **Published**: 2026-09-07T16:47:32Z
- **Authors**: Wissam Antoun, Francis Kulumba, Théo Lasnier, Benoît Sagot, Djamé Seddah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07746v1)