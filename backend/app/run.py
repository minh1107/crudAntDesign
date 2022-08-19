import os

import uvicorn
from dotenv import load_dotenv

from helper.project_helper import get_project_path

if __name__ == "__main__":
    load_dotenv(get_project_path() + '/.env')
    uvicorn.run("main:app", host=os.getenv("HOST", "localhost"),
                port=int(os.getenv("PORT", 8000)),
                log_level="info",
                reload=True)
