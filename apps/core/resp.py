from typing import Any, Optional

from fastapi.responses import JSONResponse


def render_json(
    code: int = 200,
    message: str = "ok",
    data: Optional[Any] = None,
) -> JSONResponse:
    """统一返回 JSON 格式的 API 响应

    :param code: 业务状态码，默认 200
    :param message: 返回的消息，默认 "ok"
    :param data: 可选的返回数据，默认为 None
    :return: FastAPI JSONResponse 对象
    """
    response_content = {
        "message": message,
    }
    if data is not None:
        response_content["data"] = data

    return JSONResponse(status_code=code, content=response_content)
