#!/usr/bin/python2

from __future__ import print_function

import cv2
import sys
import numpy as np
import itertools as it
import operator as op

eprint = lambda *args, **kwargs: print(*args, file=sys.stderr, **kwargs)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        eprint('missing output file name')
        sys.exit(1)

    img_raw = np.asarray(
            bytearray(sys.stdin.read()),
            dtype=np.uint8,
    )
    img_col = cv2.imdecode(img_raw, cv2.CV_LOAD_IMAGE_UNCHANGED)
    img_contours = np.copy(img_col)
    img = cv2.imdecode(img_raw, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    IMG_SCALE_FACTOR = sum(np.shape(img_col)[:2])/2
    STROKE_SIZE = int(IMG_SCALE_FACTOR * 0.01) or 1
    NEIGHBORHOOD_SIZE = int(IMG_SCALE_FACTOR * 0.01) or 3
    if NEIGHBORHOOD_SIZE % 2 == 0:
        NEIGHBORHOOD_SIZE += 1

    thresh = cv2.adaptiveThreshold(
            img,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            NEIGHBORHOOD_SIZE,
            0,
    )

    contours, h = cv2.findContours(thresh, 1, 2)

    print('Found', len(contours), 'contours.')

    def reduce_to_triangle(contour):
        i = 1
        while True:
            approx = cv2.approxPolyDP(
                    contour,
                    0.05 * i * cv2.arcLength(
                        contour,
                        True,
                    ),
                    True,
            )
            if len(approx) == 3:
                return approx
            elif len(approx) < 3:
                return None
            else:
                i += 1

    largest_contour = max(
            it.ifilter(
                lambda c: c is not None,
                (reduce_to_triangle(c) for c in contours),
            ),
            key=cv2.contourArea,
    )

    box_x, box_y, box_w, box_h = cv2.boundingRect(largest_contour)
    orig_h, orig_w = img.shape[:2]

    big_box_w = min(box_w * 5, orig_w)
    big_box_h = min(box_h * 5, orig_h)

    # zoomed in images
    #zooms = []

    #for i in range(2,6):
    #    crop_x = box_x - int(box_x/i)
    #    crop_y = box_y - int(box_y/i)

    #    crop_w = box_x+box_w + int(box_x/i)
    #    crop_h = box_y+box_h + int(box_y/i)

    #    crop_image = img[
    #            crop_y:crop_h,
    #            crop_x:crop_w,
    #    ]

    #    zooms.append(
    #            cv2.resize(
    #                crop_image,
    #                (orig_w, orig_h),
    #            ),
    #    )

    print(np.shape(img_col))
    print(largest_contour)
    cv2.drawContours(
            img_col,
            [largest_contour],
            -1,
            (0, 0, 255),
            STROKE_SIZE,
    )

    print('saving to', sys.argv[1])
    cv2.imwrite(sys.argv[1], img_col)
