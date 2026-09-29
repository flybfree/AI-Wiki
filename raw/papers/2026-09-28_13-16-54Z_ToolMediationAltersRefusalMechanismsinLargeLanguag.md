---
title: Tool Mediation Alters Refusal Mechanisms in Large Language Models
published: 2026-09-28T13:16:54Z
authors: Abel Rodríguez, Giuseppe Garofalo, Lieven Desmet, Vera Rimmer
url: http://arxiv.org/abs/2609.35117v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tool Mediation Alters Refusal Mechanisms in Large Language Models

## Abstract
Large language models (LLMs) are increasingly deployed with access to external tools, yet harmful tool-mediated interactions are less likely to be refused when compared to regular conversational ones. As this change in refusal behavior remains underexplored, we investigate its underlying mechanisms across a diverse set of open-weight language models. We find that information about the harmfulness of a request remains strongly encoded in the model's representations and transfers across conversational and tool-mediated inputs. Evidence from representation geometry and neuron-level analysis further indicates that the two interaction modes systematically distribute harm-related computation differently. Crucially, while conversational inputs can be refused at relatively low levels of perceived harmfulness, tool-mediated inputs remain permissive until harmfulness crosses a substantially higher effective refusal threshold. Moreover, tool-mediated refusal is also more brittle: progressively weakening the refusal computation disrupts tool-mediated refusal at lower intervention strengths than conversational refusal, even when benign capabilities remain intact. Together, our findings indicate that tool mediation does not simply reduce the internal perception of harm, but instead impacts its conversion into refusal. Overall, this suggests tool-mediated environments may intrinsically reduce robustness of models to harmful requests, and that conventional safety evaluations may not fully transfer to LLM agents.

## Metadata
- **Published**: 2026-09-28T13:16:54Z
- **Authors**: Abel Rodríguez, Giuseppe Garofalo, Lieven Desmet, Vera Rimmer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35117v1)