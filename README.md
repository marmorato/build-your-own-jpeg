# build-your-own-jpeg
JPEG and JPEG2000 - Seminar 1

2) RGB -YUV
    - We don't get the exact values after the round trip because we don't have infinite precision to describe the coefficients that do the transformation from RGB to YUV so when we do the change from RGB to YUB we itroduce a small "value error" and when we do the YUV to RGB same thing happens again, resulting in not the exacy precise number.If we applied rounding to the RGB converted result (since RGB doesn't use decimals) we would obtain the same result in our code, but we kept the float result so that we can see that the real result isn't exactly the same.
    Also, if we did the first conversion in BT.601 and then tried to recover the RGB values using BT.709 or the other way around, this would give the wrong result since we need to make sure we make the conversions using the same method.

3) 
    - If we take a look at the terminal screenshot of the file sizes we can see that 4:1:1 and 4:2:0 are the images that resulted with a smaller file size, and they have the same value, this is beacuse they store fewer samples and they have the same value because they end up storing the same number of samples per block, although the distribution between horizontal and vertical of these is different.
    Then 4:2:2 has larger file size, followed by 4:4:4 which has the largest file size because it preserves the full resolution of Luma and Chroma
    - If we observe the different results on blurring Chroma or Luma we can see that blurring Chroma makes the colors a bit more pale or plane since they are being averaged between neighbouring pixels but the overall image is pretty much conserved. But if we look at the Luma blurring, the image is visually more affected since the edges are very softened and its harder to look at fine details. This happens because human vision needs more information about illumination than color to be able to interpret an image so when we blurry the Luma which accounts for the illumination, we lose a bit of that image idea.
    -  JPEG and video codecs do this because chroma subsampling is a way of preserving a good quality of the image and at the same time saving space because their file size is reduced, which is a typical problem when storing images whith a lot of quality. This is possible due to the previous mentioned reasons, if we reduce the information of Luma our vision of the image will be affected, while reducing the information of Chroma isn't as noticable.

4) 
    - By default FFmpeg uses bicubic interpolation as a default method. We tried chossing ourselfs the algorithm and did the resampling with bilinear interpolation (result stored in images folder)

5) 
    - This order is because DCT accumulates high frequencies in the bottom right of the matrix, and usually in the high frequencies is where there are more zeros, so when we read the matrix this way we end up accumulating most of the zeros together to the end of the lecture, making it easier for RLE which goes next.