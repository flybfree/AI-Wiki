---
title: An Open-Source, Event-Driven Pipeline for Cryptocurrency Market Data: Ingestion, Forecasting, and On-Chain Fraud Detection
published: 2026-08-30T18:59:08Z
authors: Basil Sajid Shaikh, Melrick Mascarenhas, Nuzhat Faiz Shaikh
url: http://arxiv.org/abs/2608.29973v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Open-Source, Event-Driven Pipeline for Cryptocurrency Market Data: Ingestion, Forecasting, and On-Chain Fraud Detection

## Abstract
Cryptocurrency markets generate high-frequency, multi-source data that is expensive to work with unless a team already has commercial-grade streaming and warehousing infrastructure in place. This paper describes a fully open-source pipeline that reproduces the behavior of a cloud-native, event-driven system -- file arrival triggering a message, a message triggering compute -- entirely on commodity hardware, using Apache Kafka and a filesystem-watching poller in place of managed cloud triggers. The pipeline partitions historical Gemini exchange data into hourly and minutely files, ingests them asynchronously through two independently grouped Kafka consumers (one for audit logging, one for Spark-triggered ETL), and lands cleaned output in a PostgreSQL warehouse with historical and aggregated schemas plus asset-specific data marts. We use the resulting Bitcoin data mart to compare a seasonal ARIMA model against a single-layer LSTM network for price forecasting, and separately apply Random Forest and Gradient Boosting classifiers, with additional engineered features, to the public Ethereum fraud detection benchmark introduced by Farrugia et al. We report the architecture, the modeling methodology, and the resulting metrics, and we are explicit about the limitations of comparing forecasts issued at different horizons and of evaluating fraud detection on a static, already-labeled dataset.

## Metadata
- **Published**: 2026-08-30T18:59:08Z
- **Authors**: Basil Sajid Shaikh, Melrick Mascarenhas, Nuzhat Faiz Shaikh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29973v1)