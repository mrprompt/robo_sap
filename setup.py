import cx_Freeze

exe = [cx_Freeze.Executable("robo_extracao_FBL3N_IPE_v2.py", base = "Win32GUI")] # <-- HERE

cx_Freeze.setup(
    name = "Robo Extracao FBL3N IPE v2",
    version = "2.0",
    executables = exe
)