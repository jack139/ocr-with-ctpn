yum install libSM libXext libXrender 
pip install -r requirements.txt

chmod +x ./ctpn/utils/bbox/make.sh
cd ./ctpn/utils/bbox/ && ./make.sh