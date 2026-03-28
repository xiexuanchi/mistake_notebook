# 错题本（PySide6）

一个简洁的本地错题管理程序，支持添加/删除错题、双击查看与编辑详情、按学科分类管理，以及将错题导出为 Word 文档（仅导出题目内容）。界面简洁，数据存储在本地 SQLite。

## 功能概览
- 主界面仅显示错题列表与“导出为Word”按钮
- 添加错题、删除错题
- 双击列表项弹出详情对话框，支持从只读切换到编辑模式并保存
- 学科分类：数学、语文、英语、其他
- 导出 Word：按“1. 题目内容、2. 题目内容 ...”格式，仅导出题目，不包含答案
- 保存对话框默认文件名为“我的错题本”

## 项目结构
- 程序入口：[main.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/main.py)
- 主界面逻辑：[main_window.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/main_window.py)
- 弹窗组件（添加/编辑/查看）：[dialogs.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/dialogs.py)
- 数据库与迁移逻辑：[database.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/database.py)
- 依赖列表：[requirements.txt](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/requirements.txt)
- Mac 启动脚本（双击运行）：[run_mistake_notebook.command](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/run_mistake_notebook.command)
- 数据文件：首次运行会生成 mistakes.db

## 环境准备与运行
### 方式一：命令行运行
1. 创建并激活虚拟环境
   - macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows（PowerShell）:
     ```powershell
     python -m venv venv
     .\\venv\\Scripts\\Activate.ps1
     ```
2. 安装依赖
   ```bash
   pip install -r requirements.txt
   ```
   如需使用清华源：
   ```bash
   pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
   ```
3. 运行
   ```bash
   python main.py
   ```

### 方式二：Mac 一键脚本
- 在 Finder 中双击运行脚本：[run_mistake_notebook.command](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/run_mistake_notebook.command)
- 该脚本会自动创建/激活虚拟环境并安装依赖（使用清华源），随后启动程序

## 使用指南
- 添加错题：点击“添加错题”，输入“题目内容”和“正确答案及解析”，选择学科后保存
  - 为保持主界面简洁，列表的标题会由题目内容自动截取前 15 个字符生成
- 删除错题：选中列表中的项后，点击“删除错题”
- 查看与编辑：双击列表项打开详情（只读），点击详情中的“编辑”切换为可编辑，保存后列表自动刷新
- 导出为 Word：点击“导出为Word”，保存对话框默认文件名为“我的错题本”；导出内容为“序号 + 题目内容”，不包含答案

## 技术细节
- 界面与交互：PySide6
  - 主界面与导出逻辑在 [main_window.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/main_window.py#L22-L132)
  - 详情弹窗在 [dialogs.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/dialogs.py)
- 文档导出：python-docx
  - 仅输出序号与题目内容，示例见 [main_window.py:export_to_word](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/main_window.py#L103-L132)
- 数据库：SQLite
  - 表结构：id, title, question, answer, subject
  - 启动时自动迁移，旧库会添加 subject 字段，详见 [database.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/database.py#L5-L40)
- 学科选择：数学、语文、英语、其他；查看模式下不可编辑，编辑模式可修改，详见 [dialogs.py](file:///Users/xiexuanchi/SchoolProject/mistake_notebook/dialogs.py#L1-L100)

## 注意事项
- 首次运行会创建/迁移数据库文件 mistakes.db
- 若网络较慢，建议使用清华源安装依赖

## 许可
本项目源代码采用 PolyForm Noncommercial License 1.0.0（非商业使用许可）。要点：

- 允许：个人与非商业目的的使用、复制、修改、分发与分叉
- 禁止：任何商业用途（包括销售、收费分发、在付费服务中提供或以商业利益为目的的使用）
- 详情参见仓库根目录的 LICENSE 文件

第三方依赖与许可：
- PySide6：LGPL-3.0（以动态方式使用；需随附其许可证文本）
- python-docx：MIT

如需商业授权，请联系作者获取单独许可。
