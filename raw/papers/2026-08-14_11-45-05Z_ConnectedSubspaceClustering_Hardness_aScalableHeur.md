---
title: Connected Subspace Clustering: Hardness, a Scalable Heuristic, and an Application to Sea Level Geodesy
published: 2026-08-14T11:45:05Z
authors: Johanna Hillebrand, Jan Höckendorff, Jürgen Kusche, Kelin Luo, Heiko Röglin, Melanie Schmidt, Christian Sohler, Bernd Uebbing
url: http://arxiv.org/abs/2608.14215v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Connected Subspace Clustering: Hardness, a Scalable Heuristic, and an Application to Sea Level Geodesy

## Abstract
Constrained optimization extends classical optimization by integrating side information, making it widely applicable across scientific and engineering domains. Consider a setting where we measure variables at different physical locations. When grouping these measurements, we often want clusters that are both internally similar and physically coherent. Thus, we have a constrained clustering problem where the constraint models coherence. Motivated by an application in geodesy, where contiguous regions of the sea surface must be identified for principal component analysis, we introduce the Connected Subspace Clustering problem: given high-dimensional points and a connectivity graph, partition them into $k$ connected clusters, minimizing their total squared distance to the clusters' best-fit $m'$-dimensional affine subspaces. We prove that, even for $m' = 0$ and a grid graph with holes, the problem is NP-hard to approximate within $Ω(n^{1/2-\varepsilon})$ for every $\varepsilon>0$, where $n$ is the number of measurements. We then introduce an efficient Lloyd-style heuristic that alternates subspace fitting with an iterative merging procedure to enforce connectivity. Our method returns exactly $k$ connected regions by construction, whereas unconstrained methods leave up to $1{,}966$ disconnected fragments at higher cost. In a study of 160 configurations on global sea level time series, our merging-based repair is the strongest of four strategies in $73.75\%$ of cases, and consistently outperforms competitors such as (connected) Ward's method across all tested cluster counts. The resulting regions isolate signals aligning with climate indices such as the El Nino-Southern Oscillation and Indian Ocean Dipole. Although developed for geodesy, the approach applies to other spatially embedded multivariate time series, such as climate fields, remote sensing, neuroimaging, and sensor networks.

## Metadata
- **Published**: 2026-08-14T11:45:05Z
- **Authors**: Johanna Hillebrand, Jan Höckendorff, Jürgen Kusche, Kelin Luo, Heiko Röglin, Melanie Schmidt, Christian Sohler, Bernd Uebbing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14215v1)