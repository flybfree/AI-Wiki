---
title: DisCTI: Who Needs to Know Timely? Automated Sector-Aware Cyber Threat Intelligence Dissemination
published: 2026-08-28T06:22:48Z
authors: Fajar Wijitrisnanto, Alsharif Abuadbba, Yansong Gao, Nan Wu
url: http://arxiv.org/abs/2608.27967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DisCTI: Who Needs to Know Timely? Automated Sector-Aware Cyber Threat Intelligence Dissemination

## Abstract
The timely dissemination of cyber threat intelligence (CTI) is critical for organizations to mount swift and effective incident response. When valid CTI is delivered to the right sector at the right time, identical attacks can often be contained or mitigated. However, today's rapidly expanding CTI landscape overwhelms analysts, who must sift through massive and heterogeneous feeds. Existing platforms such as the Malware Information Sharing Platform (MISP) provide sector tagging features (e.g., energy, finance, government), but in practice, these remain largely unmapped (98% of events are left uncategorized). This lack of automated and timely sector mapping severely limits the operational value of shared intelligence, leaving organizations that belong especially to the critical information infrastructure sector exposed.   To address this gap, we formulate sector-targeted CTI dissemination as a multilabel classification problem. Leveraging deep field knowledge of CTI structures and sector-specific threat patterns, we construct a novel data set of 872 sector-labelled CTI events from a threat intelligence platform (TIP). We then apply BERT, a transformer-based model, to automate the mapping of CTI events to sectors. Using the structured threat information expression (STIX) format for cross-platform interoperability, our approach achieves a macro-averaged F1-score of 0.89 at a Hamming loss of 0.055 on the custom dataset, i.e. 94.5% of individual sector-label assignments are correct. These results not only demonstrate the feasibility of sector-aware, automated CTI dissemination but also highlight how embedding expert field knowledge into machine learning design fills a crucial gap in the threat intelligence pipeline, enabling faster and context-relevant defensive action.

## Metadata
- **Published**: 2026-08-28T06:22:48Z
- **Authors**: Fajar Wijitrisnanto, Alsharif Abuadbba, Yansong Gao, Nan Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27967v1)