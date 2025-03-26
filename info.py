from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "7737048829"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://unitedcamps.in/Images/IMG_1739470067.jpg")
API_ID = int(getenv("API_ID", "10660564"))
API_HASH = str(getenv("API_HASH", "527e6297989f4e7cda5091f5bf41d0e4"))
BOT_TOKEN = str(getenv("BOT_TOKEN", ""))
FORCE_SUB = os.environ.get("FORCE_SUB", "Radha_Rani_Backup") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://dasniru929:dasniru123@cluster0.51p5e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",))
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
