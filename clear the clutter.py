import os

def clear_clutter(folder_path) :
  files = os.listdir(folder_path)

  png_files = []

  for file in files :
    if file.endswith('.png') :
      png_files.append(file)

  for i, file_name in enumerate(png_files, start = 1) :
    os.rename(folder_path + file_name, folder_path + str(i) + ".png")
    
clear_clutter('repo/')
      
  