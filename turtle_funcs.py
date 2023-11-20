import math
import aspose.words as aw
from svg_turtle import SvgTurtle
from turtle_settings import up_act, right_act, down_act, left_act, circle_act, forward_act, repeat_act, \
    size_turtle_picture, speed_turtle, dot_thickness, svg_dir, png_dir, north, east, west, south

def delete_scope_from_string(string):
    if '[' in string:
        return string[1:]
    elif ']' in string:
        return string[:-1]
    else:
        return string


def curve(t, R, a, b, alf, k):
    if a ** 2 + b ** 2 == R ** 2:
        if a == 0:
            if b > 0:
                angle = -180
            elif b < 0:
                angle = 0
            if b == 0:
                angle = 0
        else:
            if a > 0:
                if b == 0:
                    angle = math.atan(b / a) / math.pi * 180 + 90
                else:
                    angle = math.atan(b / a) / math.pi * 180 + 90
            elif a < 0:
                if b == 0:
                    angle = math.atan(b / a) / math.pi * 180 - 90
                else:
                    angle = math.atan(b / a) / math.pi * 180 + 90
        t.seth(angle)
        t.circle(-R * k, alf)


def actions(t, commands_list, ind, k):
    string = delete_scope_from_string(commands_list[ind + 1])

    if right_act in commands_list[ind]:
        t.right(eval(string))

    elif left_act in commands_list[ind]:
        t.left(eval(string))

    elif forward_act in commands_list[ind]:
        t.forward(eval(string) * k)

    elif up_act in commands_list[ind]:
        t.up()

    elif down_act in commands_list[ind]:
        t.down()

    elif circle_act in commands_list[ind]:
        params = commands_list[ind + 1] + ' ' + commands_list[ind + 2] + ' ' + commands_list[ind + 3] + ' ' + delete_scope_from_string(
            commands_list[ind + 4])

        A = []
        for i in params.split(','):
            L = i.split()
            for j in L:
                A.append(eval(j))
        R, a, b, alf = A
        curve(t, R, a, b, alf, k)
        ind = ind + 3

    new_ind = ind + 2

    return new_ind


def check_coord(commands, t, orient):
    orient_dict = {north: 90, west: 180, south: 270, east: 0}
    begin_angle = orient_dict[orient]

    commands_list = commands.split()

    t.seth(begin_angle)
    t.speed(speed_turtle)
    k = 1

    X = []
    Y = []
    ind = 0
    while ind < len(commands_list) - 1:
        if commands_list[ind] == repeat_act:
            num_of_cicles = int(commands_list[ind + 1])
            ind += 2
            ind_begin_cicle = ind
            for i in range(num_of_cicles):
                while True:
                    if circle_act in commands_list[ind]:
                        R = eval(commands_list[ind + 1])
                        a = eval(commands_list[ind + 2])
                        b = eval(commands_list[ind + 3])
                        if type(R) == tuple:
                            R = R[0]
                        if type(a) == tuple:
                            a = a[0]
                        if type(b) == tuple:
                            b = b[0]

                        x, y = t.position()
                        x = x / k
                        y = y / k
                        X.append(x + a - R)
                        X.append(x + a + R)
                        Y.append(y + b + R)
                        Y.append(y + b - R)
                    ind = actions(t, commands_list, ind, k)
                    x, y = t.position()
                    x = x / k
                    y = y / k
                    X.append(x)
                    Y.append(y)
                    if ']' in commands_list[ind - 1]:
                        break
                if i != num_of_cicles - 1:
                    ind = ind_begin_cicle
        else:
            ind = actions(t, commands_list, ind, k)
            x, y = t.position()
            x = x / k
            y = y / k
            X.append(x)
            Y.append(y)

    t.up()

    x_min, x_max, y_min, y_max = int(min(X)), int(max(X)), int(min(Y)), int(max(Y))
    dx = x_max - x_min
    dy = y_max - y_min
    size = size_turtle_picture
    k = size / max(dx, dy)
    t.reset()

    return commands, t, k, begin_angle, x_min, x_max, y_min, y_max


def play(commands, t, k, begin_angle, x_min, x_max, y_min, y_max):
    commands_list = commands.split()
    t.up()
    x0 = (x_max + x_min) * k / 2
    y0 = (y_max + y_min) * k / 2
    t.goto(-x0, -y0)
    t.down()
    t.seth(begin_angle)
    t.speed(speed_turtle)

    X = []
    Y = []
    ind = 0
    while ind < len(commands_list) - 1:
        if commands_list[ind] == repeat_act:
            print(*commands_list[ind:ind + 2])
            num_of_cicles = int(commands_list[ind + 1])
            ind += 2
            ind_begin_cicle = ind
            for i in range(num_of_cicles):
                while True:
                    if circle_act in commands_list[ind]:
                        print(*commands_list[ind:ind + 5], end=' ')
                        R = eval(commands_list[ind + 1])
                        a = eval(commands_list[ind + 2])
                        b = eval(commands_list[ind + 3])
                        if type(R) == tuple:
                            R = R[0]
                        if type(a) == tuple:
                            a = a[0]
                        if type(b) == tuple:
                            b = b[0]
                        x, y = t.position()
                        x = x / k
                        y = y / k
                        X.append(x + a - R)
                        X.append(x + a + R)
                        Y.append(y + b + R)
                        Y.append(y + b - R)
                    else:
                        print(*commands_list[ind:ind + 2], end=' ')
                    ind = actions(t, commands_list, ind, k)
                    x, y = t.position()
                    x = x / k
                    y = y / k
                    X.append(x)
                    Y.append(y)
                    if ']' in commands_list[ind - 1]:
                        break
                if i != num_of_cicles - 1:
                    ind = ind_begin_cicle
            print()
        else:
            if commands_list[ind] == circle_act:
                print(*commands_list[ind:ind + 5])
            else:
                print(*commands_list[ind:ind + 2])
            ind = actions(t, commands_list, ind, k)
            x, y = t.position()
            x = x / k
            y = y / k
            X.append(x)
            Y.append(y)

    t.up()

    x_min, x_max, y_min, y_max = int(min(X)), int(max(X)), int(min(Y)), int(max(Y))

    for x in range(x_min - 2, x_max + 2):
        for y in range(y_min - 2, y_max + 2):
            t.goto(x * k, y * k)
            t.dot(dot_thickness)


def write_file(filename, width, height, commands, orient):
    t = SvgTurtle(width, height)
    commands, t, k, begin_angle, x_min, x_max, y_min, y_max = check_coord(commands=commands,
                                                                          t=t,
                                                                          orient=orient)
    play(commands, t, k, begin_angle, x_min, x_max, y_min, y_max)
    t.save_as(filename)


def convert_svg2png(svg_file, png_file):
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)
    shape = builder.insert_image(svg_dir + svg_file)
    shape.image_data.save(png_dir + png_file)


def do_turtle_picture_screen(commands, svg_file, orient):
    write_file(svg_dir + svg_file, 1300, 1300, commands, orient)
    png_file = svg_file.split('.')[0] + '.png'
    convert_svg2png(svg_file, png_file)

# commands = 'Направо 60 Повтори 2 [Вперёд 10 Направо 120 Вперёд 5 Направо 240] Направо 120 Вперёд 3 Направо 90 Вперёд 20*3**(1/2) Направо 90 Вперёд 8 Направо 120 Повтори 2 [Вперёд 10 Налево 120 Вперёд 5 Налево 240]'
# # commands = 'Направо 180 Вперёд 5 Направо 90 Вперёд 50 Направо 90 Вперёд 5 Повтори 5 [Дуга 5, 5, 0, 180]'
# # commands = 'Повтори 5 [Дуга 5, 0, 5, 180 Дуга 5, 5, 0, 180 Дуга 5, 0, -5, 180 Дуга 5, -5, 0, 180]'
# # commands = 'Повтори 2 [Вперёд 9 Направо 90 Вперёд 15 Направо 90] Поднять хвост Вперёд 12 Направо 90 Опустить хвост Повтори 2 [Вперёд 6 Направо 90 Вперёд 12 Направо 90]'
# do_turtle_picture_screen(commands, '1.svg', 'Север')