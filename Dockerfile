FROM ubuntu

ENV DISPLAY=host.docker.internal:0
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /app

RUN apt-get -y update && \
    apt-get -y install python3-vtk7 && \
    apt-get -y install python3 python3-pip python3-dev software-properties-common && \
    apt-get -y install python3-pyside2.qt3dcore python3-pyside2.qt3dinput python3-pyside2.qt3dlogic \
    python3-pyside2.qt3drender python3-pyside2.qtcharts python3-pyside2.qtconcurrent python3-pyside2.qtcore \
    python3-pyside2.qtgui python3-pyside2.qthelp python3-pyside2.qtlocation python3-pyside2.qtmultimedia \
    python3-pyside2.qtmultimediawidgets python3-pyside2.qtnetwork python3-pyside2.qtopengl \
    python3-pyside2.qtpositioning python3-pyside2.qtprintsupport python3-pyside2.qtqml \
    python3-pyside2.qtquick python3-pyside2.qtquickwidgets python3-pyside2.qtscript python3-pyside2.qtscripttools \
    python3-pyside2.qtsensors python3-pyside2.qtsql python3-pyside2.qtsvg python3-pyside2.qttest \
    python3-pyside2.qttexttospeech python3-pyside2.qtuitools python3-pyside2.qtwebchannel python3-pyside2.qtwebsockets \
    python3-pyside2.qtwidgets python3-pyside2.qtx11extras python3-pyside2.qtxml python3-pyside2.qtxmlpatterns

RUN mkdir /Local\ Data


COPY requirements.txt requirements.txt

# Install vtk for pyVista from third party Linux wheel
RUN pip install "https://github.com/finsberg/vtk-aarch64/releases/download/vtk-9.2.6-cp310/vtk-9.2.6.dev0-cp310-cp310-linux_aarch64.whl" \
    && pip install -r requirements.txt

COPY . .