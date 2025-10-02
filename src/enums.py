from enum import Enum
from mini.apis.api_action import MoveRobotDirection

class Emotion(str, Enum):
    HAPPY = "happy"
    SAD = "sad"
    ANGRY = "angry"

class Direction(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    FORWARD = "forward"
    BACKWARD = "backward"

    def to_sdk(self) -> MoveRobotDirection:
        return {
            Direction.LEFT: MoveRobotDirection.LEFTWARD,
            Direction.RIGHT: MoveRobotDirection.RIGHTWARD,
            Direction.FORWARD: MoveRobotDirection.FORWARD,
            Direction.BACKWARD: MoveRobotDirection.BACKWARD,
        }[self]