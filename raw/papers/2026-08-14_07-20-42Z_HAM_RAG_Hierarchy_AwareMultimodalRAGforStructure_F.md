---
title: HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved Generation
published: 2026-08-14T07:20:42Z
authors: Yin Li, Ziyang Hu, Zhiyu Guo, Xiangyu Liu, Wenbin Li, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Fugee Tsung
url: http://arxiv.org/abs/2608.14032v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved Generation

## Abstract
Existing multimodal RAG methods often flatten structured documents into isolated text and image units, weakening the source organization and local text-image logic needed for faithful evidence selection and placement. We propose HAM-RAG, a Hierarchy-Aware Multimodal RAG framework for structure-faithful interleaved generation. HAM-RAG uses document hierarchy as a grounding signal across retrieval and generation, contextualizing textual and visual evidence and preserving source position and local text-image relations in the prompt. We further introduce HAM-Bench, covering Wukong, Wiki, arXiv, and Recipe across game walkthroughs, web pages, scientific papers, and step-wise recipe documents. Across multiple backbones, HAM-RAG improves the main multimodal average by 17.3% over the strongest non-hierarchical baseline. On Wukong, HAM-RAG improves Img-CBS by 24.2% over the strongest non-hierarchical baseline, demonstrating substantially better local text-image alignment. The main experiments and ablation study together demonstrate that document hierarchy is a key grounding signal for faithful image selection, placement, and local text-image alignment. These findings highlight the value of hierarchy-aware grounding for reliable multimodal assistants that generate answers faithful to the source organization, procedural structure, and local text-image evidence of structured documents, such as technical manuals, maintenance guides, and industrial SOPs. The code is available at https://github.com/MCCodeAI/HAM-RAG.git.

## Metadata
- **Published**: 2026-08-14T07:20:42Z
- **Authors**: Yin Li, Ziyang Hu, Zhiyu Guo, Xiangyu Liu, Wenbin Li, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Fugee Tsung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14032v1)