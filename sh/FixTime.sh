echo  -e "${cyan} Entre com a data atual (mm/dd/yy)${NC} "
read -n 8 data
read -n 1

sudo date -s $data

echo  -e "${cyan} Entre com a hora atual (hh:mm:ss)${NC} "
read -n 8 hora
read -n 1

sudo date -s $hora
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear
