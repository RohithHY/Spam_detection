# Spam_detection
Spam Detector is a Flask-based web application that uses a machine learning model to classify messages as spam or not spam. Users can input a message and instantly receive a prediction. The model is trained using scikit-learn and the SMS Spam Collection dataset.

# Spam Detector

Spam Detector is a web application built with Flask and machine learning to identify spam messages. Enter any message and get an instant prediction—Spam or Not Spam.

## Features

- Modern web UI with Bootstrap and custom styles
- Trained ML model (Naive Bayes) using SMS Spam Collection dataset
- Real-time spam detection
- Easy to run and test locally

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/spam-detector.git
    cd spam-detector
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. (Optional) Train the model:
    ```sh
    python train_model.py
    ```
    This will download the dataset, train the model, and save it in the `model/` folder.

### Running the App

Start the Flask server:
```sh
python app.py
```
Visit [http://localhost:5000](http://localhost:5000) in your browser.

### Testing

Install dev requirements and run tests:
```sh
pip install -r dev-requirements.txt
pytest
```

## Project Structure

```
├── app.py
├── train_model.py
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
├── static/
│   ├── style.css
│   └── site.css
├── templates/
│   ├── index.html
│   ├── base.html
│   ├── home.html
│   └── about.html
├── tests/
│   └── test_app.py
├── requirements.txt
├── dev-requirements.txt
├── pyproject.toml
└── README.md
```
