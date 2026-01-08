#!/usr/bin/env python3
"""
AstroPaper 项目管理菜单
方便快速执行常用命令
"""

import os
import subprocess
import sys

def clear_screen():
    """清屏"""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(command):
    """运行命令"""
    print(f"\n执行命令: {command}")
    print("-" * 50)
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\n错误: 命令执行失败 - {e}")
    except KeyboardInterrupt:
        print("\n\n命令已中断")
    input("\n按 Enter 返回菜单...")

def main_menu():
    """主菜单"""
    while True:
        clear_screen()
        print("=" * 50)
        print("云触角（重庆）科技有限公司 - 网站管理菜单")
        print("=" * 50)
        print("\n开发相关:")
        print("1. 启动开发服务器 (http://localhost:4321)")
        print("2. 构建生产版本")
        print("3. 预览生产版本")
        print("\n代码质量:")
        print("4. 格式化代码 (Prettier)")
        print("5. 检查代码格式")
        print("6. 代码检查 (ESLint)")
        print("\n内容管理:")
        print("7. 打开博客文章目录")
        print("8. 打开网站配置文件")
        print("9. 打开关于页面")
        print("\n其他:")
        print("10. 同步 TypeScript 类型")
        print("11. 安装/更新依赖")
        print("\n0. 退出")
        
        choice = input("\n请选择操作 (0-11): ").strip()
        
        if choice == "0":
            print("\n退出程序")
            sys.exit(0)
        elif choice == "1":
            run_command("npm run dev")
        elif choice == "2":
            run_command("npm run build")
        elif choice == "3":
            run_command("npm run preview")
        elif choice == "4":
            run_command("npm run format")
        elif choice == "5":
            run_command("npm run format:check")
        elif choice == "6":
            run_command("npm run lint")
        elif choice == "7":
            if os.name == 'nt':  # Windows
                run_command("explorer src\\data\\blog")
            else:  # macOS/Linux
                run_command("open src/data/blog || xdg-open src/data/blog")
        elif choice == "8":
            if os.name == 'nt':
                run_command("notepad src\\config.ts")
            else:
                run_command("open -e src/config.ts || xdg-open src/config.ts")
        elif choice == "9":
            if os.name == 'nt':
                run_command("notepad src\\pages\\about.md")
            else:
                run_command("open -e src/pages/about.md || xdg-open src/pages/about.md")
        elif choice == "10":
            run_command("npm run sync")
        elif choice == "11":
            run_command("npm install")
        else:
            print("\n无效选择，请重试")
            input("按 Enter 继续...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n程序已退出")
        sys.exit(0)