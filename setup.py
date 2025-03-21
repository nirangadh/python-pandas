# Check Python version and list installed packages
import sys
print("Python version:", sys.version)
!pip list | grep pandas  # Confirms Pandas is installed in Colab
