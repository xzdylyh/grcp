客户端调用:
https://grpc.io/docs/tutorials/basic/python.html
1.grpc安装
pip install grpcio

2.grpc的python protobuf相关的编译工具
pip install grpcio-tools

3.protobuf相关python依赖库
pip install protobuf

4.一些常见原型的生成python类的集合：
pip install googleapis-common-protos

5.使用以下命令生成Python代码：
python3 -m grpc_tools.protoc -I<目标路径目录> --python_out=. --grpc_python_out=<目标文件所在目录路径> <目标文件data.proto>

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. data.proto


