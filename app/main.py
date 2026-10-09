from fastapi import FastAPI

# 创建应用实例。title / version 会显示在自动生成的文档页面上
app = FastAPI(title="LinkPulse", version="0.1.0")


@app.get("/healthz")
def healthz():
    """健康检查接口：用来确认服务是否活着。"""
    return {"status": "ok", "version": "0.1.0"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """示例接口：演示路径参数与自动类型校验。"""
    return {"item_id": item_id}