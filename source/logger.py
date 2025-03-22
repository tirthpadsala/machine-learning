import logging
from datetime import datetime
import os

logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
logFile = f"{datetime.now().strftime('%M_%d_%Y_%H_%M_%S')}.log"
logFilePath = os.path.join(logs_dir, logFile)  

# Configure logging
logging.basicConfig(
    filename=logFilePath,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


