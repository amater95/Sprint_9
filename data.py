from pathlib import Path


WAITING_TIME = 20
# Данные для создания рецепта
RECIPE_DATA = {
    "dish": 'Биг Хит',
    "ingredients": ['булка', 'говядина', 'сыр', 'салат', 'огурцы'],
    "count": '1',
    "cooking_time": '20',
    "description": 'Булочка с кунжутом, две котлеты с луком, особый соус, сыр, салат и огурцы. Легендарный вид. Это Биг Хит!',
    "photo": str(Path("photos/Big_hit.png").resolve())
}
