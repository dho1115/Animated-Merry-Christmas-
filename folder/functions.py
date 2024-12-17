import folder

def availableVersions():
   getVersions = {key: value for key, value in folder.versions.__dict__.items() if "__" not in key}
   getVersions = {key: value for key, value in getVersions.items() if key not in ['time', 'init', 'colored']}
   
   return getVersions;