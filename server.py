import uvicorn

# 가상환경 aws_tutorial
def start():
    uvicorn.run("main:app", host="localhost", port=8000, reload=False)

if __name__ == "__main__":
    start()
