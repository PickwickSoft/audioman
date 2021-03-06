import acoustid

import audioman.errors.exceptions as error
from audioman.fingerprint.api import get_api_key


class AudioFileIdentifier:

    def __init__(self, file: str):
        # The Api Key is from
        self.__API_KEY = get_api_key()
        self.__file = file
        self.__id = None

    def identify(self) -> str:
        try:
            results = acoustid.match(self.__API_KEY, self.__file, force_fpcalc=True)
        except acoustid.NoBackendError:
            raise error.ChromaprintNotFoundException(
                "Chromaprint library/tool not found")
        except acoustid.FingerprintGenerationError:
            raise error.FingerprintGenerationError(
                "Fingerprint could not be calculated")
        except acoustid.WebServiceError as exc:
            raise error.WebServiceError("Web service request failed:", exc.message)
        try:
            result = next(results)
        except StopIteration as exc:
            raise error.FingerprintGenerationError(
                "Fingerprint could not be calculated") from exc
        self.__id = result[1]
        return self.__id

    def get_id(self) -> str:
        if self.__id is None:
            raise error.FileNotIdentifiedException("Run 'identify()' first")
        return self.__id

    def set_new_file(self, file: str):
        self.__file = file
        self.__id = None
