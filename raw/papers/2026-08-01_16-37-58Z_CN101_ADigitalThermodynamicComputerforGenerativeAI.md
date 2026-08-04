---
title: CN101 - A Digital Thermodynamic Computer for Generative AI
published: 2026-08-01T16:37:58Z
authors: Lars Holdijk, Denis Melanson, Zier Mensch, Brandon Birchall, Vincent Cheung, Nicholas Lehrter, Maxwell Aifer, Samuel Duffield, Jan Ole Ernst, Rajath Salegame, Antonio J. Martinez, Gavin Crooks, Miranda Cheng, Zach Belateche, Marc Bright, Patrick J. Coles, Faris Sbahi
url: http://arxiv.org/abs/2608.00754v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CN101 - A Digital Thermodynamic Computer for Generative AI

## Abstract
Thermodynamic computing is an emerging hardware paradigm, in which stochastic physical dynamics serve as the direct computational primitive. The recent explosion of generative AI has only sharpened the search for alternative approaches to compute, and, as we show in this work, thermodynamic computing turns out to be well suited to this space. An important class of methods realises a function as the stationary expectation of an ergodic stochastic process: the answer is encoded in the time-averaged statistics of an equilibrating trajectory. To date, this equilibration-style class has been formulated exclusively through Langevin dynamics, restricting its implementations to analogue substrates and the engineering challenges those bring. In this work, we propose a substrate-independent formalisation of the equilibration-style formulation, in which the only object of design is the dynamical generator L* of an arbitrary ergodic process. The formalisation makes three hardware-level properties of the formulation explicit: the precision of a result is a knob set by how long the dynamics are run, sample averages decompose across independent trajectories, and dependent stages of a computation operate concurrently rather than serially, a property we call sequential parallelism. We instantiate the formalisation by fabricating a prototype digital thermodynamic computing chip, named CN101, that implements the formulation through discrete accumulator dynamics on standard CMOS using stochastic computing principles. We characterise CN101's success across conventional generative AI workloads in the form of VAEs and flow matching, applied to both image generation and scientific problems. Together, the formalisation and its digital instantiation show that the equilibration-style formulation is substrate-independent, and that its computational properties can be exploited on standard digital hardware.

## Metadata
- **Published**: 2026-08-01T16:37:58Z
- **Authors**: Lars Holdijk, Denis Melanson, Zier Mensch, Brandon Birchall, Vincent Cheung, Nicholas Lehrter, Maxwell Aifer, Samuel Duffield, Jan Ole Ernst, Rajath Salegame, Antonio J. Martinez, Gavin Crooks, Miranda Cheng, Zach Belateche, Marc Bright, Patrick J. Coles, Faris Sbahi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00754v1)