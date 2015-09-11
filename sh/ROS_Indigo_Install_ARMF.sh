cyan='\e[1;36m'
NC='\e[0m' # No Color

#Muda a cor do texto do terminal
sudo sed -i 's/#force/force/g' ~/.bashrc

echo  -e "${cyan} Entre com a data atual (mm/dd/yy)${NC} "
read -n 8 data
read -n 1

sudo date -s $data

echo  -e "${cyan} Entre com a hora atual (hh:mm:ss)${NC} "
read -n 8 hora
read -n 1

sudo date -s $hora
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Remover arquitetura x64 ${NC} "
sudo dpkg --remove-architecture x64
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Adicionar arquitetura armhf${NC} "
sudo dpkg --add-architecture armhf
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} Backup source list${NC} "
cp /etc/apt/sources.list /etc/apt/sources.list.backup
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Add multiverse repository${NC} "
sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe multiverse"
sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates universe multiverse"
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Update repository${NC} "
sudo apt-get update
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} G++${NC} "
sudo apt-get -y install g++
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} Set Locale${NC} "
sudo update-locale LANG=C LANGUAGE=C LC_ALL=C LC_MESSAGES=POSIX
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} Setup source.list${NC} "
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list'
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} Setup keys${NC} "
wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | sudo apt-key add -
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} Update${NC} "
sudo apt-get update
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} Installation${NC} "
sudo apt-get install ros-indigo-ros-base
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo -e "${cyan} Initialize rosdep${NC} "
sudo apt-get install python-rosdep
sudo rosdep init
rosdep update
echo -e "${cyan} Finished${NC} " && read -n 1 && clear

echo -e "${cyan} Environment setup${NC} "
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt-get install python-rosinstall
echo -e "${cyan} Finished${NC} " && read -n 1 && clear

echo -e "${cyan} Getting rosinstall${NC} "
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=14.04
DISTRIB_CODENAME=trusty
DISTRIB_DESCRIPTION="Ubuntu 14.04"
echo -e "${cyan} Finished${NC} " && read -n 1 && clear

