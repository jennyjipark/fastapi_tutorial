import uvicorn

def start():
    uvicorn.run("main:app", host="localhost", port=8000, reload=False)

if __name__ == "__main__":
    start()
