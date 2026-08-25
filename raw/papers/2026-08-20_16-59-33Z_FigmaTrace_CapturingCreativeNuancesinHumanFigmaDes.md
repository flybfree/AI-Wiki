---
title: FigmaTrace: Capturing Creative Nuances in Human Figma Design Workflows
published: 2026-08-20T16:59:33Z
authors: Darshan Deshpande, Yoshinari Fujinuma, Martyna Markiewicz, Devanshu Bansal, Shivani Jain, Nicholas Saban, Chirag Maheshwari, Anand Kannappan
url: http://arxiv.org/abs/2608.21460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FigmaTrace: Capturing Creative Nuances in Human Figma Design Workflows

## Abstract
Vision Language Models have recently shown improvements in several objective and verifiable domains such as object detection but continue to underperform on subjective and creative design tasks. A major contributor to this performance gap is the lack of high quality human workflow data that captures a diverse set of preferences and decisions that make human experts good at design tasks. In this work, we first define a unique, expert curated taxonomy of design skills and best practices which we further expand into a set of 126 open ended, subjective, long horizon tasks. Built on top of this and expert solutions, our dataset FigmaTrace contains over 200 hours of human captured video data converted into 3469 design trajectories using a novel design phase-based method. We use our dataset to train four models and show that training on FigmaTrace leads to a performance improvement comparable to frontier closed models such as \textsc{Claude-Opus-5} and \textsc{GPT-5.6-Sol} on four out of distribution agentic GUI environments. We further perform a useful ablation to attribute these performance improvements to a design phase-based video to trajectory conversion which outperforms prior length-based conversion approaches. Finally, we perform a qualitative analysis on the best performing \textsc{Qwen3.8-27B} outputs to better correlate performance improvements to FigmaTrace's trends. We open source our dataset and the best model for the community.

## Metadata
- **Published**: 2026-08-20T16:59:33Z
- **Authors**: Darshan Deshpande, Yoshinari Fujinuma, Martyna Markiewicz, Devanshu Bansal, Shivani Jain, Nicholas Saban, Chirag Maheshwari, Anand Kannappan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21460v1)