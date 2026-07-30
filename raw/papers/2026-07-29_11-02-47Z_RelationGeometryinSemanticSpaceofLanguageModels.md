---
title: Relation Geometry in Semantic Space of Language Models
published: 2026-07-29T11:02:47Z
authors: Zhihan Cao, Hiroaki Yamada, Simone Teufel, Tatsuya Hiraoka, Kentaro Inui, Hitomi Yanaka, Takenobu Tokunaga
url: http://arxiv.org/abs/2607.26762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Relation Geometry in Semantic Space of Language Models

## Abstract
When it comes to generating vector representations of words, current language models are achieving high-quality results. However, what is not known is the extent to which knowledge about semantic relations is represented in the geometry of the semantic spaces created in this way. In order to answer this question, we study the relation geometry of such semantic spaces from three perspectives. We first examine whether words standing in a particular relation to a target word~(called relata) occupy the same region in semantic space, and whether the regions corresponding to different relations are distinct from each other. We then verify to what extent semantic spaces reflect certain well-known properties of relations, such as symmetry, asymmetry, and transitivity. Finally, we consider which information about the target words and relata is more important for relation geometry: their surface forms, or their contexts. We conduct experiments on six semantic relations using causal, masked, and diffusion language models. The results show that relata in asymmetric relations relatively clearly occupy a distinct region in semantic space. Asymmetric relations' properties are only moderately well encoded in the semantic space, yet better than those of symmetric ones. Furthermore, when considering the question which information source has the strongest impact on results amongst the models we evaluated, we find that lexical information tends to be more important for the causal language model, whereas contextual information is more important for the masked and diffusion language models. Our results empirically show that relation geometry is not equally well-represented for all relations in semantic space, suggesting that there is a difference in how well semantic relations might be learned from distributional information alone.

## Metadata
- **Published**: 2026-07-29T11:02:47Z
- **Authors**: Zhihan Cao, Hiroaki Yamada, Simone Teufel, Tatsuya Hiraoka, Kentaro Inui, Hitomi Yanaka, Takenobu Tokunaga
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26762v1)