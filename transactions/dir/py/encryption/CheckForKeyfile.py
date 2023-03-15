from ..FilePaths import keyfilePath

def check_for_keyfile():
        if keyfilePath == "":
                return ""
        else:
                with open(keyfilePath, "r") as keyfileData:
                        keyfileData.read(128)
                        return keyfileData

