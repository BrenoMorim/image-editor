# Image Editor

## Video Demo:  <URL HERE>

### Description

Image Editor is a CLI application, through which you can apply filters and other modifications to images. The library argparser was used to make the command line interface work, the pillow library made the image edition possible and pytest was used for unit testing. Since the only file which contains a logic worth testing is validator.py, this was the only filed tested. There's no need to test the editor.py, as it only calls Pillow functions, which have already been tested by its owners. The same goes for project.py, that relies on argparser, which also is already well tested by the python language developers.

### How to try it on you computer

If you want to try it out, just follow these steps:

### Downloading the project

You can just clone my git repository:

```sh
git clone https://github.com/BrenoMorim/image-editor.git image-editor
cd image-editor
```

### Starting a virtual environment

It's a good practice to create virtual environments, in order to avoid conflicts between libraries in differents versions that may exist because of other projects.

```sh
virtualenv .venv
source ./.venv/bin/activate
```

### Installing the libraries

You can download all the dependencies through pip:

```sh
pip install -r requirements.txt
```

### Checking the automated tests

To run the automated tests, just run this command:

```sh
pytest
```

### Usage

You can get more information using the --help command:

```sh
python project.py --help
```

To use the application, you must provide three arguments:

- -i / --input: The file to be used as source
- -o / --output: The file to be created/overwritten to save the result
- -a / --action: The action to be applied in the image
- -s / --size: The new size of the image, only used if the action is 'resize', format accepted: WxH, like 500x300

The available actions are:

- blur
- smooth
- edge
- sharpen
- detail
- contour
- grayscale
- flip
- mirror
- invert
- resize

The valid input and output types are .png, .jpg and .jpeg, also the input and output types must be the same.

### Usage example

On the repository, there's a sample image called tv.png, which you can use to test the features. If you want to mirror the image from left to right, you can run the following command:

```sh
python project.py -i tv.png -o mirrored_tv.png -a mirror
```

To detect all the edges and draw an outline on them, you can use this statement:

```sh
python project.py -i tv.png -o outline.png -a contour
```

---

### Explaining the files

- editor.py: Contains all the image edition functions, which use the Pillo library
- validator.py: It's a class meant to store the arguments and validate them
- test_validator.py: A test file to make sure the validations in validator.py are working
- project.py: The main file, which has a main function and uses the argparser lib to catch the CLI arguments
- tv.png: A sample image to be used for manual testing
- requirements.txt: File to store all the pip dependencies
