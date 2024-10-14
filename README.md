# Image Frame Processing API

## Purpose of the Assignment

This project is part of an assignment to demonstrate proficiency in computer vision, database management, and API development. The goal is to create a system that can process, store, and retrieve image frames efficiently, while applying image processing techniques.

## Problem Statement

Given a CSV file containing image data, the challenge is to:

1. Resize the image width from 200 pixels to 150 pixels.
2. Store the resized images in a database.
3. Create an API to request image frames based on a specified depth range.
4. Apply a custom color map to the generated frames.
5. Implement the solution in Python.
6. Containerize the solution for easy deployment.

## Solution Overview

This project implements a FastAPI-based web service that:

1. Reads image data from a CSV file.
2. Processes the image data by resizing and applying a color map.
3. Stores the processed images in a SQLite database.
4. Provides an API endpoint to retrieve image frames within a specified depth range.

The solution is containerized using Docker for easy deployment and scalability.

## Key Features

- CSV data analysis and processing
- Image resizing and color mapping
- Efficient database storage and retrieval
- RESTful API for accessing image frames
- Docker containerization

## Project Structure

```
.
├── custom_logger/
│   ├── __init__.py
│   └── helper.py
├── data/
│   ├── raw/
│   │   └── image_data.csv
│   └── processed/
│       └── image_data.db
├── database/
│   ├── __init__.py
│   └── helper.py
├── image_processing/
│   ├── __init__.py
│   └── helper.py
├── utilities/
│   ├── __init__.py
│   ├── constants.py
│   └── helper.py
├── main.py
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── README.md
```

**Important Note:**

- Please check `service` folder code and README file as it includes the API implementation and its usage.

Also, check README files under each of the folders for detailed information about the modules and functionalities.

## Setup and Installation

### Prerequisites

- Docker
- Docker Compose
- Anaconda (to run locally)

### Local Setup

1. Clone the repository:

   ```
   git clone https://github.com/di37/image-frame-processing-api.git
   cd image-frame-processing-api
   ```

2. Create and activate a Conda environment:

   ```
   conda create -n image_frame_processing_api python=3.12
   conda activate image_frame_processing_api
   ```

3. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

## Running the Application

#### Locally

Run the FastAPI server:

```
python main.py
```

#### Using Docker

Build and run the Docker container:

```
docker-compose up --build
```

For any questions or support, please open an issue in the GitHub repository.
