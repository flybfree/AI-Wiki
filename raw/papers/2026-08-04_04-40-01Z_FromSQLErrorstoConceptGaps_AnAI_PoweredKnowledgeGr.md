---
title: From SQL Errors to Concept Gaps: An AI-Powered Knowledge Graph Analytics Platform for Personalized Feedback
published: 2026-08-04T04:40:01Z
authors: Abdulrahman AlRabah, Weijian Zhou, Xing Gao, Abdussalam Alawini
url: http://arxiv.org/abs/2608.03118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From SQL Errors to Concept Gaps: An AI-Powered Knowledge Graph Analytics Platform for Personalized Feedback

## Abstract
This innovative practice full paper describes an AI-powered knowledge graph platform that connects SQL errors to conceptual gaps in undergraduate and graduate database systems courses. Students learning Structured Query Language (SQL) frequently struggle with semantic errors that reflect conceptual misunderstandings rather than syntax mistakes. A query may execute yet return incorrect results due to gaps spanning related concepts; misusing NATURAL JOIN in place of an explicit subquery reflects intertwined misunderstandings of JOIN, GROUP BY, and HAVING. Autograding systems detect correctness but provide surface-level feedback without connecting errors to the conceptual structure of the course. Educational knowledge graph research has shown the value of structured concept representations for curriculum analysis and adaptive learning, but these approaches have not been applied to diagnosing SQL misconceptions from student submissions. We present a platform that automatically extracts course concepts and relations from instructional materials, links them to student submission traces through a graph database, and classifies errors at the concept level. We evaluate the platform across two database systems courses at two universities, one using real student submissions and one using simulated submissions, through an expert study with five participants and an automated evaluation using an LLM as a judge. Results show that 95.7% of extracted nodes were rated as at least somewhat valid and 63.8% of triplets were rated fully correct. Expert feedback confirmed that the generated graphs align with instructor mental models and that mapping errors to course concepts provides actionable diagnostic insight; evaluating impact on student learning remains future work.

## Metadata
- **Published**: 2026-08-04T04:40:01Z
- **Authors**: Abdulrahman AlRabah, Weijian Zhou, Xing Gao, Abdussalam Alawini
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03118v1)