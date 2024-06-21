# Fashion-Object-Detection
 
A streamlit app for Fashion Object Detection.  

    
### Features:
1. Uploading an Image to the Streamlit app
2. Detect different Fashion Items in the Image.
3. Draw Bounding Boxes around each detected Item
4. Count the number of items for each different classification.

### Model:  
A yolov8 model trained on a Colorful Fashion Dataset.  [(Dataset Link)](https://www.kaggle.com/datasets/nguyngiabol/colorful-fashion-dataset-for-object-detection)  
[Training Notebook Link](https://colab.research.google.com/drive/1AvpnvAk_HFIJDyYk4HngTFfAAxB_D1bg?usp=sharing)  

### How to use:
1. Clone the repo
2. cd to the repo
3. Type ``` streamlit run fashion_app.py ``` in the terminal
  
**Note:** Make sure you have installed all the required libraries  
``` pip install streamlit pillow ultralytics pandas ```

### Sample Output:
![image](https://github.com/MohdYasser1/Fashion-Object-Detection/assets/88620211/e42d5901-3947-43db-b91d-e88e3f06446d)

