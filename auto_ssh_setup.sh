sudo echo "--------"
echo Updating packages...
sudo apt-get update -y > /dev/null
echo Installing required packages...
sudo apt-get install -y openssh-server > /dev/null
echo Adding SSH User...
sudo useradd samsepiol22
echo "samsepiol22:PleaseChangeMyPassword_8364932" | sudo chpasswd
sudo usermod -aG sudo samsepiol22
echo "User:"
tail -1 /etc/passwd
echo Please login as samsepiol22 and change the password
echo the password is: PleaseChangeMyPassword_8364932
echo Done