FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install fontconfig to use fc-cache
RUN apt-get update && apt-get install -y fontconfig

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the font file into the container
COPY MSGOTHIC.TTC /usr/share/fonts/truetype/

# Update the font cache
RUN fc-cache -f -v

# Copy the rest of the application code into the container
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

# Define the command to run the Streamlit app
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]