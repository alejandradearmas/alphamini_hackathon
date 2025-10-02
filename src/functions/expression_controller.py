from mini.apis.api_expression import PlayExpression, SetMouthLamp, MouthLampColor, MouthLampMode
from src.functions.utils import logger, safe_api_call, is_success

class ExpressionController:

    @safe_api_call()
    async def blink(self, duration=1000):
        result_type, response = await SetMouthLamp(
            color=MouthLampColor.WHITE,
            mode=MouthLampMode.BREATH,
            duration=duration,
            breath_duration=500
        ).execute()
        logger.info(f"Blink light response: {response}")

    @safe_api_call()
    async def play_expression(self, expression_name: str) -> bool:
        block = PlayExpression(express_name=expression_name)
        result_type, response = await block.execute()
        if is_success(result_type, response):
            logger.info(f"Played expression: {expression_name}")
            return True
        logger.warning(f"Failed to play expression: {expression_name}")
        return False
