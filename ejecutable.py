from cx_Freeze import setup, Executable

setup( name = "QRDP",
           version = "0.1" ,
           description = "bursoft" ,
           executables = [Executable("QRDP.py",),], )
