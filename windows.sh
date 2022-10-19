#sudo efibootmgr -n NUMERO_BOOT
sudo sed -i '/#HibernateMode=reboot/c\HibernateMode=reboot' /etc/systemd/sleep.conf
systemctl hibernate
sudo sed -i '/HibernateMode=reboot/c\#HibernateMode=reboot' /etc/systemd/sleep.conf