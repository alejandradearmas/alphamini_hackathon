import logging, socket
from functools import wraps

from mini import MiniApiResultType

# Configure logging
logger = logging.getLogger(__name__)

def safe_api_call(raise_on_error=False):
    def decorator(coro_func):
        """Decorator for safely executing async API functions with logging."""
        @wraps(coro_func)
        async def wrapper(*args, **kwargs):
            try:
                return await coro_func(*args, **kwargs)
            except Exception as e:
                logger.exception(f"Error in {coro_func.__name__}: {e}")
                if raise_on_error:
                    raise
                return None
        return wrapper
    return decorator

def is_success(result_type, response) -> bool:
    """Helper to determine API success."""
    return result_type == MiniApiResultType.Success and response and response.isSuccess

def get_laptop_ip_address(ip_address_robot):
    laptop_ip = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((ip_address_robot, 80))
        laptop_ip = s.getsockname()[0]
    finally:
        s.close()
    if laptop_ip is None:
        logger.error("No laptop ip address, so audio cannot be shared to robot.")
    return laptop_ip