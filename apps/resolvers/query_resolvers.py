import datetime

from typing import Any, Dict, List, Optional

from tartiflette import Resolver

from apps import db


@Resolver('Query.questions')
async def resolve_query_questions(
    parent: Optional[Any],
    args: Dict[str, Any],
    ctx: Dict[str, Any],
    info: 'ResolverInfo'
) -> List[Dict[str, Any]]:
    '''
    something that
    '''
    async with ctx['app']['db'].acquire() as conn:
        cursor = await conn.execute(db.question.select())
        records = await cursor.fetchall()

    return records
