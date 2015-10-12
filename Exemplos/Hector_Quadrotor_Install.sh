echo  -e "${cyan} Install binary packages ${NC} "
sudo apt-get install ros-hydro-hector-quadrotor-demo
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

echo  -e "${cyan} Launch ${NC} "
roslaunch hector_quadrotor_demo indoor_slam_gazebo.launch
echo -e "${cyan} Finished ${NC} " && read -n 1 && clear

#echo  -e "${cyan} Control ${NC} "
#roslaunch hector_quadrotor_teleop xbox_controller.launch 
#echo -e "${cyan} Finished ${NC} " && read -n 1 && clear
