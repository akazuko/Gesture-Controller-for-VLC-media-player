# Gesture Controller for VLC Media Player

## To run the app:

- install the requirements
    ``` bash
    pip install -r app/requirements.txt
    ```
- set the env
    ```bash
    export PYTHONPATH=${PWD}/app:${PYTHONPATH}
    ```
- to detect faces in a single image:
    ``` bash
    python app/face_detector.py --filename path/to/file
    ```
- to run the app
    ``` bash
    python app/main.py
    ```
