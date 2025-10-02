from mini.apis.api_action import PlayAction, MoveRobot
from src.functions.utils import logger, safe_api_call
from src.enums import Direction

class MotionController:

    @safe_api_call()
    async def move(self, direction: str, steps: int):
        dir_enum = Direction(direction.lower()).to_sdk()
        if dir_enum:
            await MoveRobot(step=steps, direction=dir_enum).execute()
            logger.info(f"Moved {direction} for {steps} steps")
        else:
            logger.error(f"Invalid direction: {direction}")

    @safe_api_call()
    async def dance(self, action_name='018'):
        await PlayAction(action_name=action_name).execute()
        logger.info(f"Dancing with action {action_name}")

    @safe_api_call()
    async def turn_left(self):
        await MoveRobot(step=1, direction=Direction.LEFT.to_sdk()).execute()
        logger.info("Turned left.")

    @safe_api_call()
    async def turn_right(self):
        await MoveRobot(step=1, direction=Direction.RIGHT.to_sdk()).execute()
        logger.info("Turned right.")