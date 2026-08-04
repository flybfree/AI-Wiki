---
title: GABench: A Comprehensive Benchmark for Evaluating LLM Agents on Graph Analysis Tasks
published: 2026-08-03T04:18:31Z
authors: Jiarui Tan, Zhongjian Zhang, YaBo Guo, Jiawei Liu, Yujie Xing, Muhan Zhang, Cheng Yang, Chuan Shi
url: http://arxiv.org/abs/2608.01684v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GABench: A Comprehensive Benchmark for Evaluating LLM Agents on Graph Analysis Tasks

## Abstract
Large language model (LLM) agents are increasingly capable of planning, using tools, and interacting with external environments. They are typically supported by harnesses, which manage state and coordinate multi-step execution. Graph analysis provides a promising setting for evaluating their agentic capabilities, because it requires agents to access data and execute operations in a graph environment. However, existing graph benchmarks for LLMs provide limited coverage of graph tasks and graph types, making it difficult to comprehensively evaluate LLM agents. Moreover, they typically formulate graph analysis as text-based question answering, where graph information is directly provided in the prompt, limiting the evaluation of end-to-end agentic capabilities. To address these limitations, we introduce GABench, a comprehensive benchmark for agentic graph analysis. GABench spans three graph types and covers four graph analysis task categories: graph retrieval, graph theory, graph machine learning, and graph open-ended question answering. GABench also provides 84 executable tools for accessing graph data and performing diverse graph operations. Building on these tools, we develop an agentic graph analysis task generation pipeline and construct 10,400 tasks with verifiable ground truth.Using GABench, we evaluate a range of frontier LLMs and agent harnesses. Our experiments reveal three key findings: (1) Existing LLM agents still struggle with complex graph analysis tasks. (2) Harness choice significantly affects performance, yet existing harnesses remain limited on complex graph tasks. (3) Graph analysis depends more on tool-call quality than quantity. Our findings provide practical insights into the development and evaluation of LLM agents for graph analysis.

## Metadata
- **Published**: 2026-08-03T04:18:31Z
- **Authors**: Jiarui Tan, Zhongjian Zhang, YaBo Guo, Jiawei Liu, Yujie Xing, Muhan Zhang, Cheng Yang, Chuan Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01684v1)