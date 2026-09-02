---
title: Solaris: Towards Interfaces That Are Generated, Not Coded
published: 2026-09-01T06:10:49Z
authors: Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem, Michal Geyer, Kfir Goldberg, Elad Richardson, Diego Alarcón, Alejandro Alvarez, Cole Garry, Anastasis Germanidis, Tenaya Goldsen, Corina Gurau, Robin Kahlow, Joel Kwartler, Kathleen Lewis, Alejandro Matamala Ortiz, Eugene McMahon, Thon Prom, Sarah Saltonstall-Wurm, Jamie Umpherson, Hudson Yeo
url: http://arxiv.org/abs/2609.00776v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Solaris: Towards Interfaces That Are Generated, Not Coded

## Abstract
Digital interfaces are traditionally implemented through intermediate representations such as code, requiring their appearance and behavior to be specified in advance. We introduce Solaris, an interface world model that instead generates an interactive UI directly, frame by frame, in response to user actions. Solaris treats mouse interactions as conditioning signals and autoregressively synthesizes the resulting visual state at interactive speeds. To enable real-time generation while maintaining visual coherence over extended interactions, we combine autoregressive frame generation with few-step distillation and training on the model's own outputs. A language model complements the visual world model by interpreting user intent and specifying how interactions should affect the generated environment, separating high-level reasoning from visual rendering. By generating both the appearance and behavior of an interface dynamically, Solaris enables open-ended interactions that need not be explicitly programmed in advance. We view interface world models as a step toward a new paradigm for software, where interfaces are generated and adapted continuously around user intent rather than implemented as fixed collections of predefined states and

## Metadata
- **Published**: 2026-09-01T06:10:49Z
- **Authors**: Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem, Michal Geyer, Kfir Goldberg, Elad Richardson, Diego Alarcón, Alejandro Alvarez, Cole Garry, Anastasis Germanidis, Tenaya Goldsen, Corina Gurau, Robin Kahlow, Joel Kwartler, Kathleen Lewis, Alejandro Matamala Ortiz, Eugene McMahon, Thon Prom, Sarah Saltonstall-Wurm, Jamie Umpherson, Hudson Yeo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00776v1)