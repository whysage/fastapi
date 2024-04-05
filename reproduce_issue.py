from fastapi import FastAPI, Response, Depends

app = FastAPI()

def set_no_cache_headers(response: Response) -> Response:
    response.headers["Potato"] = "potato"
    return response

@app.get("/")
def testing_response(response: Response = Depends(set_no_cache_headers)):
    return {}

print("Script completed successfully, no errors.")
