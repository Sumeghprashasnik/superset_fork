<!--
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
-->

# Application Description

## Overview

Apache Superset is an open-source, enterprise-ready data exploration and visualization
platform. It enables users to build interactive dashboards and perform ad-hoc data
analysis without writing code, while also providing a powerful SQL IDE for advanced
querying.

## Core Functionality

### Data Visualization & Dashboards

- **No-code chart builder (Explore):** A drag-and-drop interface that lets analysts
  create visualizations by selecting datasets, dimensions, metrics, and chart types.
- **Interactive dashboards:** Assemble multiple charts into rich, filterable dashboards
  with cross-filtering, drill-down, and periodic refresh.
- **Wide visualization library:** Over 40 chart types powered by Apache ECharts and
  extensible via a plugin architecture—bar charts, line charts, pivot tables, maps,
  geospatial plots, treemaps, and more.

### SQL IDE (SQL Lab)

- **Web-based SQL editor** with syntax highlighting, autocomplete, and query history.
- **Multi-tab interface** for running concurrent queries against different databases.
- **Result visualization:** Instantly chart query results or save them as datasets for
  further exploration.
- **Query sharing and scheduling** for collaboration and automated reporting.

### Semantic Layer

- **Datasets (virtual and physical):** Define reusable metric definitions and dimension
  labels on top of raw tables, creating a governed analytical vocabulary.
- **Calculated columns and metrics:** Express business logic as SQL expressions stored
  at the dataset level.

### Database Connectivity

- Connects to any SQL-speaking data source with a Python DB-API driver and SQLAlchemy
  dialect.
- Supports 40+ databases out of the box: PostgreSQL, MySQL, Snowflake, BigQuery,
  Redshift, Trino, ClickHouse, DuckDB, Databricks, Apache Druid, and many more.

## Key Features

| Category | Details |
|----------|---------|
| **Security** | Role-based access control (RBAC), row-level security (RLS), and integration with OAuth, LDAP, and other authentication providers. |
| **Caching** | Configurable caching layer (Redis/Memcached) to reduce database load and speed up dashboard rendering. |
| **Async queries** | Long-running queries are offloaded to Celery workers with real-time status updates via a WebSocket service. |
| **REST API** | Full programmatic access to charts, dashboards, datasets, and database connections for automation and embedding. |
| **Alerts & Reports** | Schedule email/Slack alerts triggered by data conditions, and periodic PDF/PNG reports of dashboards. |
| **Feature flags** | Granular control over feature rollouts and experimental capabilities. |
| **Extensibility** | Plugin system for custom visualizations, database engines, and authentication backends. |
| **Cloud-native architecture** | Horizontally scalable; deployable via Docker, Kubernetes (Helm charts), or traditional server setups. |
| **Internationalization** | Translated into multiple languages for global teams. |

## Technology Stack

| Layer | Technologies |
|-------|-------------|
| **Backend** | Python, Flask, SQLAlchemy, Celery, Redis |
| **Frontend** | TypeScript, React, Redux, Ant Design, Apache ECharts |
| **Build & Tooling** | Webpack, Jest, Playwright, Docker, Helm |
| **Documentation** | Docusaurus |

## Repository Structure

```
superset/              → Python backend (APIs, models, security, queries)
superset-frontend/     → React/TypeScript SPA (dashboards, charts, SQL Lab)
superset-websocket/    → Node.js sidecar for async query status
helm/                  → Kubernetes Helm deployment charts
docs/                  → Project documentation (Docusaurus)
tests/                 → Backend test suite (pytest)
```

## Getting Started

- **Docker Compose:** `docker compose up` provides a local instance in minutes.
- **Developer setup:** See the [Contributing Guide](https://superset.apache.org/developer-docs/).
- **Production deployment:** Use the official [Docker image](https://hub.docker.com/r/apache/superset) or [Helm chart](helm/superset).
