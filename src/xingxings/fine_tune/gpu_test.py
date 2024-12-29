import torch
print(torch.cuda.is_available())  # 返回 True 表示 CUDA 可用
print(torch.cuda.get_device_name(0))  # 返回 GPU 名称

# import tensorflow as tf
# print(tf.config.list_physical_devices('GPU'))  # 返回 GPU 设备信息