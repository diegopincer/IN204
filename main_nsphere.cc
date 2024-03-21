
#include "rtweekend.h"
#include "camera.h"
#include "color.h"
#include "hittable_list.h"
#include "material.h"
#include "sphere.h"

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

struct Valeurs {
    int x;
    int y;
    int z;
    int radius;
    int fois;
};

// Fonction pour lire les valeurs du fichier et retourner une structure `Valeurs`
Valeurs lireValeursDuFichier(const string& nomDuFichier) {
    Valeurs valeurs;
    ifstream fichier(nomDuFichier);
    string ligne;

    if (fichier.is_open()) {
        while (getline(fichier, ligne)) {
            istringstream iss(ligne);
            string cle;
            int valeur;
            if (getline(iss, cle, ':') && iss >> valeur) {
                if (cle == "x") valeurs.x = valeur;
                else if (cle == "y") valeurs.y = valeur;
                else if (cle == "z") valeurs.z = valeur;
                else if (cle == "radius") valeurs.radius = valeur;
                else if (cle == "fois") valeurs.fois = valeur;
            }
        }
        fichier.close();
    } else {
        cerr << "Impossible d'ouvrir le fichier : " << nomDuFichier << endl;
    }

    return valeurs;
}


void earth() {

     Valeurs values = lireValeursDuFichier("infos_circle.txt");

    int x = values.x; //0
    int y = values.y; // 0
    int z = values.z; // -5
    int radius = values.radius; //2
    int fois = values.fois; //2

    auto earth_texture = make_shared<image_texture>("earthmap.jpg");
    auto earth_surface = make_shared<lambertian>(earth_texture);


        
    auto globe = make_shared<sphere>(point3(x*i,y*i,z*i), radius, earth_surface);
    

    camera cam;

    cam.aspect_ratio      = 16.0 / 9.0;
    cam.image_width       = 400;
    cam.samples_per_pixel = 10;
    cam.max_depth         = 50;

    cam.render(hittable_list(globe));
}

void random_spheres() {
    hittable_list world;

    auto checker = make_shared<checker_texture>(0.32, color(.2, .3, .1), color(.9, .9, .9));
    world.add(make_shared<sphere>(point3(0,-1000,0), 1000, make_shared<lambertian>(checker)));

    camera cam;

    cam.aspect_ratio      = 16.0 / 9.0;
    cam.image_width       = 400;
    cam.samples_per_pixel = 10;
    cam.max_depth         = 50;

    cam.render(world);
}



void normal() {
    hittable_list world;

    auto material_ground = make_shared<lambertian>(color(0.8, 0.8, 0.0));
    auto material_center = make_shared<lambertian>(color(0.1, 0.2, 0.5));

    world.add(make_shared<sphere>(point3( 0.0, -100.5, -1.0), 100.0, material_ground));
    world.add(make_shared<sphere>(point3( 0.0,    0.0, -1.0),   0.5, material_center));

    camera cam;

    cam.aspect_ratio      = 16.0 / 9.0;
    cam.image_width       = 400;
    cam.samples_per_pixel = 10;
    cam.max_depth         = 50;


    cam.render(world);
    system("image.jpg");
}

int main() {
    earth();
    system("image.jpg");
    
}

