---
title: Your Privacy My Cloak: Backdoor Attacks on Differentially Private Federated Learning
published: 2026-06-15T17:53:12Z
authors: Xiaolin Li, Ning Wang, Ninghui Li, Wenhai Sun
url: http://arxiv.org/abs/2606.17035v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Your Privacy My Cloak: Backdoor Attacks on Differentially Private Federated Learning

## Abstract
Prior research suggests that differential privacy (DP) inherently enhances the robustness of federated learning (FL) against backdoor attacks. In this paper, we challenge this assumption. Through an empirical analysis of two baseline attack strategies, we uncover a fundamental tension in DP-FL: while bypassing DP allows state-of-the-art defenses to detect and filter malicious updates, complying with DP inadvertently masks their distinguishing statistical characteristics. Consequently, existing defenses become ineffective as DP reduces the raw backdoor signal. Building on this masking effect, we propose RING, a novel attack that explicitly exploits DP to conceal malicious contributions while maximizing attack impact. By collaboratively crafting adversarial perturbations, compromised clients reconstruct a strong backdoor signal during aggregation without triggering anomaly detection. RING operates as a perturbation layer that is agnostic to the underlying backdoor technique, making it broadly applicable and composable with existing attacks -- a property that significantly amplifies the threat it poses to DP-FL. Extensive evaluations across four image and text datasets under non-iid distributions show that RING achieves an average attack success rate of 90.3% against six state-of-the-art defenses under a moderate privacy budget, an improvement of up to 26.08x over baseline strategies. Finally, we evaluate potential countermeasures and find that mitigating this threat incurs significant utility trade-offs, exposing a fundamental security gap in the deployment of differentially private FL.

## Metadata
- **Published**: 2026-06-15T17:53:12Z
- **Authors**: Xiaolin Li, Ning Wang, Ninghui Li, Wenhai Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.17035v1)