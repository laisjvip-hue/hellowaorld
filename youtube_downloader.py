from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable, List

import yt_dlp

def get_base_dir() -> Path:
    """Return the directory where runtime files should be stored.

    When packaged as an EXE with PyInstaller, ``sys.frozen`` is set and
    ``sys.executable`` points to the bundled executable. In that case we keep
    all generated files (log, downloads, links) next to the EXE so Windows
    users can find them easily.
    """

    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


BASE_DIR = get_base_dir()
LOG_FILE = BASE_DIR / "download.log"
DEFAULT_LINKS_FILE = BASE_DIR / "links.txt"
DEFAULT_OUTPUT_DIR = BASE_DIR / "downloads"


def log_message(message: str, level: str = "INFO") -> None:
    """Write a log message to stdout and to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {level}: {message}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")


def read_youtube_links(path: Path = DEFAULT_LINKS_FILE) -> List[str]:
    """Read YouTube links from a text file, ignoring blanks and comments."""
    file_path = Path(path)
    if not file_path.exists():
        log_message(f"未找到链接文件: {file_path}", "ERROR")
        return []

    links: List[str] = []
    with open(file_path, "r", encoding="utf-8") as handle:
        for line in handle:
            clean = line.strip()
            if not clean or clean.startswith("#"):
                continue
            links.append(clean)

    if not links:
        log_message("链接文件为空或没有有效链接", "WARNING")
    return links


def download_videos(urls: Iterable[str], output_dir: str = DEFAULT_OUTPUT_DIR) -> None:
    """Download each video URL into the output directory using yt_dlp."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    ydl_opts = {
        "outtmpl": str(output_path / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "concurrent_fragment_downloads": 4,
        "ignoreerrors": True,
    }

    urls_list = list(urls)
    total = len(urls_list)
    success = 0

    for index, url in enumerate(urls_list, start=1):
        try:
            log_message(f"正在处理第 {index}/{total} 个视频: {url}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                error_code = ydl.download([url])

                if error_code == 0:
                    success += 1
                    log_message(f"视频下载成功: {url}")
                else:
                    log_message(f"视频下载失败: {url}", "ERROR")

        except Exception as exc:  # noqa: BLE001
            log_message(f"下载失败: {exc}", "ERROR")
            log_message(f"跳过视频: {url}", "WARNING")

    log_message(f"下载完成! 成功: {success}/{total}")


def main() -> None:
    """Entry point for the downloader."""
    try:
        log_message("开始运行 YouTube 下载程序")

        links = read_youtube_links()
        if links:
            log_message(f"成功读取 {len(links)} 个链接")
            download_videos(links)
        else:
            log_message("未能读取到任何链接", "ERROR")

    except KeyboardInterrupt:
        log_message("用户中断下载", "WARNING")
        sys.exit(1)
    except Exception as exc:  # noqa: BLE001
        log_message(f"程序执行出错: {exc}", "ERROR")
        sys.exit(1)


if __name__ == "__main__":
    main()
