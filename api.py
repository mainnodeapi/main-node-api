from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Main Node API",
    version="1.0"
)

class RequestData(BaseModel):
    situation: str
    signals: list[str] = []
    context: str | None = None

class ResponseData(BaseModel):
    main_node: str
    node_type: str
    explanation: str
    first_action: str
    confidence: float
    version: str

@app.post("/v1/find-main-node", response_model=ResponseData)
def find_main_node(data: RequestData):
    text = data.situation.lower()

    if "выбрать" in text or "решить" in text:
        return ResponseData(
            main_node="отсутствие приоритета",
            node_type="structural",
            explanation="Перегрузка вариантов без критерия отбора блокирует движение",
            first_action="Выбрать один приоритет на 7 дней",
            confidence=0.82,
            version="v1.0"
        )

    return ResponseData(
        main_node="неопределённый узел",
        node_type="cognitive",
        explanation="Недостаточно данных для точного определения узла",
        first_action="Уточнить цель и ограничения системы",
        confidence=0.4,
        version="v1.0"
    )
