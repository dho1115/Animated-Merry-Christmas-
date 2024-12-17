if __name__ == '__main__':
   import folder.versions, folder.functions
   from folder.dictionaries import availableVersions, availableVersionsMap

   # #Uncomment to show ALL current versions.
   # for key, value in folder.functions.availableVersions().items():
   #    print(key);
   #    print(value(0.75, 3));

   try:
      versionEntry = input("Enter the version of 'Merry Christmas' that you want to see (one, two, three or four): ");
      key=availableVersionsMap[versionEntry];
      print(availableVersions[key]())
   except Exception:
      print(f"Sorry... enter one of these choices: {availableVersionsMap}.");



   



