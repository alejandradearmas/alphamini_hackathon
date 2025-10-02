from mini.apis.api_action import GetActionList, RobotActionType, PlayAction
from src.functions.utils import logger, safe_api_call
from typing import List

class ActionController:

    @safe_api_call()
    async def list_actions(self) -> List[str]:
        """Retrieve all built-in robot actions."""
        action_types = [
            RobotActionType.INNER,
            RobotActionType.CUSTOM
        ]
        results = []
        for at in action_types:
            result_type, response = await GetActionList(action_type=at).execute()
            if response and getattr(response, "actionList", None):
                names = [action.id for action in response.actionList]
                logger.debug(f"Available actions: {names}")
                results.append(names)
            else:
                logger.warning("Failed to retrieve action list or no actions available.")
                results.append([])

        return results

    async def play_action(self, action_name: str):
        """Play an action."""
        await PlayAction(action_name=action_name).execute()
        logger.info(f"Played action {action_name}")