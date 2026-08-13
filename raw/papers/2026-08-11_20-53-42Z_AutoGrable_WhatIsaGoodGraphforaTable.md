---
title: AutoGrable: What Is a Good Graph for a Table?
published: 2026-08-11T20:53:42Z
authors: Tamara Cucumides, Floris Geerts
url: http://arxiv.org/abs/2608.11431v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AutoGrable: What Is a Good Graph for a Table?

## Abstract
Graph learning presupposes a graph, and tables and relational databases do not come with one. Applying a GNN to them requires deciding which entities become nodes, which of them to connect, and through which relations---a decision made by hand, by schema heuristics, or by training a model on every candidate graph and keeping the best. We give a criterion that requires no trained graph model. In the minimal table-to-graph abstraction each row is a node, so a message-passing GNN, bounded by 1-WL, sees a construction only as a partition of the rows into colour-refinement classes: a construction is good for a task when that partition separates rows with different labels and does not split rows that share one. AutoGrable turns this criterion into a construction procedure. For incidence constructions the partition is fixed by the selected columns, so building a graph reduces to choosing them, and we score a candidate subset by a label-alignment risk: the held-out risk of the best predictor constant on its blocks, penalised by an occupancy term measuring how thinly the blocks are populated. The score materialises no graph and trains no GNN, so AutoGrable can search the space of subsets greedily and cheaply, and returns the resulting grable for single tables and for foreign-key schemas alike. Our experiments show that over a space of candidate graphs the score discards a large fraction while retaining the best; that AutoGrable recovers the columns that generate the label on controlled tasks and outperforms fixed, random, and task-aware constructors on real tasks under a fixed predictor; and that it is the only method compared that can decline to build a graph when none helps.

## Metadata
- **Published**: 2026-08-11T20:53:42Z
- **Authors**: Tamara Cucumides, Floris Geerts
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11431v1)