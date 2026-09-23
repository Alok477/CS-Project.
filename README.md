# 🖼️ CS Project — Image Editing Web App

> **One of my first Computer Science projects.**

This repository contains one of my earliest attempts at building a web application using Python.

The project is a simple **Image Editing Web App** built with **Streamlit**. It allows users to upload images and experiment with basic editing operations such as resizing, rotation, and image filters.

Looking back, this project represents an early step in my journey from learning programming concepts to actually building and deploying something that people could interact with through a web browser.

---

## ✨ What is this project?

The application provides a simple interface for experimenting with image editing directly in the browser.

Users can:

* 🖼️ Upload `.png`, `.jpg`, and `.jpeg` images
* 📏 Resize images
* 🔄 Rotate images
* 🎨 Apply basic image filters
* ✨ Experiment with image transformations
* 📬 Send feedback through the contact page

The application also uses animations and custom styling to make the interface more engaging.

---

## 🚀 Features

### 🖼️ Image Editor

The Image Editor page provides several basic editing tools:

* **Resize** — Change the dimensions of an uploaded image
* **Rotate** — Rotate an image between -180° and 180°
* **Blur** — Apply a blur effect
* **Contour** — Create a contour-style effect
* **Edge Enhance** — Enhance edges within an image

Image processing is handled using the **Pillow (PIL)** library.

### 📬 Contact & Feedback

A dedicated contact page allows users to submit feedback through a simple web form.

### 🎞️ Lottie Animations

The project uses Lottie animations to add visual elements to the homepage and contact page.

### 🎨 Custom UI

The application includes:

* Custom backgrounds
* Sidebar navigation
* Colored section headers
* Custom CSS
* Responsive Streamlit layout

---

## 🛠️ Tech Stack

| Technology          | Purpose                                        |
| ------------------- | ---------------------------------------------- |
| 🐍 Python           | Core programming language                      |
| 🎈 Streamlit        | Web application framework                      |
| 🖼️ Pillow          | Image processing                               |
| ✨ Streamlit-Lottie  | Lottie animations                              |
| 🎨 Streamlit Extras | UI components                                  |
| 🔗 Requests         | Fetching external resources                    |
| 🪄 rembg            | Background-removal/image processing capability |

---

## 📁 Project Structure

```text
CS-Project/
│
├── Home.py
├── requirements.txt
│
├── pages/
│   ├── 2_🖼️_Image_Editor.py
│   └── 3_📬_Contact_Page.py
│
├── lottiefiles/
│   └── code.json
│
└── style/
    └── style.css
```

### `Home.py`

The main landing page of the application.

It introduces the project, provides navigation information, displays animations, and explains the main features.

### `pages/2_🖼️_Image_Editor.py`

Contains the image editing functionality, including:

* Image uploading
* Resizing
* Rotation
* Filters

### `pages/3_📬_Contact_Page.py`

Provides the feedback/contact interface.

### `lottiefiles/`

Contains the local Lottie animation used by the application.

### `style/`

Contains custom CSS used to style parts of the application.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Alok477/CS-Project.git
cd CS-Project
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run Home.py
```

The application should then open in your browser.

---

## 📸 How It Works

The basic workflow is:

```text
Upload Image
      ↓
Choose Editing Option
      ↓
Resize / Rotate / Apply Filter
      ↓
Preview the Result
      ↓
Save the Edited Image
```

---

## 🎓 Why I Built This

This was created as a **school-level Computer Science project**.

At the time, the goal wasn't to build a production-grade image editor. The main goal was to take what I was learning in Python and turn it into an actual interactive application.

It was one of my first experiences with:

* Building a web interface with Python
* Working with third-party libraries
* Processing user-uploaded files
* Structuring a multi-page application
* Adding custom UI styling
* Using APIs and external resources
* Deploying a Python application

---

## 🧠 What I Learned

This project helped me understand several concepts that later became useful in larger projects:

* Python application structure
* Basic image processing
* Working with external libraries
* Streamlit application development
* File uploads and user input
* UI design and customization
* Multi-page web applications
* Using APIs
* Deploying applications

More importantly, it taught me that a programming project doesn't have to start out perfect. **Building something, experimenting with it, and improving over time is part of learning.**

---

## 📌 Project Status

**Archived / Legacy Project**

This repository is primarily preserved as a record of an early stage of my programming journey.

The code reflects the tools, knowledge, and development practices I was using when I first built the project. It may require updates to work correctly with modern versions of Python and its dependencies.

---

## 👨‍💻 Author

**Alok Kunmar**

This was one of my first publicly documented programming projects and an early milestone in my journey into Computer Science and software development.

---

### ⭐ A small project, but an important starting point.

Every large project starts somewhere.
This one started with a school Computer Science project and a desire to build something of my own.
