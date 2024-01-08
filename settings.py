import pathlib
import os
from logging.config import dictConfig
from dotenv import load_dotenv
import discord
import logging

load_dotenv()

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
MONGO_TOKEN = os.getenv("MONGO_TOKEN")
API_KEY= os.getenv("API_KEY")
BASE_DIR = pathlib.Path(__file__).parent

 
COGS_DIR = BASE_DIR / "cogs"

GUILDS_ID = discord.Object(id=int(os.getenv("GUILD")))


LOGGING_CONFIG = {
    "version": 1, 
    "disabled_existing_loggers": False, 
    "formatters":{
        "verbose":{
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format": "%(levelname)-5s - %(name)-5s : %(message)s"
        }
    }, 
    "handlers":{
        "console": {
            'level': "DEBUG", 
            'class': "logging.StreamHandler",
            'formatter': "standard"
        }, 
        "console2": {
            'level': "WARNING", 
            'class': "logging.StreamHandler",
            'formatter': "standard"
        }, 
        "file": {
            'level': "INFO", 
            'class': "logging.FileHandler",
            'filename': "logs/infos.log",
            'mode': "w", 
            'formatter': "verbose"
        }, 
    }, 
    "loggers":{
        "bot": {
            'handlers': ['console'],
            "level": "INFO", 
            "propagate": False
        }, 
        "discord": {
            'handlers': ['console2', "file"],
            "level": "INFO", 
            "propagate": False
        }
    }
}

dictConfig(LOGGING_CONFIG)