---
title: A Tree-Structured Approach for Phishing Template and Attacker Attribution Analysis
published: 2026-08-17T06:23:16Z
authors: Unai Agirre, Imanol Jerico, Felipe Castaño, Andrea Venturi, Francesco Zola
url: http://arxiv.org/abs/2608.16158v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Tree-Structured Approach for Phishing Template and Attacker Attribution Analysis

## Abstract
Phishing remains a persistent and evolving cybersecurity threat, with attack volumes reaching record levels. This growth is driven by the industrialization of phishing through widely available phishing kits and reusable templates, which enable cybercriminals to rapidly generate and deploy large numbers of fraudulent webpages. Although surface-level attributes may differ across these websites, their underlying structures often exhibit significant similarities. However, most existing defenses rely on reactive blocklists or supervised classification models that focus on individual phishing instances, limiting their ability to identify structural reuse and detect coordinated phishing campaigns. To address this limitation, this study investigates whether HTML structure can serve as a robust fingerprint for identifying phishing template reuse. We model webpages as Document Object Model (DOM) trees and extract structural features, optionally enriched with HTML tag-based content information. These representations are then clustered using unsupervised learning methods to group structurally similar webpages. Three clustering algorithms are evaluated and compared, while also analyzing how the depth of the extracted DOM-tree affects cluster formation and overall clustering performance. Finally, cluster quality is also evaluated both quantitatively and qualitatively, including a novel level-wise Jaccard Distance Score and manual inspection supported by visualization tools. Results demonstrate that structural representations of webpages can effectively reveal hidden similarities across phishing sites, enabling the detection of emerging and zero-day templates and supporting the analysis of coordinated phishing threats

## Metadata
- **Published**: 2026-08-17T06:23:16Z
- **Authors**: Unai Agirre, Imanol Jerico, Felipe Castaño, Andrea Venturi, Francesco Zola
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16158v1)