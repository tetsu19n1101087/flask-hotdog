from google import quickstart
import os

file_path = 'models/model3.h5'

if __name__ == '__main__':
  if os.path.exists(file_path):
    print(f"File '{file_path}' already exists.")
  else:
    print(f"File '{file_path}' does not exist. Executing function...")
    quickstart.main()