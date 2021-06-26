from cx_Freeze import setup, Executable

base = None    

executables = [Executable("colecao_robos_ipe_v1.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Coleção de Robos",
    options = options,
    version = "1.0",
    description = 'robo para executar ipe',
    executables = executables
)