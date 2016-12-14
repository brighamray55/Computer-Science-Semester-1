import turtle


def read_coords(file):
    """Take in the file handle for the file of star positions and parse it
    into three dictonaries:
    Henry Draper # : (x position, y position)
    Henry Draper # : magnitude
    Name(s) : Henry Draper #"""
    stars = file.readlines()
    coord_dict = {}
    mag_dict = {}
    name_dict = {}
    for star in stars:
        data = star.split(" ", 6)
        coord_dict.update({data[3]: (data[0], data[1])})
        mag_dict.update({data[3]: data[4]})
        if len(data) > 6:
            names = data[6].split(";")
            for name in names:
                name_dict.update({name.strip(): data[3]})
    # print(coord_dict)
    # print(mag_dict)
    # print(name_dict)
    return (coord_dict, mag_dict, name_dict)


def plot_plain_stars(picture_size, coordinates_dict):
    """Plots all the stars in a given dictionary of coordinates"""
    turtle.bgcolor("black")
    turtle.speed(0)
    for star, coords in enumerate(coordinates_dict):
        turtle.penup()
        turtle.setx(float(coords[0]) * (picture_size / 2))
        turtle.sety(float(coords[1]) * (picture_size / 2))
        turtle.pendown()
        print("test b")
        turtle.begin_fill()
        for i in range(0, 4):
            turtle.color("white", "white")
            turtle.forward(2)
            turtle.left(90)
        turtle.end_fill()


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    """Plots all the star in a given dictioanry of coordinates with the size of
    each star varying based upon its magnitude."""
    turtle.bgcolor("black")
    turtle.speed(0)
    for star in coordinates_dict:
        mag = float(magnitudes_dict[star])
        turtle.penup()
        turtle.setx(float(coordinates_dict[star][0]) * (picture_size / 2))
        turtle.sety(float(coordinates_dict[star][1]) * (picture_size / 2))
        turtle.pendown()
        # print("test b")
        turtle.begin_fill()
        size = round(10 / (mag + 2))
        if size > 8:
            size = 8
        for i in range(0, 4):
            turtle.color("white", "white")
            turtle.forward(size)
            turtle.left(90)
        turtle.end_fill()


def read_constellation_lines(file):
    """Takes in the file handle for a file of connected stars in a
    constellation and returns a dictionary:
    Star name : [connected star(s)]"""
    constellation_dict = {}
    star_lines = file.readlines()
    for line in star_lines:
        stars = line.split(",")
        # If the star has already been added to the dictionary update its
        # list
        if stars[0] in constellation_dict:
            constellation_dict[stars[0]].append(stars[1].strip())
        # Otherwise add the star to the dictionary
        else:
            constellation_dict.update({stars[0]: [stars[1].strip()]})
    return constellation_dict


def plot_constellations(picture_size, star_names, coordinates_dict,
                        constellations):
    """Plots the given constellation"""
    turtle.color("yellow")
    turtle.penup()
    for star in constellations:
        for i in constellations[star]:
            # With pen lifted, go to the key star in the constellation
            # dictionary. For each item in the list associated with that key
            # go to that star with pen down. This will sketch out the lines of
            # the constellation.
            turtle.goto(float(coordinates_dict[star_names[star]][0]) *
                       (picture_size / 2),
                        float(coordinates_dict[star_names[star]][1]) *
                       (picture_size / 2))
            turtle.pendown()
            turtle.goto(float(coordinates_dict[star_names[i]][0]) *
                       (picture_size / 2),
                        float(coordinates_dict[star_names[i]][1]) *
                       (picture_size / 2))
            turtle.penup()


def main():
    star_map = open("star_map.txt", "r")
    coord_dict, mag_dict, name_dict = read_coords(star_map)
    star_map.close()
    constellations = open("constellations.txt", "r")
    constellations_dict = read_constellation_lines(constellations)
    constellations.close()
    # plot_plain_stars(10, coord_dict)
    plot_constellations(500, name_dict, coord_dict, constellations_dict)
    plot_by_magnitude(500, coord_dict, mag_dict)


main()
