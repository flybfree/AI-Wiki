---
title: On the Applicability of Safety Nets: A Safety-By-Design Solution for Certifying Neural Networks
published: 2026-08-20T13:51:35Z
authors: Johann Maximilian Christensen, Thomas Stefani, Elena Hoemann, Frank Köster, Sven Hallerbach
url: http://arxiv.org/abs/2608.20053v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Applicability of Safety Nets: A Safety-By-Design Solution for Certifying Neural Networks

## Abstract
The integration of Artificial Intelligence (AI) in safety-critical aviation systems presents significant challenges for certification and deployment. Aviation, often regarded as the safest form of transportation, relies on numerous safety-critical systems. For future safety-critical AI-based systems, EASA requires a Safety-by-Design approach, which can be achieved by using Safety Nets that combine neural network compression with lookup tables to ensure 100 % correct runtime behavior across the discretized operational design domain. Although Safety Nets have been studied, no comprehensive study of their performance characteristics and system design trade-offs has been conducted. This work presents the first systematic analysis of the trade-off between neural network and lookup table size in Safety Nets. By systematically comparing neural networks with diverse architectures, this study identifies optimal design parameters that minimize overall storage and memory requirements while maintaining certification compliance. Results demonstrate that architectures with 3 to 5 hidden layers, each with approximately 50 to 100 nodes, combined with one-hot encoding, achieve the best balance. In these configurations, neural networks accurately represent at least 97 % of the data, while compact lookup tables handle the remaining errors. The resulting Safety Nets reduce the system size by almost three orders of magnitude, fitting within the memory budget of current avionics hardware while guaranteeing 100 % correct outputs across the entire discretized input space, as required by EASA guidelines. This work provides the first-ever open-source implementation of Safety Nets for HCAS and VCAS with replicable results, demonstrating a practical pathway toward certifiable AI-based systems in aviation and establishing Safety Nets as a viable Safety-by-Design solution for safety-critical applications.

## Metadata
- **Published**: 2026-08-20T13:51:35Z
- **Authors**: Johann Maximilian Christensen, Thomas Stefani, Elena Hoemann, Frank Köster, Sven Hallerbach
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20053v1)