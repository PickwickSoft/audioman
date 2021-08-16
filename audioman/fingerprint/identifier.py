import acoustid
from audioman.errors.exceptions import *

class AudioFileIdentifier():

    def __init__(self, file: str):
        # The Api Key is from
        self.__API_KEY = 'y27-1XzhoA8'
        self.__file = file
        self.__id = None

    def identify(self) -> str:
        try:
            results = acoustid.match(self.__API_KEY, self.__file)
        except acoustid.NoBackendError:
            raise ChromaprintNotFoundException("Chromaprint library/tool not found")
        except acoustid.FingerprintGenerationError:
            raise FingerprintGenerationError("Fingerprint could not be calculated")
        except acoustid.WebServiceError as exc:
            raise WebServiceError("Web service request failed:", exc.message)
        result = next(results)
        self.__id = result[1]
        return self.__id

    def get_id(self) -> str:
        if self.__id == None:
            raise FileNotIdentifiedException("Run 'identify()' first")
        return self.__id

    def set_new_file(self, file: str):
        self.__file = file
        self.__id = None
