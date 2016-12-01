from cx_Freeze import setup, Executable

includefiles = []

includes = ['NumericalSemigroupClass', 'GameStateClass', 'Data', 'ReceiveGensFunctions']
excludes = []
packages = []

exe = Executable(
    script = r"SylverPlayer.py"
    )
setup( name = 'Revision',
      version = '0.1',
      description = 'Revision program for studying',
      author = '',
      author_email = '',
      options = {'build_exe': {'includes': includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
      executables = [Executable('SylverPlayer.py')])
