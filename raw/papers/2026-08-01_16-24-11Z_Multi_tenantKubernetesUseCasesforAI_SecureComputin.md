---
title: Multi-tenant Kubernetes Use Cases for AI, Secure Computing and Data Services, and More
published: 2026-08-01T16:24:11Z
authors: Jake Watson, Sadaf R Alam, Christopher Woods, Abdelwahab Kawafi, Thomas Green, Ian Johnson, Ellis Pires, Jessica R. Jones, Utz-Uwe Haus
url: http://arxiv.org/abs/2608.00742v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-tenant Kubernetes Use Cases for AI, Secure Computing and Data Services, and More

## Abstract
Kubernetes, as a container orchestration engine, has been widely used in cloud-native ecosystems for several years. In supercomputing ecosystems, especially where bare-metal performance for compute and network devices are considered, the adoption is somewhat limited. However, with the increasing diversity of use cases such as AI, secure and confidential computing for sensitive data, and mixed workload orchestration, a traditional, single-tenant batch computing system does not offer the flexibility and reproducibility to which public cloud users are accustomed. Note that Kubernetes is not considered a replacement for batch scheduling systems, which have powerful features for large-scale MPI jobs with thousands of network end points. Rather, it is a complementary service provided as part of a national AI Research Resource. We evaluate Kubernetes deployment on a Hewlett Packard Enterprise (HPE) Cray EX supercomputerwith HPE Slingshot interconnect, called Isambard-AI, with co-design use cases. One is a Trusted Research Environment used for medical and health sciences. The other combines KubeRay, Ray, and vLLM to provide a distributed, sandboxed, persistent AI model hosting service targeting multi-tenant confidential computing. We discuss challenges and lessons learned, and where further development is needed to offer a production Kubernetes-as-a-Service on HPE Cray EX (and later) platforms.

## Metadata
- **Published**: 2026-08-01T16:24:11Z
- **Authors**: Jake Watson, Sadaf R Alam, Christopher Woods, Abdelwahab Kawafi, Thomas Green, Ian Johnson, Ellis Pires, Jessica R. Jones, Utz-Uwe Haus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00742v1)