
# Online Sexism Detection

This project is a web application for detecting online sexism in text using a trained machine learning model. The application is built using Flask and TensorFlow and provides a simple web interface for users to input text and receive predictions.

## Project Structure

```
your_project/
├── app.py                # Main Flask application
├── model/
│   └── model.py          # Model loading and preprocessing
├── templates/
│   └── index.html        # HTML template for the web interface
├── static/
│   └── styles.css        # CSS for styling the web interface
├── requirements.txt      # Dependencies
└── README.md             # This readme file
```

## Installation

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/online-sexism-detection.git
    cd online-sexism-detection
    ```

2. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3. **Prepare the Model and Tokenizer**:

    Ensure you have the trained model and tokenizer saved in the appropriate format. Update the paths in `model/model.py` to point to these files.

4. **Run the Flask application**:

    ```sh
    python app.py
    ```

5. **Access the web app**:

    Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Open the web application** in your browser.
2. **Enter the text** you want to analyze in the provided text area.
3. **Click the "Detect" button**.
4. The app will display whether the text is sexist or not.

## File Descriptions

- **`app.py`**: Main Flask application file. Defines routes and handles requests.
- **`model/model.py`**: Contains functions to load the trained model and tokenizer, and preprocess text for predictions.
- **`templates/index.html`**: HTML template for the web interface.
- **`static/styles.css`**: CSS file for styling the web interface.
- **`requirements.txt`**: List of dependencies required for the project.
- **`README.md`**: Detailed description of the project.

## Example

Here is an example of how to use the application:

1. Start the Flask server by running `python app.py`.
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.
3. You will see a text area where you can input text.
4. Enter a sentence and click the "Detect" button.
5. The result will display whether the input text is sexist or not.

## Model and Tokenizer

Ensure that you have the trained model and tokenizer loaded in the `model/model.py` script. Update the paths to these files as necessary.

```python
def load_model():
    # Load the tokenizer
    tokenizer = ...  # Update this line to load your tokenizer

    # Load the trained model
    model = tf.keras.models.load_model('path_to_your_model')  # Update the path

    return model, tokenizer
```

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to contact me at [your-email@example.com].

## Acknowledgments

- Thanks to the contributors of the [TensorFlow](https://www.tensorflow.org/) and [Flask](https://flask.palletsprojects.com/) projects.
- Inspired by the need to address online harassment and promote safe online environments.
