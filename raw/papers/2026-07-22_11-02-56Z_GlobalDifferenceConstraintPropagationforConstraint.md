---
title: Global Difference Constraint Propagation for Constraint Programming
published: 2026-07-22T11:02:56Z
authors: Lucas Kletzander, Jip J. Dekker, Andreas Schutt, Peter J. Stuckey
url: http://arxiv.org/abs/2607.20022v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Global Difference Constraint Propagation for Constraint Programming

## Abstract
Difference constraints of the form $x - y \leq d$ are well studied, with efficient algorithms for satisfaction and implication, because of their connection to shortest paths. Finite domain propagation algorithms, however, typically do not make use of these algorithms, and treat each difference constraint as a separate propagator. Propagation does guarantee completeness of solving, but can be needlessly slow. In this paper we describe how to build a (bounds consistent) global propagator for difference constraints that treats them all simultaneously. SAT modulo theory solvers have included theory solvers for difference constraints for some time. While a theory solver for difference constraints gives the basis of a global difference constraint propagator, we show how the requirements on the propagator are quite different. Crucially, we show how to explain propagations by a global difference constraint propagator, in order to use it within a lazy clause generation solver. We give experiments showing that treating difference constraints globally can substantially improve on the standard propagation approach.

## Metadata
- **Published**: 2026-07-22T11:02:56Z
- **Authors**: Lucas Kletzander, Jip J. Dekker, Andreas Schutt, Peter J. Stuckey
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20022v1)