import os
import json
import re
class FileManager:
 def __init__(self, directory):
  self.directory = directory
 def list_files(self):
  return os.listdir(self.directory)
 def read_file(self, filename):
  with open(os.path.join(self.directory, filename), 'r') as file:
   return file.read()
 def write_file(self, filename, content):
  with open(os.path.join(self.directory, filename), 'w') as file:
   file.write(content)
 def delete_file(self, filename):
  os.remove(os.path.join(self.directory, filename))
class DataProcessor:
 def __init__(self, data):
  self.data = data
 def filter_data(self, regex_pattern):
  return [item for item in self.data if re.match(regex_pattern, item)]
 def to_json(self):
  return json.dumps(self.data)
 def from_json(self, json_data):
  self.data = json.loads(json_data)
 def unique(self):
  return list(set(self.data))
class Utility:
 def __init__(self, dir_path):
  self.file_manager = FileManager(dir_path)
 def process_files(self):
  files = self.file_manager.list_files()
  for file in files:
   content = self.file_manager.read_file(file)
   processor = DataProcessor(content.split())
   unique_data = processor.unique()
   self.file_manager.write_file(file, ' '.join(unique_data))
