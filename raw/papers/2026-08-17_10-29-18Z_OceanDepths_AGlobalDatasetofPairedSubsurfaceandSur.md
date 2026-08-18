---
title: OceanDepths: A Global Dataset of Paired Subsurface and Surface Ocean Observations
published: 2026-08-17T10:29:18Z
authors: Simon Donike, Ruben Cartuyvels, Antonino Ian Ferola, Elisa Carli, Diego Fernandez Prieto, Marie-Helene Rio
url: http://arxiv.org/abs/2608.16373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OceanDepths: A Global Dataset of Paired Subsurface and Surface Ocean Observations

## Abstract
Despite comprising over 70\% of its surface, the world's oceans are critically underobserved compared to the land surface or the atmosphere.Understanding the global ocean requires jointly observing its surface and subsurface structure, yet no standardized, high-resolution dataset couples satellite surface fields to co-located \emph{in situ} depth profiles in an AI-ready format.Existing resources either consist of model-reconstructed gridded products rather than observations, cover only a single variable or basin, or operate at resolutions too coarse for mesoscale dynamics.We introduce \textsc{OceanDepths}, the first open, global, regridded AI-ready dataset that pairs satellite-derived sea surface temperature (SST), sea surface salinity (SSS), and sea surface height (SSH) L4 products with co-located EN4 subsurface temperature and salinity profiles, complemented by matched GLORYS12 ocean reanalysis data to support comparisons or multi-stage learning.The dataset spans 2000--2024 at \SI{0.1}{\degree}$\times$\SI{0.1}{\degree} spatial resolution and at weekly temporal resolution, covering the entire globe's sea surface and with over 9.5 million paired profiles interpolated to 50 standardized depth levels.We provide a configurable system to split the globe in equally sized spatial patches.The 4D multivariate structure, high resolution, long temporal extent, and extreme sparsity of subsurface observations (${\sim}$0.01\% per depth level) make \textsc{OceanDepths}a challenging testbed for novel AI methods.We demonstrate subsurface state reconstruction as an example task with simple baseline models, but also envision \textsc{OceanDepths}to support the development of observation-based forecast methods and other related tasks.\added{Available at: https://huggingface.co/datasets/ESA-philab/OceanDepths.}

## Metadata
- **Published**: 2026-08-17T10:29:18Z
- **Authors**: Simon Donike, Ruben Cartuyvels, Antonino Ian Ferola, Elisa Carli, Diego Fernandez Prieto, Marie-Helene Rio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16373v1)