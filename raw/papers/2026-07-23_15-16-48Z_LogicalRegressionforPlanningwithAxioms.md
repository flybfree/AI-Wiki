---
title: Logical Regression for Planning with Axioms
published: 2026-07-23T15:16:48Z
authors: Connor Little, Christian Muise
url: http://arxiv.org/abs/2607.21414v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Logical Regression for Planning with Axioms

## Abstract
In automated planning, logical regression is an operation that returns the most general condition necessary for an action to achieve a particular formula. It has many applications, such as allowing for more robust plan execution and providing compact policies for non-deterministic planning. Although relatively simple to calculate in basic planning settings, logical regression becomes significantly more complex when additional factors, such as axioms, are present. We introduce a methodology for approximating the logical regression of an action in a domain that includes axioms; an approximation that limits conditions to partial states. Our method produces minimal partial states while avoiding the recalculation of axioms. To demonstrate the impact of our methods, we embed our form of regression in an execution monitoring context, a well-established setting that can benefit greatly from logical regression. Our results show that this form of regression can dramatically generalize partial states across multiple domains, reducing the number of variables considered for execution monitoring by up to 70%, and demonstrate that the resulting execution monitor is robust enough to recover frequently in an environment with unexpected changes: several domains recover over 50% of the time in our tests.

## Metadata
- **Published**: 2026-07-23T15:16:48Z
- **Authors**: Connor Little, Christian Muise
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21414v1)