# Backend Engineering from First Principles (FastAPI Edition)

This repository is a hands-on, concept-driven exploration of backend engineering,
implemented using **FastAPI** as an execution layer and learning scaffold.

The focus of this project is **not** FastAPI itself.

The goal is to deeply understand **how backend systems work** — HTTP, routing,
serialization, authentication, databases, caching, concurrency, reliability,
and scaling — while being explicit about what the framework abstracts away.

A future iteration of this repository will reimplement the same concepts in Go
to expose lower-level system behavior and tradeoffs.

---

## Why This Repository Exists

Most backend tutorials teach *how to build an API*.

This repository is about understanding:

- Why HTTP behaves the way it does
- How requests flow through a backend system
- Where frameworks help and where they hide complexity
- How production concerns (reliability, observability, security) emerge naturally
- What changes when you scale, parallelize, or distribute a system

This is a **backend engineering lab**, not a CRUD demo.

---

## Learning Philosophy

- **Concepts over frameworks**
- **Explicit over magical**
- **System boundaries over convenience**
- **Production concerns from day one**

FastAPI is used intentionally as a **tool**, not a dependency on understanding.

---

## Tech Stack

- Language: Python
- Framework: FastAPI
- Database: PostgreSQL
- Cache: Redis
- Search: Elasticsearch

Framework features are used only after the underlying concept is understood.

---

## Repository Structure

Each folder represents a **core backend concept**.
Every module contains:
- A minimal, focused implementation
- Clear separation of responsibilities
- Documentation explaining tradeoffs and abstractions

