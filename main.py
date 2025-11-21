from fastapi import FastAPI

app = FastAPI(
    title="DatePlanner AI",
    description="ИИ-ассистент для планирования свиданий Левы и Лены 💕",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Привет! Это DatePlanner AI для Левы и Лены!"}

@app.get("/our-couple")
def our_couple():
    return {
        "couple_name": "Левая и Лена",
        "status": "Самые крутые!",
        "project": "DatePlanner AI"
    }