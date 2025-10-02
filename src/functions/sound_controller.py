import time
from mini.apis.api_sound import PlayAudio, AudioStorageType
from src.functions.utils import logger, safe_api_call

class SoundController:
    @safe_api_call()
    async def play_online_audio(self, url: str):
        """Play audio from a URL on the Alpha Mini."""
        timestamp = int(time.time())
        url = f"{url}?ts={timestamp}"
        block = PlayAudio(url=url, storage_type=AudioStorageType.NET_PUBLIC)
        result_type, response = await block.execute()
        logger.info(response)
        if not response or not response.isSuccess:
            logger.error(f"Failed to play audio {url}, code: {getattr(response, 'resultCode', 'Unknown')}")
        else:
            logger.info(f"Playing audio on robot: {url}")
        return response
