# Feature Prediction & 3D Conversion Toolkit

This repository presents an integrated suite of machine learning models and conversion scripts aimed at enhancing 3D modeling workflows. The heart of the project lies in the predictive capabilities of our trained models that can infer features from input data, alongside utilities to convert STL files into point cloud representations.

# Feature Prediction & 3D Conversion Toolkit

This repository presents an integrated suite of machine learning models and conversion scripts aimed at enhancing 3D modeling workflows. The heart of the project lies in the predictive capabilities of our trained models that can infer features from input data, alongside utilities to convert STL files into point cloud representations.

## Features

- **Feature Prediction:** Deploy machine learning models (`Trained.pth`, `Trained 2.pth`, `Trained 3.pth`) trained on extensive datasets to predict features in new 3D model inputs.
- **STL to Point Cloud Conversion:** Utilize `Stl to point cloud.py` to transform STL files, a widely used format for 3D printing and modeling, into point cloud data which can be further used for various analytical purposes in CAD applications.
- **Machine Learning Notebook:** Explore the `Feature Predicted ML model.ipynb` Jupyter notebook to understand the machine learning pipeline from data preprocessing, training, validation, to prediction phases.

## Dataset Collection

The predictive models in this repository have been trained on a diverse collection of datasets to ensure accuracy and reliability. If you are interested in training the models further, you will need to collect and preprocess your datasets accordingly.

If you need access to the datasets used for training these models or have queries regarding data collection and preprocessing, please reach out via email at [2016n1770@gmail.com](mailto:2016n1770@gmail.com).


## Getting Started

To use these tools, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Hassan23121999/Feature-Prediction-Model.git
    


2. **Set up the Environment:**
Install all the necessary Python packages using pip:
    ```bash
    pip install torch numpy tkinter open3d
    

3. **Run the Conversion Script:**
   ```bash
   python Stl_to_point_cloud.py

Convert all Training datat into pointcloud format
   


5. **Run the Machine Learning Model:**
Launch the Jupyter notebook to interact with the machine learning model:
     ```bash
     jupyter notebook Feature_Predicted_ML_model.ipynb
     
## How to Contribute

We are eager to collaborate with you! Contributions that add functionality, enhance the machine learning models, or improve user experience are warmly welcomed. Fork this repository, commit your changes, and open a pull request with a clear description of your improvements.



