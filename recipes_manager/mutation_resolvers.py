from typing import Any, Dict, Optional

from tartiflette import Resolver

from recipes_manager.data import RECIPES


@Resolver('Mutation.updateRecipe')
async def resolve_mutation_update_recipe(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: 'ResolveInfo',
) -> Dict[str, Any]:
    recipe_id = args['input']['id']
    name = args['input'].get('name')
    cooking_time = args['input'].get('cookingTime')

    if not (name or cooking_time):
        raise Exception(
            'You should provide at least one value for either name or cookingTime'
        )
    for index, recipe in enumerate(RECIPES):
        if recipe['id'] == recipe_id:
            if name:
                RECIPES[index]['name'] = name
            
            if cooking_time:
                RECIPES[index]['cookingTime'] = cooking_time
            return RECIPES[index]

    raise Exception(f'The recipe < {recipe_id}> does not exist')

