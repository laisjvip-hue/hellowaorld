# YouTube Downloader EXE

本仓库提供一个简单的 YouTube 视频下载工具，并通过 GitHub Actions 自动打包 Windows 可执行文件（`.exe`）。你无需在本地安装 Python，就能获取可运行的文件夹。

## 快速获取 EXE（无需本地安装 Python）
1. 登录 GitHub 并 Fork 此仓库到你的账号。
2. 打开 Fork 后仓库的 **Actions** 页签，选择左侧的 **Build Windows EXE** 工作流。
3. 点击 **Run workflow**，保持默认 Python 版本，确认运行。
4. 等待工作流完成（几分钟）。在运行记录的末尾找到 **Artifacts**，下载 `youtube-downloader-windows` 压缩包。
5. 解压压缩包，得到 `youtube_downloader.exe`、`README.md` 和 `links.sample.txt`。在同一文件夹创建 `links.txt`，把要下载的链接一行一个粘贴进去（程序会在 EXE 所在的文件夹里读取/生成所有文件）。
6. 双击运行 `youtube_downloader.exe`，程序会把视频保存到同级的 `downloads` 文件夹，同时在同级的 `download.log` 中记录日志。

## 手动运行（如果你有 Python 环境）
1. 安装依赖：`pip install -r requirements.txt`
2. 准备链接文件：复制 `links.sample.txt` 为 `links.txt` 并填写链接。
3. 运行：`python youtube_downloader.py`

## 项目文件
- `youtube_downloader.py`：主程序。
- `requirements.txt`：依赖列表。
- `links.sample.txt`：示例链接文件。
- `.github/workflows/build-exe.yml`：GitHub Actions 配置，自动生成 Windows EXE。
