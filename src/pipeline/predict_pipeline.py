from src.exception import CustomException
from src.logger import get_logger
import sys
logger = get_logger(__name__)

if(5==5):
    logger.error('this is false')
    raise CustomException('totally false', sys)