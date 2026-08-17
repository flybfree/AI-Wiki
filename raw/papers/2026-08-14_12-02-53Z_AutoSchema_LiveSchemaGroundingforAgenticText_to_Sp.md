---
title: AutoSchema: Live Schema Grounding for Agentic Text-to-Sparql over Heterogeneous Knowledge Graphs
published: 2026-08-14T12:02:53Z
authors: Yiming Zhang, Koji Tsuda
url: http://arxiv.org/abs/2608.14228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoSchema: Live Schema Grounding for Agentic Text-to-Sparql over Heterogeneous Knowledge Graphs

## Abstract
Life science knowledge graphs make large collections of structured data available through SPARQL, but each resource uses its own schema, identifiers, and links. TogoMCP helps language model agents query these resources by providing curated Metadata Interoperability Exchange files. Creating and maintaining these files still requires language model assisted drafting, validation, and manual review. We study \emph{live schema grounding}, where an agent obtains the schema evidence needed for a question directly from the current endpoints. We present \textsc{autoschema}, a general framework for live schema grounding that requires no training. It inspects live schemas, maps entity names in a question to graph identifiers, explores relation paths, and finds possible connections between resources during iterative query construction. We use TogoMCP as our main comparison framework. We evaluate \textsc{autoschema} on Resource Focused Biomedical KGQA, Multi Resource Biomedical KGQA, Longitudinal Biomedical Semantic QA over BioASQ Task B, and Chemistry Knowledge Graph Transfer to a previously undocumented RDF graph. \textsc{autoschema} improves mean factoid accuracy over TogoMCP in the biomedical KGQA tasks and gives consistent gains in the longitudinal BioASQ evaluation. It also reduces iteration budget exhaustion and uses fewer tool calls on average in the core evaluation. The transfer study gives preliminary evidence that live schema grounding can support irregular and previously unseen graphs without first creating a curated schema file.

## Metadata
- **Published**: 2026-08-14T12:02:53Z
- **Authors**: Yiming Zhang, Koji Tsuda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14228v1)