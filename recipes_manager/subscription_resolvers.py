import asyncio

from typing import Any, AsyncGenerator, Dict, Optional

from tartiflette import Subscription

from recipes_manager.data import RECIPES


@Subscription('Subscription.launchAndWaitCookingTimer')
async def subscribe_subscription_launch_and_wait_cooking_timer(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: 'ResolveInfo',
) -> AsyncGenerator[Dict[str, Any], None]:
    recipe = None
    for recipe_item in RECIPES:
        if recipe_item['id'] == args['id']:
            recipe = recipe_item

    if not recipe:
        raise Exception(f'The recipe < {args["id"]} > does not exist.')

    for i in range(recipe['cookingTime']):
        yield {
            'launchAndWaitCookingTimer': {
                'remainingTime': recipe['cookingTime'] - i,
                'status': 'COOKING',
            }
        }
        await asyncio.sleep(1)

    yield {'launchAndWaitCookingTimer': {'remainingTime': 0, 'status': 'COOKED'}}

