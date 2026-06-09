---
title: Machine learning operations - Azure Architecture Center
date: 2026-04-30
url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/machine-learning-operations-v2
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/machine-learning-operations-v2
scraped: 2026-04-30 03:54
---

# Machine learning operations - Azure Architecture Center

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
Machine learning operations
Feedback
Summarize this article for me
This article describes three Azure architectures for machine learning operations that have end-to-end continuous integration and continuous delivery (CI/CD) pipelines and retraining pipelines. The architectures are for these AI applications:
Classical machine learning
Computer vision (CV)
Natural language processing
These architectures are the product of the MLOps v2 project. They incorporate best practices that solution architects identified in the process of developing various machine learning solutions. The result is deployable, repeatable, and maintainable patterns. All three architectures use the Azure Machine Learning service.
For an implementation with sample deployment templates for MLOps v2, see
Azure MLOps v2 GitHub repository
.
Potential use cases
Classical machine learning: Time-series forecasting, regression, and classification on tabular structured data are the most common use cases in this category. Examples include:
Binary and multi-label classification.
Linear, polynomial, ridge, lasso, quantile, and Bayesian regression.
ARIMA, autoregressive, SARIMA, VAR, SES, LSTM.
CV: The MLOps framework in this article focuses mostly on the CV use cases of segmentation and image classification.
Natural language processing: You can use this MLOps framework to implement:
Named entity recognition
Text classification
Text generation
Sentiment analysis
Translation
Question answering
Summarization
Sentence detection
Language detection
Part-of-speech tagging
AI simulations, deep reinforcement learning, and other forms of AI aren't described in this article.
MLOps as a key design area for AI workloads
The planning and implementation of a MLOps and GenAIOps are a core design area in AI workloads on Azure. To get a background on why these machine learning workloads need specialized operations, see
MLOps and GenAIOps for AI workloads on Azure
in the Azure Well-Architected Framework.
Architecture
The MLOps v2 architectural pattern has four main modular components, or phases, of the MLOps lifecycle:
Data estate
Administration and setup
Model development, or the inner loop phase
Model deployment, or the outer loop phase
The preceding components, the connections between them, and the typical personas involved are standard across all MLOps v2 scenario architectures. Variations in the details of each component depend on the scenario.
The base architecture for MLOps v2 for Machine Learning is the classical machine learning scenario for tabular data. The CV and NLP architectures build on and modify this base architecture.
MLOps v2 covers the following architectures that are described in this article:
Classical machine learning architecture
Machine Learning CV architecture
Machine Learning natural language processing architecture
Classical machine learning architecture
[Diagram that shows the classical machine learning architecture.]
Download a
Visio file
of this architecture.
Workflow for the classical machine learning architecture
Data estate
This component illustrates the data estate of the organization and potential data sources and targets for a data science project. Data engineers are the primary owners of this component of the MLOps v2 lifecycle. The Azure data platforms in this diagram aren't exhaustive or prescriptive. A green check mark indicates the data sources and targets that represent recommended best practices that are based on the customer use case.
Administration and setup
This component is the first step in the MLOps v2 solution deployment. It consists of all tasks related to the creation and management of resources and roles that are associated with the project. For example, the infrastructure team might:
Create project source code repositories.
Use Bicep or Terraform to create Machine Learning workspaces.
Create or modify datasets and compute resources for model development and deployment.
Define project team users, their roles, and access controls to other resources.
Create CI/CD pipelines.
Create monitoring components to collect and create alerts for model and infrastructure metrics.
The primary persona associated with this phase is the infrastructure team, but an organization might also have data engineers, machine learning engineers, or data scientists.
Model development (inner loop phase)
The inner loop phase consists of an iterative data science workflow that acts within a dedicated and secure Machine Learning workspace. The preceding diagram shows a typical workflow. The process starts with data ingestion, moves through exploratory data analysis, experimentation, model development and evaluation, and then registers a model for production use. This modular component is agnostic and adaptable to the process that your data science team uses to develop models.
Personas associated with this phase include data scientists and machine learning engineers.
Machine Learning registries
After the data science team develops a model that they can deploy to production, they register the model in the Machine Learning workspace registry. CI pipelines that are triggered, either automatically by model registration or by gated human-in-the-loop approval, promote the model and any other model dependencies to the model deployment phase.
Personas associated with this stage are typically machine learning engineers.
Model deployment (outer loop phase)
The model deployment, or outer loop phase, consists of preproduction staging and testing, production deployment, and monitoring of the model, data, and infrastructure. When the model meets the criteria of the organization and use case, CD pipelines promote the model and related assets through production, monitoring, and potential retraining.
Personas associated with this phase are primarily machine learning engineers.
Staging and test
The staging and test phase varies according to customer practices. This phase typically includes operations such as retraining and testing the model candidate on production data, test deployments for endpoint performance, data quality checks, unit testing, and responsible AI checks for model and data bias. This phase takes place in one or more dedicated and secure Machine Learning workspaces.
Production deployment
After a model passes the staging and test phase, machine learning engineers can use human-in-the-loop gated approval to promote it to production. Model deployment options include a managed batch endpoint for batch scenarios or either a managed online endpoint or Kubernetes deployment that uses Azure Arc for online, near real-time scenarios. Production typically takes place in one or more dedicated and secure Machine Learning workspaces.
Monitoring
Machine learning engineers monitor components in staging, testing, and production to collect metrics related to changes in performance of the model, data, and infrastructure. They can use those metrics to take action. Model and data monitoring can include checking for model and data drift, model performance on new data, and responsible AI problems. Infrastructure monitoring might identify slow endpoint response, inadequate compute capacity, or network problems.
Data and model monitoring: events and actions
Based on model and data criteria, such as metric thresholds or schedules, automated triggers and notifications can implement appropriate actions to take. For example, a trigger might retrain a model to use new production data and then loopback the model to staging and testing for a preproduction evaluation. Or a model or data problem might trigger an action that requires a loopback to the model development phase where data scientists can investigate the problem and potentially develop a new model.
Infrastructure monitoring: events and actions
Automated triggers and notifications can implement appropriate actions to take based on infrastructure criteria, such as an endpoint response lag or insufficient compute for the deployment. Automatic triggers and notifications might trigger a loopback to the setup and administration phase where the infrastructure team can investigate the problem and potentially reconfigure the compute and network resources.
Machine Learning CV architecture
[Diagram that shows the computer vision architecture.]
Download a
Visio file
of this architecture.
Workflow for the CV architecture
The Machine Learning CV architecture is based on the classical machine learning architecture, but it has modifications that are specific to supervised CV scenarios.
Data estate
This component demonstrates the data estate of the organization and potential data sources and targets for a data science project. Data engineers are the primary owners of this component in the MLOps v2 lifecycle. The Azure data platforms in this diagram aren't exhaustive or prescriptive. Images for CV scenarios can come from various data sources. For efficiency when developing and deploying CV models with Machine Learning, we recommend Azure Blob Storage and Azure Data Lake Storage.
Administration and setup
This component is the first step in the MLOps v2 deployment. It consists of all tasks related to the creation and management of resources and roles associated with the project. For CV scenarios, administration and setup of the MLOps v2 environment is largely the same as for classical machine learning but includes an extra step. The infrastructure team uses the labeling feature of Machine Learning or another tool to create image labeling and annotation projects.
Model development (inner loop phase)
The inner loop phase consists of an iterative data science workflow performed within a dedicated and secure Machine Learning workspace. The primary difference between this workflow and the classical machine learning scenario is that image labeling and annotation is a key component of this development loop.
Machine Learning registries
After the data science team develops a model that they can deploy to production, they register the model in the Machine Learning workspace registry. CI pipelines that are triggered automatically by model registration or by gated human-in-the-loop approval promote the model and any other model dependencies to the model deployment phase.
Model deployment (outer loop phase)
The model deployment or outer loop phase consists of preproduction staging and testing, production deployment, and monitoring of the model, data, and infrastructure. When the model meets the criteria of the organization and use case, CD pipelines promote the model and related assets through production, monitoring, and potential retraining.
Staging and test
The staging and test phase varies according to customer practices. This phase typically includes operations such as test deployments for endpoint performance, data quality checks, unit testing, and responsible AI checks for model and data bias. For CV scenarios, machine learning engineers don't need to retrain the model candidate on production data because of resource and time constraints. The data science team can instead use production data for model development. The candidate model registered from the development loop is evaluated for production. This phase takes place in one or more dedicated and secure Machine Learning workspaces.
Production deployment
After a model passes the staging and test phase, machine learning engineers can use human-in-the-loop gated approval to promote it to production. Model deployment options include a managed batch endpoint for batch scenarios or either a managed online endpoint or Kubernetes deployment that uses Azure Arc for online, near real-time scenarios. Production typically takes place in one or more dedicated and secure Machine Learning workspaces.
Monitoring
Machine learning engineers monitor components in staging, testing, and production to collect metrics related to changes in performance of the model, data, and infrastructure. They can use those metrics to take action. Model and data monitoring can include checking for model performance on new images. Infrastructure monitoring might identify slow endpoint response, inadequate compute capacity, or network problems.
Data and model monitoring: events and actions
The data and model monitoring and event and action phases of MLOps for natural language processing are the key differences from classical machine learning. Automated retraining is typically not done in CV scenarios when model performance degradation on new images is detected. In this case, a human-in-the-loop process is necessary to review and annotate new images for the model that performs poorly. The next action often goes back to the model development loop to update the model with the new images.
Infrastructure monitoring: events and actions
Automated triggers and notifications can implement appropriate actions to take based on infrastructure criteria, such as an endpoint response lag or insufficient compute for the deployment. Automatic triggers and notifications might trigger a loopback to the setup and administration phase where the infrastructure team can investigate the problem and potentially reconfigure environment, compute, and network resources.
Machine Learning natural language processing architecture
[Diagram for the natural language processing architecture.]
Download a
Visio file
of this architecture.
Workflow for the natural language processing architecture
The Machine Learning natural language processing architecture is based on the classical machine learning architecture, but it has some modifications that are specific to NLP scenarios.
Data estate
This component demonstrates the organization data estate and potential data sources and targets for a data science project. Data engineers are the primary owners of this component in the MLOps v2 lifecycle. The Azure data platforms in this diagram aren't exhaustive or prescriptive. A green check mark indicates sources and targets that represent recommended best practices that are based on the customer use case.
Administration and setup
This component is the first step in the MLOps v2 deployment. It consists of all tasks related to the creation and management of resources and roles associated with the project. For natural language processing scenarios, administration and setup of the MLOps v2 environment is largely the same as for classical machine learning, but with an extra step: create text labeling and annotation projects by using the labeling feature of Machine Learning or another tool.
Model development (inner loop phase)
The inner loop phase consists of an iterative data science workflow performed within a dedicated and secure Machine Learning workspace. The typical NLP model development loop differs from the classical machine learning scenario in that the typical development steps for this scenario include annotators for sentences and tokenization, normalization, and embeddings for text data.
Machine Learning registries
After the data science team develops a model that they can deploy to production, they register the model in the Machine Learning workspace registry. CI pipelines that are triggered automatically by model registration or by gated human-in-the-loop approval promote the model and any other model dependencies to the model deployment phase.
Model deployment (outer loop phase)
The model deployment or outer loop phase consists of preproduction staging and testing, production deployment, and monitoring of the model, data, and infrastructure. When the model meets the criteria of the organization and use case, CD pipelines promote the model and related assets through production, monitoring, and potential retraining.
Staging and test
The staging and test phase varies according to customer practices. This phase typically includes operations such as retraining and testing the model candidate on production data, test deployments for endpoint performance, data quality checks, unit testing, and responsible AI checks for model and data bias. This phase takes place in one or more dedicated and secure Machine Learning workspaces.
Production deployment
After a model passes the staging and test phase, machine learning engineers can use human-in-the-loop gated approval to promote it to production. Model deployment options include a managed batch endpoint for batch scenarios or either a managed online endpoint or Kubernetes deployment that uses Azure Arc for online, near real-time scenarios. Production typically takes place in one or more dedicated and secure Machine Learning workspaces.
Monitoring
Machine learning engineers monitor components in staging, testing, and production to collect metrics related to changes in performance of the model, data, and infrastructure. They can use those metrics to take action. Model and data monitoring can include checking for model and data drift, model performance on new text data, and responsible AI problems. Infrastructure monitoring might identify problems, such as slow endpoint response, inadequate compute capacity, and network problems.
Data and model monitoring: events and actions
As with the CV architecture, the data and model monitoring and event and action phases of MLOps for natural language processing are the key differences from classical machine learning. Automated retraining isn't typically done in natural language processing scenarios when model performance degradation on new text is detected. In this case, a human-in-the-loop process is necessary to review and annotate new text data for the model that performs poorly. Often the next action is to go back to the model development loop to update the model with the new text data.
Infrastructure monitoring: events and actions
Automated triggers and notifications can implement appropriate actions to take based on infrastructure criteria, such as an endpoint response lag or insufficient compute for the deployment. Automatic triggers and notifications might trigger a loopback to the setup and administration phase where the infrastructure team can investigate the problem and potentially reconfigure compute and network resources.
Components
Machine Learning
is a cloud service that you can use to train, score, deploy, and manage machine learning models at scale. In this architecture, it's the primary platform for model development, deployment, monitoring, and management throughout the MLOps life cycle.
Azure Pipelines
is a build-and-test system that's based on Azure DevOps and is used for build and release pipelines. Azure Pipelines splits these pipelines into logical steps called
tasks
. In this architecture, it automates and manages CI/CD workflows to help ensure consistent deployment and testing of machine learning solutions.
GitHub
is a code-hosting platform. In this architecture, GitHub is the central repository for source code, version control, and collaboration. It integrates with CI/CD pipelines for automation.
Azure Arc
is a platform that uses Azure Resource Manager to manage Azure resources and on-premises resources. The resources can include virtual machines, Kubernetes clusters, and databases. In this architecture, Azure Arc provides unified management and governance for hybrid and multicloud machine learning environments.
Kubernetes
is an open-source system that you can use to automate the deployment, scaling, and management of containerized applications. In this architecture, Kubernetes orchestrates containerized machine learning workloads to enable scalable, efficient, and resilient deployments.
Azure Data Lake Storage
is a Hadoop-compatible file system. It has an integrated hierarchical namespace and the massive scale and economy of Blob Storage. In this architecture, it stores and manages large volumes of structured and unstructured data for machine learning workflows.
Microsoft Fabric
is a unified platform that can meet your organization's data and analytics needs. In this architecture, Fabric facilitates end-to-end data integration, preparation, and analytics to support the data estate component of MLOps.
Azure Event Hubs
is a service that ingests data streams that client applications generate. In this architecture, Event Hubs ingests and stores real-time streaming data to enable data capture and analysis for machine learning pipelines. Customers can connect to the hub endpoints to retrieve messages for processing. This architecture uses Data Lake Storage integration.
Other considerations
The preceding MLOps v2 architectural pattern has several critical components, including Azure RBAC that aligns with business stakeholders, efficient package management, and robust monitoring mechanisms. These components collectively contribute to the successful implementation and management of machine learning workflows.
Persona-based Azure RBAC
It's crucial that you manage access to machine learning data and resources. Azure RBAC provides a robust framework to help you manage who can take specific actions and access specific areas within your solution. Design your identity segmentation strategy to align with the lifecycle of machine learning models in Machine Learning and the personas included in the process. Each persona has a specific set of responsibilities that are reflected in their Azure RBAC roles and group membership.
Example personas
To support appropriate segmentation in a machine learning workload, consider the following common personas that inform the
identity-based Azure RBAC
group design.
Data scientist and machine learning engineer
Data scientists and machine learning engineers do various machine learning and data science activities across the software development life cycle of a project. Their duties include exploratory data analysis and data preprocessing. Data scientists and machine learning engineers are responsible for training, evaluating, and deploying models. These roles' responsibilities also include break-fix activities for machine learning models, packages, and data. These duties are out of scope for the platform's technical support team.
Type:
Person
Project specific:
Yes
Data analyst
Data analysts provide the necessary input for data science activities, such as running SQL queries for business intelligence. This role's responsibilities include working with data, performing data analysis, and supporting model development and model deployment.
Type:
Person
Project specific:
Yes
Model tester
Model testers conduct tests in testing and staging environments. This role provides functional segregation from the CI/CD processes.
Type:
Person
Project specific:
Yes
Business stakeholders
Business stakeholders are associated with the project, such as a marketing manager.
Type:
Person
Project specific:
Yes
Project lead or data science lead
The data science lead is a project administration role for the Machine Learning workspace. This role also does break-fix activities for the machine learning models and packages.
Type:
Person
Project specific:
Yes
Project or product owner (Business owner)
Business stakeholders are responsible for the Machine Learning workspace according to data ownership.
Type:
Person
Project specific:
Yes
Platform technical support
Platform technical support is the technical support staff responsible for break-fix activities across the platform. This role covers infrastructure or service but not the machine learning models, packages, or data. These components remain under the data scientist or machine learning engineer role and are the project lead's responsibility.
Type:
Person
Project specific:
No
Model end user
Model end users are the end consumers of the machine learning model.
Type:
Person or Process
Project specific:
Yes
CI/CD processes
CI/CD processes release or roll back changes across platform environments.
Type:
Process
Project specific:
No
Machine Learning workspace
Machine Learning workspaces use
managed identities
to interact with other parts of Azure. This persona represents the various services that make up a Machine Learning implementation. These services interact with other parts of the platform, such as the development workspace that connects with the development data store.
Type:
Process
Project specific:
No
Monitoring processes
Monitoring processes are compute processes that monitor and alert based on platform activities.
Type:
Process
Project specific:
No
Data governance processes
Data governance processes scan the machine learning project and data stores for data governance.
Type:
Process
Project specific:
No
Microsoft Entra group membership
When you implement Azure RBAC,
Microsoft Entra groups
provide a flexible and scalable way to manage access permissions across different personas. You can use Microsoft Entra groups to manage users

## Metadata
- **Source URL**: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/machine-learning-operations-v2
