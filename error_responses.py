from fastapi.responses import JSONResponse


class ErrorResponses:
    @staticmethod
    def get_not_found_error() -> JSONResponse:
        return JSONResponse(
            status_code=404,
            content={"error": "Not found."}
        )
