import cx_Freeze

exe = [cx_Freeze.Executable("colecao_robos_ipe_v1.py", base = "Win32GUI")]
#exe = [cx_Freeze.Executable("colecao_robos_ipe_v1.py")]
cx_Freeze.setup(
    name = "Colecao de Robos v1",
    version = "1.0",
    executables = exe
)