## Raspberry Pi Security Camera Client With Picamera2 Support

This application is intended to be a fully fledged example of an IoT application.
The app is composed of 2 different components:

* the client [Raspberry Pi Camera Client](https://github.com/mastrolinux/raspberry-pi-security-camera-client)

* the server  [Raspberry Pi Camera Server](https://github.com/mastrolinux/raspberry-pi-security-camera-server)

The client (a Raspberry Pi with a motion (PIR) sensor and the Raspberry Pi Camera Module 2),
takes a picture with the camera every time a movement is detected by the PIR sensor.
Then it immediately uploads the image on the server, and if the upload is successful,
it remove the local image to avoid filling the disk.

### PiCamera2 installation instructions
Those are the instructions to experiment with picamera2 with the file `main.py`.

**NOTE**
If you want to use the old stack, you have to adapt this code.
The only file requiring the old stack of PiCamera is `example.py`.
To use the old stack please run `sudo raspi-config`, and enable it selecting "Interface Options -> Legacy Camera Support".
Finally reboot your Raspberry Pi.

### Deps installation for PiCamera2

To use PiCamera2 you obviously have to disable the "Legacy Camera Support".

This is a simplified and corrected version of the documentation
available at https://github.com/raspberrypi/picamera2


    sudo apt install -y python3-pip git
    sudo pip3 install jinja2
    sudo apt install -y libboost-dev
    sudo apt install -y libgnutls28-dev openssl libtiff5-dev
    sudo apt install -y qtbase5-dev libqt5core5a libqt5gui5 libqt5widgets5
    sudo apt install -y meson
    sudo pip3 install pyyaml ply
    sudo pip3 install --upgrade meson
    sudo apt install -y libglib2.0-dev libgstreamer-plugins-base1.0-dev

    # Downloading libcamera with the correct branch
    mkdir $HOME/dev
    cd $HOME/dev
    git clone --branch picamera2 https://github.com/raspberrypi/libcamera.git
    cd libcamera

    # build libcamera
    meson build --buildtype=release -Dpipelines=raspberrypi -Dipas=raspberrypi -Dv4l2=true -Dgstreamer=enabled -Dtest=false -Dlc-compliance=disabled -Dcam=disabled -Dqcam=enabled -Ddocumentation=disabled -Dpycamera=enabled

    # install libcamera
    ninja -C build
    sudo ninja -C build install

    # Install DRM/KMS bindings 
    cd $HOME/dev
    git clone https://github.com/tomba/kmsxx.git
    cd kmsxx
    git submodule update --init
    sudo apt install -y libfmt-dev libdrm-dev
    meson build
    ninja -C build

    cd $HOME/dev
    git clone https://github.com/RaspberryPiFoundation/python-v4l2.git

    cd $HOME/dev
    sudo pip3 install pyopengl piexif
    sudo apt install -y python3-pyqt5 python3-pil
    git clone https://github.com/raspberrypi/picamera2.git

    sudo apt install -y python3-opencv
    sudo apt install -y opencv-data

    echo export PYTHONPATH=$HOME/dev/picamera2:$HOME/dev/libcamera/build/src/py:$HOME/dev/kmsxx/build/py:$HOME/dev/python-v4l2 >> ~/.bashrc

    source $HOME/.bashrc

### Ensure all the deps for this project are installed

    pip3 install -r requirements.txt


### Copy the env variables in your own file

To use your own settings, you can make changes to the .env file, an example file is present as env-example.
Copy it over and change it accordingly

    cp env-example .env

### Running the script

    python3 init.py