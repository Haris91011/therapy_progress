
# Streamlit Application Setup and Execution

This README provides a step-by-step guide on how to set up a Conda environment with Python 3.10, install the necessary dependencies, and run the Streamlit application.

## Prerequisites

- **Anaconda or Miniconda** installed on your system.
- **Python 3.10** or higher.

### 1. Clone the Repository (If Applicable)
If the project is in a Git repository, clone the repository first:

```bash
git clone <repo-url>
cd <project-directory>
```

### 2. Create a Conda Environment with Python 3.10

Create a new Conda environment with Python 3.10:

```bash
conda create --name streamlit-env python=3.10
```

Activate the environment:

```bash
conda activate streamlit-env
```

### 3. Install Dependencies for the application to work

To install the required packages, run the following command after navigating to the project directory:

```bash
pip install -r requirements.txt
```

If there is no `requirements.txt` file, you can manually install the essential dependencies like `streamlit`:

```bash
pip install streamlit
```

### 4. Run the Streamlit Application

Once all dependencies are installed, you can run the Streamlit application using the following command:

```bash
streamlit run main.py
```

This will start the application, and you can access it through your web browser at:

```
http://localhost:8501
```

### 5. Deactivate the Environment (Optional)

After you're done running the application, you can deactivate the Conda environment using:

```bash
conda deactivate
```

## Troubleshooting

- Ensure you have an active internet connection to install the required Python packages.
- If `streamlit run main.py` doesn't work, ensure that the `main.py` file is in the same directory as where you're running the command.
