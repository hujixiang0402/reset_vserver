from netcup_webservice import NetcupWebservice
import sys

# 替换为你的 Netcup 凭据
LOGIN_NAME = "your_login"  # 你的登录名
PASSWORD = "your_password"  # 你的 API 密码

# 初始化客户端
client = NetcupWebservice(loginname=LOGIN_NAME, password=PASSWORD)

def print_menu():
    """打印功能菜单"""
    print("\n--- Netcup vServer 管理器 ---")
    print("1. 查看所有 vServers")
    print("2. 获取 vServer 状态")
    print("3. 启动 vServer")
    print("4. 停止 vServer")
    print("5. 重启 vServer")
    print("6. 获取 vServer 流量")
    print("7. 修改 vServer 昵称")
    print("8. 更改用户密码")
    print("9. 查看 vServer 信息")
    print("10. 退出")

def get_vservers():
    """获取所有 vServer"""
    try:
        vservers = client.get_vservers()
        print("\nvServers:")
        for vserver in vservers:
            print(f"- {vserver}")
    except Exception as e:
        print(f"错误: {e}")

def get_vserver_state(vserver_name):
    """获取 vServer 状态"""
    try:
        state = client.get_vserver_state(vserver_name)
        print(f"vServer '{vserver_name}' 的状态: {state}")
    except Exception as e:
        print(f"错误: {e}")

def start_vserver(vserver_name):
    """启动 vServer"""
    try:
        client.start_vserver(vserver_name)
        print(f"vServer '{vserver_name}' 启动成功！")
    except Exception as e:
        print(f"错误: {e}")

def stop_vserver(vserver_name):
    """停止 vServer"""
    try:
        client.stop_vserver(vserver_name)
        print(f"vServer '{vserver_name}' 停止成功！")
    except Exception as e:
        print(f"错误: {e}")

def reset_vserver(vserver_name):
    """硬重置 vServer"""
    try:
        client.reset_vserver(vserver_name)
        print(f"vServer '{vserver_name}' 已硬重置！")
    except Exception as e:
        print(f"错误: {e}")

def change_user_password(new_password):
    """更改用户密码"""
    try:
        client.change_user_password(new_password)
        print("用户密码已更改！")
    except Exception as e:
        print(f"错误: {e}")

def get_vserver_traffic(vserver_name):
    """获取 vServer 流量统计"""
    try:
        traffic = client.get_vserver_traffic_of_day(vserver_name)
        print(f"vServer '{vserver_name}' 当日流量: {traffic}")
    except Exception as e:
        print(f"错误: {e}")

def get_vserver_information(vserver_name):
    """获取 vServer 详细信息"""
    try:
        info = client.get_vserver_information(vserver_name)
        print(f"vServer '{vserver_name}' 详细信息:")
        print(info)
    except Exception as e:
        print(f"错误: {e}")

def change_vserver_nickname(vserver_name, new_nickname):
    """修改 vServer 昵称"""
    try:
        client.set_vserver_nickname(vserver_name, new_nickname)
        print(f"vServer '{vserver_name}' 昵称已更改为 '{new_nickname}'！")
    except Exception as e:
        print(f"错误: {e}")

def main():
    while True:
        print_menu()
        choice = input("请选择操作：")
        
        if choice == "1":
            get_vservers()
        
        elif choice == "2":
            vserver_name = input("请输入 vServer 名称：")
            get_vserver_state(vserver_name)
        
        elif choice == "3":
            vserver_name = input("请输入 vServer 名称：")
            start_vserver(vserver_name)
        
        elif choice == "4":
            vserver_name = input("请输入 vServer 名称：")
            stop_vserver(vserver_name)
        
        elif choice == "5":
            vserver_name = input("请输入 vServer 名称：")
            reset_vserver(vserver_name)
        
        elif choice == "6":
            vserver_name = input("请输入 vServer 名称：")
            get_vserver_traffic(vserver_name)
        
        elif choice == "7":
            vserver_name = input("请输入 vServer 名称：")
            new_nickname = input("请输入新的昵称：")
            change_vserver_nickname(vserver_name, new_nickname)
        
        elif choice == "8":
            new_password = input("请输入新的密码：")
            change_user_password(new_password)
        
        elif choice == "9":
            vserver_name = input("请输入 vServer 名称：")
            get_vserver_information(vserver_name)
        
        elif choice == "10":
            print("退出程序...")
            sys.exit(0)
        
        else:
            print("无效选择，请重新选择。")

if __name__ == "__main__":
    main()
