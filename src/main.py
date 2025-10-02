import asyncio
import logging
from src.functions.robot import Robot
from interactions import interaction_demo_english

logging.basicConfig(
    level=logging.INFO,  # Use DEBUG for dev
    format="%(asctime)s [%(levelname)s] %(message)s",
)

async def main(ip_address_robot: str):
    robot = Robot()
    robot.setup_sdk()
    device = robot.get_device(ip_address_robot)
    try:
        await robot.connect_robot(device)
        await robot.start_programming()
        await interaction_demo_english.do_introduction_demo_interaction()

    except Exception as e:
        logging.error("An error occurred during robot interaction", exc_info=True)
    finally:
        await robot.stop_programming()

if __name__ == "__main__":
    asyncio.run(main("10.121.0.74"))