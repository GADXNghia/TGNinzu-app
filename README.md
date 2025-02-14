# Streamlit Application

This project is a Streamlit application that allows users to upload Excel files, process the data, and display it in a pivot table format. The application is designed to be run in a Docker container for easy deployment.

## Project Structure

```
streamlit-app
├── Dockerfile
├── Home.py
├── requirements.txt
└── README.md
```

## Requirements

The application requires the following Python packages:

- Streamlit
- pandas
- numpy
- matplotlib

These dependencies are listed in the `requirements.txt` file.

## Docker Instructions

To build and run the Docker container for this Streamlit application, follow these steps:

1. **Build the Docker Image**

   Open a terminal and navigate to the project directory. Run the following command to build the Docker image:

   ```
   docker build -t streamlit-app .
   ```

2. **Run the Docker Container**

   After the image is built, run the following command to start the container:

   ```
   docker run -p 8502:8501 streamlit-app
   ```

3. **Access the Application**

   Open a web browser and go to `http://localhost:8502` to access the Streamlit application.

## Usage

Once the application is running, you can upload an Excel file using the provided interface. The application will process the data and display it in a pivot table format. You can select different categories to view specific data.

## License

This project is licensed under the MIT License.