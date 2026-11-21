"""Helpers for planning one reference per output and screening final PNG files."""
from pathlib import Path


def choose_references(chosen, candidates, count=None):
    """Preserve student order. Candidates are distinct, visually reviewed alternates."""
    if count is None:
        count = len(chosen)
    if count < 1 or count < len(chosen):
        raise ValueError("請確認張數與指定圖片數量")
    result = list(chosen)
    for picture in candidates:
        if len(result) == count:
            break
        if picture not in result:
            result.append(picture)
    if len(result) != count:
        raise ValueError(f"還缺 {count - len(result)} 張參考圖")
    return result


def check_png(path, size=None):
    """Screen exported bytes. Inspect composites separately for interior holes or halos."""
    from PIL import Image

    with Image.open(path) as im:
        if im.format != "PNG" or (size and im.size != size):
            raise ValueError("檔案格式或尺寸有誤")
        alpha = im.convert("RGBA").getchannel("A")
        if alpha.getextrema()[0] != 0 or alpha.getbbox() is None:
            raise ValueError("缺少透明背景或可見角色")
        # Insets avoid accepting an opaque image with just a transparent border.
        w, h = im.size
        interior = alpha.crop((w // 20, h // 20, w - w // 20, h - h // 20))
        if interior.histogram()[0] == 0:
            raise ValueError("透明只在最外圈，請檢查角色輪廓")
    return Path(path).name
