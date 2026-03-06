from fastapi import FastAPI
app = FastAPI()

@app.get("/projects/top")
def get_top_projects():
    return {"message": "Top projects placeholder"}
