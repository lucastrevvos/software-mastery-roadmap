from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
ROADMAP_PATH = ROOT / "docs" / "data" / "roadmap.json"
PROGRESS_PATH = ROOT / "docs" / "data" / "progress.json"
APP_PATH = ROOT / "docs" / "js" / "app.js"

DATE = "2026-09-28"
CERT_URL = "https://www.freecodecamp.org/certification/lucas-do-amaral-santos/foundational-c-sharp-with-microsoft"
INTERVIEW_AT = "2026-09-30T14:00:00-03:00"
INTERVIEW_TITLE = "XP — entrevista técnica de System Design"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def roadmap_item(roadmap: dict, item_id: str) -> dict:
    for phase in roadmap.get("phases", []):
        for item in phase.get("items", []):
            if item.get("id") == item_id:
                return item
    raise KeyError(f"Roadmap item not found: {item_id}")


def roadmap_phase(roadmap: dict, phase_id: str) -> dict:
    for phase in roadmap.get("phases", []):
        if phase.get("id") == phase_id:
            return phase
    raise KeyError(f"Roadmap phase not found: {phase_id}")


def update_roadmap() -> None:
    roadmap = load_json(ROADMAP_PATH)
    meta = roadmap.setdefault("meta", {})
    meta["version"] = "3.1.0"
    meta["updatedAt"] = DATE
    meta["executionStrategy"] = (
        "Adaptive employment-first roadmap: the .NET 10 / financial distributed-systems window was pulled forward "
        "because of active BTG/XP opportunities. Immediate gate: XP System Design interview on 2026-09-30 at "
        "14:00 BRT using Excalidraw; after the interview, continue the Financial Distributed Systems Lab while "
        "rebalancing the paused JavaScript/SQL tracks."
    )

    principles = meta.setdefault("principles", [])
    old_window_rule = "Aprender em janelas de imersão: Node/TypeScript primeiro, .NET depois, frontend profundo em etapa própria"
    new_window_rule = (
        "Sequenciamento adaptativo: oportunidades reais de mercado podem antecipar uma janela de stack sem abandonar "
        "os fundamentos; a prioridade imediata é o menor caminho para competência demonstrável e empregabilidade."
    )
    if old_window_rule in principles:
        principles[principles.index(old_window_rule)] = new_window_rule
    elif new_window_rule not in principles:
        principles.append(new_window_rule)

    phase = roadmap_phase(roadmap, "phase-06")
    phase["title"] = ".NET 10 & Financial Distributed Systems — Active Backend Window"
    phase["goal"] = (
        "A janela .NET foi antecipada por oportunidades reais em sistemas financeiros. Consolidar C#/.NET 10 em "
        "backend e sistemas distribuídos, praticar defesa arquitetural e system design, e manter Azure como eixo cloud "
        "da trilha. O laboratório deve introduzir padrões porque o problema exige, não como checklist."
    )

    csharp = roadmap_item(roadmap, "foundational-csharp")
    csharp["status"] = "completed"
    csharp["completedAt"] = DATE
    csharp["credentialUrl"] = CERT_URL
    csharp["note"] = (
        "Concluído e certificado em 2026-09-28. Usado como revisão/validação formal da linguagem antes da janela "
        ".NET 10 focada em backend, sistemas distribuídos e system design."
    )
    csharp.setdefault("access", {}).setdefault("credential", {})["url"] = CERT_URL

    dotnet = roadmap_item(roadmap, "dotnet-backend")
    dotnet["status"] = "in-progress"
    dotnet["startedAt"] = DATE
    dotnet["priority"] = "active-senior-interview"
    dotnet["description"] = (
        "Financial Distributed Systems Lab em .NET 10: ASP.NET Core, testes, DDD, Clean Architecture, CQRS quando "
        "justificado, PostgreSQL, RabbitMQ, confiabilidade distribuída, containers, Kubernetes, observabilidade, "
        "CI/CD e defesa arquitetural."
    )
    dotnet["currentFocus"] = [
        ".NET 10 / ASP.NET Core",
        "TDD, unit, integration and architecture tests",
        "DDD and domain invariants",
        "Clean Architecture / Ports and Adapters when justified",
        "CQRS when read/write models genuinely diverge",
        "PostgreSQL",
        "RabbitMQ with explicit ACK/NACK, prefetch and redelivery semantics",
        "Idempotency, Inbox, Transactional Outbox, Retry and DLQ",
        "Eventual consistency, Saga/Process Manager and compensation",
        "Resilience, timeouts and circuit breakers",
        "Docker and local Kubernetes",
        "OpenTelemetry, logs, metrics and traces",
        "CI/CD and production-readiness",
        "Architecture-defense drills under changing constraints",
    ]
    dotnet["activeSprint"] = {
        "title": "XP System Design Interview Sprint",
        "status": "in-progress",
        "deadline": INTERVIEW_AT,
        "tool": "Excalidraw",
        "format": "Live system design + architecture defense with senior interviewers",
        "domains": ["credit", "collections", "payments"],
        "objective": (
            "Desenhar uma solução enquanto explica decisões, limites de consistência, source of truth, integração "
            "síncrona/assíncrona, escalabilidade, duplicidade, falhas, observabilidade e trade-offs."
        ),
        "questionPressure": [
            "Why RabbitMQ instead of Kafka or synchronous HTTP?",
            "What is the source of truth?",
            "What happens if the same event arrives twice?",
            "What happens if the database commits and the broker is unavailable?",
            "Where is strong consistency required and where is eventual consistency acceptable?",
            "How does the system scale and how is it observed in production?",
            "Does this need CQRS or microservices at all?",
        ],
    }

    for paused_id in ("fcc-js-v10", "cs50-sql"):
        item = roadmap_item(roadmap, paused_id)
        item["status"] = "paused"
        item["pauseReason"] = "Pausa tática para o sprint de System Design da XP."
        item["resumeAfter"] = "2026-09-30"

    save_json(ROADMAP_PATH, roadmap)


def update_progress() -> None:
    progress = load_json(PROGRESS_PATH)
    now = datetime.now(ZoneInfo("America/Sao_Paulo")).replace(microsecond=0).isoformat()
    progress["updatedAt"] = now

    courses = progress.setdefault("courses", {})
    csharp = courses.setdefault("foundational-csharp", {})
    csharp.update(
        {
            "status": "completed",
            "started": True,
            "completed": ["course-complete", "certification-exam-passed"],
            "current": None,
            "completedAt": DATE,
            "certificateUrl": CERT_URL,
            "notes": [
                "A janela C# foi antecipada devido a processos seletivos .NET em sistemas financeiros.",
                "Foundational C# with Microsoft concluído em 2026-09-28.",
                f"Certificação verificável: {CERT_URL}",
                "Conclusão do curso é evidência de validação formal; domínio aplicado será comprovado no Financial Distributed Systems Lab.",
            ],
        }
    )

    for paused_id in ("fcc-js-v10", "cs50-sql"):
        if paused_id in courses:
            courses[paused_id]["status"] = "paused"
            notes = courses[paused_id].setdefault("notes", [])
            pause_note = "Pausa tática em 2026-09-28 até a entrevista técnica da XP em 2026-09-30 às 14h; retomar após o sprint de System Design."
            if pause_note not in notes:
                notes.append(pause_note)

    courses["dotnet-backend"] = {
        "status": "in-progress",
        "started": True,
        "startedAt": DATE,
        "completed": [],
        "current": "XP System Design Interview Sprint — architecture defense in Excalidraw",
        "notes": [
            "Financial Distributed Systems Lab em .NET 10 iniciado como trilha aplicada de senioridade.",
            "Prioridade imediata: entrevista técnica da XP em 2026-09-30 às 14h.",
            "Formato esperado: desenhar system design no Excalidraw e defender decisões/trade-offs sob questionamento de seniors.",
            "Domínios de treino: crédito, cobrança e pagamentos.",
        ],
        "interview": {
            "company": "XP",
            "type": "technical-system-design",
            "scheduledAt": INTERVIEW_AT,
            "tool": "Excalidraw",
            "status": "scheduled",
        },
        "lab": {
            "title": "Financial Distributed Systems Lab — .NET 10",
            "method": "AMS — Adaptive Mastery Scaffolding",
            "status": "in-progress",
        },
    }

    progress["current"] = "dotnet-backend"
    progress["currentTask"] = "XP System Design Interview Sprint — Excalidraw architecture defense"
    progress["currentTaskUrl"] = None

    strategy = progress.setdefault("strategy", {})
    strategy["mode"] = "adaptive-employment-first"
    strategy["currentPrimary"] = "dotnet-backend"
    strategy["currentComplementary"] = None
    strategy["immediateGate"] = {
        "title": INTERVIEW_TITLE,
        "scheduledAt": INTERVIEW_AT,
        "tool": "Excalidraw",
        "focus": "System Design + architecture defense",
    }
    strategy["pausedUntilGate"] = ["fcc-js-v10", "cs50-sql"]
    strategy["afterGate"] = (
        "Continue Financial Distributed Systems Lab in .NET 10 and rebalance JavaScript/SQL according to interview outcome and active opportunities."
    )

    save_json(PROGRESS_PATH, progress)


def update_dashboard_labels() -> None:
    source = APP_PATH.read_text(encoding="utf-8")
    source = source.replace(
        "({'in-progress':'em andamento','not-started':'não iniciado','completed':'concluído','mastered':'dominado'}[status]||status)",
        "({'in-progress':'em andamento','not-started':'não iniciado','completed':'concluído','mastered':'dominado','paused':'pausado'}[status]||status)",
    )
    source = source.replace(
        "<h3>${id==='cs50x'?'CS50x':id==='fcc-js-v10'?'freeCodeCamp JavaScript':id}</h3>",
        "<h3>${id==='cs50x'?'CS50x':id==='fcc-js-v10'?'freeCodeCamp JavaScript':id==='cs50-sql'?'CS50 SQL':id==='foundational-csharp'?'Foundational C# with Microsoft':id==='dotnet-backend'?'.NET 10 · Financial Distributed Systems Lab':id}</h3>",
    )
    APP_PATH.write_text(source, encoding="utf-8")


def validate() -> None:
    roadmap = load_json(ROADMAP_PATH)
    progress = load_json(PROGRESS_PATH)

    csharp = roadmap_item(roadmap, "foundational-csharp")
    dotnet = roadmap_item(roadmap, "dotnet-backend")
    assert csharp["status"] == "completed"
    assert csharp["credentialUrl"] == CERT_URL
    assert dotnet["status"] == "in-progress"
    assert dotnet["activeSprint"]["deadline"] == INTERVIEW_AT
    assert progress["courses"]["foundational-csharp"]["status"] == "completed"
    assert progress["courses"]["dotnet-backend"]["interview"]["scheduledAt"] == INTERVIEW_AT
    assert progress["current"] == "dotnet-backend"


if __name__ == "__main__":
    update_roadmap()
    update_progress()
    update_dashboard_labels()
    validate()
    print("Roadmap updated: C# completed, XP System Design sprint active, .NET lab started.")
