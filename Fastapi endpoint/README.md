
# Therapy Session progress Tracking

This project is a FastAPI application that integrates with the OpenAI API. You can run it locally, inside a Docker container, or deploy it to Google Cloud Run.

## Prerequisites

- Python 3.10
- Conda (for local environment setup)
- Docker (for containerization)
- Google Cloud Run (for deployment on Cloud Run)

## Project Structure

- `main.py`: Contains the FastAPI application logic.
- `utils.py`: Utility functions for the app.
- `Dockerfile`: Instructions to build a Docker image.
- `.env`: Environment file to store your API keys.

## Setup Instructions

### 1. Create Conda Environment

To set up a local environment using `conda`, execute the following commands:

```bash
conda create --name myenv python=3.10
conda activate myenv
pip install -r requirements.txt
```

This creates and activates a Python 3.10 environment, and installs the necessary dependencies.

### 2. Running the FastAPI App Locally

To start the FastAPI application locally, run the following command:

```bash
python main.py
```

By default, the app will be accessible at `http://127.0.0.1:8282`.

Note: the app is accessible at `http://0.0.0.0:8282` to run in docker container for local run change it according to above statement

### 3. Creating the `.env` File

This application uses the OpenAI API. Create a `.env` file in the root directory with the following content:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Replace `your_openai_api_key_here` with your actual OpenAI API key.

### 4. Building and Running with Docker

#### Build the Docker Image

To build a Docker image for the application, use the following command:

```bash
docker build -t fastapi-app .
```

#### Running the Docker Container

To run the application in a Docker container, use this command:

```bash
docker run -d -p 8282:8282 --name container_name fastapi-app
```

This command will start the container, and the FastAPI app will be accessible at `http://localhost:8282`.



### 5. Deploying to Google Cloud Run

You can deploy the FastAPI app to Google Cloud Run using Docker. Follow these steps:

#### Build and Tag the Docker Image

```bash
docker login 
```

#### Push the Docker Image to Google Container Registry

```bash
docker push image_name
```

#### Deploy to Cloud Run

1. Add the Docker image name pushed to docker registry in the Google Cloud Run
2. Add the Port Number 
3. Add the Secret keys/variables
4. Select the Option to allow unautheticated user to access the url 
5. Select the minimum and maxium number of instance to manage the traffic load

### 6. Environment Variables

Make sure the following environment variables are set:

- `OPENAI_API_KEY`: Your OpenAI API key. This should be set in the `.env` file or as an environment variable in Cloud Run.

