# Automated Handwritten Form Recognition/ OCR/ Intelligent Text Recognition
This a an API built using Flask framwork.</br>
It accepts a Form Filled image in png format as input. Then processes the image using few simple Machine Learning and Computer Vision techniques. Then the processed result is returned in the request call.</br>
**LIMITATIONS** The flexibility of this project is heavily limited to the following factor:</br>
1.Image should have perfectly aligned boxes with the x and y axis.</br>
2.Box borders should be strong and not have any breakage. As those box will not be processed by the filtering logic.</br>
3.It doesnt results key-value pair results. It only provides the array of the lines of text it recognized.</br>
4.Doesnt contains any semantics on the field context.</br>
5.Scanned image should not have consider types of different noise in it(Theres only very little a few OPEN CV filters can do).</br>

### For Jupyter NoteBook
Jupiter notebook is attached. Run it in colab with the model and sample hand filled form.</br>
Input form image is also provided.</br>
It is heavily commented and contains all the images for step by step execution.

### For Flask setup
1.Make sure to install '64bit' Python 3 or above (3.7.4 preferred)</br>
2.Install required dependencies from the requirements.txt file - 'pip3 install -r requirements.txt --user' for Windows Users</br>
3.**IMP** Change PATH_NAME in controller.py to the location of the folder you cloned this repo to.</br>
4.To start flask app run controller.py - python controller.py</br>
5.Hit '/img_to_json' API with form filled image(sample 'madhav_updated.png' is present), and get the JSON result of the form data</br>

Please feel free to contibute, fork, clone, star and try the project and improve upon it!!</br>
