from werkzeug.exceptions import HTTPException
from werkzeug.sansio.response import Response


class MissingQueryParameterException(HTTPException):
    code = 400
    description = "Missing Paramater"

    def __init__(self, query_parameter: str | None = None) -> None:
        super().__init__(description=f"Missing '{query_parameter}' as query parameter")


class UnauthorizedException(HTTPException):
    code = 401
    description = "Unauthorized"

    def __init__(self, description: str | None = None) -> None:
        super().__init__(description=f"Unauthorized: '{description}'")


class MissingJsonValueException(HTTPException):
    code = 400
    description = "Missing Json value exception"

    def __init__(self, parameter: str | None = None) -> None:
        super().__init__(description=f"Missing: '{parameter}' in json")


class BadRequestEception(HTTPException):
    code = 400
    description = "Bad Request"

    def __init__(self, description: str | None = None) -> None:
        super().__init__(description=description)


def handle_custom_exception(error):
    return error.description, error.code
