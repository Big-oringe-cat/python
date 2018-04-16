#!/root/bin/python3

import socket

def set_addr(host, port):
    set_host = input("请输入ip地址：(默认本地)")
    set_port = input("请输入端口号：(默认9999)")
    if set_host:
        host = set_host
    else:
        host = host
    
    if set_port:
        port = set_port
    else:
        port = port
    
    return (str(host), int(port))
    
addr = set_addr('localhost', 9999)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect(addr)

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

