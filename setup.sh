sudo cp pisignal.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable pisignal.service
sudo systemctl start pisignal.service