---
title: AI Architecture Design - Azure Architecture Center | Microsoft Learn
date: 2026-05-05
url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/
scraped: 2026-05-05 02:00
---

# AI Architecture Design - Azure Architecture Center | Microsoft Learn

## Full Article

Table of contents
Exit editor mode
Ask Learn
Ask Learn
Reading mode
Table of contents
Read in English
Add
Add to plan
Edit
Copy Markdown
Print
Note
Access to this page requires authorization. You can try
signing in
or
changing directories
.
Access to this page requires authorization. You can try
changing directories
.
AI architecture design
Feedback
Summarize this article for me
AI is a technology that machines use to imitate intelligent human behavior. Machines can use AI to do the following tasks:
Analyze data to create images and videos.
Analyze and synthesize speech.
Verbally interact in natural ways.
Make predictions and generate new data.
You can incorporate AI into applications to do functions or make decisions that traditional logic or processing can't handle effectively. As an architect who designs solutions, you need to learn about the AI and machine learning landscape and how you can integrate Azure solutions into your workload design.
Get started
Azure Architecture Center provides example architectures, architecture guides, architectural baselines, and ideas that you can apply to your scenario. Workloads that use AI and machine learning components should follow the Azure Well-Architected Framework
AI workloads
guidance. This guidance includes principles and design guides that influence AI and machine learning workloads across the five architecture pillars. Implement those recommendations in the scenarios and content in the Azure Architecture Center.
AI concepts
AI concepts encompass a wide range of technologies and methodologies that machines use to do tasks that typically require human intelligence. The following sections provide an overview of key AI concepts.
Algorithms
Algorithms
or
machine learning algorithms
are pieces of code that help people explore, analyze, and find meaning in complex datasets. Each algorithm is a finite set of unambiguous step-by-step instructions that a machine can follow to achieve a specific goal. The goal of a machine learning model is to establish or discover patterns that humans can use to make predictions or categorize information. An algorithm might describe how to check whether a pet is a cat, dog, fish, bird, or lizard. A more complicated algorithm might describe how to identify a written or spoken language, analyze its words, translate them into a different language, and then check the translation for accuracy.
Choose an algorithm family that best suits your task. Evaluate the different algorithms within the family to find the appropriate fit for your workload. For more information, see
Machine learning algorithms
.
Machine learning
Machine learning
is an AI technique that uses algorithms to create predictive models. These algorithms parse data fields and learn from the patterns within data to generate models. The models can then make informed predictions or decisions based on new data.
The predictive models are validated against known data, measured by performance metrics for specific business scenarios, and then adjusted as needed. This process of learning and validation is called
training
. Through periodic retraining, machine learning models improve over time.
In your workload design, you might use machine learning if your scenario includes past observations that you can reliably use to predict future situations. These observations can be universal truths, like computer vision that detects one form of animal from another. Or these observations can be specific to your situation, like computer vision that detects a potential assembly mistake on your assembly lines based on past warranty claim data.
For more information, see
Machine learning overview
.
Deep learning
Deep learning
is a type of machine learning that can learn through its own data processing. Like machine learning, it also uses algorithms to analyze data. But it analyzes data by using artificial neural networks that have many inputs, outputs, and layers of processing. Each layer can process the data in a different way. The output of one layer becomes the input for the next. Deep learning uses this process to create more complex models than traditional machine learning can create.
Deep learning requires a large investment to generate highly customized or exploratory models. You might consider other solutions in this article before you add deep learning to your workload.
For more information, see
Deep learning overview
.
Generative AI
Generative AI
trains models to generate original content based on many forms of content, including natural language, computer vision, audio, or image input. By using generative AI, you can describe a desired output in everyday language, and the model can respond by creating appropriate text, image, and code. Examples of generative AI applications include Microsoft 365 Copilot and Microsoft Foundry.
Copilot
is primarily a user interface (UI) that helps you write code, documents, and other text-based content. It's based on popular models from OpenAI and Anthropic and is integrated into a wide range of Microsoft applications and user experiences.
Foundry
is a development platform as a service (PaaS) that provides access to agent hosting and a catalog of language models, including the following options:
GPT-5.2 (OpenAI)
Claude (Anthropic)
Phi (Microsoft)
Grok (xAI)
You can adapt these models to the following specific tasks:
Content generation
Content summarization
Image understanding
Semantic search
Natural language to code translation
Video generation
Speech to speech
Language models
Language models
are a subset of generative AI that focus on natural language processing tasks, like text generation and sentiment analysis. These models represent natural language based on the probability of words or sequences of words that occur in a given context.
Conventional language models are used in supervised settings for research purposes. These models are trained on well-labeled text datasets for specific tasks. Pretrained language models provide an easy way to start using AI. They're more widely used in recent years. These models are trained on large-scale text collections from the internet via deep learning neural networks. You can fine-tune them on smaller datasets for specific tasks.
The number of parameters, or
weights
, determine the size of a language model. Parameters influence how the model processes input data and generates an output. During training, the model adjusts the weights to minimize the difference between its predictions and the actual data. This process is how the model learns parameters. The more parameters a model has, the more complex and expressive it is. But it's also more computationally expensive to train and use.
Small language models usually have fewer than 10 billion parameters, and large language models have more than 10 billion parameters. For example, the Microsoft Phi-4 model family includes the following versions:
Phi-4-Mini, which has 3.8 billion parameters
Phi-4-Multimodal-instruct, which has 5.6 billion parameters
Phi-4 (the base model), which has 14 billion parameters
For more information, see the
language model catalog
.
Copilots
The availability of language models led to new ways to interact with applications and systems by using digital copilots and connected, domain-specific agents.
Copilots
are generative AI assistants that integrate into applications, often as chat interfaces. They provide contextualized support for common tasks in those applications.
Microsoft 365 Copilot
integrates with a wide range of Microsoft applications and user experiences. It's based on an open architecture where non-Microsoft developers can create their own plug-ins to extend or customize the user experience by using Copilot. Partner developers can also create their own copilots by using the same open architecture.
For more information, see the following resources:
Adopt, extend, and build Copilot experiences across the Microsoft Cloud
Microsoft Copilot Studio overview
Foundry overview
Retrieval-augmented generation
Retrieval-augmented generation (RAG)
is an architecture pattern that augments the capabilities of a language model, like ChatGPT, that's trained only on public data. You can use this pattern to add a retrieval system that provides relevant grounding data in the context with the user request. An information retrieval system provides control over grounding data that a language model uses when it formulates a response. RAG architecture helps you scope generative AI to content that's sourced from vectorized documents, images, and other data formats. RAG isn't limited to vector search storage. You can use any data store technology.
For more information, see
Design and develop a RAG solution
and
Choose an Azure service for vector search
. Use
Foundry IQ knowledge bases
for grounding data that Foundry agents need as a turnkey approach to RAG.
Agent-based architecture
Agents are more than just code that calls language models to respond to user prompts. They can autonomously do tasks, make decisions, and interact with other systems. You can design agents to handle specific tasks or operate in complex environments, which makes them suitable for many applications. Multiâagent architecture lets you break complex problems into specialized agents that coordinate to produce a solution.
Tools like
Microsoft Agent Framework
and
Foundry workflows
can help you build agent-based architectures.
For information about how to coordinate multiple agents in complex AI scenarios, see
AI agent orchestration patterns
.
Foundry Tools
By using
Foundry Tools
, developers and organizations can use ready-made, prebuilt, and customizable APIs and models to create intelligent, market-ready, and responsible applications. Use cases include natural language processing for conversations, search, monitoring, translation, speech, vision, and decision-making.
For more information, see the following resources:
Choose a Foundry Tools technology
Foundry Tools overview
Choose a natural language processing technology in Azure
AI language models
Language models
, like the OpenAI GPT models, are powerful tools that can generate natural language across different domains and tasks. To choose a model, consider factors like data privacy, ethical use, accuracy, and bias.
Phi open models
are small, less compute-intensive models for generative AI solutions. A small language model might be more efficient, interpretable, and explainable than a large language model.
When you design a workload, you can use language models as a hosted solution behind a metered API. For many small language models, you can host language models in-process or at least on the same compute as the consumer. When you use language models in your solution, consider your choice of language model and its available hosting options to help ensure an optimized solution for your use case.
AI development platforms and tools
The following AI development platforms and tools can help you build, deploy, and manage machine learning and AI models.
Azure Machine Learning
Azure Machine Learning is a machine learning service that you can use to build and deploy models. Machine Learning provides web interfaces and SDKs for you to train and deploy your machine learning models and pipelines at scale. Use these capabilities with open-source Python frameworks like PyTorch, TensorFlow, and scikit-learn.
For more information, see the following resources:
Compare Microsoft machine learning products and technologies
Machine Learning documentation
What is Machine Learning?
AI and Machine learning reference architectures for Azure
Baseline Foundry chat reference architecture in an Azure landing zone
Baseline Foundry chat reference architecture
describes how to build an end-to-end chat architecture by using the OpenAI GPT models in Foundry. It incorporates grounding via enterprise data sources to enrich responses with contextual information.
[Diagram that shows a baseline end-to-end chat architecture that uses Foundry.]
The diagram presents a detailed Azure architecture for deploying an AI solution. On the left, a user connects through an application gateway with a web application firewall, which is part of a virtual network. This gateway links to private DNS zones. Azure DDoS Protection protects the gateway. Below the gateway, private endpoints connect to services like Azure App Service, Azure Key Vault, and Azure Storage, which are used for client app deployment. App Service is managed with identity and spans three zones. Application Insights and Azure Monitor provide monitoring, and Microsoft Entra ID handles authentication. To the right, the virtual network has several subnets: App Service integration, private endpoint, Foundry integration, Azure AI agent integration, Azure Bastion, jump box, build agents, and Azure firewall. Each subnet hosts specific endpoints or services, like storage, Foundry, Azure AI Search, Azure Cosmos DB, and knowledge store, all connected via private endpoints. Outbound traffic from the network passes through Azure Firewall to reach internet sources. To the far right, a separate box represents Foundry, which includes an account and a project. Managed identities are used to connect Foundry Agent Service to the Foundry project, which in turn accesses Azure OpenAI. The diagram uses numbered green circles to indicate the logical flow, which shows how user requests traverse the network, interact with different endpoints, and ultimately connect to Foundry Tools and storage, with dependencies clearly grouped and labeled.
Automated machine learning
Automated machine learning (AutoML)
is the process of automating the time-consuming, iterative tasks of machine learning model development. Data scientists, analysts, and developers can use AutoML to build machine learning models that have high scale, efficiency, and productivity while sustaining model quality.
For more information, see the following resources:
What is AutoML?
Train a classification model by using AutoML in Machine Learning studio
Set up AutoML experiments in Python
Install and set up the CLI
MLflow
Machine Learning workspaces are MLflow-compatible, which means that you can use a Machine Learning workspace the same way that you use an MLflow server. This compatibility provides the following advantages:
Machine Learning doesn't host MLflow server instances but can use the MLflow APIs directly.
You can use a Machine Learning workspace as your tracking server for any MLflow code, whether or not it runs in Machine Learning. You need to set up MLflow to point to the workspace where the tracking should occur.
You can run training routines that use MLflow in Machine Learning without making any changes.
For more information, see
MLflow and Machine Learning
and
MLflow
.
Generative AI tools
Foundry
provides a platform to help you experiment, develop, and deploy generative AI apps and APIs responsibly. Use the
Foundry portal
to find Foundry Tools, foundation models, a playground, and resources to help you fine-tune, evaluate, and deploy AI models and AI agents.
Foundry Agent Service
hosts agents that you define. These agents connect to a foundation model in the AI model catalog and optionally your own custom knowledge stores or APIs. You can define these agents declaratively or Foundry can containerize and host them.
Copilot Studio
extends Copilot in Microsoft 365. You can use Copilot Studio to build custom copilots for internal and external scenarios. Use an authoring canvas to design, test, and publish copilots. You can easily create generative AI-enabled conversations, provide greater control of responses for existing copilots, and accelerate productivity by using automated workflows.
Data platforms for AI
The following platforms provide solutions for data movement, processing, ingestion, transformation, real-time analytics, and reporting.
Microsoft Fabric
Microsoft Fabric is an end-to-end analytics and data platform for enterprises that require a unified solution. Workload teams can use data within Fabric. The platform covers data movement, processing, ingestion, transformation, real-time event routing, and report building. It provides a suite of services, including Fabric Data Engineer, Fabric Data Factory, Fabric Data Science, Fabric Real-Time Intelligence, Fabric Data Warehouse, and Fabric Databases.
Fabric integrates separate components into a cohesive stack. Instead of relying on different databases or data warehouses, you can centralize data storage by using OneLake. AI capabilities are embedded within Fabric, which eliminates the need for manual integration.
For more information, see the following resources:
What is Fabric?
Learning path: Get started with Fabric
Foundry Tools in Fabric
Use Azure OpenAI in Fabric with REST API
Use Fabric for generative AI: A guide to building and improving RAG systems
Build custom AI applications with Fabric: Implement RAG for enhanced language models
Copilots in Fabric
You can use Copilot and other generative AI features to transform and analyze data, generate insights, and create visualizations and reports in Fabric and Power BI. You can build your own copilot or choose one of the following prebuilt copilots:
Copilot in Fabric
Copilot for Data Science and Data Engineer
Copilot for Data Factory
Copilot for Data Warehouse
Copilot for Power BI
Copilot for Real-Time Intelligence
Data agent in Fabric
Data agent in Fabric is a feature that you can use to build your own conversational Q&A systems by using generative AI. A Fabric data agent makes data insights easier to use and more actionable for everyone in your organization.
For more information, see the following resources:
Fabric data agent overview
Create data agent
Example of a data agent
Difference between a Fabric data agent and a copilot
Apache Spark-based data platforms for AI
Apache Spark is a parallel processing framework that supports in-memory processing to boost the performance of big data analytic applications. Spark provides basic building blocks for in-memory cluster computing. A Spark job can load and cache data into memory and query it repeatedly, which is faster than disk-based applications, like Hadoop.
Spark in Fabric
Fabric Runtime is an Azure-integrated platform based on Spark that you can use to implement and manage data engineering and data science experiences. Fabric Runtime combines key components from internal and open-source sources, which provides a comprehensive solution.
Fabric Runtime has the following key components:
Spark
is an open-source distributed computing library that you can use for large-scale data processing and analytics tasks. Spark provides a versatile platform for data engineering and data science experiences.
Delta Lake
is an open-source storage layer that integrates atomicity, consistency, isolation, and durability (ACID) transactions and other data reliability features with Spark. Integrated within Fabric Runtime, Delta Lake enhances data processing capabilities and helps ensure data consistency across multiple concurrent tasks.
Default-level packages for Java, Scala, Python, and R
are packages that support diverse programming languages and environments. These packages are automatically installed and configured, so developers can apply their preferred programming languages for data processing tasks.
Fabric Runtime is built on an open-source operating system that provides compatibility with different hardware configurations and system requirements.
For more information, see
Spark runtimes in Fabric
.
Azure Databricks Runtime for Machine Learning
Azure Databricks
is a Spark-based analytics platform that includes workflows and an interactive workspace for collaboration between data scientists, engineers, and business analysts.
You can use
Databricks Runtime for Machine Learning
to start a Databricks cluster that has all the libraries required for distributed training. This feature provides an environment for machine learning and data science. It has multiple popular libraries, including TensorFlow, PyTorch, Keras, and XGBoost. It also supports distributed training via Horovod.
For more information, see the following resources:
Azure Databricks documentation
Machine learning capabilities in Azure Databricks
Deep learning overview for Azure Databricks
Spark in Azure HDInsight
Spark in Azure HDInsight
is the Microsoft implementation of Spark in the cloud. Spark clusters in HDInsight are compatible with Azure Storage and Azure Data Lake Storage, so you can use HDInsight Spark clusters to process data that you store in Azure.
SynapseML
is the Microsoft machine learning library for Spark. This open-source library adds many deep learning and data science tools, networking capabilities, and production-grade performance to the Spark ecosystem.
For more information, see the following resources:
SynapseML features and capabilities
HDInsight overview
Tutorial: Build an Spark machine learning application in HDInsight
Spark best practices on HDInsight
Set up HDInsight Spark cluster settings
Create an Spark machine learning pipeline on HDInsight
Data storage for AI
You can use the following platforms to efficiently store, use, and analyze large volumes of data.
Fabric OneLake
OneLake in Fabric is a unified and logical data lake that you can tailor to your entire organization. It's the central hub for all analytics data and is included with every Fabric tenant. OneLake in Fabric is built on the foundation of Data Lake Storage.
OneLake in Fabric provides the following benefits:
Supports structured and unstructured file types
Stores all tabular data in Delta-Parquet format
Provides a single data lake within tenant boundaries that's governed by default
Supports the creation of workspaces within a tenant so that your organization can distribute ownership and access policies
Supports the creation of different data items, like lakehouses and warehouses, where you can use data
For more information, see
OneLake, the OneDrive for data
.
Data Lake Storage
Data Lake Storage is a single, centralized repository where you can store your structured and unstructured data. Use a data lake to quickly and easily store, use, and analyze a wide variety of data in a single location. You don't need to conform your data to fit an existing structure. Instead, you can store your data in its raw or native format, usually as files or as binary large objects, or blobs.
Data Lake Storage provides file system semantics, file-level security, and scale. Because these capabilities are built on Azure Blob Storage, you also get low-cost, tiered storage that has high availability and disaster recovery capabilities.
Data Lake Storage uses the infrastructure of Storage to create a foundation to build enterprise data lakes on Azure. Data Lake Storage can service multiple petabytes of information while sustaining hundreds of gigabits of throughput so that you can manage massive amounts of data.
For more information, see the following resources:
Introduction to Data Lake Storage
Tutorial: Data Lake Storage, Azure Databricks, and Spark
Data processing for AI
You can use the following tools to prepare data for machine learning and AI applications. Ensure that your data is clean and structured so that you can use it for advanced analytics.
Fabric Data Factory
You can use Fabric Data Factory to ingest, prepare, and transform data from multiple data sources, like databases, data warehouses, lakehouses, and real-time data streams. This feature can help you meet your data operations requirements when you design workloads.
Data Factory supports code solutions and no-code or low-code solutions:
Use
data pipelines
to create workflow capabilities at cloud scale. Use the select-and-move interface to build workflows that can refresh your dataflow, move petabyte-size data, and define control-flow pipelines.
Use
dataflows
as a low-code interface to ingest data from hundreds of data sources and transform it by using over 300 data transformations.
For more information, see
Data Factory end-to-end scenario: Introduction and architecture
.
Azure Databricks
You can use the Databricks Data Intelligence Platform to write code to create a machine learning workflow by using feature engineering.
Feature engineering
is the process of transforming raw data into features that you can use to train machine learning models. The Databricks Data Intelligence Platform includes key features that support feature engineering:
Data pipelines
ingest raw data, create feature tables, train models, and do batch inference. When you use feature engineering in Unity Catalog to train and log a model, the model is packaged with feature metadata. When you use the model for batch scoring or online inference, it automatically retrieves feature values. The caller doesn't need to know about the values or include logic to look up or join features to score new data.
Model and feature serving endpoints
are instantly available and provide milliseconds of latency.
Mon

## Metadata
- **Source URL**: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/
