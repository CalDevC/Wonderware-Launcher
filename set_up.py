import os
import vars

# Create aliases folder
os.chdir('/')
os.makedirs('aliases')


# Create macros
os.system(f'doskey maker=python {vars.PROGRAM_LOCATION}/main.py --maker')
os.system(f'doskey viewer=python {vars.PROGRAM_LOCATION}/main.py --viewer')

# Save macros
os.system('doskey /macros>C:/aliases/macros.doskey')
os.system('reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /d "doskey /macrofile=\"C:/aliases/macros.doskey\"" /f')
