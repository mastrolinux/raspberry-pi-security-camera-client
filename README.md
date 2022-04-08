### Deps installation

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
    sudo apt install -y python3-pyqt5
    git clone https://github.com/raspberrypi/picamera2.git

    sudo apt install -y python3-opencv
    sudo apt install -y opencv-data

    echo export PYTHONPATH=$HOME/dev/picamera2:$HOME/dev/libcamera/build/src/py:$HOME/dev/kmsxx/build/py:$HOME/dev/python-v4l2 >> ~/.bashrc

    source $HOME/.bashrc