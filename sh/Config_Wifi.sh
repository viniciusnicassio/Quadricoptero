#sudo ifconfig wlan0 up
#sudo iwconfig wlan0 essid drone
#sudo dhclient wlan0
#iwconfig wlan0
#ifconfig wlan0

iwconfig
echo  -e "${cyan} Indique o nome do modulo desejado. ex:wlan1${NC} "
read wlan
sudo ifconfig $wlan up
sudo iwconfig $wlan power up

echo  -e "${cyan} Escolha o nome da rede.${NC} "
read essid_name
sudo iwconfig $wlan essid $essid_name
sudo dhclient $wlan
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

iwconfig
