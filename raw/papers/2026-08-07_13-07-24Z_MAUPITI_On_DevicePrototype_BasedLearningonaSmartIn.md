---
title: MAUPITI: On-Device Prototype-Based Learning on a Smart Infrared Sensor
published: 2026-08-07T13:07:24Z
authors: Beatrice Alessandra Motetti, Tanguy Dugas du Villard, Matteo Risso, Alessio Burrello, Francesco Daghero, Enrico Macii, Massimo Poncino, Marco Castellano, Alfio Basile, Daniele Jahier Pagliari
url: http://arxiv.org/abs/2608.07192v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAUPITI: On-Device Prototype-Based Learning on a Smart Infrared Sensor

## Abstract
Low-resolution infrared (IR) array sensors represent an interesting solution for privacy-preserving human sensing in embedded systems. In this letter, we describe a smart multi-pixel IR sensor integrating a 16$\times$16 thermal MOSFET (TMOS) array and a RISC-V microcontroller extended with low-precision SIMD instructions, capable of on-device learning and continual adaptation for pose and gesture recognition tasks under tight memory and power constraints ($<$32kB on-chip memory, $\approx$1.5mW). To avoid the memory overheads of backpropagation and replay buffers, we adopt a prototype-based Nearest Class Mean (NCM) classifier in which a simple Convolutional Neural Network (CNN) encoder is trained and quantized offline, while class prototypes are stored and updated on the device in streaming mode. With experiments on two datasets, we show that this approach yields accuracy on par with a conventional classifier, with negligible latency overheads in both the classification and the prototype update ($<$0.29% considering both phases), effectively enabling online adaptation of the perception framework.

## Metadata
- **Published**: 2026-08-07T13:07:24Z
- **Authors**: Beatrice Alessandra Motetti, Tanguy Dugas du Villard, Matteo Risso, Alessio Burrello, Francesco Daghero, Enrico Macii, Massimo Poncino, Marco Castellano, Alfio Basile, Daniele Jahier Pagliari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07192v1)