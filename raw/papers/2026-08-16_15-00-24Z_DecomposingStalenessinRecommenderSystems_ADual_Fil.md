---
title: Decomposing Staleness in Recommender Systems: A Dual-Filter Framework for Supersession and Decay
published: 2026-08-16T15:00:24Z
authors: Di Bai, Feng Han, Zhenwei Tang, Jintao Liu, Luoshu Wang, Jialu Liu
url: http://arxiv.org/abs/2608.15780v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decomposing Staleness in Recommender Systems: A Dual-Filter Framework for Supersession and Decay

## Abstract
Stale recommendations are a pervasive challenge and a leading source of user complaints on large-scale content platforms. Items lose relevance through two primary mechanisms: supersession, where emerging updates render prior coverage stale, and relevance decay, where an item's informational value naturally diminishes over its lifecycle. Traditional countermeasures serve as crude proxies: age cutoffs poorly reflect actual relevance loss, while engagement heuristics rely on lagging signals, broadly exposing users to stale content before the system adapts.   We present SDF (Supersession-Decay Filtering), a staleness filtering system fully deployed in Google Discover, a personalized recommendation feed with hundreds of millions of daily and billions of monthly active users. SDF targets both mechanisms with complementary filters, each powered by a learned model: a relational staleness model that detects supersession between item pairs, and a predicted traffic ratio (PTR) model that forecasts relevance decay from the item's content, trained on lifetime visit traffic. Applied via disjunction upstream of the ranking stage, SDF prunes stale candidates, measurably reducing downstream serving costs. Online experiments demonstrate that these filters significantly reduce the prevalence of stale content while improving user engagement. Over a two-year production deployment, user-filed staleness reports (in-product user feedback) declined by 54.9% relative to the pre-deployment baseline, establishing SDF as a robust and scalable paradigm for resolving content staleness at industrial scale.

## Metadata
- **Published**: 2026-08-16T15:00:24Z
- **Authors**: Di Bai, Feng Han, Zhenwei Tang, Jintao Liu, Luoshu Wang, Jialu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15780v1)