---
title: Losing the name before the box: measuring and repairing what narrow fine-tuning costs a detector outside its deployment vocabulary
published: 2026-09-29T00:36:03Z
authors: Trung Minh Bui, Jongsul Moon, YoungOuk Kim, Jung-Hoon Hwang, Dongin Shin
url: http://arxiv.org/abs/2609.36426v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Losing the name before the box: measuring and repairing what narrow fine-tuning costs a detector outside its deployment vocabulary

## Abstract
A detector pretrained on a broad corpus is fine-tuned on a narrow domain, its in-domain accuracy improves, and it ships. We ask what happens meanwhile to its coverage of objects the vocabulary never names, which in obstacle detection and inspection carry the risk. No in-domain test set holds an example of one. We give a longitudinal protocol: one pretrained checkpoint against its own fine-tuned descendants. It tracks held-out top-$K$ proposal coverage $C_τ$: of categories pretraining covered and the vocabulary omits, the share of boxes a detector's top $K$ regions still cover. The quantity is the open-world proposal literature's; the longitudinal reading is not. $C_τ$ falls while in-domain accuracy rises, on four architectures and three domains, by $5.12$ to $63.35$ points on boxes above $1024$ px$^2$. No in-domain number identifies the fall, and neither does detection average precision, which charges a missed and a misnamed box alike. On the one architecture scoring both, adaptation costs $87\%$ of the AP against a fifth of the coverage, and the naming goes first at all six depths of its freeze ladder, every run. What breaks is structured: three architectures sharing no pretraining run agree on which categories lose coverage, and those a model never learned do not lose any. A repair follows and needs no training: mixing a quarter of the pretrained state back, normalisation statistics included, raises coverage on every cell swept for at most $2.47$ points of in-domain accuracy. Seeing it costs one extra evaluation pass.

## Metadata
- **Published**: 2026-09-29T00:36:03Z
- **Authors**: Trung Minh Bui, Jongsul Moon, YoungOuk Kim, Jung-Hoon Hwang, Dongin Shin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36426v1)