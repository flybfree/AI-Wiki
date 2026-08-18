---
title: PLSQLBench: Benchmarking LLM Systems for Executable Procedural Database Programming
published: 2026-08-16T21:03:21Z
authors: Marianne Menglin Liu, Leonid Boytsov, Daniel W. Peterson, Pramuditha Perera, Rongguang Wang, Sai Ashish Somayajula, Syed Hamza Rafique, Rohit Saini, Shubham Pathak, Sujeeth Bharadwaj, Tao Sheng, Graham Horwood, Fahad Shah, Ankan Bansal, Sujith Ravi, Dan Roth
url: http://arxiv.org/abs/2608.15931v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PLSQLBench: Benchmarking LLM Systems for Executable Procedural Database Programming

## Abstract
We present PLSQLBench, to our knowledge the first benchmark for evaluating whether LLMs can write executable PL/SQL programs, with correctness measured through execution-based tests. Existing LLM evaluations largely target general-purpose code generation or declarative text-to-SQL, leaving procedural database programming underexplored. PLSQLBench contains 2,865 instances: 2,594 single-turn tasks and 271 multi-turn conversations spanning 978 turns. The benchmark combines complex schema-grounded tasks over enterprise-style Spider 2 databases, simpler schema-grounded tasks derived from Spider, and MBPP-derived procedural problems, covering varying levels of database grounding and procedural complexity. Experiments with eight LLMs reveal recurring difficulties in schema grounding, PL/SQL dialect fidelity, procedural control flow, exception handling, and cross-turn consistency. Tool-augmented LLM agents improve performance on several schema-grounded evaluations, although substantial gaps remain. These results highlight procedural database programming capabilities not directly assessed by conventional code generation or text-to-SQL benchmarks. Our code is available at https://github.com/oracle-samples/plsqlbench.

## Metadata
- **Published**: 2026-08-16T21:03:21Z
- **Authors**: Marianne Menglin Liu, Leonid Boytsov, Daniel W. Peterson, Pramuditha Perera, Rongguang Wang, Sai Ashish Somayajula, Syed Hamza Rafique, Rohit Saini, Shubham Pathak, Sujeeth Bharadwaj, Tao Sheng, Graham Horwood, Fahad Shah, Ankan Bansal, Sujith Ravi, Dan Roth
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15931v1)