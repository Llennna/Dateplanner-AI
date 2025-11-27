from fastapi import FastAPI
from app.api.endpoints import users, couples
from app.db.database import create_tables
# Создаем таблицы при старте
create_tables()

app = FastAPI(
    title="DatePlanner AI", 
    description="ИИ-ассистент для планирования свиданий Левы и Лены 💕",
    version="1.0.0"
)


app.include_router(users.router)
app.include_router(couples.router)



@app.get("/")
def read_root():
    return {"message": "Привет! Это DatePlanner AI для Левы и Лены!"}

@app.get("/our-couple")
def our_couple():
    return {
        "couple_name": "Лева и Лена",
        "status": "Самые крутые!",
        "project": "DatePlanner AI",
        "motivation": "Заработать много денег и съехать жить вместе! 💕"
    }

@app.get("/motivation")
def motivation():
    return {
        "message": "Лева, ты сможешь!",
        "progress": "От пиццамейкера до Senior Developer!",
        "goal": "Создать крутой проект с Леной",
        "remember": "Ты уже: Выиграл хакатон, Создал ТГ бота, Сделал спидридер"
    }

@app.get("/debug/users")
def debug_users():
    """Эндпоинт для быстрой проверки что users роутер подключен"""
    return {"message": "Users router is working!"}

@app.get("/debug/couples") 
def debug_couples():
    """Эндпоинт для быстрой проверки что couples роутер подключен"""
    return {"message": "Couples router is working!"}



@app.get("/api/status")
def api_status():
    return {
        "status": "API работает! 🚀",
        "available_endpoints": [
            "/docs - документация",
            "/users/ - создание пользователей", 
            "/couples/ - создание пар",
            "/our-couple - наша пара",
            "/motivation - мотивация"
        ],
        "project_stage": "Active Development",
        "next_features": ["ИИ рекомендации", "Интеграция с картами"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)