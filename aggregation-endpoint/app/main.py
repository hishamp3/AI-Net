import uvicorn

if __name__ == '__main__':
    uvicorn.run("aggregation.app:app", host="127.0.0.1", port=9000, reload=True)
