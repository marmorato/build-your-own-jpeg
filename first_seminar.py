class ColorTranslator:
    def rgb_to_yuv(self, r, g, b):
        
        y = 0.299 * r + 0.587 * g + 0.114 * b
        u = -0.14713 * r - 0.28886 * g + 0.436 * b
        v = 0.615 * r - 0.51499 * g - 0.10001 * b
        return (y, u, v)

    def yuv_to_rgb(self, y, u, v):
        r = y + 1.13983 * v
        g = y - 0.39465 * u - 0.58060 * v
        b = y + 2.03211 * u
        return (r, g, b)

    def resize(self, input_path, output_path, factor):
        import subprocess
        scale_filter = f"scale=iw/{factor}:ih/{factor}"
        command = ["ffmpeg", "-i", input_path, "-vf", scale_filter, output_path]
        subprocess.run(command, check=True)