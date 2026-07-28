---
title: Rendering on Real Silicon: GPU Render-Timing as a Passive, AI-Resistant CAPTCHA Signal
published: 2026-07-25T23:10:24Z
authors: David Noever, Forrest McKee
url: http://arxiv.org/abs/2607.23389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rendering on Real Silicon: GPU Render-Timing as a Passive, AI-Resistant CAPTCHA Signal

## Abstract
Conventional CAPTCHAs pose puzzles that modern AI systems increasingly solve, while behavioral and cryptographic-attestation defenses carry privacy or enrollment costs. We investigate an orthogonal signal: the physical timing behavior of a client's GPU under a controlled WebGL rendering workload. Unlike WebGL fingerprinting, which hashes pixel output into a static device identifier, we measure render-timing dynamics to classify rather than identify, leaking no persistent identifier. We characterize the in-the-wild adversary with a 12-hour passive deployment (207 unsolicited requests; 86% automated; 85% of browser-claiming clients failed HTTP header-consistency checks). We then collect labeled GPU-timing samples through a single public endpoint exercised by real browsers (positive class, 13 distinct GPUs) and by keyed headless automation across a render-backend matrix (negative class). Software-rendered automation -- empirically the dominant real-world adversary -- separates from genuine GPUs by roughly 5x in mean render time. On a confound-controlled comparison (identical GPU family and browser engine, differing only in headless vs. interactive execution), headless automation on real hardware still exhibits a distinct timing signature, separating from human samples by 75-106% on frame jitter, timer-quantization ratio, and coefficient of variation. We report these as pilot-scale findings on a single GPU architecture and outline the cross-architecture collection required to establish generalization.

## Metadata
- **Published**: 2026-07-25T23:10:24Z
- **Authors**: David Noever, Forrest McKee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23389v1)