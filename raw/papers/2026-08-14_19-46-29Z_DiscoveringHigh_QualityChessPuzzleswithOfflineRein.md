---
title: Discovering High-Quality Chess Puzzles with Offline Reinforcement Learning
published: 2026-08-14T19:46:29Z
authors: Allen Nie, Anirudhan Badrinath, Nicholas Tomlin, Timothy Dai, Carissa Yip, Rose E Wang, Emma Brunskill, Chris Piech
url: http://arxiv.org/abs/2608.14851v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Discovering High-Quality Chess Puzzles with Offline Reinforcement Learning

## Abstract
Learning and skill mastery require extensive and deliberate practice. In many learning settings, producing high-quality pedagogical materials can require a high level of domain expertise and be very time-consuming. Pedagogical materials often need to train students to engage in different thinking patterns. In some domains, such as chess, puzzles are used to help students practice their skills in calculating the next moves and recognizing known patterns on a board. Giving students a practice set of puzzles to help them learn different modes of thinking is challenging because the teacher needs to carefully balance between different motifs and how many look-ahead steps a student needs to perform. Popular online platforms like Chess.com and Lichess offer players millions of puzzles. Unlike chess tactics puzzles procured by human experts, where chess beginners can learn valuable insights, these puzzles are automatically generated and often regarded as having low pedagogical value. These platforms also rely on a heuristic to recommend puzzles to users for practice. Using the user history data over an entire year, a total of 1.5 billion puzzle-solving histories, we learn the pedagogical value of a puzzle and how to automatically choose a set of puzzles to better support chess learners using insights from offline reinforcement learning. We show that using offline policy evaluation, our trained policy has significant impact on beginners with puzzle-solving Elo range of 100--1000, particularly for the group of beginners whose learning growth was stagnant. We also performed a qualitative analysis of the puzzles discovered by our model by collecting annotation ratings from expert chess players. The success of our pipeline shows promise for a future where we can understand the pedagogical values of practice items given general user interaction data.

## Metadata
- **Published**: 2026-08-14T19:46:29Z
- **Authors**: Allen Nie, Anirudhan Badrinath, Nicholas Tomlin, Timothy Dai, Carissa Yip, Rose E Wang, Emma Brunskill, Chris Piech
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14851v1)