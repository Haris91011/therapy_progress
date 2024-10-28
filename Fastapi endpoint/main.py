from fastapi import FastAPI, status, File, UploadFile
import uvicorn
from fastapi.responses import JSONResponse , HTMLResponse
import json
from utils import generate_unique_key, ranker_chain, progress_genertaion_chain

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    message = "Welcome to Therapy Progress Application"
    html_content = f"<html><body><h1>{message}</h1></body></html>"
    return HTMLResponse(content=html_content)

@app.post("/generate-progress")
async def generate_progress(files: list[UploadFile] = File(...)):
    try:
        uploaded_files_data = {}
        random_key_to_summary = {}
        existing_keys = set()

        for file in files:
            content = await file.read()
            text_data = content.decode('utf-8') 
            json_data = json.loads(text_data)
            brief_summary = json_data['Brief Summary of Session']
            if brief_summary:
                random_key = generate_unique_key(existing_keys)
                existing_keys.add(random_key)
                random_key_to_summary[random_key] = brief_summary
                uploaded_files_data[random_key] = json_data

        generated_response = ranker_chain(random_key_to_summary)
        ordered_ids = [int(item.split(': ')[1]) for item in generated_response]
        reranked_data = {key: uploaded_files_data[key] for key in ordered_ids}

        final_query = "\n\n".join(
            f"'{idx + 1} session information:' {session}"
            for idx, (key, session) in enumerate(reranked_data.items())
        )
        final_response = progress_genertaion_chain(final_query)

        res = {"progress": final_response}
        return JSONResponse(
            content={"succeeded": True, "message": "Successfully generated Progress", "httpStatusCode": status.HTTP_200_OK, "data": res},
            status_code=status.HTTP_200_OK
        )
    except Exception as ex:
        return JSONResponse(
            content={"succeeded": False, "message": "Unsuccessful to generate progress", "httpStatusCode": status.HTTP_404_NOT_FOUND},
            status_code=status.HTTP_404_NOT_FOUND
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8282)
