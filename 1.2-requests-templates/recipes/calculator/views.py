from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet(request):
    if not request.GET.get("servings"):
        context = {"recipe": DATA.get("omlet")}
    else:
        servings = int(request.GET.get("servings"))
        omlet_recipe = {}
        for ingredient, amount in DATA.get("omlet").items():
            omlet_recipe[ingredient] = amount * servings
        context = {"recipe": omlet_recipe}
    return render(request, "calculator/index.html", context)


def pasta(request):
    if not request.GET.get("servings"):
        context = {"recipe": DATA.get("pasta")}
    else:
        servings = int(request.GET.get("servings"))
        pasta_recipe = {}
        for ingredient, amount in DATA.get("pasta").items():
            pasta_recipe[ingredient] = amount * servings
        context = {"recipe": pasta_recipe}
    return render(request, "calculator/index.html", context)


def buter(request):
    if not request.GET.get("servings"):
        context = {"recipe": DATA.get("buter")}
    else:
        servings = int(request.GET.get("servings"))
        buter_recipe = {}
        for ingredient, amount in DATA.get("buter").items():
            buter_recipe[ingredient] = amount * servings
        context = {"recipe": buter_recipe}
    return render(request, "calculator/index.html", context)

