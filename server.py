import uvicorn

def start():
    uvicorn.run("main:app", host="localhost", port=8000, reload=False)
    # uvicorn.run("main:app", host="ec2-43-201-10-156.ap-northeast-2.compute.amazonaws.com", port=3306, reload=False)

if __name__ == "__main__":
    start()

# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", port=8000, reload=False)
    # uvicorn.run('app.main:app', host='localhost', port=8000, reload=False)
