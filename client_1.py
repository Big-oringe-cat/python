#!/root/bin/python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = str(socket.gethostname())

port = 9999

s.connect((host,port))

while 1:
    try:
        cmd = input("请输入命令:")
        if (cmd ==  'quit'):
            cmd = "echo 'quit'"
            s.sendall(cmd.encode('utf-8'))
            s.close()
            print("连接结束")
            break
        else:
            s.sendall(cmd.encode('utf-8'))
            data = s.recv(1024)
            print(data.decode('utf-8'))
    except EOFError:
        print('\r\n' + "快捷键退出。。。")
        break
    except KeyboardInterrupt:
        print('\r\n' + "contrl C取消")
        break

s.close()
print("连接中断")

