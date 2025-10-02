import asyncio
from mini.apis.api_action import PlayAction

from src.enums import Emotion
from src.functions.motion_controller import MotionController
from src.functions.expression_controller import ExpressionController
from src.functions.speech_controller import SpeechController
from src.functions.utils import logger, safe_api_call

class EmotionController:

    def __init__(self, motion_controller: MotionController, expression_controller: ExpressionController, speech_controller: SpeechController):
        self.motion_controller = motion_controller
        self.expression_controller = expression_controller
        self.speech_controller = speech_controller

    @safe_api_call()
    async def express_emotion(self, name: str):
        if name == Emotion.HAPPY:
            await asyncio.gather(self.expression_controller.blink(), self.motion_controller.dance())
            await self.speech_controller.speak("I'm so happy!")
            logger.info("Expressed happiness.")
        elif name == Emotion.SAD:
            await self.motion_controller.move("backward", 5)
            await self.speech_controller.speak("I'm feeling sad...")
            logger.info("Expressed sadness.")
        elif name == Emotion.ANGRY:
            await PlayAction(action_name='angry_action').execute()
            await self.speech_controller.speak("I'm angry!")
            logger.info("Expressed anger.")
        else:
            logger.warning(f"Unknown emotion: {name}")
