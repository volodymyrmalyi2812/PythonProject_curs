import os
import sys
import tempfile
import tkinter as tk
import unittest
from abc import ABC, abstractmethod
from enum import Enum
from tkinter import filedialog, messagebox, simpledialog

from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageTk


class FilterType(Enum):
    GRAY = "gray"
    BLUR = "blur"
    SEPIA = "sepia"


class Effect(ABC):
    @abstractmethod
    def apply(self, image):
        pass


class GrayEffect(Effect):
    def apply(self, image):
        return ImageOps.grayscale(image).convert("RGB")


class BlurEffect(Effect):
    def apply(self, image):
        return image.filter(ImageFilter.GaussianBlur(2))


class SepiaEffect(Effect):
    def apply(self, image):
        gray = ImageOps.grayscale(image)
        return ImageOps.colorize(gray, "#3b2618", "#f3d5a3")


class ImageProcessor:
    def __init__(self):
        self._original = None
        self._image = None
        self._history = []
        self._effects = {
            FilterType.GRAY: GrayEffect(),
            FilterType.BLUR: BlurEffect(),
            FilterType.SEPIA: SepiaEffect(),
        }

    def load(self, path):
        with Image.open(path) as file:
            image = ImageOps.exif_transpose(file)
            if image.mode == "RGBA" or (image.mode == "P" and "transparency" in image.info):
                layer = image.convert("RGBA")
                background = Image.new("RGBA", layer.size, "white")
                image = Image.alpha_composite(background, layer).convert("RGB")
            else:
                image = image.convert("RGB")
        self._original = image.copy()
        self._image = image
        self._history.clear()

    def get_image(self):
        if self._image is None:
            return None
        return self._image.copy()

    def _change(self, new_image):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        self._history.append(self._image.copy())
        if len(self._history) > 10:
            self._history.pop(0)
        self._image = new_image

    def apply_filter(self, filter_type):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        self._change(self._effects[filter_type].apply(self._image))

    def rotate(self, degrees):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        self._change(self._image.rotate(degrees, expand=True))

    def mirror(self):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        self._change(ImageOps.mirror(self._image))

    def brightness(self, factor):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        self._change(ImageEnhance.Brightness(self._image).enhance(factor))

    def contrast(self, factor):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        self._change(ImageEnhance.Contrast(self._image).enhance(factor))

    def resize(self, width, height):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        if width < 1 or height < 1:
            raise ValueError("Некоректний розмір")
        self._change(self._image.resize((width, height), Image.Resampling.LANCZOS))

    def reset(self):
        if self._original is not None:
            self._change(self._original.copy())

    def undo(self):
        if not self._history:
            return False
        self._image = self._history.pop()
        return True

    def save(self, path):
        if self._image is None:
            raise ValueError("Спочатку відкрийте фото")
        if path.lower().endswith((".jpg", ".jpeg")):
            self._image.save(path, quality=95)
        else:
            self._image.save(path)


class PhotoEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Фоторедактор")
        self.geometry("1050x690")
        self.minsize(720, 530)
        self.configure(bg="#e8edf2")
        self.processor = ImageProcessor()
        self.current_file = ""
        self.preview = None
        self.create_widgets()
        self.bind("<Control-o>", lambda event: self.open_photo())
        self.bind("<Control-s>", lambda event: self.save_photo())
        self.bind("<Control-z>", lambda event: self.undo())

    def add_button(self, parent, title, action):
        tk.Button(
            parent, text=title, command=action, font=("Arial", 11),
            bg="white", fg="#222222", relief="flat", cursor="hand2",
            padx=8, pady=3, anchor="w"
        ).pack(fill="x", padx=12, pady=1)

    def add_title(self, parent, title):
        tk.Label(
            parent, text=title, font=("Arial", 11, "bold"),
            bg="#dce5ee", fg="#203247", anchor="w"
        ).pack(fill="x", padx=12, pady=(8, 3))

    def create_widgets(self):
        header = tk.Frame(self, bg="#293b53", height=60)
        header.pack(fill="x")
        tk.Label(
            header, text="МІЙ ФОТОРЕДАКТОР", font=("Arial", 17, "bold"),
            fg="white", bg="#293b53"
        ).pack(side="left", padx=20, pady=15)

        sidebar = tk.Frame(self, bg="#dce5ee", width=230)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        self.add_title(sidebar, "Файл")
        self.add_button(sidebar, "Відкрити фото", self.open_photo)
        self.add_button(sidebar, "Зберегти як...", self.save_photo)

        self.add_title(sidebar, "Обробка")
        self.add_button(sidebar, "Чорно-біле", lambda: self.apply_filter(FilterType.GRAY))
        self.add_button(sidebar, "Розмиття", lambda: self.apply_filter(FilterType.BLUR))
        self.add_button(sidebar, "Сепія", lambda: self.apply_filter(FilterType.SEPIA))
        self.add_button(sidebar, "Яскравість +", lambda: self.edit(self.processor.brightness, 1.2))
        self.add_button(sidebar, "Яскравість -", lambda: self.edit(self.processor.brightness, 0.8))
        self.add_button(sidebar, "Контраст +", lambda: self.edit(self.processor.contrast, 1.2))
        self.add_button(sidebar, "Контраст -", lambda: self.edit(self.processor.contrast, 0.8))

        self.add_title(sidebar, "Інструменти")
        self.add_button(sidebar, "Повернути ліворуч", lambda: self.edit(self.processor.rotate, 90))
        self.add_button(sidebar, "Повернути праворуч", lambda: self.edit(self.processor.rotate, -90))
        self.add_button(sidebar, "Віддзеркалити", lambda: self.edit(self.processor.mirror))
        self.add_button(sidebar, "Змінити розмір", self.change_size)
        self.add_button(sidebar, "Скасувати дію", self.undo)
        self.add_button(sidebar, "Повернути оригінал", lambda: self.edit(self.processor.reset))

        content = tk.Frame(self, bg="#e8edf2")
        content.pack(side="right", fill="both", expand=True)
        self.canvas = tk.Canvas(content, bg="#f7f9fb", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True, padx=14, pady=(14, 4))
        self.canvas.bind("<Configure>", lambda event: self.show_photo())
        self.status = tk.Label(
            content, text="Відкрийте фото, щоб почати роботу", font=("Arial", 10),
            fg="#415266", bg="#e8edf2", anchor="w"
        )
        self.status.pack(fill="x", padx=15, pady=(4, 12))

    def show_photo(self):
        self.canvas.delete("all")
        image = self.processor.get_image()
        width = max(1, self.canvas.winfo_width())
        height = max(1, self.canvas.winfo_height())
        if image is None:
            self.canvas.create_text(
                width // 2, height // 2, text="Тут буде ваше фото",
                fill="#8695a6", font=("Arial", 17)
            )
            return
        image.thumbnail((max(1, width - 30), max(1, height - 30)), Image.Resampling.LANCZOS)
        self.preview = ImageTk.PhotoImage(image)
        self.canvas.create_image(width // 2, height // 2, image=self.preview)
        original = self.processor.get_image()
        self.status.config(
            text=f"{os.path.basename(self.current_file)}  |  {original.width} x {original.height} пікселів"
        )

    def open_photo(self):
        path = filedialog.askopenfilename(
            title="Виберіть фото",
            filetypes=[("Зображення", "*.png *.jpg *.jpeg *.bmp *.webp"), ("Усі файли", "*.*")]
        )
        if not path:
            return
        try:
            self.processor.load(path)
            self.current_file = path
            self.show_photo()
        except Exception as error:
            messagebox.showerror("Помилка", f"Не вдалося відкрити фото:\n{error}")

    def save_photo(self):
        if self.processor.get_image() is None:
            messagebox.showinfo("Фоторедактор", "Спочатку відкрийте фото")
            return
        path = filedialog.asksaveasfilename(
            title="Зберегти фото",
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp")]
        )
        if not path:
            return
        try:
            self.processor.save(path)
            messagebox.showinfo("Готово", "Фото успішно збережено!")
        except Exception as error:
            messagebox.showerror("Помилка", f"Не вдалося зберегти фото:\n{error}")

    def edit(self, action, *args):
        if self.processor.get_image() is None:
            messagebox.showinfo("Фоторедактор", "Спочатку відкрийте фото")
            return
        try:
            action(*args)
            self.show_photo()
        except Exception as error:
            messagebox.showerror("Помилка", str(error))

    def apply_filter(self, filter_type):
        self.edit(self.processor.apply_filter, filter_type)

    def undo(self):
        if self.processor.undo():
            self.show_photo()
        else:
            messagebox.showinfo("Фоторедактор", "Немає дій для скасування")

    def change_size(self):
        image = self.processor.get_image()
        if image is None:
            messagebox.showinfo("Фоторедактор", "Спочатку відкрийте фото")
            return
        width = simpledialog.askinteger(
            "Змінити розмір", "Нова ширина (пікселі):",
            initialvalue=image.width, minvalue=1, maxvalue=8000, parent=self
        )
        if width is None:
            return
        height = simpledialog.askinteger(
            "Змінити розмір", "Нова висота (пікселі):",
            initialvalue=image.height, minvalue=1, maxvalue=8000, parent=self
        )
        if height is not None:
            self.edit(self.processor.resize, width, height)


class ImageProcessorTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.folder.name, "photo.png")
        image = Image.new("RGB", (6, 4), (70, 130, 190))
        image.putpixel((0, 0), (255, 0, 0))
        image.save(self.path)
        self.processor = ImageProcessor()
        self.processor.load(self.path)

    def tearDown(self):
        self.folder.cleanup()

    def test_load(self):
        self.assertEqual(self.processor.get_image().size, (6, 4))

    def test_grayscale(self):
        self.processor.apply_filter(FilterType.GRAY)
        r, g, b = self.processor.get_image().getpixel((0, 0))
        self.assertEqual(r, g)
        self.assertEqual(g, b)

    def test_blur(self):
        before = self.processor.get_image().getpixel((0, 0))
        self.processor.apply_filter(FilterType.BLUR)
        self.assertNotEqual(before, self.processor.get_image().getpixel((0, 0)))

    def test_sepia(self):
        self.processor.apply_filter(FilterType.SEPIA)
        r, g, b = self.processor.get_image().getpixel((0, 0))
        self.assertGreater(r, b)

    def test_rotate(self):
        self.processor.rotate(90)
        self.assertEqual(self.processor.get_image().size, (4, 6))

    def test_mirror(self):
        self.processor.mirror()
        self.assertEqual(self.processor.get_image().getpixel((5, 0)), (255, 0, 0))

    def test_brightness(self):
        self.processor.brightness(0.5)
        self.assertLess(self.processor.get_image().getpixel((2, 2))[0], 70)

    def test_contrast(self):
        before = self.processor.get_image().getpixel((2, 2))
        self.processor.contrast(1.5)
        self.assertNotEqual(before, self.processor.get_image().getpixel((2, 2)))

    def test_resize(self):
        self.processor.resize(20, 10)
        self.assertEqual(self.processor.get_image().size, (20, 10))

    def test_undo(self):
        self.processor.rotate(90)
        self.assertTrue(self.processor.undo())
        self.assertEqual(self.processor.get_image().size, (6, 4))

    def test_reset(self):
        self.processor.resize(12, 10)
        self.processor.reset()
        self.assertEqual(self.processor.get_image().size, (6, 4))

    def test_save(self):
        output = os.path.join(self.folder.name, "result.png")
        self.processor.save(output)
        with Image.open(output) as image:
            self.assertEqual(image.size, (6, 4))

    def test_undo_empty(self):
        self.assertFalse(self.processor.undo())

    def test_invalid_resize(self):
        with self.assertRaises(ValueError):
            self.processor.resize(0, 10)

    def test_original_unchanged(self):
        self.processor.apply_filter(FilterType.GRAY)
        self.processor.reset()
        self.assertEqual(self.processor.get_image().getpixel((0, 0)), (255, 0, 0))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        unittest.main(argv=[sys.argv[0]])
    else:
        PhotoEditor().mainloop()
