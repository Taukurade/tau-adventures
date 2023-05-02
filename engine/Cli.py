from dataclasses import dataclass

class Colorize:
    @dataclass
    class ForegroundColor:
        red: int
        green: int
        blue: int
        
        def __str__(self):
            return f"\033[38;2;{self.red};{self.green};{self.blue}m"

    @dataclass
    class BackgroundColor:
        red: int
        green: int
        blue: int
        
        def __str__(self):
            return f"\033[48;2;{self.red};{self.green};{self.blue}m"

    @dataclass
    class Decorations:
        bold:bool = False
        italic:bool = False
        underline:bool = False
        strikethrough:bool = False

        def __str__(self) -> str:
            x = []
            if self.bold: x.append('1')
            if self.italic: x.append('3')
            if self.underline: x.append('4')
            if self.strikethrough: x.append('9')
            if len(x) > 0:return f"\033[{';'.join(x)}m"
            return ""
    def reset():
        return "\033[0m"



class ColorfulCLI:




    def c_string(string:str,params:set[Colorize,Colorize.ForegroundColor,Colorize.BackgroundColor,Colorize.Decorations]):
        
        return f"{params[1]}{params[2]}{params[3]}{string}{params[0].reset()}"
