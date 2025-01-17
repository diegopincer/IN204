#ifndef COLOR_H
#define COLOR_H

#include "vec3.h"

#include <iostream>

using color = vec3;

color write_color(color pixel_color, int samples_per_pixel) {
    
    auto r = pixel_color.x();
    auto g = pixel_color.y();
    auto b = pixel_color.z();

    // Divide the color by the number of samples.
    auto scale = 1.0 / samples_per_pixel;
    r *= scale;
    g *= scale;
    b *= scale;


    int ir = int(255.99 * r);
    int ig = int(255.99 * g);
    int ib = int(255.99 * b);

    return color(ir, ig, ib);
}


#endif
