    
import pathlib


prompts_path = pathlib.Path("prompts")

class NeuronPrompts(object):
    def __init__(self):
        self.A1 = self.read_text(prompts_path / 'A1.xml')
        self.A2 = self.read_text(prompts_path / 'A2.xml')
        self.B = self.read_text(prompts_path / 'B.xml')
        self.C = self.read_text(prompts_path / 'C.xml')

    @classmethod
    def read_text(cls, path: str) -> str:
        with open(path, mode='r') as f:
            return "".join(f.readlines())
    