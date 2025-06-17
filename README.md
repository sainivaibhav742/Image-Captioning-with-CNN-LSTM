# 🖼️ Image Captioning with CNN-LSTM

This project generates human-like image captions using a deep learning model that combines **Convolutional Neural Networks (CNN)** for image feature extraction and **Long Short-Term Memory (LSTM)** networks for sequence generation.

---

## 🛠️ Technologies Used

| Category             | Technologies / Libraries |
|----------------------|--------------------------|
| **Programming Language** | Python 3.x |
| **Deep Learning**         | TensorFlow, Keras |
| **NLP**                   | Keras Tokenizer, text preprocessing |
| **Image Processing**      | PIL (Pillow), OpenCV (optional) |
| **Web Framework**         | Flask |
| **Frontend**              | HTML5, CSS3, Jinja2 Templates |
| **Visualization**         | matplotlib |
| **Utilities**             | NumPy, Pandas, tqdm, os, pickle |

---

## 💡 Features

- 📷 Image Feature Extraction using **Pretrained CNN (e.g., InceptionV3)**
- ✍️ Caption Generation using **LSTM-based Decoder**
- 🧠 Trained on **Flickr8k Dataset**
- 🔤 Custom **Tokenizer** and **Vocabulary Builder**
- 🖥️ Flask-powered **Web Interface** to upload and caption any image
- 📁 Modular code structure for easy experimentation

---
## 💡 Features

- 🧠 **Deep Learning Powered Captioning**  
  Generates human-like captions using a trained CNN + LSTM architecture.

- 📷 **CNN-Based Image Feature Extraction**  
  Uses pretrained **InceptionV3** to encode images into feature vectors.

- 📝 **Sequence Generation with LSTM Decoder**  
  LSTM network converts image features to natural language sentences.

- 🧾 **Custom Vocabulary and Tokenizer**  
  Tokenizer built from the dataset for accurate word-to-index mapping.

- 🧠 **Trained on Flickr8k Dataset**  
  Trained using real-world images and corresponding captions.

- 🌐 **Web Interface with Flask**  
  Upload an image and get a caption instantly via a simple web UI.

- 🧪 **Modular Codebase for Experimentation**  
  Well-structured files for model training, inference, and frontend integration.

- 📁 **Support for Image Uploads**  
  Upload and process any JPG or PNG image to generate a caption.

- 🧪 **Reusability**  
  Easily extend to use other datasets (Flickr30k, MS-COCO) or encoders (ResNet, VGG).

- 🔄 **Fully Offline**  
  Run the entire pipeline locally without needing an internet connection.


