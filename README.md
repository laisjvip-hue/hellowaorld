# YouTube Downloader EXE

本仓库提供一个简单的 YouTube 视频下载工具，并通过 GitHub Actions 自动打包 Windows 可执行文件（`.exe`）。你无需在本地安装 Python，就能获取可运行的文件夹。

## 快速获取 EXE（无需本地安装 Python）
1. 登录 GitHub 并 Fork 此仓库到你的账号。
2. 打开 Fork 后仓库的 **Actions** 页签，选择左侧的 **Build Windows EXE** 工作流。
3. 点击 **Run workflow**，保持默认 Python 版本，确认运行。
4. 等待工作流完成（几分钟）。在运行记录的末尾找到 **Artifacts**，下载 `youtube-downloader-windows` 压缩包。
5. 解压压缩包，得到 `youtube_downloader.exe`、`README.md` 和 `links.sample.txt`。在同一文件夹创建 `links.txt`，把要下载的链接一行一个粘贴进去（程序会在 EXE 所在的文件夹里读取/生成所有文件）。
6. 双击运行 `youtube_downloader.exe`，程序会把视频保存到同级的 `downloads` 文件夹，同时在同级的 `download.log` 中记录日志。

## 上传到自己的 GitHub 并生成 EXE
如果你本地已下载了本仓库的代码，并想推送到你自己的 GitHub 仓库以触发 Actions 打包 EXE，可按以下步骤操作：

1. 在 GitHub 上新建一个空仓库，例如 `youtube-downloader`，不要初始化 README。
2. 在本地（或 Codespaces/远程环境）进入项目根目录，添加远程地址：
   ```bash
   git remote add origin https://github.com/<你的用户名>/youtube-downloader.git
   ```
3. 将当前分支推送到远程（首次推送会建立 upstream）：
   ```bash
   git push -u origin work
   ```
4. 推送完成后，到 GitHub 仓库页面的 **Actions** 里手动运行 **Build Windows EXE** 工作流，或在发布 tag（形如 `v1.0.0`）时自动运行。
5. 等待工作流完成，在运行记录底部下载 `youtube-downloader-windows` artifact，解压后即可获取 EXE。

## 手动运行（如果你有 Python 环境）
1. 安装依赖：`pip install -r requirements.txt`
2. 准备链接文件：复制 `links.sample.txt` 为 `links.txt` 并填写链接。
3. 运行：`python youtube_downloader.py`

## 项目文件
- `youtube_downloader.py`：主程序。
- `requirements.txt`：依赖列表。
- `links.sample.txt`：示例链接文件。
- `.github/workflows/build-exe.yml`：GitHub Actions 配置，自动生成 Windows EXE。
