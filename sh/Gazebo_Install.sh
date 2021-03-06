echo  -e "${cyan} Setup sources.list ${NC} "
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-latest.list'
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Set up your keys ${NC} "
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Installation ${NC} "
sudo apt-get -y update
sudo apt-get install libgazebo6
sudo apt-get install gazebo6
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear
