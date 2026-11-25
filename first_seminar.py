from unittest import result

from pyparsing import col


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

    def zigzag(self, matrix):
        row=0
        col=0

        result=[]
        for i in range(64):
            result.append(matrix[row][col])
            #Diagonal going up
            if (row + col) % 2 == 0:
                if col == 7:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            #diagonal going down
            else:
                if row == 7:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1
        return result

    def inverse_zigzag(self, array):
        row = 0
        col = 0
        matrix = []

        for i in range(8):
            rows= [0] * 8
            matrix.append(rows)

        for i in range(64):
            matrix[row][col] = array[i]
            # Diagonal going up
            if (row + col) % 2 == 0:
                if col == 7:
                    row += 1
                elif row == 0:
                    col += 1
                else:
                    row -= 1
                    col += 1
            # Diagonal going down
            else:
                if row == 7:
                    col += 1
                elif col == 0:
                    row += 1
                else:
                    row += 1
                    col -= 1

        return matrix
