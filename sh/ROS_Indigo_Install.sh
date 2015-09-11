echo  -e "${cyan} Setup sources.list ${NC} "
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Set up your keys ${NC} "
sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net --recv-key 0xB01FA116
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Installation ${NC} "
sudo apt-get -y update
#Ask if user is using 14.04.02 if it isn't xx.xx.02 then dont install
sudo apt-get -y install xserver-xorg-dev-lts-utopic mesa-common-dev-lts-utopic libxatracker-dev-lts-utopic libopenvg1-mesa-dev-lts-utopic libgles2-mesa-dev-lts-utopic libgles1-mesa-dev-lts-utopic libgl1-mesa-dev-lts-utopic libgbm-dev-lts-utopic libegl1-mesa-dev-lts-utopic
sudo apt-get -y install libgl1-mesa-dev-lts-utopic
sudo apt-get -y install ros-indigo-desktop-full
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Initialize Rosdep ${NC} "
sudo rosdep init -y
rosdep update
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Environment setup ${NC} "
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Roinstall ${NC} "
sudo apt-get -y install python-rosinstall
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear





