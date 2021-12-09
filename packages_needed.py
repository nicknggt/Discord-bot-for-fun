def pip_install(package):
  import subprocess
  import sys
  subprocess.check_call([sys.executable, "-m", "pip", "install", package])