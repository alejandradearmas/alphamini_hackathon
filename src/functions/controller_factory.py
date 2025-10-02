from src.functions.action_controller import ActionController
from src.functions.emotion_controller import EmotionController
from src.functions.motion_controller import MotionController
from src.functions.speech_controller import SpeechController
from src.functions.expression_controller import ExpressionController
from src.functions.sound_controller import SoundController

class ControllerFactory:
    def __init__(self):
        self.motion = MotionController()
        self.sound = SoundController()
        self.speech = SpeechController(self.sound)
        self.expression = ExpressionController()
        self.action = ActionController()
        self.emotion = EmotionController(self.motion, self.expression, self.speech)


# Create a global singleton-like instance (optional)
controllers = ControllerFactory()