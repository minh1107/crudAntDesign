import re
from typing import Dict, Sequence, List, Optional

from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.middlewares.ratelimit import Rule
from app.middlewares.ratelimit.types import ASGIApp
from app.service.endpoint_pattern_service import get_endpoint_pattern_map_user_limit
from helper.logger_helper import LoggerSimple

logger = LoggerSimple(name=__name__).logger

LST_LIMIT_ENDPOINT_RULE = None


def on_blocked(exc: Exception) -> ASGIApp:
    return JSONResponse({"message": "Limit exceeded"}, status_code=401)


def get_group_by_user_id(user_id) -> str:
    return f"group_{user_id}"


def get_user_str_by_user_id(user_id) -> str:
    return f"user_{user_id}"


class EndpointLimitRule(BaseModel):
    endpoint: str
    lst_limit_rule: List[Rule] = []


def cache_lst_limit_endpoint_rule():
    global LST_LIMIT_ENDPOINT_RULE
    LST_LIMIT_ENDPOINT_RULE = []
    endpoint_pattern_map_user_limit = get_endpoint_pattern_map_user_limit()
    for endpoint_pattern in endpoint_pattern_map_user_limit.keys():
        lst_user_endpoint_limit = endpoint_pattern_map_user_limit.get(endpoint_pattern, [])
        if len(lst_user_endpoint_limit) > 0:
            lst_limit_rule = []
            for user_endpoint_limit in lst_user_endpoint_limit:
                lst_limit_rule.append(Rule(
                    group=get_group_by_user_id(user_endpoint_limit.get('user_id')),
                    second=user_endpoint_limit.get('second', None),
                    minute=user_endpoint_limit.get('minute', None),
                    hour=user_endpoint_limit.get('hour', None),
                    day=user_endpoint_limit.get('day', None),
                    month=user_endpoint_limit.get('month', None),
                    block_time=user_endpoint_limit.get('block_time', None),
                    zone=user_endpoint_limit.get("key", None)
                ))
            LST_LIMIT_ENDPOINT_RULE.append(EndpointLimitRule(
                endpoint=fr"{endpoint_pattern}",
                lst_limit_rule=lst_limit_rule
            ))
    logger.info(f"loaded {len(LST_LIMIT_ENDPOINT_RULE)} endpoint pattern rule to memcache")


def get_lst_limit_endpoint_rule() -> Optional[List[EndpointLimitRule]]:
    global LST_LIMIT_ENDPOINT_RULE
    if LST_LIMIT_ENDPOINT_RULE is None:
        return []
    return LST_LIMIT_ENDPOINT_RULE


def get_limit_rule_config() -> Dict[re.Pattern, Sequence[Rule]]:
    rule_config = get_lst_limit_endpoint_rule()
    return {
        re.compile(x.endpoint): x.lst_limit_rule for x in rule_config
    }
