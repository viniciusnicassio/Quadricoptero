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

cd
echo  -e "${cyan} Instalando arquivos essenciais.${NC} "

#sudo apt-get install linux-headers-rpi2

sudo apt-get install build-essential
sudo apt-get install gcc
sudo apt-get install python-dev
sudo apt-get install python-devel
sudo apt-get install unzip
#sudo apt-get install ca-certificates
sudo apt-get install git
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Preparando modulo wi-fi.${NC} "
#sudo apt-get install wireless-tools
#sudo env GIT_SSL_NO_VERIFY=true git clone https://github.com/porjo/mt7601.git
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Baixando arquivos do git.${NC} "
git clone https://github.com/viniciusnicassio/Quadricoptero.git
#git config --global user.email "s.fotakos@gmail.com"
#git config --global user.name "SFotakos"
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear
