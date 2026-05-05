# ChaloGhumo: Context-Aware AI Travel Intelligence

ChaloGhumo is a next-generation AI travel recommendation system designed to provide hyper-personalized, context-aware trip suggestions. By synthesizing personal preferences with real-time environmental conditions and societal constraints, ChaloGhumo ensures that users find the best possible trip for their exact situation.

## 🤝 Community Project

This is a joint community project driven by the brilliant and innovative team at **[Aligned Automation](https://www.alignedautomation.com)**. We are committed to pushing the boundaries of AI-driven decision-making in the travel and hospitality sector.

## 🚀 The Vision

Our mission is to move beyond static travel filtering and toward a dynamic "Understanding Engine." We optimize for:

- **Personal Preferences**: Deep alignment with user desires and constraints.
- **Environmental Conditions**: Real-time weather, temperature, and seasonal shifts.
- **Real-World Constraints**: Crowd density, infrastructure availability, and over-tourism mitigation.

## 🛠️ Technical Stack

ChaloGhumo is built on a decoupled, high-performance backend architecture:

- **Core Engine**: FastAPI (Python 3.11+) with Pydantic V2 for strict schema enforcement.
- **AI/LLM**: Gemini 1.5 Pro/Flash via Vertex AI & Google Generative AI SDKs.
- **Vector Memory**: Qdrant for semantic contextual embeddings.
- **Relational Store**: PostgreSQL for destination metadata and user profiles.
- **Event Streaming**: Apache Kafka for real-time signal ingestion.
- **Cache**: Redis for signal entropy and state management.

## 📚 Documentation

Detailed documentation is available in the `/docs` directory:

- [Technical Stack](./docs/tech_stack.md): Detailed architectural choices and Mermaid diagrams.
- [System Ontology](./docs/ontology.md): Core data structures and primitives.
- [Epistemic Foundations](./docs/epistemic_foundations.md): The philosophical and logical framework.
- [Invariants & Entropy](./docs/invariants_and_entropy.md): Safety rules and signal decay management.

## 🏗️ Project Structure

```text
chaloghumo/
├── api/          # API v1 routes and endpoints
├── core/         # Settings and configuration
├── models/       # Database models
├── schemas/      # Pydantic schemas (Strict JSON)
├── services/     # Core logic & Reasoning Engine
├── tests/        # Unit and integration tests
├── main.py       # Application entry point
└── docker-compose.yml
```

## ⚡ Getting Started

### Prerequisites

- Docker & Docker Compose
- Google AI / Vertex AI API Key

### Launch with Docker

1. Clone the repository.
2. Create a `.env` file from `.env.example`:

   ```bash
   cp .env.example .env
   ```

3. Update your `GOOGLE_API_KEY` in the `.env` file.
4. Launch the stack:

   ```bash
   docker-compose up --build
   ```

5. Access the API at `http://localhost:8000`.
6. Interactive API docs are available at `http://localhost:8000/docs`.

---
*Note: This project is in its early developmental stages and will evolve rapidly.*
