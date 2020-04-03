from typing import Any, Dict, List, Optional

from tartiflette import Resolver

from recipes_manager.data import INGREDITEMS, RECIPES


@Resolver("Query.recipes")
async def resolve_query_recipes(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> List[Dict[str, Any]]:
    """
    Resolver in charge of returning all recipes,
    :param parent: initial value filled in to the engine `execute` method
    :param args: computed arguments related to the field
    :params info: information related to the execution and field resolution
    :type params: Option[ANy]
    :type ctx: Dict[str, Any]
    :return: the list of all recipes
    :rtype: List[Dict[str, Any]]
    """

    return RECIPES


@Resolver("Query.recipe")
async def resolve_query_recipe(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> Optional[Dict[str, Any]]:
    """
    Resolver in charge of returning a recipe depending on the filled in `id`
    :param parent: initial value filled in to the engine `execute` method
    :param args: computed arguments related to the field
    :param ctx: context filled in at engine initialization
    :param info: infomation related to the execution and field resolution 
    :type parent: Option[Any]
    :type args: Dict[str, Any]
    :type ctx: Dict[str, Any]
    :type info: ResolveInfo
    :return: a recipe
    :rtype: List[Dict[str, Any]]
    """
    for recipe in RECIPES:
        if recipe["id"] == args["id"]:
            return recipe

    return None


@Resolver("Recipe.ingredient")
async def resolve_recipe_ingredients(
    parent: Optional[Dict[str, Any]],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: "ResolveInfo",
) -> Optional[List[Dict[str, Any]]]:
    """
    Resolver in charge of returning the ingredient list of a recipe
    :param parent: the recipe for which to return the ingredients
    :param args: computed arguments related to the fields
    :param ctx: context filled in at engine initilization
    :param info: information related to the execution and field resolution
    :type parent: Option[Dict[str, Any]]
    :type args: Dict[str, Any]
    :type ctx: Dict[str, Any]
    :type info: ResolveInfo
    :return: the ingredient list of a recipe
    :rtype: Optional[List[DIct[str, Any]]]
    """
    if parent and parent["id"] in INGREDITEMS:
        return INGREDITEMS[parent["id"]]

    return None
