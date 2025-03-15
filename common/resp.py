from typing import Any, Optional

from fastapi.responses import JSONResponse


def render_json(
    code: int = 200,
    message: str = "ok",
    description: Optional[str] = None,
    data: Optional[Any] = None,
) -> JSONResponse:
    """统一返回 JSON 格式的 API 响应。

    :param code: 业务状态码，默认 200
    :param message: 返回的消息，默认 "ok"
    :param description: 可选的详细描述信息，默认为 None
    :param data: 可选的返回数据，默认为 None
    :return: FastAPI JSONResponse 对象
    """
    response_content = {
        "code": code,
        "message": message,
        "description": description,
        "data": data,
    }

    return JSONResponse(content=response_content, status_code=code)
