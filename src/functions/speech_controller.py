import asyncio

from mini.apis.api_expression import PlayExpression
from mini.apis.api_sound import StartPlayTTS
from mini.apis.api_action import PlayAction
from mini.mini_sdk import translate
from mini.apis.api_config import LanType, ServicePlatform
from src.functions.utils import logger, safe_api_call
from src.functions.sound_controller import SoundController

class SpeechController:
    def __init__(self, sound_controller: SoundController):
        self.useCoquiTTS = True
        self.sound_controller = sound_controller

    @safe_api_call()
    async def speak(self, text: str):
        """Robot speaks."""
        result_type, response = await StartPlayTTS(text=text).execute()
        if not response or not response.isSuccess:
            logger.warning(f"TTS failed with code: {getattr(response, 'resultCode', 'Unknown')}")
        else:
            logger.info(f"TTS succeeded: {text}")

    @safe_api_call()
    async def speak_with_action(self, text: str, action_name: str):
        """Speak while performing an action."""
        tts = asyncio.create_task(StartPlayTTS(text=text).execute())
        action = asyncio.create_task(PlayAction(action_name=action_name).execute())
        await asyncio.gather(tts, action)
        logger.info(f"Speaking '{text}' with action '{action_name}'")

    @safe_api_call()
    async def speak_with_expression(self, text: str, expression_name: str):
        """Speak while performing an expression."""
        tts = asyncio.create_task(StartPlayTTS(text=text).execute())
        expression = asyncio.create_task(PlayExpression(expression_name=expression_name).execute())
        await asyncio.gather(tts, expression)
        logger.info(f"Speaking '{text}' with expression '{expression_name}'")

    @safe_api_call()
    async def translate_and_speak(self, text: str, from_lang: LanType = LanType.EN, to_lang: LanType = LanType.NL,
                                  platform: ServicePlatform = ServicePlatform.GOOGLE):
        """Translate and speak text."""
        succes = await translate(text, from_lang, to_lang, platform)
        if not succes:
            logger.warning(f"Translation failed with code: {getattr(succes, 'resultCode', 'Unknown')}")
            return
        logger.info(f"Translation succeeded: {text}")

    @safe_api_call()
    async def translate_and_speak_with_action(self, text: str, action_name: str, from_lang: LanType = LanType.EN, to_lang: LanType = LanType.NL,
                                  platform: ServicePlatform = ServicePlatform.GOOGLE):
        """Translate and speak text."""
        translation = asyncio.create_task(translate(text, from_lang, to_lang, platform))
        action = asyncio.create_task(PlayAction(action_name=action_name).execute())
        succes = await translate(text, from_lang, to_lang, platform)
        if not succes:
            logger.warning(f"Translation failed with code: {getattr(succes, 'resultCode', 'Unknown')}")
            return
        logger.info(f"Translation succeeded: {text}")

