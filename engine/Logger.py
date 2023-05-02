from .Cli import ColorfulCLI, Colorize
from .Utils import Map
import os
from datetime import datetime as dt
import json
from dataclasses import dataclass


class Logger:
    def __init__(self) -> None:
        self.config =Map( json.load(open("config/logger.json",'r')))
        os.makedirs(os.path.dirname(self.config.logger.path), exist_ok=True)
        self.log_file = open(self.config.logger.path+"main.log",'a+')
        self.levels = self.config.logger.levels.keys()
        self.stdout = self.config.logger.stdout
        self.init_time = 0#dt.now().timestamp()

        self.log("system","Logger")
        
        
        
    def log(self,level:str,message:str):
        if level in self.levels:
            formated = self.config.logger.levels[level].format.format(
                        tag=level,
                        timestamp=int(dt.now().timestamp()-self.init_time),
                        message=message
                        )
            if self.stdout:                
                print(
                    ColorfulCLI.c_string(formated,(
                            Colorize,
                            Colorize.ForegroundColor(*self.config.logger.levels[level].color.foreground),
                            Colorize.BackgroundColor(*self.config.logger.levels[level].color.background) if self.config.logger.levels[level].color.background else "",
                            Colorize.Decorations(**self.config.logger.levels[level].color.decorations)))
                        
                        )
            self.log_file.write(formated)

        else: raise ValueError("There is no '?' level".format(level))


    