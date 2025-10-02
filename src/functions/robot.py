import logging
from mini import mini_sdk as MiniSdk
from mini.dns.dns_browser import WiFiDevice

class Robot:

    robot_ip = None

    def __init__(self, name="AlphaMiniRobin"):
        self.robot_name = name

    def setup_sdk(self):
        MiniSdk.set_log_level(logging.INFO)
        MiniSdk.set_robot_type(MiniSdk.RobotType.EDU)

    def get_device(self, ip: str) -> WiFiDevice:
        self.robot_ip = ip
        return WiFiDevice(self.robot_name, ip)

    async def connect_robot(self, device: WiFiDevice):
        await MiniSdk.connect(device)

    async def start_programming(self):
        await MiniSdk.enter_program()

    async def stop_programming(self):
        await MiniSdk.quit_program()
        await MiniSdk.release()