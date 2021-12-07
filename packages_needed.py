#-------------------------------
# pip install
def install_packages():
  import subprocess
  import sys
  def pip_install(package):
      subprocess.check_call([sys.executable, "-m", "pip", "install", package])

  pip_install("discord.py")
  pip_install("flask")
#-------------------------------