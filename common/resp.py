from fastapi.responses import JSONResponse


def json_data(code=200, message="ok", description=None, data=None):
    """统一返回 json 格式
    :return:
    """
    return JSONResponse(
        content={
            "code": code,
            "message": message,
            "description": description,
            "data": data,
        },
    )
