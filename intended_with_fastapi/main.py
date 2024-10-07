import gc

import uvicorn
from fastapi import FastAPI, HTTPException, status, BackgroundTasks
from pydantic import BaseModel, Field


class SimpleModel(BaseModel):
    name: str = Field(..., title="Name", description="Name of the item")
    description: str = Field(..., title="Description", description="Description of the item")

    class InnerModel(BaseModel):
        name: str = Field(..., title="Name", description="Name of the item")
        description: str = Field(..., title="Description", description="Description of the item")


class ListResponseUserInfo(BaseModel):
    results: list["SimpleModel.InnerModel"] = Field([], title="List of items")


ListResponseUserInfo.model_rebuild()

app = FastAPI()
test_stack = []


def mem_leak():
    global test_stack
    test_stack.append(["a"] * 10000)


@app.get("/intended_mem_leak")
async def intended_mem_leak():
    global test_stack
    # test_stack.append(str(len(test_stack)) * 10000)
    # if i use this, object count does not increase.
    # but it causes memory leak
    mem_leak()
    # if i use this, object count increases
    # very clear that it is a memory leak

    return {
        "Hello": "World",
        "len": len(test_stack),
        "object_count": len(gc.get_objects()),
    }


@app.get("/async")
async def async_read_root():
    return {"Hello": "World"}


@app.get("/sync")
async def sync_read_root():
    return {"Hello": "World"}


@app.get("/sync/check-object-count")
def sync_check_object_count():
    return {"object_count": len(gc.get_objects())}


@app.post("/async/pydantic")
async def create_item(item: SimpleModel):
    return {
        "router_name": "/async/pydantic",
        "item": item.model_dump(),
        "object_count": len(gc.get_objects()),
    }


@app.post("/sync/pydantic")
def create_item(item: SimpleModel):
    return {
        "router_name": "/sync/pydantic",
        "item": item.model_dump(),
        "object_count": len(gc.get_objects()),
    }


@app.get("/sync/intended_exception")
def sync_intended_exception():
    raise HTTPException(
        detail=f"gc object count: {len(gc.get_objects())}",
        status_code=status.HTTP_200_OK,
    )


@app.get("/async/intended_exception")
async def async_intended_exception():
    raise HTTPException(
        detail=f"gc object count: {len(gc.get_objects())}",
        status_code=status.HTTP_200_OK,
    )


@app.get("/sync/hierarchy-pydantic")
def sync_hierarchy_pydantic():
    return {
        "router_name": ListResponseUserInfo(),
        "object_count": len(gc.get_objects()),
    }


@app.get("/async/hierarchy-pydantic")
async def async_hierarchy_pydantic():
    return {
        "router_name": ListResponseUserInfo(),
        "object_count": len(gc.get_objects()),
    }


@app.get("/sync/background-tasks")
def sync_background_tasks(background_tasks: BackgroundTasks):
    background_tasks.add_task(mem_leak)
    return {
        "router_name": "/sync/background-tasks",
        "object_count": len(gc.get_objects()),
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
