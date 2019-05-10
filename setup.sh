pip install numpy scipy matplotlib pillow
pip install easydict opencv-python keras h5py PyYAML
pip install cython==0.24

# for gpu
#pip install tensorflow-gpu==1.3.0

# for cpu
pip install tensorflow==1.3.0

chmod +x ./ctpn/utils/bbox/make.sh
cd ./ctpn/utils/bbox/ && ./make.sh